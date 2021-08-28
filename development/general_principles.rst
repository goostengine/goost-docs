General principles
==================

Development philosophy
----------------------

As of now, Goost tries to follow some of the philosophical principles when it
comes to the development itself. This page is continuously updated to convey
the current development approach.

If something should be in Godot, let it be in Godot
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you really believe that a particular feature should be implemented directly
in Godot Engine for the greater good of everyone, please go ahead and create a
`Godot Improvement Proposal <https://github.com/godotengine/godot-proposals>`_
to be discussed and reviewed by Godot core developers first. A feature backed up
by a Godot proposal that received a decent amount of user support is more likely
to be approved for Goost development, even if no consensus is reached among
Godot core contributors.

One of the main reasons why Goost exists as a project is because of
`Godot's idea of being small <https://docs.godotengine.org/en/stable/about/faq.html#why-does-godot-aim-to-keep-its-core-feature-set-small>`_
to prevent feature bloat, which, of course, leads to a problem of being
bare-bones in contrast with other equivalent (commercial) game engines. Goost
aims to solve this problem by building upon Godot's core functionality to
deliver feature-rich experience.

No need to wait
~~~~~~~~~~~~~~~

We use Goost as a bridge that allows us to implement features independently of
Godot's review process and release cycles. Following this kind of development
approach helps us to port existing Goost features to Godot itself with ease in
the future, given that a particular feature is eventually approved for Godot
development. If you think that a particular feature might be a bit controversial
to implement directly in Godot, in all likelihood you should consider
contributing to Goost. Don't allow your feature proposals and pull requests
stagnate in the Limbo!

Maximum workflow compatibility
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Goost is **not** an engine fork, but we aim to replicate existing Godot
development workflows in the best way possible. This allows to minimize the time
it would take for existing Godot contributors to start implementing features in
Goost. If you're already familiar with the engine development process, whenever
fixing a bug or implementing a new feature, always try to think of a problem in
terms of Godot first.

Completeness
~~~~~~~~~~~~

There are type of tools which are not used often, but when you need them, you
really wish they were there. Therefore, we strive to have the "batteries
included" mentality whenever possible. Even if something won't be used often,
always strive for **completeness**. A user doesn't have to make yet another
utility script for something which should be an inherent part of a feature.

Extensibility and customization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Goost is designed to be **extensible** and **customizable** from the ground up.
If something cannot be disabled, it's most likely a bug.

We strive to look into the future, which help us avoid to redesign and rewrite
the software, even before a limitation or problem starts to pop up in real-life
projects.

We strive to find balance between extreme pragmatism and future-proofing. We
don't look too far into the future either, because that's not designing for the
future - that's just anxious thinking.

Mindfulness is not speculation. Always think about possible consequences in
relation to current state of art.

Scope of features being developed
---------------------------------

In order to set up correct expectations, lets outline what kind of features are
deemed meaningful for Goost development.

Goost's development is mainly focused on game development needs, even if they're
marginally related. We also realize that Godot can be used to develop general
GUI-only applications, so we don't exclude the possibility of supporting these
type of features as well.

Regardless of below criteria, you can also refer to
`the list of features already pre-approved for development <https://github.com/goostengine/goost/issues/7>`_,
which is continuously updated.

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
benefit other developers (see "Usefulness" criterion). The most common
bottlenecks may be math operations, procedural generation, machine learning etc.

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
directory. But bear in mind that the complexity of the added features is always
taken into account, as it has to be maintained. Likewise, if a new feature is
specific to a single genre of games (or domains), it **must** be implemented as
a module.

Community
~~~~~~~~~

If you're an independent Godot Engine C++ modules developer who wants to link an
existing module to be included as part of Goost, it may be worth to link the
module as a ``git submodule``. This might be the best option if you'd like to
have more freedom over your module's development, but most of the time this is
not required since the module can be maintained independently of Goost.

Nonetheless, if you'd like to share your module to increase discoverability,
then feel free to open a pull request in the dedicated
`goostengine/godot-modules <https://github.com/goostengine/godot-modules>`_
repository.

.. seealso::
    :ref:`doc_adding_community_modules`.

Feature removal policy
----------------------

Features take never-ending maintenance work, but the capabilities to maintain
them (personal motivation, funding, active maintainers etc.) may not be enough
to further advance the project as a whole. Due to this, Goost defines a set of
rules for removing features which may be obsolete, no longer useful, or prove to
be very difficult to maintain.

Before removal, we always reach out to potential users using communication
platforms (GitHub, Discord etc.) to figure out the current demand of a
particular feature.

Note that we are unlikely (if ever) remove a feature just because it's used only
by a few users at a given period of time, as long as a feature is relatively
easy to maintain. Unlike in Godot, Goost does not impose engine binary size
limits which result from having new features implemented. Since Goost's core
development principles are customization and extensibility, engine's binary size
is a bad reason to remove a particular feature in Goost.

While we understand the frustration which may result from a lacking feature
which was present in previous versions of Goost, we also hope that you
understand the amount of work needed to maintain those features, especially when
the work is done on a voluntary basis.

Whether a particular feature is going to remain or be removed largely depends on
user support and the number of contributors interested in development.

You can find a list of such features at
`A list of deprecated and removed features in Goost <https://github.com/goostengine/goost/issues/95>`_
tracker.

Rules
~~~~~

1. If no user expresses interest in a particular feature for 90 days after
   announcement at the public tracker linked above, it may be removed in future
   versions.

2. If a feature proves to be very difficult to maintain but is still desired, we
   attempt to disable a feature using build-time instructions first. This way,
   the code can remain in the Goost repository, and interested contributors can
   have a chance to update the code so that a feature properly works in the
   latest stable version of Godot Engine.

3. If a particular feature is still needed but had to be removed due to huge
   maintenance cost, it can be resurrected in future versions of Goost by
   interested contributors.

4. If feature is marked as experimental (via documentation), it may be removed
   regardless of the rules above.
