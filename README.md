# Goost documentation

[![Documentation Status](https://readthedocs.org/projects/goost/badge/?version=gd3)](https://goost.readthedocs.io/en/latest/?badge=gd3)

This repository contains the source files of
[Goost](https://github.com/goostengine/goost)'s documentation.

See [Godot Engine Documentation](https://github.com/godotengine/godot-docs)
for existing documentation writing workflow and other instructions.

## Goost-specific instructions

### Building documentation

Documentation can be built using the same tool which builds Godot Engine:
```
scons
```

This will build `html` pages by default as seen in the
[Goost documentation](https://goost.readthedocs.io/en/latest/).

If you'd like to build documentation in other formats supported by Sphinx, 
run `scons --help` to retrieve a list of all supported build targets.

For instance, to build a single large HTML file:

```
scons target=singlehtml
```

### Generating class reference

The following instructions assume that you compile Goost with the `scons` option,
so that Godot repository is cloned inside Goost repository (default behavior):

```
cd goost
python godot/doc/tools/makerst.py "godot/doc/classes" "godot/modules" "doc" "modules" --output "../goost-docs/classes" --filter "^(?!.*godot)"
```

The `"godot/doc/classes" "godot/modules"` specify the path to Godot XML classes,
and `"doc" "modules"` specify Goost classes relative to current directory. This 
is needed so that the `makerst` script can properly check and generate the
classes as Goost uses built-in types provided by Godot.

You can specify the output to Goost Docs `classes` directory using absolute path
as well if you have this repository cloned in a separate location.

The `--filter "^(?!.*godot)"` tells `makerst` to skip generating classes
originating from Godot itself (requires Godot 3.2.4+).
