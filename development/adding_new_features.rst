Adding new features
===================

Godot's architecture is based on object-oriented paradigm, and everything
inherits from :ref:`Object<class_Object>`, directly or indirectly.

Since Goost is an engine extension, what applies to Godot development also
applies to the process of developing classes in Goost. Refer to Godot's
":ref:`doc_object_class`" documentation to learn the basics of dealing with
:ref:`Object<class_Object>` classes.

The following sections describe the process of writing new classes specifically
in Goost. Please refer to Godot's
:ref:`Engine development<toc-devel-cpp-source-beginner>` section if you are not
familiar with engine development in general.

Writing new classes
-------------------

Declaration
~~~~~~~~~~~

Components in Goost are comprised of individual classes. For demonstration
purposes, we'll use ``FiniteStateMachine`` and ``FiniteStateMachineNode`` class
names as examples.

First and foremost, declare new classes in ``goost.py::classes``, for instance:

.. code-block:: python

    classes = {
        # ...
        "FiniteStateMachine" : "ai",
        "FiniteStateMachineNode" : "ai",
        # ...
    }

The key is the class name, and the value is the component a new class belongs
to. If a new class relates to existing Goost components as seen in
:ref:`goost_api`, you should use the component name as declared in
``goost.py::components`` list:

.. code-block:: python

    components = [
        "core/image",
        "core/math/geometry",
        "scene/physics",
        "scene/gui",
        "editor",
    ]

In our case, we don't have an AI component, so we should add it ourselves:

.. code-block:: python

    components = [
        # ...
        "scene/ai", # AI component which is part of scene.
        # ...
    ]

If one of the classes depend on the other (due to inheritance or composition
design), dependencies must also be declared in ``goost.py::class_dependencies``:

.. code-block:: python

    class_dependencies = {
        # ...
        "FiniteStateMachine" : "FiniteStateMachineNode",
        # ...
    }

In our case, ``FiniteStateMachine`` depends on ``FiniteStateMachineNode``,
because it uses ``FiniteStateMachineNode`` to represent states.

A single class can depend on a set of classes, and Goost will try to resolve
all linked dependencies.

.. note::

    Declaring dependencies is required because Goost allows to disable
    individual classes via ``custom.py`` file generated with
    ``python goost.py config`` command. If any such class is accidentally
    disabled, a user must not stumble upon a build or run-time error, so
    dependent classes are going to be automatically enabled.
    
Declaring components and classes like this is mostly needed for documentation
generation purposes and customizations, see :ref:`doc_configuring_the_build`
page for more information.

Implementation
~~~~~~~~~~~~~~

Depending on a component, we can choose to implement our classes in ``core/``,
``scene/``, ``editor/`` etc. folders in Goost's source tree.

In our case, we've picked the ``scene`` component as the root component to
implement our first ``FiniteStateMachine`` class in ``ai`` component. Even
though components in Goost don't always represent structural meaning, we choose
to create a new subfolder under ``scene/`` for the new component:

.. code-block:: shell

    mkdir -p scene/ai

Create new ``finite_state_machine.h`` header and ``finite_state_machine.cpp``
source files there:

.. code-block:: shell

    cd scene/ai
    touch finite_state_machine.h
    touch finite_state_machine.cpp

.. note::

    Make sure that the filenames represent the ``snake_case`` style of original
    class names written in ``PascalCase``. Goost recognizes this pattern and
    allows to skip compiling the sources of those classes which got disabled via
    ``custom.py`` file.

We'll skip the actual process of implementing the entire class, but here's a
minimal working implementation that we'll use for learning purposes:

.. code-block:: cpp

    // finite_state_machine.h
    
    #ifndef GOOST_FINITE_STATE_MACHINE
    #define GOOST_FINITE_STATE_MACHINE
    
    #include "scene/main/node.h"
    
    class FiniteStateMachineNode : public Node {
        GDCLASS(FiniteStateMachineNode, Node);
    
    protected:
        static void _bind_methods();
    
    public:
        virtual void _update() {};
        virtual void _enter() {};
        virtual void _exit() {};
    };

    class FiniteStateMachine : public Node {
        GDCLASS(FiniteStateMachine, Node);
    
    private:
        FiniteStateMachineNode *state = nullptr;
    
    protected:
        static void _bind_methods();
    
    public:
        void set_state(Node *p_state);
        Node *get_state() const { return state; }
    };
    
    #endif // GOOST_FINITE_STATE_MACHINE
    
.. code-block:: cpp

    // finite_state_machine.cpp
    
    #include "finite_state_machine.h"

    void FiniteStateMachineNode::_bind_methods() {
        BIND_VMETHOD(MethodInfo(Variant::NIL, "_update"));
        BIND_VMETHOD(MethodInfo(Variant::NIL, "_enter"));
        BIND_VMETHOD(MethodInfo(Variant::NIL, "_exit"));
    }
    
    void FiniteStateMachine::set_state(Node *p_state) {
        ERR_FAIL_NULL_MSG(p_state, "Invalid state.");
    
        auto new_state = Object::cast_to<FiniteStateMachineNode>(p_state);
        ERR_FAIL_NULL_MSG(new_state, "The state is not `FiniteStateMachineNode`.");
    
        state = new_state;
    }
    
    void FiniteStateMachine::_bind_methods() {
        ClassDB::bind_method(D_METHOD("set_state", "state"), &FiniteStateMachine::set_state);
        ClassDB::bind_method(D_METHOD("get_state"), &FiniteStateMachine::get_state);
        ADD_PROPERTY(PropertyInfo(Variant::OBJECT, "state"), "set_state", "get_state");
    }    

Once you copy-paste the implementation, the next step is to tell Goost to
compile those files. Because we've introduced a new ``ai`` component, we need to
create a new ``SCsub`` file which is going to collect those sources to compile:

.. code-block:: shell

    cd scene/ai
    touch SCsub

Copy the following contents to ``SCsub``:

.. code-block:: python

    # SCsub

    Import("env")
    Import("env_goost")

    env_goost.add_source_files(env.modules_sources, "*.cpp")

But we're not done yet. We've previously declared ``ai`` as part of ``scene``
component. Usually, you'll have to look for parent ``SCsub`` and call into our
own ``SCsub`` we're working on. In this case, lets add the following content
to already existing ``scene/SCsub``:

.. code-block:: python

    if env["goost_ai_enabled"]:
        SConscript("ai/SCsub", exports="env_goost")

The ``goost_ai_enabled`` is an construction environment which is automatically
defined in ``config.py`` in Goost. This way, users can skip compiling the
component in the first place if they specify ``scons goost_ai_enabled=no`` via
command-line or via ``custom.py`` file created with ``python goost.py config``.

After all above steps, you should be able to compile those sources in Goost if
you call ``scons`` command:

.. code-block:: shell

    cd goost
    scons

Next, classes must be registered in :ref:`class_classdb`. Create
``register_ai_types.h`` and ``register_ai_types.cpp`` where we can register
``FiniteStateMachine`` and ``FiniteStateMachineNode`` classes respectively:

.. code-block:: shell

    cd scene/ai
    touch register_ai_types.h
    touch register_ai_types.cpp

.. code-block:: cpp

    // scene/ai/register_ai_types.h

    namespace goost {

    void register_ai_types();
    void unregister_ai_types();
    
    } // namespace goost
    
.. code-block:: cpp

    // scene/ai/register_ai_types.cpp

    #include "register_ai_types.h"
    #include "goost/classes_enabled.gen.h"
    
    namespace goost {
    
    void register_ai_types() {
        goost::register_class<FiniteStateMachine>();
        goost::register_class<FiniteStateMachineNode>();
    }
    
    void unregister_ai_types() {
        // Nothing to do yet.
    }
    
    } // namespace goost

If you look closer, we don't use ``ClassDB`` directly to register our classes.
We use a template specialization technique which allows Goost to register those
classes only if they are enabled. If those classes are disabled via
``custom.py``, then the implementation of those will be no-op (as declared in
auto-generated ``classes_enabled.gen.h``). Unlike components, we don't have to
use preprocessor defines to conditionally register individual classes.

Every ``register_*_types()`` callback implementation in Goost requires inclusion
of ``"goost/classes_enabled.gen.h"`` header, where all Goost classes are
included. Due to this, we'll need to include our ``FiniteStateMachine``
declaration in ``"goost/goost.h"`` as well, which is an umbrella header of all
classes defined in Goost:

.. code-block:: cpp

    // goost.h
    // ...
    #include "scene/2d/poly_shape_2d.h"
    #include "scene/2d/visual_shape_2d.h"
    #include "scene/ai/finite_state_machine.h" // FiniteStateMachine
    #include "scene/gui/grid_rect.h"
    #include "scene/physics/2d/poly_collision_shape_2d.h"
    // ...

Just like with parent ``SCsub``, we also need to call into
``register_ai_types()`` from within parent ``scene`` component, namely in
``register_scene_types()``:

.. code-block:: cpp

    // scene/register_scene_types.cpp

    #include "register_scene_types.h"

    #include "physics/register_physics_types.h"
    #include "ai/register_ai_types.h" // FiniteStateMachine

    #include "goost/classes_enabled.gen.h"

    namespace goost {

    void register_scene_types() {
        // ...
    #ifdef GOOST_AI_ENABLED
	    register_ai_types(); // FiniteStateMachine
    #endif
    }

    void unregister_scene_types() {
        // ...
    #ifdef GOOST_AI_ENABLED
        unregister_ai_types(); // FiniteStateMachine
    #endif
    }

    } // namespace goost

Similarly to construction environment variables in ``SCsub``, Goost
automatically defines a set of preprocessor defines ``GOOST_*_ENABLED`` which
allows us to compile code conditionally.

Once you've made the changes above, you should be able to compile Goost again
with ``scons`` command. If everything goes well, you can run the engine with
the following command:

.. code-block:: shell

    cd goost
    python run.py editor

Verify that new classes exists in documentation and are usable in GDScript.

Documentation
~~~~~~~~~~~~~

Once you've implemented and built new classes, you can (or rather should)
document them. Goost slightly simplifies this process by running the following
command:

.. code-block:: shell

    cd goost
    python run.py doc
    
In our case, you'll see ``FiniteStateMachine.xml`` and
``FiniteStateMachineNode.xml`` files generated at ``doc/`` directory. Fill them
out just like other ``xml`` files in the same directory and compile Godot again
with:

.. code-block:: shell

    scons
    
If you'd like to see how the built-in documentation looks with new classes from
within the Godot's editor, run:

.. code-block:: shell

    cd goost
    python run.py editor

.. note::
    
    Unlike in Godot, you don't have to manually list a new class in
    ``config.py::get_doc_classes()``, because those are collected automatically
    in Goost from ``goost.py::classes``.

Unit tests
~~~~~~~~~~

While implementing new classes, you want to make sure that they work as
expected! Running existing unit tests is similar to generating documentation:

.. code-block:: shell

    cd goost
    python run.py tests

Unit tests reside under ``tests/project`` directory. The ``project`` folder is a
master Godot test project which contains ``goost`` directory with tests. Tests
are organized in such a way to closely resemble Goost's source tree.

Since we've introduced ``ai`` component as described in previous sections, we
create ``res://goost/scene/ai`` folder and create
``test_finite_state_machine.gd`` unit test file there. Goost currently uses
`GUT <https://github.com/bitwes/Gut>`_ unit testing framework to write and run
tests using GDScript:

.. code-block:: gdscript

    extends "res://addons/gut/test.gd"

    func test_state():
        var fsm = FiniteStateMachine.new()
        add_child_autofree(fsm)

        var state = FiniteStateMachineNode.new()
        fsm.add_child(state)
        fsm.state = state

        assert_eq(fsm.state, state)

Save the file and run:

.. code-block:: shell

    cd goost
    python run.py tests

To speed up the development, you can run a single unit test file as well:

.. code-block:: shell

    python run.py tests -t "scene/ai/test_finite_state_machine.gd"

.. note::

    It's not necessary to start Godot editor to write and run tests. All unit
    test files in Goost must be prefixed with ``test_`` to be run from the
    command-line interface.

Editor icons
~~~~~~~~~~~~

The process of adding editor icons for new classes is no different from Godot,
please refer to Godot's :ref:`doc_editor_icons` documentation.

Integrating third-party code
----------------------------

If you want to add a feature which relies on external code written by other
developers, there are several requirements to resolve and steps to perform:

1. The third-party code must be compatible with MIT license.
2. Do not use ``git`` submodules, unless third-party code does not allow to
   distribute its source code directly, or when it's more safe to distribute the
   code via submodules. Whenever possible, always try to bundle the third-party
   code (the Godot way).
3. Place third-party code in ``goost/thirdparty/`` under respective directory.
4. Compile third-party code from within ``goost/thirdparty/SCsub``, compile
   conditionally if it's part of existing Goost component.
5. Make sure to list third-party code in ``goost/thirdparty/README.md``.
6. Update ``goost/COPYRIGHT.txt`` to comply with third-party license terms. Add
   new license text if it doesn't already exist.
7. Build the engine, run editor and go to ``Help`` → ``About Goost`` to open
   Goost "About" dialog. Make sure the third-party component appears at the
   "Third-party Licenses" tab.
