---
layout: single
title: "Change is Good"
date: 2023-04-16 00:00:01 -04:00
author_profile: true
header: 
  image: assets/images/beetle.png
  teaser: assets/images/teasers/beetle.png
  caption: "Photo credit: Dalle and Me"
toc: true
toc_sticky: true
categories: [Freetime, Growing Up]
---

"There are some things you can only find in a messy room" — Yuto Suzuki, "Chapter 100: Lightning Strikes" in *Sakamoto Days*

## Audience
>"The village, to grandfather." — Anton Chekhov, "Vanka"

I didn't know that so many of my classmates read this blog, but I'm happy that they enjoy it. I have always written with the assumption that people read my blogs so I do try to refine some of my ideas before I put them on the internet forever. 

## Let him cook
Near the start of spring break, my mom went to China. A few days before she left, she passed the responsibility of cooking for me, my sister, and my dad, to me. 

As my sister said, "It's ur housewife era."

Now, many people I know have been cooking for themselves for many years, so they are probably unfazed. And actually, one of my friends said, "Welcome to the team," when I told her. 

Nonetheless, I have only made a few types of food (mostly) by myself:
1. Egg fried rice
2. Stir-fried egg and tomato
3. Salmon, avocado, and cucumber sushi

My experience is very limited, as you can tell.

However, here is my very vague understanding of stir-frying vegetables:
1. Wash 3 times
2. Chop
3. Add oil to pan, wait for vapor
4. Insert vegetables
5. Stir-fry
6. Add water if needed
7. Add salt + taste

I hope I will survive. 

## An update on my cooking endeavors
I have washed and cooked vegetables for myself quite a few times now. I've improved at it by quite a lot, but I still burn the vegetable sometimes if I have not cooked it before. However, I am getting a sense of when I should stop cooking. I haven't undercooked anything yet, but I assume that I will do it at some point. 

The time before adding water is most crucial because if missed, the food will burn and be undercooked at the same time, which is possible because the outside cooks faster than the inside. This can be mitigated by stirring the vegetables faster so that each piece gets contact with the pan before another piece takes its place. For me, since I cannot sense when it's done, I just wait to see a small burn and then add water. 

## Growing up
My dad recently showed me a picture of my 8th grade graduation, and I once again learned that time flies. I think I've changed a lot since then, but many of the things I've learned have been internalized, so I couldn't even teach my younger self to be like me even if I wanted to. Perhaps it is my fault for forgetting what I've learned, but maybe that's just part of growing up. 

If everyone knew exactly how they had changed, then they could always revert back to how they were before the changes happened. By turning my experiences into part of my subconscious, it cannot be reeled up to the surface. So, perhaps it is better to not know. 

## Changing for whom?
Something I've learned is that people only change selfishly. When people change for others, there is always a sense that they are owed something. Something is fundamentally wrong, like 

However, the other person is unaware of this and will proceed as if nothing happened. This miscommunication builds resentment and strains the relationship. Eventually, the change will revert.

## Diamond is Unbreakable
One of my great achievements over break was getting diamond in League. 

I was able to achieve this goal mostly because I had a lot of free time over break, but also because I improved my gameplay a lot over the years. There are many principles that I've learned from playing every role. The most important tip I have is to try to learn the limits of what is possible for every character. 

For example, many characters rely on hitting a projectile ability, so if you know the range of it, you can wiggle on the maximum range and bait out the ability. If you know which fights you win and you have the skill to dodge and land abilities, then getting a higher rank is very possible. 

This is something that I have wanted to accomplish for many years, so I was quite nervous in the final promotion game, but now that I am diamond, I can finally buy noodles in China at those shops that give discounts for being high rank (I don't know if they are real). 

The character that I attribute this success to is Kha'zix, a purple grasshopper/beetle with sharp claws. One of his main quotes is, "Change is good," so it's interesting how I picked him up after writing the previous section. 

## Song search
In 5th grade, I heard my brother play a fingerstyle song on guitar that sounded really nice but one that I never knew the name of. Recently, I hummed it into the Google app's song humming search service and found it. I get extremely obsessed over finding songs, so this was a big relief. However, the song doesn't sound as good as I originally thought, which is a shame. 

{% include video id="vlj0SzNVB6s" provider="youtube" %}

I also found this song for my friend:
{% include video id="S2oxFIsENgM" provider="youtube" %}
This song was pretty popular a few years ago, but the beginning is much more popular than the rest of it so it was pretty easy to find. 

Some people in the comment section found it by just typing "Mmmmmmmmmm" into the YouTube search bar, which surprisingly works. 

## My Projects
I am currently working on a physics simulation suite, and it is going decently. I completed a lot of the content already, now I just need to add instructions.

I am also doing an biostatistics internship, and I finally wrote and ran the code to record which residue combinations in different chains are interacting. I knew that the search would take a long time because it is a seriously bad O(n^2) algorithm, scaling with the number of atoms in each chain. However, I didn't realize that it would take 8 hours! 

### Annoying auto-update
The first time it finished running, I was asleep and my computer automatically restarted and updated. So, my notebook runtime ended and I could not do anything. So, I reran the program the next day and got the results, so it's all good. 

Actually, there was a bug the first time I ran the code. I was breaking out of one extra loop and my loops were in the wrong order, so I rewrote the program at 6 AM the day of the restart and then went back to sleep and then ran it at 10 AM when I woke up for real. 

The loops should be in this order:
```python
for residue1 in chain1:
  for residue2 in chain2:
    isinside = False
    for atom1 in residue1:
      for atom2 in residue2:
        if close:
          # Record residue combination in dictionary
          isinside = True
          break
      if isinside:
        break
```

So, that was a learning experience. 

## A New Friend
I met a future classmate J who plays League and is from Toronto. He only plays hard champions which is pretty interesting.

I met another classmate J who had a lot of praise for me, which reminded me of an important lesson.

### Keep the critics
Out of the group of people that a person willingly interacts with, most of them will already share the same opinions. However, it is important for people to be near those who will criticize honestly. Of course, after a "negative interaction" people are likely to feel bad about being criticized, but after a while, a reasonable person will take it to heart and change. 

For example, in a Plat 2 League game, I was criticized by a very salty, ill-mannered player who said I had low CS numbers + hardstuck. Initially, I was very mad; however, I realized that he was right about my CS numbers. 

So, I improved my CS... by changing back to playing jungle (a role that doesn't need to CS). And now, I'm diamond and that guy fell down to plat 3. So, I came out on top. 

Now, whenever someone criticizes me, I cut out the bad intentions associated with it and only focus on whether the criticism is true and can help me improve. 

There are two ways of becoming better at anything: 
- Bolstering your strengths
- Fixing your weaknesses 

The latter of which only comes from self-examination and awareness. Of course, there are two kinds of people you can be around:
- Those who praise your strengths
- Those who mock your weaknesses

Obviously, people don't like the second kind. But, just because someone doesn't like you doesn't mean what they say isn't true. 

So, do not let your ego get in the way of becoming better. 

### Observation
Of course, you can also learn from observation and judgement.

There are two types of people you will observe:
- Those who are better than you
- Those who are worse

Of course, people like to think that being around people who are more proficient will bring themselves up. However, seeing the mistakes of those who are worse will reveal what not to do. Of course, after that, you can easily do the opposite. 

Be sure not to become too attached to the idea of "They are worse = I could never make that mistake." You might even find that they do some things better than you expected. Creating a fundamental separation between worse and better doesn't make sense because that is only on average. There could be many discrepancies at any point, so associating with absolutes will not lead to learning. 

I will spare you the LoL analogy for this one. 