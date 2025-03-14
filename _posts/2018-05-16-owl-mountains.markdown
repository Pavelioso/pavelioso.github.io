---
layout: post
title:  OWL MOUNTAINS - Art Direction and Game World Concept
description: Check out a concept for a game world, complete with art direction.
date:   2018-05-16 15:01:35 +0300
image:  '/images/bunker/bunker-lights2.jpg'
tags:   [concept, gamedev, thoughts]
featured: true
category: gamedev
---

## It's year 1979,
 northern Czechoslovakia, under the communist regime. Karel, of 65 years, a history teacher, is sitting in his home, looking out the window with cigarette in his hand. The weather outside is murky, it's almost raining. Clouds are gray, blending in with the surroundings buildings, painted dark from coal smog in the air. Karel remembers the time before the regime - the freedom that he possessed for few years. He always remembers, it's always on his mind, like a worm stuck and growing in his brain. Karel isn't a revolutionary. He prefers to stand in line, never thought of himself as anything else than a teacher in a small town school on a northern border with Poland. His fascination with history allowed him to possess deep understanding of when and where, but, he himself, rarely ever left his small town of Hronov. He never used that knowledge for anything. 

<p><iframe src="https://www.youtube.com/embed/9LXRBHtphPw" frameborder="0" allowfullscreen></iframe></p>

## Something has to change in his life...

Karel can no longer just stand by, and watch his life dissipate right in front of his very own eyes. He does have something on his mind, but he never went through with it. Always thought of it as an option that he will do "eventually". Eventually, his time to be the explorer. The adventurer, the rover. Though, as a historian, he himself wasn't sure if the underlying information, the main pillar holding up this idea of his, is real or not.

Is the hidden Hitler's underground city in the Owl Mountains real? A massive complex, dug from the core of the mountains, as a hideout for the Hitlers elite, was it even built or was it destroyed? He needed to know. This was the time to make the decision. Karel, through his own doing and his own thought, stopped, and realized that his heartbeat is pounding. He is stressed, because he knows that the decision has been already done, and he cannot undo it. It is the time, to finally set off to Owl Mountains.

<p><iframe src="https://www.youtube.com/embed/BCXLWvrWLHE" frameborder="0" allowfullscreen></iframe></p>

## The Visual Style of Owl Moutains.

A little of a history here: The Owl Mountains is a supposed nazi bunker complex that could house thousands of people, and it was build in southern Poland, in Owl Mountains, on a border with Czechoslovakia. There are a lot of stories and myths around this bunker, and it is a perfect environment and setting for a linear horror adventure experience. These stories are sometimes not so nice, though, it is a perfect opportunity for a game designer to feed off for inspiration.
- Apparently this complex could have thousands of people inside, but most is unknown, because of lack of documentation. This sets up the game to be "technically possible".
- It is told that Soviets blew up the entrances to the complex, trapping all the present populace inside. This is great setup for enemies that player might find in game. 
- There are stories that a Nazi "Bell" was present, which was supposedly used to enrich uranium. This gives opportunity for the typical trope "radiation = mutated stuff around". 
- The only thing that can grow in darkness are mushrooms. What if the people trapped inside actually survived on mushrooms?

![Bunker]({{site.baseurl}}/images/bunker/bunker-08.jpg)
*Bunkers, riddled around the border.*

## A little word from me.

It is important that a story develops in an environment that supports it, and is a bit grounded. Dead Space games make sense, it feels "real" and the setting supports the atmosphere - the setting is carefully crafted so nothing seems to be off. Of course, you play as an engineer that uses sci-fi tools to kill monstrosities in zero-g, though it does feel real. The world building makes sense. Another example with Half Life 2. The world feels real, there could be an invasion of galactic faring species, that slowly start assimilating yet its another victim - humanity.
In this game concept, we are playing around with topics that just beg to be source of inspiration. But to keep the concept grounded, I gathered as much of information, and connected that information into this environment setting and potentially the environment's story:

![Bunker]({{site.baseurl}}/images/bunker/bunker-01.jpg)

## The Environment's Story.

The Owl Mountains bunker complex's entrances were blown by Soviets, trapping all inside. Mass panic ensued, all were fighting for food, light, and survival. After all resources were depleted, cannibalism became common. Though few survivors started cultivating a special mushroom, left over in one of the kitchens, a supposed delicatesse for the Reich's elites. 

Now, the mushroom acting as the only source of food, it needed to grow from something - the cultivators used dead bodies as substrate. Morbid but functional. After years being stuck in darkness, human flesh and mushroom as the only source of food, the survivors were psychologically long gone. To try to dig yourself out was impossible, the noise attracted any that wanted to use your body as a source of nutrition or as a substrate. But yet another horror slowly grown in the background - the mushroom that ultimately saved many started spreading, changing, ever hungry now for what it was used to - for human flesh. It also is found out that a "Nazi" bell is present in the complex, spilling out irradiated water, which seeped through the entire bunker complex, killing everything is its path, and worse of all, mutating the mushroom. The mushroom started to devour the entire surviving populace, growing through wall cracks and crannies, almost as if the mushroom became a stomach, and everyone was in it, being eaten alive. 

With most people dead, or mutated and crazed by the mushroom and the environment, Karel arrives to the complex through a crack in the mountain. In this extremely hostile environment, he has to survive, explore the complex and find a way out. Few inside are still a bit sane, and start talking to Karel through pipes and intercoms, that there is a supposed "hidden golden exit", for Hitler himself. Through Karel's help and knowledge, they will try to rediscover this golden exit, and try to get out.

![Bunker]({{site.baseurl}}/images/bunker/bunker-02.jpg)

<div class="gallery-box">
  <div class="gallery">
    <img src="/images/bunker/bunker-03.jpg">
    <img src="/images/bunker/bunker-04.jpg">
    <img src="/images/bunker/bunker-05.jpg">
    <img src="/images/bunker/bunker-06.jpg">
    <img src="/images/bunker/bunker-07.jpg">
    <img src="/images/bunker/bunker-09.jpg">
    <img src="/images/bunker/bunker-10.jpg">   
  </div>
</div>


## The Environment Creation Pipeline

The environment in this case is designed around the fact that small indie team would be in charge of production. This means that the fastest and easiest means of production were researched, in order to stay within supposed budgets but still keep the visual quality. Therefore, through R&D, I have concluded that:

- Models need to be modelled with UV unwrapping in mind - should be as easy to unwrap as possible (for example leave the polygons when should be seams disconnected, more vertexes, but much faster unwrapping speed).
- No high to low baking of models. Making two models for one has priority.
- Normal maps should be auto generated, but very flat, almost not present at all.
- No roughness maps, except for very metallic objects or wet vertex painting for puddles.
- No auto generated textures - It is fast, but textures are what will make the models pop in this case, and they have to look natural.
- Good hand UV unwrapping is essential, so it's readable in photoshop (straight polygons, seams should be in natural and hideable places...) 
- Depending on the size of the model, automatically the artist should choose corresponding texture size (for example door 1024px, and a cup should have 128px) to keep the scene pixel density uniform.
- Preselected source textures and decals are chosen. A bunker is build from one concrete material in real life, this means that textures are going to have one concrete material. Same with wood, metal, paint. Decals are created for leaks, rust, holes, words, numbering, etc. All of these have to fit together and must be interchangeable. 
- Textures should be made in photoshop from scratch, from pre-selected textures, finished of with decals that would be in natural places, and dirt.
- Main structure models have to be modular. 

Following this set of instructions, few scenes were created to check the speed of the production, and the general atmosphere and vibe.




![Bunker]({{site.baseurl}}/images/bunker/bunker-lights3.jpg)
<div class="gallery-box">
  <div class="gallery">
    <img src="/images/bunker/bunker-lights1.jpg">
    <img src="/images/bunker/bunker-lights2.jpg">
  </div>
</div>

## Thank you for reading my take on this environment and story. The scenes are not perfect, but what does interest me the most is to develop a workflow that is efficient, while still keeping the desired visual quality.

<div class="gallery-box">
  <div class="gallery">
    <img src="/images/bunker/bunker-prison_1.jpg">
    <img src="/images/bunker/bunker-prison_2.jpg">
    <img src="/images/bunker/bunker-prison_3.jpg">
  </div>
</div>

