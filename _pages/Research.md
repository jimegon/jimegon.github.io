---
layout: archive
title: "Working Papers and Projects"
permalink: /research/
author_profile: true
---

{% include base_path %}

<details open>
<summary>
Environmental Economics
</summary>

{% for post in site.research reversed %}
  {% if post.category == 'environmental' %}
  {% include archive-single-publications.html %}
  {% endif %}
{% endfor %}

</details>


<details open>
<summary class="id1">
Behavioral and Environmental Economics
</summary>

{% for post in site.research reversed %}
  {% if post.category == 'behavioral' %}
  {% include archive-single-publications.html %}
  {% endif %}
{% endfor %}

</details>

<details open>
<summary class="id2">
Pedagogy
</summary>

{% for post in site.research reversed %}
  {% if post.category == 'pedagogy' %}
  {% include archive-single-publications.html %}
  {% endif %}
{% endfor %}

</details>

\\
\\
\* Undergraduate Student \\
\*\* MBA Student