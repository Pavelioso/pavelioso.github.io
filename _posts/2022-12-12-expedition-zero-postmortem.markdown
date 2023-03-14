---
layout: post
title:  My First Indie - Expedition Zero - Postmortem
description: A little step back to look at developement of my first indie game.
date:   2022-12-12 18:05:55 +0300
image:  '/images/ez/expeditionzero-keyart-nologo.png'
tags:   [gamedev, ideas]
featured: true
---




<p><iframe src="https://www.youtube.com/embed/OHhpW-nZVms" frameborder="0" allowfullscreen></iframe></p>

[STEAM STORE PAGE](https://store.steampowered.com/app/1247570/Expedition_Zero/)

My biggest game dev project yet. Since I've spent few years making it, it is a shame that the reviews are not that great, and that it didn't sell well. So I thought, why not have at least a little postmortem, and write down my opinion on what didn't work, and maybe others can learn.

> It's not that hard to make games, just put some models in there, make it move, and done, no?
>
> <cite>Me at 22 years old</cite>



Expedition Zero is a game where you are trying to get out of a walled off zone. While you meet a mysterious trader, you are tasked with killing a monster in exchange for a ticket out of the zone. While on a mission, you need to survive harsh conditions, cold and radiation.

We started developing this few years back, and we went through multiple concepts and MVPs to see what fits the best. Because of time constrains, we had to throw most of the stuff away - for example sled that you could take with you and modify, food and water, sleeping, day and night cycle. 

Here are my thoughts that I would relay to any other game dev.

![GIF]({{site.baseurl}}/images/ez/EZ_gif_1.gif)

## Have fun gameplay mechanic first.

It doesn't matter if your game is going to have top notch graphics. It doesn't matter how good looking of a trailer you make, no one is going to give a sh*t. You need gameplay mechanics and gameplay trailers, so it looks fun to play. Gamers want to play, not to watch a movie, they can go to Netflix for that. Most of successful developers that I have seen post short videos on twitter or youtube with mechanics that differentiate their game from any other game that gets released on Steam. There is more than 300 games getting released on Steam a month, and with free availability of tools like Unreal, there is going to be more. Everybody wants to be gamedev right?
That being said, starting with the core mechanic of a game is the most important rule I can ever give to anyone. Start with white level, block out some shapes, and get going on the stuff that's going to make the game fun.
Here, I will give few examples.

#### Example - The Vanishing Of Ethan Carter
One might think that graphics is the main gameplay pillar, but in my opinion it's exploration, puzzle, and story telling. The way to create first version to test the mechanics would be:
- Create a blockout level for the player to explore and for the player to get "just enough" lost in.
- Create a fun puzzle system for the player to solve.
- As a reward, player listens to a new part of a story -> New progress unlocks.

#### Example - Long Dark
One of the most challenging games I've seen to create. To balance out survival so well, like in Long Dark, must have taken many iterations and balancing. It's one thing to spawn and item, but generally as a developer you can't just leave it on chance. The player needs a little help sometime, for example if the player is starving, maybe we should spawn piece of food around him, so the player doesn't get frustrated? Or maybe the player has too much food in inventory? Well we can stop spawning food all together. And what about distances between houses and points of interests? Is it not too far, can the player actually make it? What if it's too cold? Again, so much balancing... But in order to have tested fun gameplay mechanics, these are the steps I would do. 
- Create large landscape level with demo trees, create few blockouts of houses, place them around with different distances, to test what is too far and what is too close.
- The hardest part, but create a survival system, with editable SCV or any kind of table where values are easily adjusted. Survival includes basic crafting, food, sleep, cold.
- Create comprehensive game panel from which the game can be controlled and different systems and values can be triggered (trigger wind, temperature, change value of hunger, sleepiness) so during gameplay another developer can act as a "dungeon master". 
- Test on the map, adjust and test.

![GIF]({{site.baseurl}}/images/ez/EZ_gif_2.gif)

## Prepare Project's Architecture

It is easy to pop up YouTube, and start replicating "how to make a light switch" tutorial. Generally, tutorials have extremely bad architecture - such as placing logic into a level's "Begin Play" in UE. But there are barely any tutorials that talk about architecture. So, making a light switch is easy - but making a light switch a part of a game's system? That is a different ballgame. 

Therefore, it is important to sketch out exactly what a light switch going to be doing, and what are the features that it needs.
Maybe:

- There are two or more light switches connected to one lightbulb. How do they know about each other? 
- Three light switches control five lightbulbs. Does one light switch just loop through all light bulbs and changes bool value or is there something more effective?
- The light's status needs to be saved. Does it save per lightbulb, or can we create "light manager" instead that saves status of all bulbs and switches? Other actors should be saved too, so do we create general "save manager" instead?
- We need to add in electricity. Should we create "electricity manager" that all classes report to and check if there is enough electricity?
- What is the master class? The project will have different lights, LEDs, halogens, round, spotlights, etc. How do we design a master class for lights and switches?

Those are just a few examples about a light switch. But this also has to be done with character, levels, secondary systems, etc.

![GIF]({{site.baseurl}}/images/ez/forest_gun.gif)

## Developer's Console and Ability to Save Game as Developer

At one point of testing it will be very important to have as many tools prepared to be able to test a game mechanic properly. This, in our case was often overlooked, and was added in later, which would have eased our testing exponentially. This also includes saving - it is very important to be able to save game as soon as possible, so as a developer, you can resume from whichever point in game, and test whatever needs to be tested. 
Therefore, when we code, we automatically create ways to be able to call functions or change different values dynamically from a widget that can be called "Developer's Console". Developer console can have many tabs, such as weather, character, spawning, etc. I cannot stress enough how much easier it is to test and balance game mechanics when this is prepared.

![GIF]({{site.baseurl}}/images/ez/monster_fight2.gif)

## Keep Documentation

People can come and go, maybe someone will get sick, something needs to be fixed quickly, or the developer just forgets how a certain feature works after 1 year of not looking at it. Therefore, it is essential to keep documentation. Every time a new feature gets implemented, we immediately go to documentation and write down how it works. Then, when something needs to be changed or fixed, it is much easier just to search in documentation, rather than trying to understand the whole code in-engine. 

![GIF]({{site.baseurl}}/images/ez/plane.gif)


## Have clear goals and project structure, review any new features.

Either you do sprints, or scrum, it doesn't matter. The team needs to know what has to be done. One of the most frustrating things for developers is to wake up, sit by the computer, and not knowing what to do, while time is just passing. 
Having clear project management structure is also essential, and a good project manager that makes sure that every new feature is properly tested and review will help the development tremendously. 


# I hope that some of these thoughts of mine will help anyone that goes through development. Have a good day!






