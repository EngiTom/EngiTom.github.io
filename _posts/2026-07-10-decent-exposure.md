---
layout: single
title: "Decent Exposure"
date: 2026-07-10 00:00:01 +08:00
author_profile: true
header: 
  image: assets/images/numba.JPG
  teaser: assets/images/teasers/numba8.jpg
  caption: "Credit to Me" 
toc: true
toc_sticky: true
tags: [Exposure, Hong Kong, Anthony Bourdain, Japan]
categories: [Singapore, Photography, Advice, Food]
---

"I don't get it, what's the kick?" — Saul Goodman *Breaking Bad S2E8*

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

{% include spotifySong.html id="1NYXrU1mlnnoV6k2p1xBl8" %} <!-- Worlds Away -->

## Picture That
I've been trying to shoot in manual mode on my Sony Cybershot HX7V, because the "intelligent auto" mode can only get you so far. There was a moment where I tried taking a picture of these spherical street lamp next to the water at Boat Quay and couldn't get it to look the way I wanted because I was shooting on auto mode. 

So, attempting to get the lights looking the way I wanted, with a nostalgic warm, orange blur that reminded me of the spherical lamps in Shanghai next to the river, but also the P-orbital lamps at Beckman Auditorum, was basically a gamble based on where the camera would choose to focus. 

{:refdef: style="text-align: center;"}
![lights1](/assets/images/goodlight.JPG)
1st picture
{:refdef} 

As it turns out, none of them were as good as the first photo.

{:refdef: style="text-align: center;"}
![lights1](/assets/images/light5.JPG)
5th picture
{:refdef} 

However, this experience did make me appreciate the depths of photography much more, learning about the exposure triangle and how I can improve at getting the desired look. 

As for the theme of the picture, nostalgia, I like that one of the lights is broken, since it shows that in every image of the past, there are blurry details and blind spots. 

## Data Analysis Blog
This was originally supposed to be some kind of educational data analysis blog, but it's clearly turned into something else much better. 

### Nice Weather?
I'm going to Osaka next weekend, and Beijing the next. 

I was trying to book tickets when I would be less likely to be hit by a typhoon, but I didn't think there would be much point because I need to buy somewhat early to prevent from high flight/hotel prices, and there was not enough information available to estimate when the next time the typhoon would hit. 

However, things just got serious because I found a [Japanese typhoon dataset](https://agora.ex.nii.ac.jp/digital-typhoon/ibtracs/WP/), and I'm going to do some data analysis. 

First, I want to count the number of typhoons that hit the NW Pacific in mid-July, so basically, I just took the start and end dates and got the number of typhoons in each year that overlap with July 10-20. 

{:refdef: style="text-align: center;"}
![typhoon_midjuly_graph](/assets/images/typhoon_graph.jpg)
Looks like climate change is real.
{:refdef} 

So, seems like we have a good chance of not getting hit because every time there's a year with 6 typhoons in mid-July, it usually drops to a small number the next year, although climate change might cause some issues. 

Instead, let's try to look at the time between typhoons. I make the assumption that we can just use the midpoint time of the hurricane to mark them, which I think makes sense because it's probably around the middle of the hurricane that it would hit anyway, the end will be out in the ocean and the start would be also in the ocean somewhere and weak. 

I apply some filters here like: 
- date must be after 1891
- gap must be less than 30 days

And I get this histogram:
{:refdef: style="text-align: center;"}
![intertyphoon_time_hist](/assets/images/typhoon_gaps.jpg)
Seems like typhoons are typically 5 days apart in July, wow!
{:refdef} 
 
I guess this means that there's no point in planning ahead for typhoons... Oh well, at least this was a bit fun. 

### Reality
I seem to be flying around one of the biggest typhoons in decades, [Typhoon Bavi](https://en.wikipedia.org/wiki/Typhoon_Bavi_(2026)) which is a "category 5-equivalent super typhoon." 

On the bright side, it's not going to hit Osaka. Hopefully the flight can be safe and not delayed, which might be a lot to ask for in a category 5 storm.

## Parts Known
After binging so many Anthony Bourdain YouTube videos, I really want to express my view of foods and places through a video format, because I think I would do a pretty good job. 

Also, I think it's one of my 2026 resolutions, and 2026 is almost over (it's July, buddy). 

### Conundrums of Philosophy
My main problem is that I'm not sure how to get talk on camera without ruining my ability to be in the moment. 

I think what Anthony Bourdain does is probably voiceovers after the events actually happen, but he writes notes when experiencing things, which I might need to do as well. 

{% include video id="2LyJtouQfFU" provider="youtube" %}

Watching this video really made me want to buy a plane ticket to Hong Kong to eat the food and vibe in the city.  

Christopher Doyle is also an amazing guide to Hong Kong because he basically defined the way that people view it, and his perspective and aesthetic is what defines the city even more than reality itself. 

### Place, Japan
It reminds me of this meme: 

{:refdef: style="text-align: center;"}
![placejapan](/assets/images/placejapan.jpeg)
"Place, Japan" Meme
{:refdef} 

The point of this meme seems to be that Japan is overrated because it's possible to find basically roughly the same types of places in other countries. 

And that point is not entirely wrong, because people tend to underappreciate things about their own country and idealize other ones. 

However, what the meme misses is that there is a legitimate appeal to the Japanese culture and aesthetic. If the world were a game of *Civilization*, then Japan would have won a "Cultural Victory" by now, and Hong Kong is only a few steps behind Japan. 

### In the Mood for Food
I really like this quote from Doyle in this episode: 

> So-called beauty is not "my make-up is so good and then I lifted my face a bit." No, beauty is the darkness and the pleasure of embracing that and giving you more of your experience of life.

I'm not exactly sure what the second half means, but I do know that beauty is not as simple as appearances. 

## Madeon
For those who don't know Madeon, he's Porter Robinson's French best friend and they made "Shelter" together, which means he's definitely not bad at making music.

{% include spotifySong.html id="7vm3Z78elWY11Xl6MNuXng" %}  <!-- Be Fine -->

Above is my current favorite song from him. His songs on this album have a very strong beat and somewhat gospel-like aspects which he incorporates into sort of old-school French EDM/Daft Punk melodies. 

### Victory 
His new album, *Victory*, is really good too, but it's more like a high-energy grungy, punk rock/hyperpop EDM album. I think I like basically all the songs except for "Super Platinum" which just doesn't sound good

{% include spotifySong.html id="09T22xu0U9AW2d3s8T3OwE" %}  <!--Enjoy -->

"Enjoy" is my favorite song from the album currently because the bridge after the second chorus is one of the greatest bridges I've ever heard in any song. It kind of reminds me of Carly Rae Jepson or maybe like "Africa" by Toto. 