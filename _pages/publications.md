---
layout: archive
title: "Publications"
permalink: /publications/
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

{% if site.author.googlescholar %}
  <div class="wordwrap">You can also find my articles on <a href="{{site.author.googlescholar}}">my Google Scholar profile</a>.</div>
{% endif %}

{% include base_path %}

<br>

# __Peer-Reviewed Journal Articles__

<details open>
<summary>
Environmental 
</summary>

{% for post in site.publications reversed %}
  {% if post.type == 'pr' %}
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

{% for post in site.publications reversed %}
  {% if post.type == 'pr' %}
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

{% for post in site.publications reversed %}
  {% if post.type == 'pr' %}
    {% if post.category == 'pedagogy' %}
    {% include archive-single-publications.html %}
    {% endif %}
  {% endif %}
{% endfor %}

</details>

\\
\\
\* Undergraduate Student \\
\*\* MBA Student

# __Other Publications__

<details open>
<summary>
Environmental Economics
</summary>

{% for post in site.publications reversed %}
  {% if post.type == 'other' %}
    {% if post.category == 'environmental' %}
    {% include archive-single-publications.html %}
    {% endif %}
  {% endif %} 
{% endfor %}

</details>
