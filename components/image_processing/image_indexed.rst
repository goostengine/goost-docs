Indexed image
=============

.. image:: img/image_indexed_palette.*
    :alt: Image palettes
    
The support for indexed images is provided by
:ref:`ImageIndexed<class_ImageIndexed>` class, which can do the following:

* create and operate on indexed pixels;
* generate an optimal palette from an image with specified number of colors and
  optional dithering;
* create palette and modify palette manually;
* extract color palette from PNG images when loading from disk;
* save PNG with a palette associated with it to modified within Godot, also
  supporting saving indexed color images.

Examples
--------

Taking a screenshot and reducing number of colors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This allows to optimize for size when saving such images as indexed.

::

    func save_screenshot():
        get_viewport().render_target_v_flip = true # hmm
        yield(VisualServer, "frame_post_draw")
        get_viewport().render_target_v_flip = false

        screenshot.convert(Image.FORMAT_RGBA8)
        screenshot.generate_palette()
        screenshot.save_png("screenshot_indexed.png")

Finding dominant or average colors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As palette generation involves color quantization, limiting the number of colors


::

    image.generate_palette(2) # first color is usually background
    var dominant_color = image.get_palette_color(1)
    # or...
    image.generate_palette(8)
    var average_colors = image.get_palette()

.. image:: img/image_indexed_average_colors.*
    :alt: Image average colors by color quantization.

Image posterization
~~~~~~~~~~~~~~~~~~~

::

    var image = get_node('sprite').texture.get_data()
    image.generate_palette(8)
    image.apply_palette()
    

.. image:: img/image_indexed_posterization.*
    :alt: Image posterization.

Palette swapping
~~~~~~~~~~~~~~~~

.. note:: 

    Palette swapping of sprites is usually done via shaders, which is much
    faster and doesn't have any unrecoverable consequences for the original
    texture.

::

    var image = get_node('sprite').texture.get_data()
    if not image.has_palette():
        image.generate_palette(16)

    image.set_palette_color(5, Color.red)
    image.set_palette_color(9, Color.gold)
    image.set_palette_color(1, Color.darkred)

    image.apply_palette()

.. image:: img/image_indexed_palette_swapping.*
    :alt: Image palette swapping.

Example project
~~~~~~~~~~~~~~~

The indexed image processing is demonstrated at
`Goost Examples repository <https://github.com/goostengine/goost-examples/tree/gd3/imaging/image_indexed>`_.
