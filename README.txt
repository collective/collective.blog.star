Introduction
============

collective.blog.*, or just blog.star, for short, is a suite of blogging
modules for Plone. It is primarily designed for integrators. Most people who
use Plone for blogging also uses Plone as a customized content management
system, and they have specific requirements and their own skin, custom content
types and other integrations. It turned out that other Plone blogging products
make a lot of assumption about how you are to use it, what you want from a
blog, and how your site is set up.

blog.star follows a set of principles to avoid these problems:

* Be modular. Not everyone wants everything your blogging software has to
  offer.
  
* Be flexible. Don't assume that people want to use your software in one
  particular way.
  
* Be simplistic. If there is a simple way of doing it, do it that way.

* Be Ploneish. Plone already has 90% of what a blog needs built in. Use it.

Modular
-------

blog.star is made up of several separate modules, that each do one thing only.
The modules so far is:

* **collective.blog.view**: Provides a blog-style view for Plone folders and
  collections, with support for use in monthly archives.

* **collective.blog.feeds**: Uses basesyndication and fatsyndication to provide
  several types of XML/RDF feeds for fodlers/collections.

* **collective.blog.portlets**: Portlets useful for blogging, such as a monthly
  archive and a last posts portlet.
  
* **collective.blog.star**: A module that uses all of the above plus some extra
  modules like qi.portlet.tagClouds useful for blogging. Use this is if you
  just want simple blogging support in Plone.
  The development of collective.blog.star was sponsored by **Jarn AS** -
  http://www.jarn.com


  
Flexible
--------

If a portlet would work great in a normal folder, why shouldn't it? There is
no need to add the arbitrary requirement that your portlets only works in
folders that have a specific marker interface, for example. Marker interfaces
are there to mark an object as being something special, even though that
"special" doesn't need a separate interface. Now a blog is just a container of
blog entries with a blog view and archives etc. There is no reason any of your
"blog" portlets would only work with a folder that is marked as being a blog.
The portlets I'm writing for blog.star will work in any folder or collection.


Simplistic
----------

The blog view doesn't require anything particular from the blog entries, as
long at they are archetypes objects. If they aren't, well, then you need to
make your own blog entry view, something you might want to do anyway, to
control how they look in detail. Doing it is easy, you just create a view
called blog_item_view for your content type.


Ploneish
--------

Yes, you can configure Plone so that an objects default view becomes a special
blog view when you set a marker interface on that object. But you can also
just add the view to the list of allowed views in the portal type, and select
the view from the view drop down. It's simpler, more easily configurable,
because you can now add that view even to custom folder types that you may
have without digging into the code and figuring out what marker interface to
put where. This is how the blog view of collective.blog.view works.


Requirements
------------

blog.star requires Plone 3 or Plone 4.


Installation
------------

To install blog.star you simply add "collective.blog.star" to the list of
eggs in your buildout, run buildout and restart the Plone server. In Plone's
portal_quickinstaller you select "blog.star" and install it.

Now you can create a normal folder, and in the Display menu you can select
"Blog view" to make the folder into a blog. You add blog entries with the
standard Page type, and you can even create podcast entries with the 
standard File type.

You also have a set of new portlets available, like a Monthly Archive, a
Last Entries and a Tag Cloud portlet.


Commenting
----------

If you need commenting, we recommend plone.app.discussion. The reason it's
not installed by blog.star is because under Plone 3 it's not trivial to
install, and in Plone 4 it's included.
