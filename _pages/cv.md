---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
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
<br>

Below, you find highlights from my CV related to publications and academic presentations generated from this website's content. 

For my complete CV, click here. 

Academic Appointments
======

* __O'Malley School of Business, Manhattan College__ - Riverdale, NY <br>
  * Associate Professor (2022 - Present) 
  * Assistant Professor (2016 - 2022)

Education
======
* Ph.D in Economics, __Iowa State University__, 2016
* B.S. in Applied Mathematics and Economics, __Loras College__, 2009
  * _Maxima Cum Lade_



Peer-Reviewed Publications
======
  <ol reversed>{% for post in site.publications reversed %}
    {% if post.type == 'pr' %}
    {% include archive-single-cv.html %}
    {% endif %} 
  {% endfor %}</ol>
  
Other Publications
======
  <ul>{% for post in site.publications reversed %}
    {% if post.type == 'other' %}
    {% include archive-single-cv.html %}
    {% endif %} 
  {% endfor %}</ul>
   
Working Papers
=====

## Environmental: 
  <ul>{% for post in site.research reversed %}
    {% if post.type == 'working paper' %}
        {% if post.category == 'environmental' %}
        {% include archive-single-cv.html %}
        {% endif %}
    {% endif %} 
  {% endfor %}</ul>

## Behavioral: 
  <ul>{% for post in site.research reversed %}
    {% if post.type == 'working paper' %}
        {% if post.category == 'behavioral' %}
        {% include archive-single-cv.html %}
        {% endif %}
    {% endif %} 
  {% endfor %}</ul>


Presentations
======
  <ul>{% for post in site.talks reversed %}
    {% include archive-single-talk-cv.html  %}
  {% endfor %}</ul>
  
<!-- Teaching
======
  <ul>{% for post in site.teaching reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
  
Service and leadership
======
* 


Skills
======
* Skill 1
* Skill 2
  * Sub-skill 2.1
  * Sub-skill 2.2
  * Sub-skill 2.3
* Skill 3
-->