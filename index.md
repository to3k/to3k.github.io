---
layout: default
title: Strona główna
---

<h1>Tomasz Dunia - Blog</h1>

<nav style="margin-bottom: 30px; border-bottom: 1px solid #eee; padding-bottom: 10px;">
  <a href="/archive">Spis treści</a> /
  <a href="/about">O mnie</a> /
  <a href="/donate">Donate</a> /
  <a href="/rodo">RODO</a>
</nav>

<div style="margin-bottom: 30px;">
  <input type="text" id="search-input" placeholder="Szukaj wpisu..." style="width: 100%; padding: 8px; font-family: monospace;">
  <ul id="results-container" style="list-style: none; padding-left: 0; margin-top: 10px;"></ul>
</div>

<div id="all-posts">
  <h3>Najnowsze wpisy:</h3>
  <ul style="list-style: none; padding-left: 0;">
    {% for post in site.posts %}
      <li style="margin-bottom: 5px;">
        <span style="color: #666; font-family: monospace;">{{ post.date | date: "%d-%m-%Y" }}</span>
        &raquo;
        <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
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
    searchResultTemplate: '<li style="margin-bottom: 5px;"><span style="color: #666; font-family: monospace;">{date}</span> &raquo; <a href="{url}">{title}</a></li>',
    noResultsText: 'Nie znaleziono wpisów.',
    success: function() {
        // Ukryj główną listę, gdy ktoś zaczyna pisać (opcjonalne, tutaj zostawiam obie)
    }
  })
</script>
