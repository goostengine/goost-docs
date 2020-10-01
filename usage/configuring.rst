.. _doc_configuring_the_build:

Configuring the build
=====================

.. note::

    This page assumes that you've read :ref:`doc_installation`.

Extension
---------

The root ``SConstruct`` allows you to compile the engine with the extension by
running the same ``scons`` command, and the behavior can be configured.

By default, running ``scons`` from within Goost source root will clone the Godot
repository within the current working directory. If you'd like to prevent this
behavior, you can define ``GODOT_SOURCE_PATH`` environment variable pointing to
Godot source within your filesystem before compiling:

.. tabs::
 .. code-tab:: bash Linux/macOS

     export GODOT_SOURCE_PATH="/path/to/godot"

 .. code-tab:: bat Windows (cmd)

     set GODOT_SOURCE_PATH=C:\src\godot

 .. code-tab:: powershell Windows (powershell)

     $env:GODOT_SOURCE_PATH="C:/src/godot"
     
If the path is invalid, the script shall try to find Godot at the parent
directory. If this fails too, then the Godot repository is cloned from the
remote URL defined by ``GODOT_REPO_URL`` environment variable, which can be
configured similarly as above.

Command-line options
~~~~~~~~~~~~~~~~~~~~

+----------------------------+-------------------------------------------------------------------+
| Option                     | Description                                                       |
+----------------------------+-------------------------------------------------------------------+
| ``godot_version``          | Godot Engine version (branch, tags, commit hashes).               |
+----------------------------+-------------------------------------------------------------------+
| ``godot_sync``             | Synchronize Godot Engine version from remote URL before building. |
+----------------------------+-------------------------------------------------------------------+
| ``godot_modules_enabled``  | Build all Godot builtin modules.                                  |
+----------------------------+-------------------------------------------------------------------+
| ``parent_modules_enabled`` | Build all modules which may reside in the same parent directory.  |
+----------------------------+-------------------------------------------------------------------+

The specific Godot version can also be overridden with ``GODOT_VERSION``
environment variable accepting the same branch names, tags, commit hashes,
everything which is supported by ``git``.

Usage examples
^^^^^^^^^^^^^^

Compile the stable version of the engine with Goost::

    scons godot_version=3.2-stable

Compile the beta or development versions of the engine, synchronizing any
changes from remote URL automatically::

    scons godot_version=3.2 godot_sync=yes

Disable non-essential Godot modules for testing and development purposes (speeds
up compilation, optimizes for size)::

    scons godot_modules_enabled=no

Compile additional modules which may reside alongside Goost::

    scons parent_modules_enabled=yes

Components
----------

By default, all extension components are built, but it's also possible to
disable them. Disabling a single component involves compiling the engine with
one of the ``goost_*_enabled`` build options:

.. code-block:: shell

    scons goost_math_enabled=no

It's also possible to disable a entire branch of components:

.. code-block:: shell

    # For instance, this disables both ``image`` and ``math`` components.
    scons goost_core_enabled=no
    
See each component build options in the :ref:`sec-components` section.

Modules
-------

The extension provides as set of optional modules (regular C++ modules just like
this extension) which are compiled alongside this extension by default if you
build the engine from within Goost root with the ``scons`` command.

If you compile the Goost extension externally, those modules can be compiled by
appending to the list of paths specified by ``custom_modules`` option:

.. code-block:: shell

    scons custom_modules="/path/to/dir/containing/goost,/path/to/goost/modules"

It's possible to compile the modules independently of whether Goost is enabled:

.. code-block:: shell

    scons module_goost_enabled="no" custom_modules="/path/to/goost/modules"

Configuring modules
~~~~~~~~~~~~~~~~~~~

Goost distinguishes between built-in and community modules. Built-in modules are
officially maintained by the Goost authors and are versioned as part of the
extension. Community modules represent ``git`` submodules which are maintained
by third-party developers.

The ``disable_builtin.py`` and ``disable_community.py`` configuration scripts
located at ``modules/`` directory aim to list all modules in such a way that
they can be disabled by users, as modules are enabled by default once detected
by the build system, unless they are explicitly disabled via
``config.py::is_enabled`` method per each module.

If you'd like to opt-out from compiling certain modules, you'll have to disable
each of the unused modules explicitly:

.. code-block:: shell

    scons custom_modules="/path/to/dir/containing/goost,/path/to/goost/modules" \
    module_a_enabled="no" module_b_enabled="no" module_c_enabled="no" ...

All of the above options can be conveniently defined by creating ``custom.py`` at
the root of Godot source, or pointing to an existing configuration file such as
above:

.. code-block:: shell

    scons profile="modules/goost/disable_community.py"

Community modules can be fetched with:

.. code-block:: shell

    git submodule update --init --recursive

Or if you haven't yet cloned Goost:

.. code-block:: shell

    git clone https://github.com/goostengine/goost.git --recurse-submodules

Other
-----

For other Godot and Goost options which may be provided by components, run::

    scons --help
