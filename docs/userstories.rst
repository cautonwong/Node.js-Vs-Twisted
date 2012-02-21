==========================
YukeYukeYuke: User Stories
==========================

This section deals with identifying the core pieces of functionality, which will drive further design decisions moving forward.

User Management
===============
There needs to be a way to manage users who have access to the system. They need to be grouped into projects. Users will be given certain roles on each project, such as 'Team Member', 'Product Owner' and 'Scrum Master', which will drive their access level and how the user interfaces are presented.

At minimum users should provide a user name, a password and an e-mail.

Implementation Details
----------------------
0.0.1a
~~~~~~
In the first release, the application will be self-organizing, focusing on the meeting helper UIs. 

A user interface will be provided for users to claim a role when creating or joining a meeting. Roles will be implemented as text strings with no additional meta-data.



Profile Management
==================
Profile data should be flexible and extensible by someone setting up the system.



User Authentication
===================
People will need to identify themselves when using the system. External authentication should be supported.

Specific authentication providers that should be supported:
    
    - `openid <http://openid.net/>`_.
    - `Kerberos <http://en.wikipedia.org/wiki/Kerberos_%28protocol%29>`_
    - `LDAP <http://en.wikipedia.org/wiki/Ldap>`_
    
Implementation Details
----------------------
I don't want to have to build user management interfaces at this stage, so the plan during the initial development phase is to use a self-organizing approach. 

The user who initially establishes a meeting will have 'admin' rights for the meeting, and subsequent users will be considered 'team members'.

So initially, 'logging in' is just a matter of entering your basic information.

But beyond that, the application will respect a couple of special headers:

    - X_HTTP_USER - contains the user name if other authentication is used
    - X_YUKE_ROLE - contains a role string that will be used, assumed to be provided by the authentication that happened prior.
  
.. note::
   These are not set in stone; the format of the headers and what can be marshaled between an external authentication mechanism and the application will solidify as the other parts of the app are finalized.
   
   That said, I think this may be the best approach moving forward; it's relatively easy to put some sort of web proxy out front of an app like this, and then the person deploying the app is free to use whatever authentication mechanism that meets their requirements. 

User Authorization
==================
Administrators of the system should be able to restrict what privileges a user has relative to specific actions or data.

Concerns:
    - How fine-grained should the access control be?
    - Where should this control be managed? Centrally? User-relative? Content-relative?

Implementation Details
----------------------
I like how permissions are handled within the `Pyramid <http://docs.pylonsproject.org/projects/pyramid/en/1.3-branch/index.html>`_ framework (specifcally, http://docs.pylonsproject.org/projects/pyramid/en/1.3-branch/narr/security.html).

This follows the Zope philosophy of 'object protect thyself'. 

It uses an arbitrary set of strings that represent permissions. Some are obvious ('Read', 'Edit'), but the permissions don't always map to concepts like file system permissions do. Some examples: 'Can Execute Remote Code', 'Is Allowed To Use The Stove'.

The roles are applied to users and/or groups by a given content object (pyramid uses a 'magic' property called __acl__).

.. code-block:: python

   ...
   __acl__ = [
       (Allow, Everyone, 'view'),
       (Allow, 'group:editors', 'add'),
       (Allow, 'group:editors', 'edit'),
   ]
   ...

Pyramid is also aware of inherited permissions if the object is set up as the child of another object. The framework will walk up the lineage of an object and reconcile the permissions before deciding if the user is authorized or not.

How this is implemented really depends on how well the 'self-organizing' approach to authentication works out, and how much fine-grained control of access is really appropriate.

User Story Management
=====================
The system should allow the user to create/modify/delete user stories. User stories capture the following data at minimum:

    :Title: the short-name of the story.
    :Body: The content of the story, rich text.
    :Author: Who initially wrote it.
    :Contributors: Any additional collaborators/editors/other people to credit.
    :Estimate: The current estimate, in story points
    :Priority: A relative numeric value used for sorting stories by priority.
    :Status: What is the status of the story? Typical values would be 'Not Started', 'In Progress', 'Blocked', and 'Complete'.
    :Sprint: which sprint(s) this User Story is included in.
    :Release: which version of the software is associated with this story.
    
User stories should also allow for the following amendments to be uploaded or attached to the story:
    
    :Implementation Details: The current implementation plan (technical details go here).
    :IT Resources: Any IT needs anticipated.
    :Test Plan: How does the developer prove that this story is complete?
    :Uncertainties: Lists of outstanding questions.

The amendments can contain rich text and images (we will often add links, mockups and other media). 
    
It would be great if the fields and amendments could be defined at runtime by the user.

All fields short of Title and Body should be optional.

Sprint Management
=================
Users should be able to create/modify/delete sprints. Sprints have a title, start/end dates, a description, a release, and a list of associated user stories.

Sprint Retrospective Meeting
============================
A Scrum Master should be able to establish a sprint retrospective meeting, invite attendees, and hold the meeting on-line.

The basic flow of the meeting goes like this:
    
    #. Each team member is asked for the following information, in regards to the sprint:
    
        - What was good about the sprint
        - What was bad about the sprint
    
    #. The information is kept secret until all team members are finished.
    #. Everyone's answers are revealed one after the other, in random order.
    #. The group discusses the values.
    #. Each team member is asked 'What can we try to improve?'. Those responses are also collected in secret.
    #. The group discusses these ideas and then selects some to commit to.

Implementation Details
----------------------
This will be the first scrum tool that is built in this dual-platform project.

The user interface will be 100% browser-based. It's unclear at this point how the static javascript and html files will be served to the user.

For data storage, we'll use flat files containing JSON. 


