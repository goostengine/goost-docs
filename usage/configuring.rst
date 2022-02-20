.. _doc_configuring_the_build:

Configuring the build
=====================

.. note::

    This page assumes that you've read :ref:`doc_building`.

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
     
If the path is invalid, then the Godot repository is cloned from the remote URL
defined by ``GODOT_REPO_URL`` environment variable, which can be configured
similarly as above.

Command-line options
~~~~~~~~~~~~~~~~~~~~

+----------------------------+----------------------------------------------------------------------------------------------------------------------------------+----------------------+
| SCons build option         | Description                                                                                                                      | Default value        |
+----------------------------+----------------------------------------------------------------------------------------------------------------------------------+----------------------+
| ``godot_version``          | Godot version to build. Accepts the branch names, tags, ``git`` commit hashes. Can be overridden with ``GODOT_VERSION`` env var. | Run ``scons --help`` |
+----------------------------+----------------------------------------------------------------------------------------------------------------------------------+----------------------+
| ``godot_sync``             | Synchronize Godot version from remote ``GODOT_REPO_URL`` before building.                                                        | ``no``               |
+----------------------------+----------------------------------------------------------------------------------------------------------------------------------+----------------------+
| ``godot_modules_enabled``  | Build all Godot builtin modules. If ``no``, disables modules which are not essential to build to test out Goost.                 | ``yes``              |
+----------------------------+----------------------------------------------------------------------------------------------------------------------------------+----------------------+
| ``use_godot_patches``      | Apply custom fixes and small enhancements to Godot source before building from the ``godot_patches`` directory.                  | ``no``               |
+----------------------------+----------------------------------------------------------------------------------------------------------------------------------+----------------------+
| ``godot_patches``          | A directory path containing custom Godot patches. Patches at the default directory won't be applied if using a custom path.      | ``"misc/patches"``   |
+----------------------------+----------------------------------------------------------------------------------------------------------------------------------+----------------------+

Usage examples
^^^^^^^^^^^^^^

Compile the stable version of the engine with Goost:

.. code-block:: shell

    scons godot_version=3.4-stable

Compile the beta or development versions of the engine, synchronizing any
changes from remote URL automatically:

.. code-block:: shell

    scons godot_version=3.4 godot_sync=yes

Disable non-essential Godot modules for testing and development purposes (speeds
up compilation, optimizes for size):

.. code-block:: shell

    scons godot_modules_enabled=no

Components
----------

By default, all extension components are built, but it's also possible to
disable them. Disabling a single component involves compiling the engine with
one of the ``goost_*_enabled`` build options:

.. code-block:: shell

    scons goost_math_enabled=no

It's also possible to disable an entire branch of components. For instance, the
following disables both ``image`` and ``math`` components:

.. code-block:: shell

    scons goost_core_enabled=no
    
If you're only interested in using a single Goost component, then you should
use ``goost_components_enabled=no`` to tell the build system that all components
are disabled by default. For instance, the following will enable the ``image``
component.

.. code-block:: shell

    scons goost_components_enabled=no goost_image_enabled=yes
    
The above will also force parent components to be enabled as well (in this case,
``core``), otherwise child components won't compile at all. Similarly, if
``goost_components_enabled=yes`` and you disable a single component, all child
components are going to be disabled recursively.

If you don't need the functionality provided by some components, Goost allows to
disable individual classes as well! It may not be practical to specify all those
options via command-line interface, so you can also create ``custom.py`` at the
root of Goost repository to configure both enabled components and individual
classes:

.. code-block:: python

    # custom.py

    components_enabled_by_default = False
    components = {
        "math": True,
        "gui": False,
    }

    classes_enabled_by_default = True
    classes = {
        "GoostEngine": True,
        "LinkedList": False,
        "VariantMap": False,
        "VariantResource": False,
    }

If some classes depend on others, you don't have to worry about enabling them
manually, dependencies are going to be satisfied automatically.

.. tip::

    You can run ``python goost.py config`` at the root of Goost repository
    to generate the ``custom.py`` file above with all the components and
    classes.

.. note::
    
    It's not possible configure individual classes via command-line interface,
    only via ``custom.py``.

See each component build options in the :ref:`sec-components` section as well.

Modules
-------

The extension provides as set of optional modules (regular C++ modules just like
this extension) which are compiled alongside this extension by default if you
build the engine from within Goost root with the ``scons`` command.

If you compile Goost externally and don't want to compile modules provided by
Goost, use ``custom_modules_recursive=no``:

.. code-block:: shell

    scons custom_modules="/path/to/dir/containing/goost" custom_modules_recursive=no

It's possible to compile the modules independently of whether Goost is enabled:

.. code-block:: shell

    scons module_goost_enabled="no" custom_modules="/path/to/goost/modules"

Configuring modules
~~~~~~~~~~~~~~~~~~~

Goost distinguishes between built-in and community modules. Built-in modules are
officially maintained by the Goost authors and are versioned as part of the
extension. Community modules represent ``git`` submodules which are maintained
by third-party developers.

If you'd like to opt-out from compiling certain modules, you'll have to disable
each of the unused modules explicitly:

.. code-block:: shell

    scons custom_modules="/path/to/dir/containing/goost,/path/to/goost/modules" \
    module_a_enabled="no" module_b_enabled="no" module_c_enabled="no" ...

All of the above options can be conveniently defined by creating ``custom.py`` at
the root of Godot source, or pointing to an existing configuration file:

.. code-block:: shell

    scons profile="/path/to/profile.py"

Community modules can be fetched with:

.. code-block:: shell

    git submodule update --init --recursive

Or if you haven't yet cloned Goost:

.. code-block:: shell

    git clone https://github.com/goostengine/goost.git --recurse-submodules

Patching
--------

The Godot core cannot be modified without tinkering with the engine source, but
in some cases, it's necessary to do so.

The engine can be optionally modified by applying custom ``git diff`` patches
which match ``*.patch`` or ``*.diff`` filenames automatically. This is disabled
by default, and can be enabled with the ``use_godot_patches`` build option:

.. code-block:: shell

    scons use_godot_patches=yes

By default, patches are searched within the built-in ``misc/patches`` directory
in Goost. All patches in the directory are collected and applied automatically
before building Godot with Goost.

.. note::

    Patching only works if you have Godot cloned under the Goost directory.

The ``godot_patches`` build option can be overridden to point to a custom
directory path. If you do specify a custom directory, the built-in patches will
not be applied. It's recommended that you copy built-in patches to your own
directory instead:

.. code-block:: shell

    scons use_godot_patches=yes godot_patches=/path/to/custom/patches

The built-in ``misc/patches`` directory exists for the purpose of collecting
various patches which may benefit other developers, and may not always apply
to the current version of Godot.

Creating patches
~~~~~~~~~~~~~~~~

The following commands can be run to generate patches from within Godot Engine
repository:

.. tabs::
 .. code-tab:: bash Linux/macOS (shell)

    # From committed changes:
    git format-patch HEAD~1 -o ../misc/patches/custom.patch
    # From non-committed changes (working tree):
    git diff > ../misc/patches/custom.patch
    # From a pull request/remotely (from root):
    curl https://github.com/godotengine/godot/pull/42653.patch > misc/patches/custom.patch

 .. code-tab:: powershell Windows (powershell)

    # From committed changes:
    git format-patch HEAD~1 --stdout | Out-File -Encoding utf8 ../misc/patches/custom.patch
    # From non-committed changes (working tree):
    git diff | Out-File -Encoding utf8 ../misc/patches/custom.patch
    # From a pull request/remotely (from root):
    Invoke-RestMethod "https://github.com/godotengine/godot/pull/42653.patch" | Out-File -Encoding utf8 "misc/patches/custom.patch"

On some systems, the resulting patch encoding and line endings may not be
compatible with ``git``, so they may fail to apply. Patches must use ``utf8``
encoding and have ``LF`` line endings.

Other
-----

For other Godot and Goost options which may be provided by components, run::

    scons --help
