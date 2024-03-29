:github_url: hide

.. Generated automatically by doc/tools/make_rst.py in Godot's source tree.
.. DO NOT EDIT THIS FILE, but the PolyCapsule2D.xml source instead.
.. The source is found in doc/classes or modules/<name>/doc_classes.

.. _class_PolyCapsule2D:

PolyCapsule2D
=============

**Inherits:** :ref:`PolyNode2D<class_PolyNode2D>` **<** :ref:`Node2D<class_Node2D>` **<** :ref:`CanvasItem<class_CanvasItem>` **<** :ref:`Node<class_Node>` **<** :ref:`Object<class_Object>`

A capsule :ref:`PolyNode2D<class_PolyNode2D>` shape.

Description
-----------

Builds a polygon outline closely approximating a capsule in 2D (also known as "stadium").

Properties
----------

+---------------------------+----------------------------------------------------------+----------+
| :ref:`float<class_float>` | :ref:`height<class_PolyCapsule2D_property_height>`       | ``64.0`` |
+---------------------------+----------------------------------------------------------+----------+
| :ref:`float<class_float>` | :ref:`max_error<class_PolyCapsule2D_property_max_error>` | ``0.25`` |
+---------------------------+----------------------------------------------------------+----------+
| :ref:`float<class_float>` | :ref:`radius<class_PolyCapsule2D_property_radius>`       | ``32.0`` |
+---------------------------+----------------------------------------------------------+----------+

Property Descriptions
---------------------

.. _class_PolyCapsule2D_property_height:

- :ref:`float<class_float>` **height**

+-----------+-------------------+
| *Default* | ``64.0``          |
+-----------+-------------------+
| *Setter*  | set_height(value) |
+-----------+-------------------+
| *Getter*  | get_height()      |
+-----------+-------------------+

Capsule's total height. When ``height == 0.0``, then a circle is generated instead.

----

.. _class_PolyCapsule2D_property_max_error:

- :ref:`float<class_float>` **max_error**

+-----------+----------------------+
| *Default* | ``0.25``             |
+-----------+----------------------+
| *Setter*  | set_max_error(value) |
+-----------+----------------------+
| *Getter*  | get_max_error()      |
+-----------+----------------------+

Represents the maximum gap in pixels allowed between capsule's half circle segment and the boundary of the mathematical circle, with low values increasing the accuracy.

----

.. _class_PolyCapsule2D_property_radius:

- :ref:`float<class_float>` **radius**

+-----------+-------------------+
| *Default* | ``32.0``          |
+-----------+-------------------+
| *Setter*  | set_radius(value) |
+-----------+-------------------+
| *Getter*  | get_radius()      |
+-----------+-------------------+

Capsule's semicircle radius, applies to both ends.

.. |virtual| replace:: :abbr:`virtual (This method should typically be overridden by the user to have any effect.)`
.. |const| replace:: :abbr:`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`
.. |vararg| replace:: :abbr:`vararg (This method accepts any number of arguments after the ones described here.)`
