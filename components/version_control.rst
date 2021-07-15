Version Control
===============

.. include:: /classes/component_vcs.rsti

Overview
--------

The component provides built-in implementation of various version control
providers. Only Git is currently supported out of the box.

Git
~~~

The "Commit" dock and "Version Control" bottom panel will automatically appear
once the editor is launched if you have a repository already initialized for
Godot project. Otherwise, go to "Project" → "Version Control" and press on one
of the available built-in providers to initialize a new repository, for
instance:

.. image:: img/version_control_setup_git.*
    :alt: Initialize Git repository

Once the repository is initialized or new changes are detected, you'll see a
list of files in the "Commit" dock:

.. image:: img/version_control_commit_dock.*
    :alt: Commit dock

Press "Stage All" or "Stage Selected" to prepare files for commit, provide
a commit message, and press "Commit Changes" button.

.. note::
    
    Unlike Godot's official GDNative implementation of the Git plugin, Goost
    does not create an initial empty commit automatically upon repository setup,
    so you can control the contents of the initial commit yourself.

If you don't want the plugin to be automatically initialized upon editor launch
(say, you want to use external GDNative implementation of the same provider), go
to "Editor" → "Editor Settings" → "Version Control" → "Git", and disable
``Initialize Plugin At Editor Startup`` option:

.. image:: img/version_control_git_settings.*
    :alt: Git Settings
    
You can also override ``user.name`` and ``user.email`` signature via editor
settings if you don't have Git installed or configured system-wide. Signature is
required to configure in order to use the commit functionality.
