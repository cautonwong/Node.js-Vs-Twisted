==================================================
YukeYukeYuke: A Real-Time SCRUM Collaboration Tool
==================================================

.. admonition:: OH, By the Way...

   This project also aims to pit two frameworks against each other in mortal kombat: `Node.js <http://nodejs.org>`_ and `Twisted <http://twistedmatrix.com/trac/>`_.

:author: Josh Johnson <lionface.lemonface@gmail.com>

Overview
========
This project aims to create real-time collaboration-based apps to help facilitate the SCRUM process. The main aim is to implement the front-end entirely in HTML+CSS+JQuery, and implement the back-end *twice*, once in Node.js, once in Twisted.

The idea is to create a realistic set of requirements in wich to explore these two tools, and compare them *apples-to-apples*.

Motivations
===========

This project has a few primary objectives:
    
    #. Give the core developer an excuse to explore technologies they haven't used yet.
    #. Take a critical look at what event-based, lower-level web development can be.
    #. Draw some attention to Twisted.
    #. Make some of the mundane meetings/tasks that are keystones of the SCRUM methodology more *agile*.    

Node.js Vs. Twisted
===================
I decided to try a parallel approach to evaulating the two tools when a pythonista friend of mine lamented on Twitter about how Node.js gets so much more attention than Twisted.

I had heard of both tools, but not until he made that post did it dawn on me that the two tools serve very, very simuilar purposes. It's all about event-driven client/server communications.

The primary difference between them seems to boil down to language (python vs javascript) and maturity (node is realitvely new compared to twisted). 

I'm a pythonista from 'way-back', and I'm also very competent with javascript. One of the hardest parts of evaulating platforms can be learning the language they're implemented in; I've got that covered. 

So I feel like I'm in a very good place to compare the two tools in as comprehensive a way as I can. I can also stretch some of my client-side muscles to completely decouple the back and front-ends.

In the end, I should have a really solid example of a difficult (but not too difficult) poblem solved to the same spec in both platforms. From there, I can do benchmarks, get feedback from the developer communities about optimizations, and form some sort of opnion about both tools.

And of course, by publishing this code and writing about it on my blog ( http://lionfacelemonface.wordpress.com ), I hope to:
    
    - Draw attention to Twisted from folks looking for Node.js
    - Give others who may be looking for node.js/twisted examples a leg up
    - Provide some souce material for folks pleading a case for adoption of either (or both) tools.
    
Development Theme
=================
I've used a couple of variants of the SCRUM development methodology for several years. I believe it's made me a better developer; the quality of my work has gone up exponentially since I adopted it.

But at its heart, there is a lot of information to track and process (and re-process), and there are a large number of mandatory meetings. 

Further, a lot of the meetings are often difficult to do remotely.

The data and meeting managment requirements of SCRUM can be daunting; it's easy to loose sight of the core tennants of the methodology. That hurts productivity and can derail initial adoption entirely.

To that end, the general goal of this project is to provide solutions to help smooth out the rough edges of the methodology.

Since a lot of the meetings involve team members stating opnion in private, then revealing for the group (planning poker, sprint retrospective), it makes sense to use a real-time, event-driven service archetecture. 

Research and Development
========================

Research for this project has been sparse so far:

    - I'm intentionally going into this project with a limited knowledge of the tools being evaluated.
    - I've opted to ignore existing tools in the same problem space. 

On a typical project I would not proceed with development in either case. 

For this project, however, both situations are absolutely necessary.

There's merrit in taking a completely fresh look at a problem, and I think over all it will produce a more fair comparison of the tools when all is said and done.

Development Guidelines
======================

    - There will be a very strict division between the client and server components.
    - Unit tests and inline documentation are manditory. 
    - The specs will be **strictly** implementation in-specific.

