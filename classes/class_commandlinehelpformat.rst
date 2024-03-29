:github_url: hide

.. Generated automatically by doc/tools/make_rst.py in Godot's source tree.
.. DO NOT EDIT THIS FILE, but the CommandLineHelpFormat.xml source instead.
.. The source is found in doc/classes or modules/<name>/doc_classes.

.. _class_CommandLineHelpFormat:

CommandLineHelpFormat
=====================

**Inherits:** :ref:`Reference<class_Reference>` **<** :ref:`Object<class_Object>`

This class contains formatting options for constructing a help message in :ref:`CommandLineParser<class_CommandLineParser>`.

Description
-----------

The class is used to pass formatting parameters to the :ref:`CommandLineParser.get_help_text<class_CommandLineParser_method_get_help_text>` method.

Properties
----------

+-----------------------------+--------------------------------------------------------------------------------------------+----------+
| :ref:`bool<class_bool>`     | :ref:`autogenerate_usage<class_CommandLineHelpFormat_property_autogenerate_usage>`         | ``true`` |
+-----------------------------+--------------------------------------------------------------------------------------------+----------+
| :ref:`String<class_String>` | :ref:`footer<class_CommandLineHelpFormat_property_footer>`                                 | ``""``   |
+-----------------------------+--------------------------------------------------------------------------------------------+----------+
| :ref:`String<class_String>` | :ref:`header<class_CommandLineHelpFormat_property_header>`                                 | ``""``   |
+-----------------------------+--------------------------------------------------------------------------------------------+----------+
| :ref:`int<class_int>`       | :ref:`left_pad<class_CommandLineHelpFormat_property_left_pad>`                             | ``2``    |
+-----------------------------+--------------------------------------------------------------------------------------------+----------+
| :ref:`int<class_int>`       | :ref:`line_length<class_CommandLineHelpFormat_property_line_length>`                       | ``80``   |
+-----------------------------+--------------------------------------------------------------------------------------------+----------+
| :ref:`int<class_int>`       | :ref:`min_description_length<class_CommandLineHelpFormat_property_min_description_length>` | ``40``   |
+-----------------------------+--------------------------------------------------------------------------------------------+----------+
| :ref:`int<class_int>`       | :ref:`right_pad<class_CommandLineHelpFormat_property_right_pad>`                           | ``4``    |
+-----------------------------+--------------------------------------------------------------------------------------------+----------+
| :ref:`String<class_String>` | :ref:`usage_title<class_CommandLineHelpFormat_property_usage_title>`                       | ``""``   |
+-----------------------------+--------------------------------------------------------------------------------------------+----------+

Property Descriptions
---------------------

.. _class_CommandLineHelpFormat_property_autogenerate_usage:

- :ref:`bool<class_bool>` **autogenerate_usage**

+-----------+-------------------------------+
| *Default* | ``true``                      |
+-----------+-------------------------------+
| *Setter*  | set_autogenerate_usage(value) |
+-----------+-------------------------------+
| *Getter*  | is_usage_autogenerated()      |
+-----------+-------------------------------+

If ``true``, the usage text will be automatically generated according to passed options.

----

.. _class_CommandLineHelpFormat_property_footer:

- :ref:`String<class_String>` **footer**

+-----------+-------------------+
| *Default* | ``""``            |
+-----------+-------------------+
| *Setter*  | set_footer(value) |
+-----------+-------------------+
| *Getter*  | get_footer()      |
+-----------+-------------------+

Contains text to be displayed at the end of the help text.

----

.. _class_CommandLineHelpFormat_property_header:

- :ref:`String<class_String>` **header**

+-----------+-------------------+
| *Default* | ``""``            |
+-----------+-------------------+
| *Setter*  | set_header(value) |
+-----------+-------------------+
| *Getter*  | get_header()      |
+-----------+-------------------+

Contains text to be displayed at the beginning of the help text.

----

.. _class_CommandLineHelpFormat_property_left_pad:

- :ref:`int<class_int>` **left_pad**

+-----------+---------------------+
| *Default* | ``2``               |
+-----------+---------------------+
| *Setter*  | set_left_pad(value) |
+-----------+---------------------+
| *Getter*  | get_left_pad()      |
+-----------+---------------------+

The amount of indentation in spaces to the left of the options in the help text.

----

.. _class_CommandLineHelpFormat_property_line_length:

- :ref:`int<class_int>` **line_length**

+-----------+------------------------+
| *Default* | ``80``                 |
+-----------+------------------------+
| *Setter*  | set_line_length(value) |
+-----------+------------------------+
| *Getter*  | get_line_length()      |
+-----------+------------------------+

The maximum length of the line with option and description in help text. If the line exceeds this length, then its description will be split into several lines. See also :ref:`min_description_length<class_CommandLineHelpFormat_property_min_description_length>`.

----

.. _class_CommandLineHelpFormat_property_min_description_length:

- :ref:`int<class_int>` **min_description_length**

+-----------+-----------------------------------+
| *Default* | ``40``                            |
+-----------+-----------------------------------+
| *Setter*  | set_min_description_length(value) |
+-----------+-----------------------------------+
| *Getter*  | get_min_description_length()      |
+-----------+-----------------------------------+

The minimum description size used to split description when the line with option and description is too large. See also :ref:`line_length<class_CommandLineHelpFormat_property_line_length>`.

----

.. _class_CommandLineHelpFormat_property_right_pad:

- :ref:`int<class_int>` **right_pad**

+-----------+----------------------+
| *Default* | ``4``                |
+-----------+----------------------+
| *Setter*  | set_right_pad(value) |
+-----------+----------------------+
| *Getter*  | get_right_pad()      |
+-----------+----------------------+

The amount of indentation in spaces to the right of the options in the help text.

----

.. _class_CommandLineHelpFormat_property_usage_title:

- :ref:`String<class_String>` **usage_title**

+-----------+------------------------+
| *Default* | ``""``                 |
+-----------+------------------------+
| *Setter*  | set_usage_title(value) |
+-----------+------------------------+
| *Getter*  | get_usage_title()      |
+-----------+------------------------+

Title that will be displayed in usage text. If empty, the name of the current executable file will be used.

.. |virtual| replace:: :abbr:`virtual (This method should typically be overridden by the user to have any effect.)`
.. |const| replace:: :abbr:`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`
.. |vararg| replace:: :abbr:`vararg (This method accepts any number of arguments after the ones described here.)`
