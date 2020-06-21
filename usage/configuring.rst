.. _doc_configuring_the_build:

Configuring the build
=====================

Components
----------

By default, all extension components are built, but it's also possible to
disable them.

Disabling a single component involves compiling the engine with one of the
``goost_*_enabled`` build options:

.. code-block:: shell

    scons custom_modules="/path/to/dir/containing/goost" goost_math_enabled=no

It's also possible to disable a entire branch of components:

.. code-block:: shell

    # For instance, this disables both ``image`` and ``math`` components.
    scons custom_modules="/path/to/dir/containing/goost" goost_core_enabled=no
    
See each component build options in the :ref:`sec-components` section.

Modules
-------

The extension provides as set of optional modules (regular C++ modules just like
this extension) which are not compiled alongside this extension by default. In
order to compile them, you can append to the list of paths specified by
``custom_modules`` option:

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

    git clone https://github.com/GoostGD/goost.git --recurse-submodules

Other
-----

For other Goost-specific build options, run:

.. tabs::
  .. code-tab:: bash Linux/macOS
  
      scons --help | grep goost_
  
  .. code-tab:: bat Windows
  
      scons --help | Select-String goost_
