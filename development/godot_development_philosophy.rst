:orphan:

.. _doc_godot_development_philosophy:

Godot development philosophy
============================

.. warning::

    This page describes the development philosophy of Godot itself, not Goost.
    For Goost development philosophy, refer to :ref:`doc_goost_development_philosophy`.
    
    Most of what's written here was inferred from the words of Godot's
    representatives scattered over the Internet, but please note that what is
    written below is not an official description of Godot's development
    philosophy, but rather an interpretation of it, because according to Godot
    advisors, there's
    `"no absolute development philosophy in Godot" <https://github.com/godotengine/godot-proposals/issues/575>`_.

Introduction
------------

The development of Godot Engine is governed by various explicit and implicit
thinking processes which might not be instantly or completely obvious to a new
person interested in contributing, especially if that person has already some
preconceived notions regarding the purpose and ideas behind Godot, so it's
important that both new contributors and existing core developers share the same
understanding and vision regarding Godot Engine development to achieve best
results.

This allows to eliminate any confusion and to further improve existing
relationships between contributors, as revealing development ideas is essential
to reaching a general consensus regarding the direction of the project.

Taking into account various cultural differences, the purpose of this page is to
document the history, culture, philosophy, vision, mission, priorities, goals,
non-goals, principles, direction and intention of the Godot Engine project as an
open-source game engine and as a community in general.

History and culture
-------------------

One of the best ways to understand the ideas behind the engine is by going
through the history of Godot development.

The following are some resources which outline the origins of Godot Engine, some
of which may already suggest a general direction of the project, so you can
better see all the aspects and the background behind the engine development for
yourself.

Release news
~~~~~~~~~~~~

* `First public release! <https://godotengine.org/article/first-public-release>`_
* `Godot Engine reaches 1.0, first stable release <https://godotengine.org/article/godot-engine-reaches-1-0>`_
* `Godot 1.1 is out! <https://godotengine.org/article/godot-1-1-out>`_
* `Godot Engine reaches 2.0 stable <https://godotengine.org/article/godot-engine-reaches-2-0-stable>`_
* `Godot reaches 2.1 stable! <https://godotengine.org/article/godot-reaches-2-1-stable>`_
* `Godot 3.0 is out and ready for the big leagues <https://godotengine.org/article/godot-3-0-released>`_
* `Godot 3.1 is out, improving usability and features <https://godotengine.org/article/godot-3-1-released>`_
* `Here comes Godot 3.2, with quality as priority <https://godotengine.org/article/here-comes-godot-3-2>`_

Articles
~~~~~~~~

* `Godot history in images <https://godotengine.org/article/godot-history-images>`_
* `Open source Godot gets two years old! <https://godotengine.org/article/open-source-godot-gets-two-years-old>`_
* `As an Open Source project, Godot is more than a game engine <https://godotengine.org/article/as-oss-godot-is-more-than-a-game-engine>`_
* `A decade in retrospective and future <https://godotengine.org/article/retrospective-and-future>`_

General principles
------------------

In short, there is no absolute philosophy behind Godot Engine development.
Unfortunately, all people interested in contributing may have to go through
various discussions to determine what kind of changes would be meaningful to
incorporate at the moment, which means that a lot of feature proposals will be
either ignored or rejected by the core developers.

The core development philosophy of Godot is created through the **uncertainty**
regarding the direction of the project. This vision is proliferated as
"accepting the reality of that nothing can be truly finished", or "what kind of
problem we're dealing with *right now*". This is largely characterized by
`Extreme programming <https://en.wikipedia.org/wiki/Extreme_programming>`_, like
not programming features until they are actually needed as seen by Godot core
developers.

Due to this,
`Godot Improvement Proposals <https://github.com/godotengine/godot-proposals>`_
was created as the main platform which allows contributors to share and discuss
concrete problems, which could benefit Godot in its current state in hopes to
satisfy user expressed needs. If you don't have a project that you're working on
with Godot, or not ready/allowed to reveal it to the general public, the
proposal will most likely be ignored.

.. seealso::

    `Introducing the Godot Proposals repository <https://godotengine.org/article/introducing-godot-proposals-repository>`_

Nonetheless, there are more or less firm objectives which govern the engine
development that might not be completely obvious to contributors at first (and
even core developers themselves due to extremely pragmatic "down to Earth"
attitude), so it's necessary to reveal and outline them.

**Every game engine is different and fits different needs**, and it's impossible
for an engine to solve *every problem that exists under the sun*, so lets
describe those differences and try to setup correct expectations for what
constitutes Godot as a game engine and determine the scope of features being
developed, so you can better understand the Godot priorities.

Vision, goals and non-goals
---------------------------

General vision
~~~~~~~~~~~~~~

Unlike other game engines with a dedicated editor, Godot aims for high-level
functionality and implementing back-ends which allow to make games to look
pretty, cover **the most common use cases** and only allow **some tweaking**.

The idea is that out of the box the games made in Godot should look as good as
in other game engines, while at the same time making the engine easy to use and
accessible for most people, which may also include non-programmers.

One way, or no way
~~~~~~~~~~~~~~~~~~

Due to the above, the ability to tweak the engine performance for corner use
cases may be lacking. If we take the rendering part, the vision here is that
ability to customize can be achieved with a relatively simple renderer, so that
any renderer engineer can still tweak the rendering by themselves that require
specific functionality in their game projects.

Likewise, if there are too many different possible approaches to implement
something (such as AI), the default decision is to not support such a feature
out of the box, but instead provide necessary tools to facilitate implementing
those kind of features by the community via modules and plugins. This allows to
avoid complexity and improve maintainability.

Similar approach applies to changing the default parameters: unless there's
something useful to implement, the default decision is to not change the default
parameters and values unless there's a clear use case that warrants adjusting
the defaults.

Preventing bloat
~~~~~~~~~~~~~~~~

The goal is to provide only the most common tools which are typically used by a
vast majority of developers creating video games. This is why Godot is striving
to have a good enough set of editor tools which allow developers to customize
virtually any part of the editor to satisfy specific use cases. If you'd like to
start contributing to Godot's development, pull requests that improve the editor
itself are by far more likely to be merged.

This way, the core stays lean and mean, so the engine developers can better
focus on other aspects such as usability, stability and extensibility provided
by modules and plugins. Community plugin ecosystem should be improved to avoid
bloating the engine with features that will be rarely used. The Godot Editor is
often seen as the final product and tends to be prioritized over everything
else.

Performance is low priority
~~~~~~~~~~~~~~~~~~~~~~~~~~~

`Godot is not an ECS-based game engine <https://godotengine.org/article/why-isnt-godot-ecs-based-game-engine>`_.

Godot favors ease of use and maintenance over absolute performance. Performance
may still be an important aspect for some projects which use Godot, so
performance optimizations will be considered, but they may not be acceptable if
they make something too difficult to use or if they add too much complexity to
the codebase. A clear example of this is the following rejected pull request:

* `Using the slowest data structure almost every time <https://github.com/godotengine/godot/issues/23998>`_

Not invented here
~~~~~~~~~~~~~~~~~

Oftentimes, `NIH <https://en.wikipedia.org/wiki/Not_invented_here>`_ is seen as
negative statement, which describes the tendency to avoid using third-party
solutions. However, Godot core developers take this decision deliberately, as
this allows Godot to make independent decisions without trying to fit
third-party solutions into Godot's specific design. A lot was tested and dumped
in Godot over years like SDL, Lua, Squirrel, Assimp, Box2D and Bullet, because
either glue or politics were a problem.

However, from the user side, this "freedom" results in inability to customize
the engine when you have specific cases to solve. Due to this, forking the
engine locally for the project you're working on is the most natural decision to
take if you do have problems that cannot be solved with Godot out of the box
even with custom modules and plugins, or when you're not willing to go through
the strict, bureaucratic Godot proposals process.

Final notes
~~~~~~~~~~~

While forking the engine could be the ultimate solution for you, we ask you not
to do this unless you see no other way, or would like to achieve independence as
needed by your project.

In order to minimize the excess division of Godot community (which is
inevitable), `Goost <https://goostengine.github.io/>`_ was created. Please
proceed to :ref:`doc_goost_development_philosophy`.
