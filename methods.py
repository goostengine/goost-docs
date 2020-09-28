import os
import subprocess


def sphinx_build(env, custom_args=None):
    build_args = ["sphinx-build"]
    if not custom_args:
        build_args.extend(["-b", env["target"], ".", env.GetTargetBuildDir()])
    else:
        build_args.extend(custom_args)
    return subprocess.call(build_args)


def validate_target(key, val, env):
    if not val in env["supported_targets"]:
        raise ValueError("Invalid documentation build target: '%s'" % val)


def get_target_build_dir(env):
    return os.path.join(env["build_dir"], env["target"])
