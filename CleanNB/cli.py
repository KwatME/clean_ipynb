from click import Path, argument, command, option, secho

from .clean_notebook import clean_notebook


@argument("paths", nargs=-1, type=Path(exists=True))
@option("--new", is_flag=True)
def cli(paths, new):
    """
    Clean Jupyter notebook.

    https://github.com/KwatME/CleanNB.py
    """

    for path in paths:

        secho(path, fg="bright_green", bold=True)

        clean_notebook(path, new)
