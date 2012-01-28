===================
Node.js vs. Twisted
===================

Overview
========
This repository contains a `zc.buildout <http://pypi.python.org/pypi/zc.buildout/1.5.2>`_ sandbox environment to support a series of blog posts pitting `Node.js <http://nodejs.org>`_ against `Twisted <http://twistedmatrix.com/trac/>`_.

The goal is to get into event-driven application development by working through the same requirements. Two servers, one fully-decoupled UI.

The blog posts are on-going, starting with http://wp.me/p8How-9n. I'll collect (and probably expand on) the posts at http://lionfacelemonface.wordpress.com/node-js-vs-twi…he-whole-story/ when the series is complete.

I'm also going to break out the node, python, and front-end parts into separate packages, and distribute them via the standard channels. 

So think of this project as 'soup to nuts' evaluation of Twisted, Node.js, and event-driven web development. 

About the App
=============
See the documentation for more information. It's essentially a tool to help make SCRUM collaborations easier. 

The working title is "YukeYukeYuke". It's how my 3 year-old nephew called his dog Luke.

Directions For Use
==================
.. note:: 
   This project is for intra-cranial use only. **Eye Irritant.** *If product gets into eyes, flush with water.*
   
If you've used zc.buildout before, you know this dance, but I want to go into details for folks that may be seeing a buildout for the first time.

Prerequisites
-------------
To effectively use any buildout, you will need the following:

    - `python <http://www.python.org>`, and its source - this project is built with version 2.6.6, should work with any version greater than 2.5 but less than 3.0.
    - Common build tools (make, gcc, etc).
    - git

For this project, you will also need:
    
    - a unix-like operating system (built with Ubuntu 10.10)

I might be able to support windows and OS X with a few modifications in how things are done, feel free to open an issue with problems.

On a debian-based system, something like this will install all of the packages you need:

   ::
       
       $ sudo apt-get install python python-dev build-essential
   
       
.. note::
   Keep an eye on this file, as the persistence story evolves there may be additional requirements.
   
Running The Build
-----------------
#. Check out the source
   
   ::
       
       $ cd ~
       $ git://github.com/jjmojojjmojo/Node.js-Vs-Twisted.git
       
   
#. Bootstrap and buildout
   
   ::
       
       $ cd ~/Node.js-Vs-Twisted
       $ python bootstrap.py
       $ bin/buildout
       
That's all there is to it.

Running the Apps
----------------
The buildout sets up node.js, Twisted, and serves html documentation generated with `sphinx <http://sphinx.pocoo.org/>`_.

All three processes are controlled by `supervisor <http://supervisord.org>`_, but can be controlled independently.

Once the build is complete, you can start the services manually like this:

Twisted:
    
    ::
        
        $ cd ~/Node.js-Vs-Twisted
        $ bin/twistd -l - yuke
        
    
Node:
    
    ::
        $ cd ~/Node.js-Vs-Twisted/parts/nodejs
        $ source bin/activate
        $ yukeyukeyuke &
        
    
Documentation:
    
    ::
        
        $ cd ~/Node.js-Vs-Twisted/www
        $ python -m SimpleHTTPServer 9997 &
        
    
*I will leave stopping them as an exercise for the user :)*
        
Or just start them with supervisor (preferred method):

    ::
        
        $ cd ~/Node.js-Vs-Twisted
        $ bin/supervisord
        
    
You can check the status of the processes with supervisorctl:

    ::
        
        $ cd ~/Node.js-Vs-Twisted
        $ bin/supervisorctl status
        site:docs                        RUNNING    pid 2565, uptime 0:00:02
        site:node                        RUNNING    pid 2564, uptime 0:00:02
        site:twisted                     RUNNING    pid 2566, uptime 0:00:02
        
To stop supervisord, get the PID file, and kill it:

    ::
        
        $ cd ~/Node.js-Vs-Twisted
        $ kill `cat var/supervisord.pid`
        
There is a template for an init.d script in the source. Once the app is fleshed out a bit more, I'll implement adding it to your system startup/shutdown process.

Once the services are running, you can view them at the following URLs:

    node.js: 
        http://127.0.0.1:8124/
        
    Twisted:
        http://127.0.0.1:8000/
        
    Docs:
        http://127.0.0.1:9997/


