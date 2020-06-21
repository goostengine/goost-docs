Physics
=======

.. note::
    To disable this component, use ``goost_physics_enabled=no`` option (see
    :ref:`doc_configuring_the_build`).

This component provides classes which are useful for performing physics queries
using the existing low-level Godot physics API, but which are difficult to
implement and use via GDScript, such as
:ref:`Physics2DShapeQueryParameters<class_Physics2DShapeQueryParameters>`.

For now, there's only one class which partially fulfills this need:

* :ref:`ShapeCast2D<class_ShapeCast2D>`
