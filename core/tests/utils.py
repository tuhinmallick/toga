import asyncio


def async_test(coroutine):
    """Run an async test to completion."""

    def _test(self):
        asyncio.run(coroutine(self))

    return _test


def order_test(*items):
    def _test(self):
        for i in range(len(items) - 1):
            for j in range(i + 1, len(items)):
                self.assertLess(items[i], items[j])
                self.assertGreater(items[j], items[i])
                self.assertFalse(items[j] < items[i])
                self.assertFalse(items[i] > items[j])

    return _test
