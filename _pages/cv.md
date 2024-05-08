---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

Education
======
* Ph.D in Economics, Iowa State University, 2016
* B.S. in Applied Mathematics and Economics, Loras College, 2009

Work experience
======
* Spring 2024: Academic Pages Collaborator
  * Github University
  * Duties includes: Updates and improvements to template
  * Supervisor: The Users

* Fall 2015: Research Assistant
  * Github University
  * Duties included: Merging pull requests
  * Supervisor: Professor Hub

* Summer 2015: Research Assistant
  * Github University
  * Duties included: Tagging issues
  * Supervisor: Professor Git
  
Skills
======
* Skill 1
* Skill 2
  * Sub-skill 2.1
  * Sub-skill 2.2
  * Sub-skill 2.3
* Skill 3

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
   
Talks
======
  <ul>{% for post in site.talks reversed %}
    {% include archive-single-talk-cv.html  %}
  {% endfor %}</ul>
  
Teaching
======
  <ul>{% for post in site.teaching reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
  
Service and leadership
======
* Currently signed in to 43 different slack teams
