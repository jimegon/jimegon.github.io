---
layout: archive
title: "Research Projects"
permalink: /research/
author_profile: true
---

<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-Q95WSVMDNZ"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-Q95WSVMDNZ');
</script>

{% include base_path %}


## __Working Papers__

<details open>
<summary>
Environmental 
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
Behavioral 
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

<hr style="border: 2px solid;">

# __Work in Progress__

{% for post in site.research reversed %}
  {% if post.type == 'work in progress' %}
    {% include archive-single-research.html %}
  {% endif %}
{% endfor %}

\\
\\
\* Undergraduate Student \\
\*\* MBA Student