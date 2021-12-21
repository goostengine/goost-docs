# Goost documentation

[![Documentation Status](https://readthedocs.org/projects/goost/badge/?version=1.2-gd3)](https://goost.readthedocs.io/en/latest/?badge=1.2-gd3)

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

The following assumes that you compile Goost with the `scons` option, so that
Godot repository is cloned inside Goost repository (default behavior):

```
cd goost
python goost.py --generate-doc-api "/path/to/goost-docs/classes"
```

The above will generate the class reference using Godot's `makerst` tool
automatically, along with Goost components information included in
`components/`.
