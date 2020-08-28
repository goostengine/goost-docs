General principles
==================

Development philosophy
----------------------

As of now, Goost tries to follow some of the philosophical principles when it
comes to the development itself.

Simplicity should not come at the cost of limited features
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Even if something won't be used often, always strive for completeness. The most
obvious example of this is the presence of math operations. Even if the division
operation won't be used as often compared to other operations, it's silly to
deny the existence of it. A user doesn't have to make yet another utility script
for something which should be an inherent part of a feature.

Designing for extensibility is not future-proofing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The technology moves at a fast pace. Expect people to use the software in
unexpected ways. Don't make it difficult for your future self having to redesign
and rewrite the software. But don't look too far into the future either, because
that's not designing for the future - that's just anxious thinking.

Problems demand solutions, solutions resolve problems
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

While solutions may certainly create new problems, the problems themselves are
not inherently a bad thing as long as they bring valuable insights, leading to
new solutions. It's the circle of life.

Scope of features being developed
---------------------------------

In order to set up correct expectations, lets outline what kind of features are
deemed meaningful for Goost development.

Usefulness
~~~~~~~~~~

Unfortunately, there's no objective criteria when it comes to determining if a
particular feature would be useful or needed for most or only a handful of the
users, but lets make some estimations.

If you're developing a new feature directly in Godot Engine, the proposed
feature must be useful for at least **70%** of the users. Now, if you're
developing a new feature in Goost, the feature must be useful for at least
**30%** of the users.

A lot of the existing Goost functionality is a result of not approved and
not-yet-approved proposals by Godot Engine's core developers but which received
a general positive feedback from the rest of the community, or features which
were removed in previous versions of Godot. Such a feature can most likely be
considered as the best candidate for being included as part of Goost.

Performance
~~~~~~~~~~~

If you think that GDScript is still too slow for your use cases, you may
consider re-implementing a feature in Goost using C++ if you think that it will
benefit other developers (see Usefulness criteria). The most common bottlenecks
may be math operations, procedural generation etc.

For instance, there are a lot of finite-state machine implementations which
should be better implemented via script currently, as it may be difficult to
implement a general-purpose implementation to suite most use cases. But if some
parts are too slow, this could be optimized by creating general-purpose enough
C++ data structures and algorithms to help you speed up computation. Again,
those classes and methods should be useful to a decent percentage of developers
using Goost.

Reusability
~~~~~~~~~~~

Some existing Goost classes and methods reuse existing Godot Engine
functionality which are unavailable in the official builds (a feature may be
deemed too corner case for it to be exposed by Godot Engine core developers). If
there's some Godot feature which is inaccessible to scripting but nonetheless
reachable through C++ code, that's a good opportunity to expose it via Goost.

If you don't want to reinvent the wheel and you need to use a feature for which
there's an existing C/C++ library which can be bundled as part of Goost, that's
also a justifiable reason for a feature to be integrated.

Alternatives
~~~~~~~~~~~~

If none of this applies to you, chances are that a feature doesn't belong to
Goost as it can (and likely should) be implemented via GDScript, especially if
the feature can be implemented in various ways which would only benefit a
handful of users. Instead, consider contributing to a project such as
`Godot Node Extensions <https://github.com/godot-extended-libraries/godot-next>`_
which aims to fulfill this need.

If you really want a feature to be included in Goost despite all of the above,
it might make sense to implement it as a module under the ``modules/``
directory. But bear in mind that users will need to enable extra modules support
manually, and the complexity of the added features is always taken into account.
Likewise, if a new feature is specific to a single genre of games (or domains),
it **must** be implemented as a module.

Community
~~~~~~~~~

If you're an independent Godot Engine C++ modules developer who wants to link an
existing module to be included as part of Goost, feel free to open a pull
request linking your module as a ``git submodule``. This might be the best
option if you'd like to have more freedom over your module's development.

.. seealso::
    :ref:`doc_adding_community_modules`.
