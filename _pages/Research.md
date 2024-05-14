---
layout: archive
title: "Research Projects"
permalink: /research/
author_profile: true
---

{% include base_path %}

<br>
# __Working Papers__

<details open>
<summary>
Environmental Economics
</summary>
{% for post in site.research reversed %}
  {% if post.type == 'working paper' %}
    {% if post.category == 'environmental' %}
    {% include archive-single-publications.html %}
    {% endif %}
  {% endif %}
{% endfor %}

</details>


<details open>
<summary class="id1">
Behavioral and Environmental Economics
</summary>

{% for post in site.research reversed %}
  {% if post.type == 'working paper' %}
    {% if post.category == 'behavioral' %}
    {% include archive-single-publications.html %}
    {% endif %}
  {% endif %}
{% endfor %}

</details>

<details open>
<summary class="id2">
Pedagogy
</summary>

{% for post in site.research reversed %}
  {% if post.type == 'working paper' %}
    {% if post.category == 'pedagogy' %}
    {% include archive-single-publications.html %}
    {% endif %}
  {% endif %}
{% endfor %}

</details>

# __Work in Progress__

\\
\\
\* Undergraduate Student \\
\*\* MBA Student