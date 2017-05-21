"""Module to provide easy backwards compatibility with urllib."""


try:
    from urllib.request import urlopen  # noqa
except ImportError:
    from urllib.request import urlopen  # noqa
try:
    from urllib.request import pathname2url  # noqa
except ImportError:
    from urllib.request import pathname2url  # noqa
