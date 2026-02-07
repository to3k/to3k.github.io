---
layout: default
title: Strona główna
---

<h1>Witaj na moim blogu</h1>
<p>Poniżej znajdziesz listę moich wpisów:</p>

<ul>
  {% for post in site.posts %}
    <li>
      <span>{{ post.date | date: "%Y-%m-%d" }}</span>
      &raquo;
      <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
    </li>
  {% endfor %}
</ul>
