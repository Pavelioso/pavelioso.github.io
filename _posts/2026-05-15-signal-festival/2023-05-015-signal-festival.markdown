---
layout: post
title:  Prague Signal Festival Interactive Wall
description: A 3D camera based interactive projection wall. 
date:   2026-05-15 15:01:35 +0100
image:  signal_short_clip.mp4
fallback_image: signal_fallback.jpg
tags:   [programming, events]
---


<p><iframe src="https://www.youtube.com/embed/2X6Iw7lBXww" frameborder="0" allowfullscreen></iframe></p>


I don't have many screenshots for this project, but I was approached by Prague's 3DSense to program interactive full year installation for Prague's Signal Festival. 
This installation was designed for kids to play with spheres projected on a wall, where different "themes" were avalaible, switching the gameplay in each theme. 
Programmed in Unity, some features:
- Input is from a 3D depth camera.
- Various modes, prepared a command UI to be able to fine tune everything directly on site. 
- The 3D skeleton tracking is smoothed out with Unity's game time, making the sphere's physics calculations and the skeleton movement aligned - meaning the physics work actually as expected and reliably (otherwise if the player touched a sphere, the sphere would sometimes just fly away).