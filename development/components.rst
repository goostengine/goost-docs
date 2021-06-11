Components
==========

The Goost's source tree structure closely resembles Godot Engine's structure. In
fact, you can see this extension as a mini-engine which builds on top of the
existing core functionality of Godot, as most of the functionality is easily
accessible within a module, which is the **extension** in the Goost terms.

What are components?
--------------------

Components are mostly structure-agnostic, functional parts of the extension.
Similarly to how Godot gives you a way to enable or disable certain modules,
Goost provides a way to enable or disable a bulk of features. This promotes
modularity within the extension itself.

Components are developed in terms of functional value. It's the responsibility
of Goost developers to make the necessary internal structural changes to
maintain this user expectation.

Similarly, most classes and methods are broken down into their own `2d` and `3d`
subfolders, so that either 2D or 3D components can be easily disabled by using
Godot's ``disable_3d`` build option, and possibly defining ``disable_2d`` to
disable 2D features in Goost specifically in the future.

The gist of functional modularity
---------------------------------

The components are first declared at ``goost.py`` which is located at source
tree root, with the contents similar to the following:

.. code-block:: python

    components = [
        "core/image",
        "core/math/geometry",
        "scene/physics",
        "scene/gui",
        "editor",
    ]

The list represents parent/child relationship of related components, so that the
entire branch of features can be disabled. The rightmost items represent the
actual functional components this extension provides. Despite appearances, this
relationship does not necessarily represent the actual file structure.

The list is then transformed in both ``config.py`` and ``SCsub`` to achieve
the following:

1. Define command line options in the form of ``goost_*_enabled``.
2. List disabled components, optionally disabling a branch of components.
3. Define preprocessor constants of enabled components from those options.

Ideally, the relevant sources of components should be compiled only when
requested by the build system, for instance:

.. code-block:: python

    if env_goost["goost_image_enabled"]:
        SConscript("image/SCsub", exports="env_goost")

The only thing left is figuring out a way to only register the classes of
interest. Godot provides ``register_*_types`` and ``unregister_*_types``
callbacks for this, but given the fact that a lot of the Goost functionality
can be disabled, we define similar methods for each of the component:

.. code-block:: cpp

    #include "register_types.h"

    #include "core/register_core_types.h"
    #include "scene/register_scene_types.h"

    void register_goost_types() {
    #ifdef GOOST_CORE_ENABLED
        goost::register_core_types();
    #endif
    #ifdef GOOST_SCENE_ENABLED
        goost::register_scene_types();
    #endif
    }

Here, we use previously defined preprocessor constants to only register core and
scene types if they weren't disabled explicitly. We use ``goost::`` namespace
specifically for those methods to avoid naming collision with Godot's
``register_core_types``, for instance.
