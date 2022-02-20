Modules
=======

The extension provides optional C++ modules which can be compiled alongside, and
has mostly convenience purpose of "batteries included". They are no different to
the Goost extension, which is in fact a regular C++ module.

Creating built-in modules
-------------------------

Built-in modules are versioned as part of Goost and are located at ``modules/``
directory.

See Godot Engine's :ref:`Custom modules in C++ <doc_custom_modules_in_c++>` for
an exhaustive instructions on developing modules.

.. _doc_adding_community_modules:

Adding community modules
------------------------

The following command must be used from within the root of the Goost repository:

.. code-block:: shell

    git submodule add --name module_name <URL> modules/module_name

The ``--name`` option is recommended to specify as cloning the module via the
URL may not always produce correct module name required by the build system. For
instance, if you have a module with URL similar to:

.. code-block:: shell

    https://github.com/Godette/gd_module-godette

You'll need to add the module with:

.. code-block:: shell

    git submodule add --name godette https://github.com/Godette/gd_module-godette modules/godette
