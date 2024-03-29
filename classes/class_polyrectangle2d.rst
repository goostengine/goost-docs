:github_url: hide

.. Generated automatically by doc/tools/make_rst.py in Godot's source tree.
.. DO NOT EDIT THIS FILE, but the PolyRectangle2D.xml source instead.
.. The source is found in doc/classes or modules/<name>/doc_classes.

.. _class_PolyRectangle2D:

PolyRectangle2D
===============

**Inherits:** :ref:`PolyNode2D<class_PolyNode2D>` **<** :ref:`Node2D<class_Node2D>` **<** :ref:`CanvasItem<class_CanvasItem>` **<** :ref:`Node<class_Node>` **<** :ref:`Object<class_Object>`

A rectangle :ref:`PolyNode2D<class_PolyNode2D>` shape.

Description
-----------

Builds a rectangle-based outline.

Properties
----------

+-------------------------------+--------------------------------------------------------+-----------------------+
| :ref:`Vector2<class_Vector2>` | :ref:`extents<class_PolyRectangle2D_property_extents>` | ``Vector2( 32, 32 )`` |
+-------------------------------+--------------------------------------------------------+-----------------------+

Property Descriptions
---------------------

.. _class_PolyRectangle2D_property_extents:

- :ref:`Vector2<class_Vector2>` **extents**

+-----------+-----------------------+
| *Default* | ``Vector2( 32, 32 )`` |
+-----------+-----------------------+
| *Setter*  | set_extents(value)    |
+-----------+-----------------------+
| *Getter*  | get_extents()         |
+-----------+-----------------------+

The rectangle's half extents. The width and height of this shape is twice the half extents.

.. |virtual| replace:: :abbr:`virtual (This method should typically be overridden by the user to have any effect.)`
.. |const| replace:: :abbr:`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`
.. |vararg| replace:: :abbr:`vararg (This method accepts any number of arguments after the ones described here.)`
