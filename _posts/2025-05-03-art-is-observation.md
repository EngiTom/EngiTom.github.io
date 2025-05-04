---
layout: single
title: "Art is Observation"
date: 2025-05-03 00:00:01 -07:00
author_profile: true
header: 
  image: assets/images/badapple.jpg
  teaser: assets/images/teasers/marriage.PNG
  caption: "Credit to me and G" 
toc: true
toc_sticky: true
tags: [Drawing, Sketching, Dating, The Marriage Problem]
categories: [Art, College, Math]
---

"Just give up." — Prof. Andrew Sinclair

{% comment %}
<!-- write emojis, use *i* and **b** 

{% include video id="X_OfuZa3xcE" provider="youtube" %}

{% include spotifySong.html id="3hlGuz3loYoLfI3bpwieWq" %}

{:refdef: style="text-align: center;"}
![alttext](/assets/images/link)
Caption
{:refdef} 
-->
{% endcomment %}

## The Marriage Problem
In BEM 114, Hedge Funds, we learned about a version of *the marriage problem*:
- Suppose you will meet 1,000 potential partners in your life,
  - Assume that your compatibility with partners follows an i.i.d. uniform distribution between [0, 1],
- If you ask a partner to marry you, they will say yes,
- However, if you pass over a partner, you can never go back to ask them to marry you,

Given this, what is the optimal strategy?
### Backwards Induction
begins by starting at the end and moving up to the beginning of the problem.

In this case, if there is only one person left to meet, then this person will have an expected compatibility of 0.5, since we are drawing from a uniform distribution from 0 to 1. 

If the expected compatibility is 0.5, then anything over 0.5 is better than expected and under 0.5 is worse than expected. Essentially, we want to propose to anyone who is better than expected. 

Well, we know what to do if there's one person left, but what if there are more people remaining?

### Hard Part
If there is more than one person left, let's define that as N+1 people left, and the minimum compatibility that we will accept to be A. Let's also define the minimum compatibility we will accept at N people left to be B.

So, let's try to find A from B using some case-by-case thinking with a hypothetical A' which is a proxy for A:
1. If A' is less than B, we would just want B
2. If A' is greater than B, we want whatever A' is

So, when A' is in the range from 0 to B, we want B, and when A' is in the range from B to 1, we want A'. Let's try to find the average compatibility that we will accept across all A' then, since that will be A.

To get the average compatibility for A', we just average the **score we are getting** over the **cases where that score will occur**. 

{:refdef: style="text-align: center;"}
![backinductgraph](/assets/images/back_induct_graph.png)
Case 1 is purple (left) and 2 is orange (right)[^1], the areas together become A.
{:refdef} 

Specifically:
1. Purple is (B-0) * B, a square
2. Orange is (1-B) * A', but this is actually a trapezoidal shape (1-B) * (1+B) / 2, which is (1-B^2) / 2

Adding these, we get A = 1/2 + B^2/2. 

### Methods
Now, let's write a quick Python script to calculate this A for many steps, just modify N and you can run this code by just copy-pasting the below into this [online code runner](https://www.programiz.com/python-programming/online-compiler/).

```python
N = 1000 # the number of people left
B = 0.5 # the initial B
for i in range(N): # loop N times
  A = 1/2 + pow(B, 2)/2 # the formula described above
  B = A # restart the process with B set as A

print(f"Minimum comptibility acceptable with {N} people remaining: {B:.3f}")
```
This gives the following output with different N:[^2]
> Minimum acceptible compatibilities at 1 people remaining: 0.500
> 
> Minimum acceptible compatibilities at 10 people remaining: 0.861
> 
> Minimum acceptible compatibilities at 50 people remaining: 0.964
> 
> Minimum acceptible compatibilities at 100 people remaining: 0.981
> 
> Minimum acceptible compatibilities at 500 people remaining: 0.996
> 
> Minimum acceptible compatibilities at 1000 people remaining: 0.998

### Results
So, let's graph this result from 1 to 1000:

{:refdef: style="text-align: center;"}
![lineplotmarriageproblem](/assets/images/marriage_line_plot.png)
Line plot showing minimum acceptable compatibility at each remaining number of candidates in this variation of the Marriage Problem. I've also included a baseline for what some are willing to accept. 
{:refdef} 

### Discussion
So, as we can see, it rapidly goes from 0.5 to approaching 1, the model is saying, "If someone is not perfectly matched with you, then *just give up*."

Now, this weird outcome may seem like a problem with the model: there may be external factors that we are not considering or some problem with the process.

These are valid concerns, since it's unrealistic to not date anyone who isn't an ideal match, but the gist of it is that you shouldn't settle for less, and certainly not the *bare-minimum.*[^3]

### Acknowledgements
Thanks to Professor Andrew Sinclair for including this variation of the Marriage Problem in "Lecture 8: Fixed Income and LTCM" of BEM 114: Hedge Funds as bonus slides on backwards induction. 

If you are interested in exploring the code in a Python Notebook, check out this [Github respository](https://github.com/EngiTom/MarriageProblem) or this [Google Colaboratory Notebook](https://colab.research.google.com/drive/1Tibjt5GbpHYTlDhTLTs5PpzROxkjTzex?usp=sharing). 

If you don't know how to run code, I suggest going to the Notebook and pressing Connect in the top right and then pressing the triangle "Play button" on all of the code blocks. 

## Art is Observation
I got a bit distracted exploring that idea, but now we are back on track!

### JoJo's Reference
In Part 4 of *JoJo's Bizarre Adventure*, the manga artist Rohan Kishibe claims that 

> "Reality is the energy that breathes life into a piece of work, and reality itself is entertainment."

Despite Rohan's weird behavior, I agree completely with this statement because without understanding reality, or more specifically, *your reality*, you cannot portray that to other people to your fullest capability. 

### Learning Reality
Every time I learn how to draw something better, it feels really good. It's like the feeling of reaching into a jar of candy and pulling out two pieces of candy.[^4] 

For example, when I learned in a reel that you can draw noses simply by drawing some horizontal lines, I was completely amazed and needed to try it out. It actually went extremely well and 'm Ishocked by my abilities.

### Back to the drawing board
I've been drawing my friends on the Avery UGT lounge whiteboard and those have ended up being really nice drawings that I'm quite proud of. Obviously there are big improvements to be made like the shapes of things and their dimensions, but overall, you can get the vibe of the person just by seeing the picture. 

{:refdef: style="text-align: center;"}
![badappledrawing](/assets/images/badapple.jpg)
Snow White and her stand, "BAD APPLE"
{:refdef} 

My friend G drew Snow White on the board before I got to the lounge and so I turned SW into a JoJo's character with a stand. I drew a dwarf with a funny hat with a cotton ball on top and called it "7 DWARVES" but then I named it "BAD APPLE" instead, after the song "Bad Apple" from Dance Dance Revolution. 

{% include spotifySong.html id="57JRZbE80MLsYbmb24cPee" %}

I think that this was the peak of my art, but it's all based on my perception and observation of reality.

### Back to Work
Well, the moment has passed. Gotta go do my midterms now. 

## Footnotes
[^1]: In case you are colorblind
[^2]: I know it's off by one, but it doesn't matter
[^3]: Which some are known to do
[^4]: Or maybe I'm just conditioned to love drawing like a dog. 