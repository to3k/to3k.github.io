---
layout: default
title: Tomasz Dunia - Blog
---

<div style="margin-bottom: 30px;">
  <input type="text" id="search-input" placeholder="🔍 Szukaj / Search" style="width: 100%; padding: 8px; font-family: monospace; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box;">
  <ul id="results-container" style="list-style: none; padding-left: 0; margin-top: 10px;"></ul>
</div>

<div id="all-posts">
  <h3>Spis treści / Table of contents:</h3>
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

<script>
  (function () {
    var input = document.getElementById('search-input');
    var results = document.getElementById('results-container');
    var started = false;

    function initSearch() {
      if (started) return;
      started = true;
      var s = document.createElement('script');
      s.src = 'https://unpkg.com/simple-jekyll-search@1.10.0/dest/simple-jekyll-search.min.js';
      s.integrity = 'sha384-UN+lyciv8Ta643YxZ9sY2tdTSmk3KE61Qq84ZIXG9NRTbD9+NFXy38m9h6Exxx3n';
      s.crossOrigin = 'anonymous';
      s.onload = function () {
        SimpleJekyllSearch({
          searchInput: input,
          resultsContainer: results,
          json: '/search.json',
          searchResultTemplate: '<li style="margin-bottom: 8px;"><span style="color: #666; font-family: monospace; margin-right: 10px;">{date}</span> &raquo; <a href="{url}" style="font-weight: bold;">{title}</a></li>',
          noResultsText: 'Nie znaleziono pasujących wpisów.',
          limit: 500,
          fuzzy: false,
          success: function () {
            if (input.value && input.value.trim().length > 0) {
              this.search(input.value);
            }
          }
        });
      };
      document.body.appendChild(s);
    }

    input.addEventListener('focus', initSearch, { once: true });
    input.addEventListener('input', initSearch, { once: true });
  })();
</script>
