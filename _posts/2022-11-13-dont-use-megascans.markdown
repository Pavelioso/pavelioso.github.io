---
layout: post
title:  Opinion - Megascans is not for everyone.
description: Prevent yourself from falling into the "Realistic Graphics" pit.
date:   2022-11-13 15:01:35 +0300
image:  '/images/owl_mountains_bunker.jpg'
tags:   [gamedev, thoughts]
---
## Try not to use Megascans as Indie. Hear me out.

I hope everyone knows what Megascans is. Ever since Epic Games acquired the parent company Quixel, and made them freely available, I've seen them overused and I have some concerns.

I still remember using Quixel products when they were mere plugins for Photoshop. Normal map generators, clunky texture generators - they paved the way for much easier texture creation. Before that, we used Headus UV layout to create UVs that were humanly readable, XNormal to bake out high to low poly... The whole process was a click fest, and making a quality texture was a lengthy process. And then, came Photogrammetry. Models, from real photos... I was going around old factories, taking thousands of pictures of different objects, reconstructing them in 3D through photogrammetry software. And some time after, came Quixel's Megascans. 

All of a sudden, acquiring realistic models became a lot easier, and so the game ideas became wilder.

Megascans were excellent quality assets for the time, since they were scanned in an environment with equalized lighting conditions (among other things). During our development, we jumped on Megascans heads on, since we believed that "the more realistic graphics = more attention and sales" rabbit hole. But soon after we realized what we got ourselves into.

![Most of assets here were scanned from old factories in Prague.]({{site.baseurl}}/images/owl_mountains_1.jpg "Owl Mountains Bunker")
*Photogrammetry was used to scan and create these objects that we found in deserted factory.*

![We found and scanned an old bunker.]({{site.baseurl}}/images/owl_mountains_bunker.jpg "Owl Mountains Bunker")
*We used photogrammetry to scan a bunker.*


The images above are a few examples of environments that I was working on with our own scans.
They look great once you look at it from one angle. But his is a computer game goddammit, and the player has to walk around! 

When we started using hyper realistic 3D assets, soon it became quite visually obvious, that we need to have the characters also hyper realistic, and even if we wanted to, it didn't end there - let me just not down what else had to be realistic: modular models, all other models, particle effects, sound, light, light bakes, atmosphere, dynamic lighting, model scaling... pretty much the whole game.

Anything that was a bit off, just didn't fit with rest of the scene, and this started to pose a big issue for the visual fidelity of the world and the scene.

Instead of focusing on game mechanics, game pacing, game design, we were just making realistic levels. Instead of prototyping and boxing out level designs, it was more important what actual 3D scan assets we had available. Modelling anything that was missing had to be done by hand, and because it had to look as realistic as the 3D scan assets, it became extremely lengthy process to make one model, and our motivation started sinking. Slowly but surely, 3D scans started deciding on how the levels should look like, feel like, and play like.
We fell into the 3D scans' asset trap.


![We found and scanned an old bunker.]({{site.baseurl}}/images/bunker/owl-mountains-outside-2.jpg "A rock.")
*Photoscanned rock from a forest. Now all rocks have to look good.*


> If one rock looks hyper realistic, everything has to be hyper realistic.

**Prototype the game first, then choose a style later**.

Therefore, I believe Epic Game's decision to release all scans for free is an amazing opportunity to learn from, but it can become a downwards spiral for small indie studios, that will slowly start eating up a lot of the team's budget, when they will try to equalize the in-house asset quality with the scan's quality.

If I work on any project, I always ask - is there budget for realistic graphics? There usually isn't. Only the top dogs got the budget for it, hundreds of talented artists, creating a game, that will be marketable and better than the last. But indie studios do not have to do this!

Therefore, try to look at the game design, level design of the game, and find a way to create something original. Maybe the graphics can be done from pen drawings. Maybe, the design can be flat textures with a lot of decals. Or the style can be cartoony? Don't like it myself, but maybe low-poly? 

I am going to write in more detail about visual stability of a scene a later posts. But it is important to think about, why does Half Life 2 still looks quite realistic? Why did Firewatch use the style they did? Why does Blizzard's Overwatch is styled as it is? 

> Realistic graphics aren't important. The entire feel of the game is.