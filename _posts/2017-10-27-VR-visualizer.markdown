---
layout: post
title:  VR Vehicle Visualizer
description: A VR optimized vehicle visualizer!
date:   2017-10-27 15:01:35 +0300
image:  '/images/vehicle-vis/carvis-spaceship-2.jpg'
tags:   [VR, gamedev]
---
![Bunker]({{site.baseurl}}/images/vehicle-vis/spaceship_13.jpg)

## What is this?

We were approached by a VR company that they want us to create an "Automotive Holodeck", that would be used to present their VR technology. The VR headset had almost 10000 pixels on horizontal axis, so performance was of the utmost importance - basically the "holodeck" had to be realistic, but take as little of horsepower to render. 


<div class="gallery-box">
  <div class="gallery">
    <img src="/images/vehicle-vis/silo-1.jpg">
    <img src="/images/vehicle-vis/silo-2.jpg">
    <img src="/images/vehicle-vis/silo-4.jpg">
    <img src="/images/vehicle-vis/silo-6.jpg">
    <img src="/images/vehicle-vis/silo-7.jpg">
    <img src="/images/vehicle-vis/silo-8.jpg">
    <img src="/images/vehicle-vis/silo-10.jpg">
    <img src="/images/vehicle-vis/silo-11.jpg">
    <img src="/images/vehicle-vis/silo-19.jpg">
    <img src="/images/vehicle-vis/silo-20.jpg">    
  </div>
</div>

## How was it done?

In the time we were making it, there was no real-time global illumination, and even today, I am not sure if it's even possible to render real-time GI to VR. So, everything had to be baked by Unreal Engine, which proved to be more challenging than we thought. 

## Challenges

- The model was bought, but it was all polygons were subdivision surfaces, so it had to be manually readjusted, and some parts had to be remodeled. 

- All the parts of the car had to be UW unwrapped, so shadows maps will correctly bake in Unreal. This unwrapping had to be done, so the pixel density was roughly equal across all polygons.

- There was an idea to bake the shadow maps directly in 3Ds Max, so no baking had to be done in Unreal. Though, it proved inefficient when car environment changes - reflections and shadows were off and not accurate. Therefore, some shadow quality was sacrificed, and baked directly in Unreal. 

- Some parts were interactive (interactivity was done by Leap Motion), so some shadow maps had to be added in to hide seams. 

- The floor had no shadow maps at all, instead, the shadow on the floor is faked with Photoshop. That gave us that very smooth shadow, that makes the car truly fit into the scene. 

- Materials were modified Unreal Engine Automotive materials. They are usually world mapped, but we converted them to be UWV mapped, so there would be no seams on the car panels.


<div class="gallery-box">
  <div class="gallery">
    <img src="/images/vehicle-vis/garage-1.jpg">
    <img src="/images/vehicle-vis/garage-2.jpg">
    <img src="/images/vehicle-vis/garage-3.jpg">
    <img src="/images/vehicle-vis/garage-4.jpg">
    <img src="/images/vehicle-vis/garage-5.jpg">
    <img src="/images/vehicle-vis/garage-6.jpg">   
  </div>
</div>

## Performance?

In the end the clients were very happy. The performance was well above 120 FPS (I believe 150 FPS) on almost 4k screen per eye (so 2x 4k), on GTX 1080. Fake it till you make it!

<div class="gallery-box">
  <div class="gallery">
    <img src="/images/vehicle-vis/bungalow_01.jpg">
    <img src="/images/vehicle-vis/bungalow_05.jpg">
    <img src="/images/vehicle-vis/bungalow_07.jpg">
    <img src="/images/vehicle-vis/bungalow_10.jpg">
    <img src="/images/vehicle-vis/bungalow_20.jpg">
    <img src="/images/vehicle-vis/bungalow_27.jpg">

       
  </div>
</div>