:github_url: hide

.. Generated automatically by doc/tools/make_rst.py in Godot's source tree.
.. DO NOT EDIT THIS FILE, but the PolyDecomp2D.xml source instead.
.. The source is found in doc/classes or modules/<name>/doc_classes.

.. _class_PolyDecomp2D:

PolyDecomp2D
============

**Inherits:** :ref:`Reference<class_Reference>` **<** :ref:`Object<class_Object>`

Polygon partitioning.

Description
-----------

A singleton which provides various methods for polygon decomposition, partitioning etc.

A new local instance must be created manually with :ref:`new_instance<class_PolyDecomp2D_method_new_instance>` method if you need to override the default :ref:`parameters<class_PolyDecomp2D_property_parameters>`, else the methods in this class are available globally:

::

    var polygons = []
    # Globally.
    polygons = PolyDecomp2D.decompose_polygons([boundary, hole])
    # Locally.
    var pd = PolyDecomp2D.new_instance()
    pd.parameters.fill_rule = PolyDecompParameters2D.FILL_RULE_EVEN_ODD
    polygons = pd.decompose_polygons([boundary, hole])

Properties
----------

+-------------------------------------------------------------+-----------------------------------------------------------+
| :ref:`PolyDecompParameters2D<class_PolyDecompParameters2D>` | :ref:`parameters<class_PolyDecomp2D_property_parameters>` |
+-------------------------------------------------------------+-----------------------------------------------------------+

Methods
-------

+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Array<class_Array>`         | :ref:`decompose_polygons<class_PolyDecomp2D_method_decompose_polygons>` **(** :ref:`Array<class_Array>` polygons, :ref:`Decomposition<enum_PolyDecomp2D_Decomposition>` type **)** |const| |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Array<class_Array>`         | :ref:`decompose_polygons_into_convex<class_PolyDecomp2D_method_decompose_polygons_into_convex>` **(** :ref:`Array<class_Array>` polygons **)** |const|                                     |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Reference<class_Reference>` | :ref:`new_instance<class_PolyDecomp2D_method_new_instance>` **(** **)** |const|                                                                                                            |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Array<class_Array>`         | :ref:`triangulate_polygons<class_PolyDecomp2D_method_triangulate_polygons>` **(** :ref:`Array<class_Array>` polygons **)** |const|                                                         |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Enumerations
------------

.. _enum_PolyDecomp2D_Decomposition:

.. _class_PolyDecomp2D_constant_DECOMP_TRIANGLES_EC:

.. _class_PolyDecomp2D_constant_DECOMP_TRIANGLES_OPT:

.. _class_PolyDecomp2D_constant_DECOMP_TRIANGLES_MONO:

.. _class_PolyDecomp2D_constant_DECOMP_CONVEX_HM:

.. _class_PolyDecomp2D_constant_DECOMP_CONVEX_OPT:

enum **Decomposition**:

- **DECOMP_TRIANGLES_EC** = **0** --- Triangulate a polygon using the ear clipping algorithm. Time/Space complexity: O(n^2)/O(n).

- **DECOMP_TRIANGLES_OPT** = **1** --- Optimal triangulation in terms of edge length using dynamic programming algorithm. Time/Space complexity: O(n^3)/O(n^2).

- **DECOMP_TRIANGLES_MONO** = **2** --- Partition the polygon into monotone polygons, then triangulate. Time/Space complexity: O(n\*log(n))/O(n).

- **DECOMP_CONVEX_HM** = **3** --- Convex polygon partitioning using Hertel-Mehlhorn algorithm. Time/Space complexity: O(n^2)/O(n).

- **DECOMP_CONVEX_OPT** = **4** --- Optimal convex partition using dynamic programming algorithm by Keil and Snoeyink. Time/Space complexity: O(n^3)/O(n^3).

Property Descriptions
---------------------

.. _class_PolyDecomp2D_property_parameters:

- :ref:`PolyDecompParameters2D<class_PolyDecompParameters2D>` **parameters**

+----------+-----------------------+
| *Setter* | set_parameters(value) |
+----------+-----------------------+
| *Getter* | get_parameters()      |
+----------+-----------------------+

Parameters to configure the default behavior of operations. Cannot be configured via the global instance, use :ref:`new_instance<class_PolyDecomp2D_method_new_instance>` first if you need to override the defaults.

Method Descriptions
-------------------

.. _class_PolyDecomp2D_method_decompose_polygons:

- :ref:`Array<class_Array>` **decompose_polygons** **(** :ref:`Array<class_Array>` polygons, :ref:`Decomposition<enum_PolyDecomp2D_Decomposition>` type **)** |const|

Partitions polygons into several other convex polygons. The exact algorithm used depends on the type from :ref:`Decomposition<enum_PolyDecomp2D_Decomposition>`.

Both outer and inner polygons can be passed to cut holes during decomposition and are distinguished automatically, with potential performance cost.

\ **Note:** :ref:`DECOMP_TRIANGLES_OPT<class_PolyDecomp2D_constant_DECOMP_TRIANGLES_OPT>` and :ref:`DECOMP_TRIANGLES_OPT<class_PolyDecomp2D_constant_DECOMP_TRIANGLES_OPT>` do not support partitioning of a polygon with holes.

----

.. _class_PolyDecomp2D_method_decompose_polygons_into_convex:

- :ref:`Array<class_Array>` **decompose_polygons_into_convex** **(** :ref:`Array<class_Array>` polygons **)** |const|

Similar to :ref:`decompose_polygons<class_PolyDecomp2D_method_decompose_polygons>`, but partitions polygons with the :ref:`DECOMP_CONVEX_HM<class_PolyDecomp2D_constant_DECOMP_CONVEX_HM>`.

----

.. _class_PolyDecomp2D_method_new_instance:

- :ref:`Reference<class_Reference>` **new_instance** **(** **)** |const|

Instantiates a new local ``PolyDecomp2D`` instance, and :ref:`parameters<class_PolyDecomp2D_property_parameters>` can be configured.

----

.. _class_PolyDecomp2D_method_triangulate_polygons:

- :ref:`Array<class_Array>` **triangulate_polygons** **(** :ref:`Array<class_Array>` polygons **)** |const|

Similar to :ref:`decompose_polygons<class_PolyDecomp2D_method_decompose_polygons>`, but triangulates multiple polygons with the :ref:`DECOMP_TRIANGLES_MONO<class_PolyDecomp2D_constant_DECOMP_TRIANGLES_MONO>`.

.. |virtual| replace:: :abbr:`virtual (This method should typically be overridden by the user to have any effect.)`
.. |const| replace:: :abbr:`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`
.. |vararg| replace:: :abbr:`vararg (This method accepts any number of arguments after the ones described here.)`
