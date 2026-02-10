---
layout: post
title: "Jekyll - a brilliant engine for your blog [ENG 🇬🇧]"
published: true
categories: 
  - "projects"
  - "self-hosting-eng"
  - "tutorials"
tags: 
  - "jekyll"
  - "github"
  - "blog"
  - "html"
  - "json"
  - "markdown"
  - "dns"
  - "javascript"
image: "/images/jekyll.png"
---

[🇬🇧->🇵🇱 Przejdź do polskiej wersji tego wpisu / Go to polish version of this post](https://blog.tomaszdunia.pl/blog-jekyll-github/)

Table of contents:
* TOC
{:toc}

This post is partially connected to my [post regarding the migration of my blog from WordPress to the Jekyll engine and GitHub Pages infrastructure](https://blog.tomaszdunia.pl/migracja-bloga-eng/). I described why I did it there, and now it is time to focus on **how I did it**. As I wrote before, it is very simple, and I believe that absolutely anyone can handle it, regardless of their level of technical expertise. To the best of my knowledge, I don't know of an easier way to launch your own personal blog, and completely for free at that. Therefore, if you are thinking about creating your own humble corner on the Internet, fasten your seatbelt, because I am taking you on a short journey through the world of **GitHub Pages**, **Jekyll**, **Markdown**, and **static HTML pages**.

## Preparing the GitHub environment

1. If you don't have a GitHub account yet, [**sign up**](https://github.com/signup) and **log in**.
2. Go to the [**Create a new repository** page](https://github.com/new).
3. In the **General** section, in the **Repository name** field, enter: `(your_github_login).github.io`, where *(your_github_login)* must be your actual GitHub username. In my case, it was exactly `to3k.github.io`. In the **Description** field, enter a short description of the project. It's not very important, so you can write something like `Repository for my private blog`.
4. Fill in the **Configuration** section as follows:
    - **Choose visibility** - *Public*
    - **Add README** - *ON* (check this option)
    - **Add .gitignore** - *No .gitignore*
    - **Add license** - *No license*. In my opinion, there is no need to configure this at this stage, although I personally recommend the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0) license for a blog, so we will deal with this later.
5. Finally, confirm with the green **Create repository** button.

## Launching Jekyll

The main advantage of doing this using GitHub Pages is that practically everything happens by itself, and the only thing you need to know is which options to enable in the settings.

1. Go to the newly created repository and select **Settings** from the top menu bar.
2. On the left, select the **Code and automation** section and then the **Pages** tab.
3. Here we must check if everything is correctly configured in the **Build and deployment** section, i.e.:
    - **Source** - *Deploy from a branch*
    - **Branch** - *main* and folder */root* (if it was different, change it and confirm with the **Save** button).
4. Return to the main repository view (**Code** tab).
5. Now we will create the Jekyll configuration file. To do this, use the **Add file** button and then **Create new file**.
6. The new file creator will open. In the **Name your file...** field, type `_config.yml`. Paste the following into the file content:

```yaml
{% raw %}
# --- MAIN SETTINGS ---
title: Blog Title # Enter your blog title here
description: Blog Description # Enter your blog description here
url: "https://to3k.github.io" # Change my login to yours here
baseurl: "" 
favicon: favicon.png # upload the icon to the main repository folder under this name (preferably 192x192 or 512x512 resolution)

# --- THEME ---
remote_theme: riggraz/no-style-please # By default, Jekyll uses the minima theme, but I didn't like it, so I immediately changed it to this one and I recommend doing the same

# --- LINK SETTINGS ---
permalink: /:title/ # Such permalinks are consistent with the WordPress standard, which will later facilitate the possible migration of an existing blog from WP

# --- PLUGINS ---
plugins:
  - jekyll-feed
  - jekyll-seo-tag
  - jekyll-remote-theme
  - jekyll-sitemap

# --- AUTHOR DATA ---
author:
  name: John Doe # Fill in as you wish
  url: https://example.com # Fill in as you wish

# --- MARKDOWN SETTINGS ---
markdown: kramdown
kramdown:
  input: GFM
  syntax_highlighter: rouge
{% endraw %}
``` 

7. Save the file in this form in the repository using the green **Commit changes...** button located in the upper right corner and then **Commit changes...** again in the window that pops up. It is good practice on GitHub to enter a short description of what we did in the **Commit message** field with every Commit, which will later be visible in the change history. It is enough to type even `Created _config.yml file`.

8. Now it's time for the homepage file. Our blog will be kept in the spirit of minimalism, so for the moment, it will consist only of a bold title and a table of contents listing all posts.

```html
{% raw %}
---
layout: default
title: Home # Enter the homepage title here
---

<div id="all-posts">
  <h3>Table of contents:</h3>
  <ul style="list-style: none; padding-left: 0;">
    {% for post in site.posts %}
      <li style="margin-bottom: 8px;">
        <span style="color: #666; font-family: monospace; margin-right: 10px;">{{ post.date | date: "%d-%m-%Y" }}</span>
        &raquo;
        <a href="{{ post.url | relative_url }}" style="font-weight: bold;">{{ post.title }}</a>
      </li>
    {% endfor %}
  </ul>
</div>
{% endraw %}
```

9. Time to create the first, test post. According to the Jekyll documentation, all files that are to be classified as posts and displayed as such on the blog must be placed in the `_posts` folder. So we need to create such a folder, and on GitHub, this is done simply by creating the first file inside it. To do this, use the **Add file** and **Create new file** buttons again.
10. The new file creator will open. In the **Name your file...** field, type `_posts/`, which will automatically change the path where we create the file. Then, type the name of the post normally: `2026-02-10-hello-world.md`.

It is very important here to understand the syntax:
* The post name must start with the date in the YYYY-MM-DD (year-month-day) format because this is how Jekyll sorts posts from newest to oldest, plus the date provided this way is displayed inside the post as information for the visitor.
* After the date, there is a hyphen and the post identifier. Some people mistakenly write that it must be the title. That's not the point. In our case, the identifier will be the phrase `hello-world`, which means the link to the post will look like this: `https://(your_github_login).github.io/hello-world/`.
* At the end of the file name, there must of course be the `.md` extension.

In the file content, paste:

```yaml
{% raw %}
--- 
layout: post
title: "Hello World!"
published: true # Useful for later creating drafts of posts before their official publication; simply keep it false until the post is ready, and Jekyll will ignore it
categories: # Here you throw in categories by which posts can be sorted later
  - "category1"
  - "category2"
tags: # Here you throw in tags by which posts can be sorted later
  - "tag1"
  - "tag2"
image: "/images/COVERIMAGE.png" # Link to the leading image of the post, if you plan to use such
---

This is my first post on the new blog with the Jekyll engine running on GitHub Pages.
{% endraw %}
```

11. Save the file in the repository using the green **Commit changes...** button located in the upper right corner and **Commit changes...** again in the window that pops up.
12. This is the sufficient minimum to launch a basic blog. Now you need to give GitHub a few minutes to build the site (you can track this in the **Actions** tab of our repository).

When everything is ready, we can go to the page at `https://(your_github_login).github.io` and view the result of the above work.

## Custom domain

Of course, it is possible to connect the blog to your own domain, e.g., `blog.tomaszdunia.pl`. In this case, it is rather a subdomain of the `tomaszdunia.pl` domain, but it does not matter much because it is possible for both top-level domains and subdomains.

### Settings on the GitHub side

1. Return to the repository and select **Settings** from the top menu bar.
2. On the left, select the **Code and automation** section and then the **Pages** tab.
3. Find the **Custom domain** section and enter the domain you want to connect to the blog in the text field, then confirm with the **Save** button.
4. Below, `DNS Check in Progress` should appear, which means GitHub is already waiting for configuration from the domain provider's side.
5. Additionally, GitHub will create a `CNAME` file in our repository. Do not throw it away, it is supposed to be there.
6. That's it for the GitHub side for now; now we must go to the domain provider's page and log in to the DNS record administration panel.

### Settings for a top-level domain (e.g., tomaszdunia.pl)

You must set the following records:
- **A** - label *empty* -> value *185.199.108.153*
- **A** - label *empty* -> value *185.199.109.153*
- **A** - label *empty* -> value *185.199.110.153*
- **A** - label *empty* -> value *185.199.111.153*
- **CNAME** - label *www* -> value *(your_github_login).github.io*

*Note: remember that if there were any records there before, you must clear them.*

### Settings for a subdomain (e.g., blog.tomaszdunia.pl)

If the higher-level domain belongs to you (`tomaszdunia.pl`), go to its DNS record settings and set:
- **CNAME** - label *blog* (enter the first part of the subdomain here) -> value *(your_github_login).github.io*

However, if you only have the ability to manage the subdomain (because the parent domain is, for example, managed by another entity), you do everything from the level of its DNS record settings and set:
- **CNAME** - label *empty* -> value *(your_github_login).github.io*

*Note: remember that if there were any records there before, you must clear them.*

### Back to GitHub settings

Now all that remains is to wait for the DNS to propagate across the network. Sometimes it can be a moment, and in other cases even 24 hours... We will be sure about the completion of the entire process when, after entering **Settings** -> **Code and automation** section -> **Pages** tab -> in the **Custom domain** section, we see the green text `DNS check successful`.

At this point, we need to go a little lower to check the **Enforce HTTPS** option, which will generate an SSL certificate for our site. GitHub manages this, so we absolutely do not have to worry about it.

Now you can type the connected domain into the browser address bar and enjoy the blog appearing at the new address.

## Menu

Usually, a blog is not just posts. It is worth enriching it with additional pages like `About`, `Privacy Policy`, or even `Donate`. So let's make such a sample menu, which everyone can later adapt for themselves.

1. The *No Style Please* theme, which we use for this blog, essentially keeps information about the page structure in the `/_layouts/default.html` file. To add our menu, we must pull the prototype of this file straight from the [theme repository](https://github.com/riggraz/no-style-please), create a copy, overwrite the original in our repository, and add our code fragment to it.
2. I will save you all the trouble and below I will prepare the ready content of the file that you must create in the `_layouts/` folder of your repository under the name `default.html`:

```html
{% raw %}
<!DOCTYPE html>
<html lang="{{ site.lang | default: "en" }}">
  {% include head.html %}

  <body>
    <div style="max-width: 700px; margin: 0 auto; padding: 20px;">

      <header class="masthead" style="margin-bottom: 40px;">
        <h1 style="margin-bottom: 10px;">
          <a href="{{ "/" | relative_url }}" style="text-decoration: none; color: inherit;">{{ site.title }}</a>
        </h1>
  
        <nav style="border-bottom: 1px solid #eee; padding-bottom: 10px;">
          <a href="{{ "/about" | relative_url }}">About</a> /
          <a href="{{ "/donate" | relative_url }}">Donate</a> /
          <a href="{{ "/rodo" | relative_url }}">Privacy Policy</a>
          
        </nav>
      </header>

      <main>
        {{ content }}
      </main>

      <footer style="margin-top: 80px; padding-top: 20px; border-top: 1px dashed #ccc; font-size: 0.8em; color: #666;">
        <p>
          &copy; {{ site.time | date: '%Y' }} {{ site.author.name }}.
          Content available under license <a href="https://creativecommons.org/licenses/by-sa/4.0/" target="_blank">CC BY-SA 4.0</a>.
        </p>
        <p>
          Blog created based on the tutorial available at <a href="https://blog.tomaszdunia.pl/blog-jekyll-github/">blog.tomaszdunia.pl</a>!
        </p>
       
        <p>I also encourage you to subscribe to this blog via the <a href="/feed.xml">RSS feed</a>.</p>
      </footer>

    </div>
  </body>
</html>
{% endraw %}
```

3. Save the file in this form in the repository using the green **Commit changes...** button located in the upper right corner and **Commit changes...** again in the window that pops up.
4. As a bonus, in the file above I included a footer in which I included information about the license, that the blog was created based on this tutorial (you can go ahead and delete this information or leave it, I would be very pleased), and I added a link to the RSS feed to make it easier for your future readers to add it to their favorite reader.
5. Returning to the menu topic, I created it so that it consists of links to three subpages - `/about`, `/donate`, and `/rodo`.

At this stage, the links lead nowhere, so using them will result in a 404 error. To prevent this, you must create these three subpages in the main repository folder, but that is your homework.

I can only show you the code of my subpages to give you material to model on:
- my **about.md** - [page on blog](https://blog.tomaszdunia.pl/about/) and here [source code](https://raw.githubusercontent.com/to3k/to3k.github.io/refs/heads/main/about.md)
- my **donate.md** - [page on blog](https://blog.tomaszdunia.pl/donate/) and here [source code](https://raw.githubusercontent.com/to3k/to3k.github.io/refs/heads/main/donate.md)
- my **rodo.md** - [page on blog](https://blog.tomaszdunia.pl/rodo/) and here [source code](https://raw.githubusercontent.com/to3k/to3k.github.io/refs/heads/main/rodo.md)

## Search Engine

Every self-respecting blog should have a tool for searching for relevant phrases in the titles, content, and tags of its posts. We are self-respecting authors, so of course, we will provide such a tool to our readers.

1. The main problem to solve is that in this post we are discussing a static site that does not have an SQL database that could be searched.
2. Therefore, for the needs of our search engine, we must create a file that will dynamically fill with a list of all posts along with their content. This will be like a database in which we will look for relevant records that match our query.
3. We will create this file in the main repository folder, name it `search.json`, and its content will be as follows:

```
{% raw %}
---
layout: null
---
[
  {% for post in site.posts %}
    {
      "title"    : {{ post.title | jsonify }},
      "url"      : "{{ site.baseurl }}{{ post.url }}",
      "date"     : "{{ post.date | date: "%d-%m-%Y" }}",
      "content"  : {{ post.content | strip_html | strip_newlines | jsonify }}
    } {% unless forloop.last %},{% endunless %}
  {% endfor %}
]
{% endraw %}
```

2. Save the file in this form in the repository using the green **Commit changes...** button located in the upper right corner and **Commit changes...** again in the window that pops up.
3. Now we also need to modify the main page file `index.md`, in which we will load the `unpkg.com/simple-jekyll-search` library, write the search engine script based on it, and place an interactive text field for entering the phrase. Here is the ready code:

```html
{% raw %}
---
layout: default
title: Home # Enter the homepage title here
---

<div style="margin-bottom: 30px;">
  <input type="text" id="search-input" placeholder="Search..." style="width: 100%; padding: 8px; font-family: monospace; border: 1px solid #ccc; border-radius: 4px;">
  <ul id="results-container" style="list-style: none; padding-left: 0; margin-top: 10px;"></ul>
</div>

<div id="all-posts">
  <h3>Table of contents:</h3>
  <ul style="list-style: none; padding-left: 0;">
    {% for post in site.posts %}
      <li style="margin-bottom: 8px;">
        <span style="color: #666; font-family: monospace; margin-right: 10px;">{{ post.date | date: "%d-%m-%Y" }}</span>
        &raquo;
        <a href="{{ post.url | relative_url }}" style="font-weight: bold;">{{ post.title }}</a>
      </li>
    {% endfor %}
  </ul>
</div>

<script src="[https://unpkg.com/simple-jekyll-search@latest/dest/simple-jekyll-search.min.js](https://unpkg.com/simple-jekyll-search@latest/dest/simple-jekyll-search.min.js)"></script>
<script>
  SimpleJekyllSearch({
    searchInput: document.getElementById('search-input'),
    resultsContainer: document.getElementById('results-container'),
    json: '/search.json',
    searchResultTemplate: '<li style="margin-bottom: 8px;"><span style="color: #666; font-family: monospace; margin-right: 10px;">{date}</span> &raquo; <a href="{url}" style="font-weight: bold;">{title}</a></li>',
    noResultsText: 'No matching posts found.',
    limit: 500,
    fuzzy: false
  })
</script>
{% endraw %}
```

## Markdown

For people accustomed to Word or the classic WordPress editor (Gutenberg), Markdown may seem like a step backward at first glance. After all, instead of clicking comfortable icons, we have to type some "weird characters".

In reality, **Markdown** is freedom. It is a lightweight markup language that allows you to format text without taking your hands off the keyboard. It is universal (works on GitHub, Notion, Obsidian, Discord) and – most importantly – it is plain text. This means that in 10 years you will open your posts in any editor without any problems, not worrying that the WordPress database has fallen apart.

In Jekyll, it is precisely Markdown `.md` files that are the source of content. During the site build, Jekyll automatically converts them into ready HTML code.

### Quick Markdown Cheat Sheet

Here are the absolute basics that I use when writing every post:

- **Headers:** Instead of choosing "Heading 2" from a list, we place hashes.
    * `# Main Title (H1)`
    * `## Subtitle (H2)`
    * `### Smaller Header (H3)`
- **Bold and Italics:**
    * `**This will be bold**` → **This will be bold**
    * `*This will be italic*` → *This will be italic*
- **Lists:**
    * `- List element` (bullet)
    * `1. List element` (numbered)
- **Links and Images:**
    * Link: `[Link text](https://address.com)`
    * Image: `![Alt text](link-to-image.jpg)`
- **Code (my favorite tool on a tech blog):**
    * Single backtick `code` for inline snippets.
    * Triple backtick (\`\`\`) for code blocks.

## Final Words

That's just it, and that's all. In my opinion, technically a blog doesn't need anything else. When creating your site, especially the first one, we usually catch ourselves wanting to squeeze everything possible out of it - so it's "fancy". Both in terms of appearance and gadgets (e.g., widgets). In practice, these are not important things. However, we forget about what is most important, namely the content. It is precisely the content that is key and constitutes the true value of the blog. Therefore, the content should be "fancy", and everything around it should be as minimalist as possible, so as not to overshadow with its apparent brilliance what should naturally shine the brightest. Holy moly, look at me philosophizing... Coming back to Earth, I hope this tutorial is useful to someone, and if that person is you, be sure to show me your blog when you publish it!
