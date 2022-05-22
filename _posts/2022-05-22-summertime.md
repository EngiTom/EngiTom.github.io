---
layout: single
title: "Summertime"
date: 2022-05-22 15:00:00 -04:00
author_profile: true
header: 
  image: assets/images/angello-pro.jpg
  caption: "Photo credit: [**Angello Pro**](https://unsplash.com/photos/UljbyG2UcVI)"
toc: true
toc_sticky: true
categories: [Leisure, Coding, Learning]
---

"Well we do have someone named Palm Zhang in our list" - Dentist's office

## Wisdom Teeth Consulting
When my mom called the dentist's office about a consulting appointment, it turns out they registered my name as Palm instead of Tom which is very interesting. Is there even anyone with such a name? I suppose it really is summer if they assumed that my name is Palm Zhang.

## Coding Extravaganza
I have decided to take on a number of programming challenges over this month, including some programming problems and personal projects. 

### Joke Similarity
I finally completed my joke similarity project which I planned at the very beginning of the year. I guess I figured that I had enough jokes from both of my teachers to actually make the project.

#### How It Works
BERT is a pretrained natural language processing (NLP) machine learning model that can turn sentences into vectors through embedding. Similar sentences will have similar embeddings. So, by calculating the cosine of the angle between two jokes's embeddings, a joke similarity value between 0 and 1 is obtained. Note that cosine increases in value the smaller the angle is. 

Say that I have 80 jokes from Teacher A and 60 jokes from Teacher B. If I line up their embeddings in a table, Teacher A along the top and teacher B along the side, I can have each entry of the table be a cosine similarity value based on the corresponding jokes in the row and column. Below is an illustration (left is Teacher A and B):

{:refdef: style="text-align: center;"}
![Graph Illustration](/assets/images/summertime2022post/table.png)
{:refdef}

#### Improvements
If I can get my hands on a dataset of other comedians's jokes, I can create a graph of how similar, on average, each person's jokes is to every other person. 

{:refdef: style="text-align: center;"}
![Graph Illustration](/assets/images/summertime2022post/graph.png)
{:refdef}

### Neural Network from Scratch
Over this schoolweek, I decided to program a neural network in processing capable of playing flappy bird. It evolves not with back propagation but with genetic algorithms. Basically, the top few percent of birds get to go into the next generation with some mutations.

My classmates were all pretty impressed with this which was nice. 

### Project Euler
I used to think that Project Euler wasn't really worth doing, but there are some real programming problems in there, so I will see how far I can get. It will probably help with number theory, discrete math, and competitive programming. 

### Rookie Hacks II

I participated in the Rookie Hacks II hackathon this weekend with my friend Rafe. It was decently fun and I learned a lot about programming in C# and Unity. However, what I learned was that making multiplayer games is very hard with the type of physics that I want to incorporate, so I should probably stick to single player. 

In addition, working in the Unity developing platform with multiple people at once is very annoying with the failure to update all of the files. 

We didn't win anything, but learning is winning. Next time, I hope that we can make a useful React website. 

{% raw %}
<iframe frameborder="no" width="720" height="380" src="https://i.simmer.io/@jarate/sumo-ball" style="text-align: left"></iframe>
{% endraw %}

## New York Federal Reserve High School Challenge
My team actually won the the economics podcast script challenge this year and are going to get published in a journal. Our topic was how the metaverse and virtualization will impact climate change, which is a very eye-catching idea. Since the topic was the economics of climate change, I would assume that there is an article about how the poor suffer more than the rich as a result of climate change. Although this is likely true, it's kind of like telling people what they already assume to be true. 

I went a bit heavy on the climate change research, but luckily I was told to stop putting a billion words in the introduction. 

## Empty Math Class
My school allows seniors to go on internships during schooltime at the start of May, which has left me alone in math class. It gets boring sometimes so I just start programming. 

## 10000 Hours and Specialization
After reading *Outliers*, I have a new sense of how I should try to balance my life. 

In the book, the author describes how the time for mastery is 10000 hours, and anything less is unlikely to result in anything. For me, I think that I should try to get up to that mark very quickly if I want to do what I want and be good at it. So, less video games, more research. 