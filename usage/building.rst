.. _doc_building:

Building from source
====================

If you plan to customize Godot/Goost by picking only the features you need, or
would like to integrate other modules beside Goost in your projects, you'll need
to learn how to compile Godot from source yourself.

Please follow the Godot Engine official documentation instructions for your
target platform of interest if you're not familiar with the build process yet:

- :ref:`Compiling Godot Engine<toc-devel-compiling>`

Compatibility
-------------

Goost aims to target both Godot Engine's stable and development versions. For
the current version this documentation targets, you'll need to checkout the
respective Godot branch:

.. parsed-literal::
    cd godot
    git checkout |godot_branch|

If you ever need to compile Goost for other versions, the compatibility table
can be summarized as following:

+----------------------+---------------------+
|     Goost branch     |    Godot branch     |
+======================+=====================+
| ``gd3`` (latest)     | ``3.4`` (stable)    |
+----------------------+---------------------+
| ``1.0-gd3`` (stable) | ``3.4`` (stable)    |
+----------------------+---------------------+
| ``gd4`` (latest)     | ``master`` (latest) |
+----------------------+---------------------+

.. note::
    The default Goost branch always targets the latest Godot *stable* version. 

Compiling Goost
---------------

Building Godot with Goost is done in the same way as building the engine itself:

.. code-block:: shell

    git clone https://github.com/goostengine/goost
    cd goost
    scons
    
This clones the Godot Engine repository automatically and allows to compile the
engine with all the Goost components and other modules provided alongside the
extension.

After compilation is done, the resulting binaries can be found at ``godot/bin``
directory relative to the Goost repository. The binaries have the ``goost``
suffix appended for each target platform. Run the executable and search the
built-in documentation pages to make sure that the classes provided by the
extension are instantly accessible (as seen in the
:ref:`Class reference <toc-class-ref>`).

.. note:: 
    Please `report any issues <https://github.com/goostengine/goost/issues/new/choose>`_ 
    if you stumble upon compilation errors.

Compiling externally
--------------------

Goost is implemented as a regular C++ module, so please refer to the official 
Godot Engine documentation on how to compile the engine with custom modules:

- :ref:`Introduction to the build system: Custom modules <doc_buildsystem_custom_modules>`
- :ref:`Custom modules in C++ <doc_custom_modules_in_c++>`

An alternative way to compile Goost is by using the ``custom_modules`` build
option explicitly from within Godot source root:

.. code-block:: shell

    cd godot
    scons custom_modules="/path/to/directory/containing/goost"

.. tip::
    You can use ``extra_suffix`` build option if you want to distinguish between
    vanilla Godot binaries and Godot with the Goost extension:
    
    .. code-block:: shell

        scons custom_modules=".." extra_suffix="goost"
