import sys
from pathlib import Path

import toga
from toga import App


class Paths:
    # Allow instantiating Path object via the factory
    Path = Path

    @property
    def app(self):
        try:
            return Path(sys.modules["__main__"].__file__).parent
        except (KeyError, AttributeError):
            # If we're running in test conditions,
            # there is no __main__ module.
            return Path.cwd()

    @property
    def data(self):
        return Path.home() / ".local" / "share" / App.app.app_name

    @property
    def cache(self):
        return Path.home() / ".cache" / App.app.app_name

    @property
    def logs(self):
        return Path.home() / ".cache" / App.app.app_name / "log"

    @property
    def toga(self):
        """Return a path to a Toga resources."""
        return Path(toga.__file__).parent


paths = Paths()
