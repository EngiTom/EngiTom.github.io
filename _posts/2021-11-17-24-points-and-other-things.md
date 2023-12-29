---
layout: single
title: "24 Points and Other Things"
date: 2021-11-17 19:00:00 -05:00
author_profile: true
header: 
  image: assets/images/shubham-dhage.jpg
  teaser: assets/images/teasers/shubham-dhage.jpg
  caption: "Photo credit: [**Shubham Dhage**](https://unsplash.com/photos/TbhRAV5xDtA)"
toc: true
toc_sticky: true
categories: [Personal, Games]
---

Hey there, I'm back for another post on this cloudy Wednesday. 

## Savings

It's actually been so long since the last post that [Daylight savings time](https://en.wikipedia.org/wiki/Daylight_saving_time) (DST) is over and I am back to UTC-5. 

In addition, it's interesting that America still has DST after such a long time. I think it had something to do with [saving energy during wartime](https://www.timeanddate.com/time/us/daylight-saving-usa.html), but I have some speculations as to why it still remains. 

It's very hard for large groups of people to make changes, but it is quite easy for people to adapt. If people can be convinced of a critical situation, they will try to make the situation better. 

For instance, FDR called DST "War Time" which is mega dramatic and shows how it was seen. Of course, steps were then taken to attempt to accomplish that goal. 

I don't know if DST actually accomplished that goal properly, but no one really cares anymore because there is no more crisis. So, why would ordinary people care to change back when there is no severe reason to do so?

## 24 Points

I recently downloaded an app for a math card game known as "24 Points," the "24 Game," or, in Mandarin, "二十四点." It was made by one of my old classmates from Shanghai. He's quite the programmer and introduced me to [Huffman encoding](http://web.stanford.edu/class/archive/cs/cs106b/cs106b.1178/assn/huffman.pdf). 

Essentially, four cards are drawn from a deck of 52, and the player is allowed to use the basic operations (+, -, *, /) in a combination that includes all four cards drawn, in any order, to end up with a result of 24. Operations can be used repeatedly, in any order, or ignored. 

For example, if you draw 3, 3, 8, 8 (a hard combination), you can write the expression, 8/(3-8/3).

The first time that I played the game was in middle school back in Shanghai. This game might be one of the most interesting simple games out there. A friend of mine actually has played dozens of thousands of rounds, meaning he has seen every playable combination of cards several times. Personally, I've gotten a bit over 1000 in a week. It's been a great warmup for my brain during breaks in class. 

In fact, during the AMC 12, I noticed that I could do subtraction in my head a lot faster, probably from trying to see different combinations that would work. I probably got around 13 questions right due to not knowing a lot of the theory behind some of the angle-related problems later on. I think it isn't so bad considering that I didn't prepare. 

I introduced the app to a lot of my classmates, who are kind of hooked on the game now, at least from what I can see. 

## New Friends

I am currently attending an online summit by a school in France that has invited students from around the world. I am actually learning a lot about different cultures in this event. For example, that some countries, like Spain, do not have after school clubs, and others allow students to choose the core subjects they want to pursue during high school. 

One French student said that, because she does not enjoy math, she can just opt out of it and focus on others. I feel like this system definitely has some advantages for specialization, but specialization is not necessarily a completely good thing. 

On the first day of the event, it was really quiet, but it definitely got a lot nicer on the second day. I feel that is the major goal of online meetings: to make it as "warm" as possible. I actually have another story that I just thought of about when I taught Python during the summer of 2020, so that will go on the list of future topics. 

I also met a very kind peer from Scandinavia that has a similar background to me, so it was definitely very nice to be able to relate to someone on that kind of level. 

Notes from 8 months in the future: always communicate intentions clearly in all relationships, do not grip tightly onto personal perceptions, and keep small talk to the first week. 

## USACO

I am back on the USACO grind after a long hiatus, and I am glad that I can still remember some concepts from silver. I was worried I would have to start from bronze again, but I don't think that will be necessary. Hopefully, I will be able to get to gold by around January. 

The problem I'm currently working on is [this](https://codeforces.com/problemset/problem/632/C). I guess the main issue is that I don't know how to sort these strings in alphabetical order. Putting the sorted list of strings together is the easy part. However, I guess alphanumerical strings are secretly just base-26 numbers (take a moment to ponder how), so that idea will definitely help. 

Now the problem becomes setting up the comparison function, or, "What is the fastest way to compare two strings?" 

I would suppose something to do with comparing each letter of both strings from left to right. If one is bigger then just end it there. However, if by the end of one string it is still the same, I'm not too sure what to do.

Ok, I figured out that it might be to compare the letter immediately after the ending of one string to the first letter of both strings. 

I looked at the first sample again and realized that this only works for non-repeating situations. So, it should actually be the first different letter from the starting letter after one string ends. 

Alternatively, I could just put the two strings together in the two possible combinations and then see which one wins. This would take up some memory and time though in most cases. Assuming that one str was 50 long and the other was 49 with both having the same letters in the first 49, then it would take about twice the time to do the second method compared to the first. 

Whatever, I'll do it tomorrow, cy@.