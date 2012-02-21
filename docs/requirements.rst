==========================
YukeYukeYuke: Requirements
==========================

Problem Domain
==============
The `SCRUM <http://www.scrum.org/>`_ project management methodology prescribes a lot of mandatory meetings as part of the process. Those meetings often involve sorting through reams of User Stories and other intermediate products, and discussions that involve input from the entire team, often at the same time.

Some specific problem areas:
    
    - Planning Poker
    - Discussion/Estimation/Prioritizing of User Stories
    - Sprint Retrospective Meeting
    
Planning Poker
--------------
This process involves each member of the team deciding on an estimation value for a given User Story.

This is typically expressed as a Fibonacci sequence printed on playing cards.

.. seealso::
   Wikipedia Article on Planning Poker
        http://en.wikipedia.org/wiki/Planning_poker
        

Some issues:
    
    - it can be hard to keep developers from taking too much time
    - doing it remotely can be difficult

User Story Processing
---------------------
In many meetings in the SCRUM process, the back-log of User Stories is worked through, often in many passes over time.

This happens during planning, back-log grooming, estimation, prioritizing, and often happens ad-hoc as well.

A good User Story is well written, and is looked at enough to clarify any ambiguities or uncertainties. Better User Stories produce better products.

Aside from general organizational issues (people use databases, content management systems, online tools, issue trackers, spreadsheets, and even pen and paper), it can be difficult to systematically work through a set of User Stories.

A user interface that would organize User Stories and allow for quick online processing would tremendously streamline the whole process.

Sprint Retrospective
--------------------
At the end of each sprint, the team gets together for a retrospective meeting, where each member expresses their feelings about the work that was done. 

It's typically expressed in these terms:

    :Good: What went 'right' during the sprint.
    :Bad: What went 'wrong' during the sprint.
    :Try: What can we do to make things better next time?
    :Commit: List action items that the team will commit to during the next sprint.
    
Ideally, the team members come up with this information on the spot during the meeting, jotting responses to each column down while hiding their response from their teammates. They then reveal their responses at once, one column at a time.

At my current job we've been using a shared Google docs spreadsheet, hiding our responses by setting the font color to white on a white background. 

I'd like to see this put into a simple user interface with timers and a little guidance from the tool as to how the process works.

Technical Requirements
======================
Server-Side 
-----------
We will require two server-side applications that utilize the same networking protocols. One written in Node.js, one in Twisted.

The client/server api should be identical in both implementations. The internal design, however, can diverge a bit to accommodate best-practices of either framework.

The protocol will be httpd-based, using JSON for data interchange when necessary.

Some sort of static back-end will likely be required. No specific requirements exist except that the storage API be abstracted such that the data back-end could be migrated with minimal refactoring.

The application should run in any modern Linux. MacOS X support is desired but not required.

Windows support would be a great bonus (I'm fairly certain both platforms will run on that platform), but is not a primary target.

Client-Side
-----------
The client-side of the app should run in any 'modern' browser. 

Javascript is encouraged (preference for jQuery framework if possible)

HTML5 is on the table if required.

Specific browser targets:
    - Firefox 9.x
    - Chrome 16.0.x

License
-------
The application should be released under a GPL license.

Packaging
---------
The applications should be packaged and distributed as installable modules using the mechanisms that exist for each platform (python eggs and npm packages).

Each should come with a zc.buildout sandbox environment for testing.


