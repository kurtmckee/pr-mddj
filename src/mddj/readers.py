import pathlib

import build.util


def get_wheel_metadata(
    source_dir: pathlib.Path, isolated: bool = True, quiet: bool = True
) -> dict[str, str]:
    """
    'quiet' is currently a no-op.

    After the next release of build, change usage to this:

        import pyproject_hooks

        ...

        runner = pyproject_hooks.quiet_subprocess_runner
        if not quiet:
            runner = pyproject_hooks.default_subprocess_runner
        return build.util.project_wheel_metadata(
            source_dir, isolated=isolated, runner=runner
        ).json
    """
    return build.util.project_wheel_metadata(source_dir, isolated=isolated).json
