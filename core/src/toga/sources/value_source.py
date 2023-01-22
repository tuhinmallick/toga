from .base import Source


class ValueSource(Source):
    def __init__(self, value=None):
        self._source = None
        self.value = value

    def __str__(self):
        return "" if self.value is None else str(self.value)

    def __setattr__(self, attr, value):
        super().__setattr__(attr, value)
        if not attr.startswith("_") and self._source is not None:
            self._source._notify("change", item=self)
