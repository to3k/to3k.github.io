import requests
import xml.etree.ElementTree as ET
from datetime import datetime
import time

# ================= KONFIGURACJA =================
GITHUB_TOKEN = "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"
REPO_OWNER = "to3k"
REPO_NAME = "to3k.github.io"
CATEGORY_NAME = "Comments" # Upewnij się, że taka kategoria istnieje w Discussions!
XML_FILE = "export.xml" # Twój plik z WordPressa
# ================================================

API_URL = "https://api.github.com/graphql"
HEADERS = {"Authorization": f"Bearer {GITHUB_TOKEN}"}

def run_query(query, variables=None):
    response = requests.post(API_URL, json={'query': query, 'variables': variables}, headers=HEADERS)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Błąd zapytania: {response.status_code} {response.text}")

def get_ids():
    query = """
    query($owner: String!, $name: String!) {
      repository(owner: $owner, name: $name) {
        id
        discussionCategories(first: 10) {
          nodes {
            id
            name
          }
        }
      }
    }
    """
    result = run_query(query, {"owner": REPO_OWNER, "name": REPO_NAME})
    repo_id = result['data']['repository']['id']
    categories = result['data']['repository']['discussionCategories']['nodes']
    
    category_id = next((c['id'] for c in categories if c['name'] == CATEGORY_NAME), None)
    if not category_id:
        raise Exception(f"Nie znaleziono kategorii '{CATEGORY_NAME}'. Sprawdź nazwę w GitHub Discussions.")
        
    return repo_id, category_id

def find_discussion_by_title(repo_owner, repo_name, title):
    # Szukamy dyskusji po tytule (GitHub Search)
    search_query = f"repo:{repo_owner}/{repo_name} in:title {title}"
    query = """
    query($search_query: String!) {
      search(query: $search_query, type: DISCUSSION, first: 1) {
        nodes {
          ... on Discussion {
            id
            title
          }
        }
      }
    }
    """
    result = run_query(query, {"search_query": search_query})
    nodes = result['data']['search']['nodes']
    return nodes[0]['id'] if nodes else None

def create_discussion(repo_id, category_id, title, url):
    mutation = """
    mutation($repositoryId: ID!, $categoryId: ID!, $title: String!, $body: String!) {
      createDiscussion(input: {repositoryId: $repositoryId, categoryId: $categoryId, title: $title, body: $body}) {
        discussion {
          id
        }
      }
    }
    """
    # Giscus zazwyczaj szuka po tytule lub mapowaniu URL. 
    # Dodajemy URL w treści dla pewności.
    body = f"Komentarze do wpisu: {url}\n\nAutomatycznie utworzona dyskusja."
    result = run_query(mutation, {
        "repositoryId": repo_id,
        "categoryId": category_id,
        "title": title,
        "body": body
    })
    return result['data']['createDiscussion']['discussion']['id']

def add_comment(discussion_id, body):
    mutation = """
    mutation($discussionId: ID!, $body: String!) {
      addDiscussionComment(input: {discussionId: $discussionId, body: $body}) {
        comment {
          id
        }
      }
    }
    """
    run_query(mutation, {"discussionId": discussion_id, "body": body})

def parse_wordpress_xml():
    tree = ET.parse(XML_FILE)
    root = tree.getroot()
    
    # Przestrzenie nazw w XML WordPressa są upierdliwe
    ns = {'wp': 'http://wordpress.org/export/1.2/', 'content': 'http://purl.org/rss/1.0/modules/content/'}
    
    repo_id, category_id = get_ids()
    print(f"Połączono z repozytorium: {REPO_NAME} (ID: {repo_id})")

    # Iterujemy po wpisach
    for item in root.findall('./channel/item'):
        title = item.find('title').text
        link = item.find('link').text
        post_type = item.find('wp:post_type', ns).text
        
        # Pomijamy strony, załączniki i wpisy bez komentarzy
        if post_type != 'post':
            continue
            
        comments = item.findall('wp:comment', ns)
        valid_comments = [c for c in comments if c.find('wp:comment_approved', ns).text == '1']
        
        if not valid_comments:
            continue

        print(f"\nPrzetwarzanie wpisu: {title} ({len(valid_comments)} komentarzy)")
        
        # 1. Sprawdź czy dyskusja istnieje, jak nie to stwórz
        discussion_id = find_discussion_by_title(REPO_OWNER, REPO_NAME, title)
        
        if not discussion_id:
            print(f" -> Tworzenie nowej dyskusji...")
            try:
                discussion_id = create_discussion(repo_id, category_id, title, link)
                time.sleep(1) # Chwila oddechu dla API
            except Exception as e:
                print(f"BŁĄD przy tworzeniu dyskusji: {e}")
                continue
        else:
            print(f" -> Znaleziono istniejącą dyskusję.")

        # 2. Dodaj komentarze
        for comment in valid_comments:
            author = comment.find('wp:comment_author', ns).text
            date_str = comment.find('wp:comment_date', ns).text
            content = comment.find('wp:comment_content', ns).text
            
            # Formatowanie komentarza (bo wysyłamy jako Ty)
            formatted_body = (
                f"> **Autor:** {author}\n"
                f"> **Data:** {date_str}\n\n"
                f"{content}"
            )
            
            try:
                add_comment(discussion_id, formatted_body)
                print(".", end="", flush=True)
                time.sleep(0.5) # Unikamy limitu rate-limit
            except Exception as e:
                print(f"x (Błąd: {e})")

if __name__ == "__main__":
    parse_wordpress_xml()
