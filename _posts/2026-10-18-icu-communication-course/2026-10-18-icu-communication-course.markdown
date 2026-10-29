---
layout: post
title:  "ICU Communication Course: AI Virtual Patients in Moodle"
description: "Product owner and sole developer of a bilingual Moodle course for ICU teams: AI-evaluated voice virtual patients, 14 custom plugins, Stripe storefront."
date:   2026-10-18 12:00:00 +0200
image:  icu-comguide.jpg
featured: true
tags:   [programming, interactive]
---

[VISIT THE LIVE COURSE](https://komunikace-icu.cz)

## What is this?
"Difficult communication in the ICU environment" is an online course for healthcare teams. It covers the conversations nobody really wants to have: delivering bad news with a structured, step-by-step approach, responding to emotions, end-of-life decision making, working with your own emotions, and clinical debriefing, including a VR scenario.

The course has 5 core training areas and 4 virtual patient checkpoints. It is self-paced and access doesn't expire. Each chapter is built the same way: short lessons, printable materials, a virtual patient, a test and a summary.

## My role
I was the sole product owner, and I did the whole development. I programmed the entire site, built the custom Moodle plugins and made the interactive virtual patients. So every decision about how something should work, and then actually making it work, landed on my desk.

## The problem
You can read about communication frameworks all day, but the hard part is saying it out loud to someone who is upset. Stock Moodle is good at hosting lessons and quizzes, not at letting you practice a conversation. It also doesn't look or feel like a modern course out of the box, and it doesn't sell itself. So most of the job was bending Moodle into something it wasn't really made for, without breaking the parts it is good at.

![Public course homepage listing the 5 core training areas and 4 virtual patient checkpoints](icu-objectives.jpg)
*The public course homepage: 5 training areas, 4 virtual patient checkpoints*

## What I built

### Virtual patients
The core of the course. The trainee plays the doctor - for example delivering serious news to a patient's mother - and talks to the virtual patient through the microphone. The avatar is animated and lip-synced in real time, and the trainee's responses are evaluated by AI. The interface has a medical report to look at, a button to end the conversation, and a "Report a Bug" button.

This is built as two of my own activity modules: Conversation Avatar (the avatar and voice conversation) and AI Reply Box (the AI-evaluated replies).

![Virtual patient interface: an animated avatar of Mrs. Nováková in a consultation room, with numbered callouts for the scenario title, patient name, Report a Bug and End buttons, View Medical Report, the avatar and the microphone button](icu-vp-guide.jpg)
*The virtual patient interface, explained element by element in the course guide*

![Lesson 4.4 Virtual Patient: instructions to use a microphone and headphones, and a Start Conversation button](icu-vp-start.jpg)
*Each chapter ends with a virtual patient checkpoint, started with one click*

### ComGuide, the communication part as its own web app
The communication practice was also built as a separate web app, ComGuide. You talk to conversational AI virtual patients by voice, in settings like a home bedroom or a hospital room. In the de-escalation scenarios, an emotional to rational meter shows how the conversation is going, and a side panel lists techniques to try: naming emotions, paraphrasing, asking follow-up questions, fogging (partial agreement) and support.

![ComGuide: Theresa Black, a virtual patient in a hospital room, with an emotional to rational meter on the left and a panel of de-escalation techniques on the right](icu-comguide-deescalation.jpg)
*ComGuide: a de-escalation conversation with Theresa Black, with the emotional to rational meter and the techniques panel*

![ComGuide: Mr. Newman, a virtual patient in a hospital corridor, with the emotional to rational meter, a "Your last response" box and the same de-escalation techniques panel](icu-comguide-corridor.jpg)
*Another scenario, with Mr. Newman in a hospital corridor*

### 14 custom Moodle plugins
Everything custom has the `cg` prefix:

- **Activity modules:** CG Accordion, AI Reply Box, CG content, Conversation Avatar, Course Completion Summary, CG Drag To Folder, CG Form, Hot-Cold Form, Microphone Test, CG Multiple Questions Slideshow Test, CG Spacer.
- **Course format:** a custom course format with branded gradient section headers, a collapsible nested chapter tree, previous/next navigation, locked sections and a sticky chapter progress bar. Section nesting, translations and progress are all settings, not hard-coded.
- **Local plugins:** CG Consent Manager and Student Tracking.

![Moodle admin plugin list showing the custom cg activity modules: CG Accordion, AI Reply Box, CG content, Conversation Avatar, Course Completion Summary, CG Drag To Folder, CG Form, Hot-Cold Form and Microphone Test](icu-cg-plugins.jpg)
*Part of the custom plugin set, as listed in the Moodle admin*

On top of those, I wrote my own local plugins for pages, a registration gate and a single-course storefront.

### Course experience
Chapters go one after another, with short lessons and tips, materials you can print, and a progress bar that stays visible while you read. The Microphone Test activity is there for a boring but very real reason: if the microphone doesn't work, the virtual patient doesn't either, so it's better to find out before the conversation starts. The whole site runs on the Universe theme and is bilingual (Czech and English).

![Course overview page with a collapsible nested chapter tree on the left and branded teal gradient section headers](icu-course-overview.jpg)
*Course overview: nested chapter tree and branded section headers from the custom course format*

![Lesson 4.2.1 from the chapter on delivering bad news, with cyan Tip boxes and a sticky chapter progress bar at the bottom](icu-lesson-tips.jpg)
*A lesson on delivering bad news, with Tip boxes and the sticky chapter progress bar*

### Storefront and payments
The course is sold directly on the site. A single-course storefront and a registration gate handle access, and payments go through Stripe.

![Public landing page of the course with Buy course and View course details buttons](icu-hero.jpg)
*The public landing page, where the course is sold*

## Result
The course is live at [komunikace-icu.cz](https://komunikace-icu.cz): a full Moodle-based product, from the landing page and payments all the way to practicing difficult conversations with an AI-evaluated virtual patient. Designed and built by me, as product owner and sole developer.
