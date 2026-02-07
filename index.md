---
layout: default
title: Strona główna
---

<div style="margin-bottom: 30px;">
  <input type="text" id="search-input" placeholder="Szukaj / Search" style="width: 100%; padding: 8px; font-family: monospace; border: 1px solid #ccc; border-radius: 4px;">
  <ul id="results-container" style="list-style: none; padding-left: 0; margin-top: 10px;"></ul>
</div>

<div id="all-posts">
  <h3>Najnowsze wpisy:</h3>
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

<script src="https://unpkg.com/simple-jekyll-search@latest/dest/simple-jekyll-search.min.js"></script>
<script>
  SimpleJekyllSearch({
    searchInput: document.getElementById('search-input'),
    resultsContainer: document.getElementById('results-container'),
    json: '/search.json',
    searchResultTemplate: '<li style="margin-bottom: 8px;"><span style="color: #666; font-family: monospace; margin-right: 10px;">{date}</span> &raquo; <a href="{url}" style="font-weight: bold;">{title}</a></li>',
    noResultsText: 'Nie znaleziono wpisów.',
    limit: 10,
    fuzzy: false
  })
</script>
