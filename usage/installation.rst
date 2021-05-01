.. _doc_installation:

Installing Goost
================

Downloading
-----------

Goost officially provides custom Godot editor and export templates which you can
freely download for each platform of interest. Proceed to the
`Download <https://goostengine.github.io/download.html>`_ page to get the latest
released version.

Installing export templates
---------------------------

The process of installing the export templates that you download from
`Goost website <https://goostengine.github.io/>`_ is similar to Godot, with the
caveat that they cannot be downloaded from within the editor directly.

1. `Download <https://goostengine.github.io/download.html>`_ export templates
   (either ``Standard`` or ``Mono`` version).
2. Launch Godot editor and go to ``Editor`` → ``Manage Export Templates...``
   menu option.
3. You'll see a window asking you to download the export templates. Do **not**
   press the ``Download`` button as it will download raw Godot export templates
   without Goost:
   
   .. image:: img/export_templates_no_download.*
    :alt: Export Template Manager - No download
    
   If you already have export templates installed, uninstall them first.
4. Instead, you need to install export templates from a downloaded ``tpz`` file:

   .. image:: img/export_templates_install_from_file.*
    :alt: Export Template Manager - Install From File
    
   .. image:: img/export_templates_open.*
    :alt: Export Template Manager - Open a File
    
   This will extract templates into editor templates folder on your filesystem.
   
   .. image:: img/export_templates_installed.*
    :alt: Export Template Manager - Installed
5. Close the window and go to ``Project`` → ``Export...`` to export a project
   with Goost!

Again, do not attempt to re-download the export templates if you need to change
the export templates due to **Goost** update. Uninstall and install export
templates manually. However, if the update is coming from Godot, it should be
safe to install a new set of export templates for each released **Godot**
version.

Installing separately
~~~~~~~~~~~~~~~~~~~~~

If you don't want to replace Godot's official export templates with the ones
provided by Goost, you have two options:

- Run Godot in self-contained mode. Create a file with a ``_sc_`` name next to
  downloaded Goost editor executable, and proceed to installing export templates
  as described above. The resulting export templates are going to be extracted
  under ``editor_data/templates`` directory relative to the editor executable.
- Extract the downloaded export templates yourself and specify custom export
  templates via ``Custom Template`` option for each new export preset:
  
  .. image:: img/export_custom_template.*
   :alt: Export - Custom templates
