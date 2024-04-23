---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% if site.author.googlescholar %}
  <div class="wordwrap">You can also find my articles on <a href="{{site.author.googlescholar}}">my Google Scholar profile</a>.</div>
{% endif %}

{% include base_path %}

<details open>
<summary>
Environmental Economics
</summary>

{% for post in site.publications reversed %}
  {% if post.category == 'environmental' %}
  {% include archive-single-publications.html %}
  {% endif %}
{% endfor %}

</details>


<details open>
<summary class="id1">
Behavioral Economics
</summary>

{% for post in site.publications reversed %}
  {% if post.category == 'behavioral' %}
  {% include archive-single-publications.html %}
  {% endif %}
{% endfor %}

</details>

<details open>
<summary class="id2">
Pedagogy
</summary>

{% for post in site.publications reversed %}
  {% if post.category == 'pedagogy' %}
  {% include archive-single-publications.html %}
  {% endif %}
{% endfor %}

</details>