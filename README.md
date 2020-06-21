# Goost documentation

[![Documentation Status](https://readthedocs.org/projects/goost/badge/?version=gd3)](https://goost.readthedocs.io/en/latest/?badge=gd3)

This repository contains the source files of
[Goost](https://github.com/GoostGD/goost)'s documentation.

See [Godot Engine Documentation](https://github.com/godotengine/godot-docs)
for existing documentation writing workflow and other instructions.

## Goost-specific instructions

### Generating class reference

If the Goost module resides inside Godot source tree:

```
cd godot
python doc/tools/makerst.py "doc/classes" "modules" --output "/path/to/goost-docs/classes/"
```

If using `custom_modules` build option:

```
python doc/tools/makerst.py "doc/classes" "modules" "/path/to/goost/doc" --output "/path/to/goost-docs/classes/"
```

Specifying `doc/classes` path is needed so that the `makerst` script can properly
check and generate the classes as Goost uses built-in types provided by Godot.
Make sure that only Goost related classes are added or updated.
