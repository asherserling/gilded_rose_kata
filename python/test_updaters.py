# -*- coding: utf-8 -*-
import unittest

from quality_updater import AgedBrieUpdater
from gilded_rose import Item

class AgedBrieUpdaterTest(unittest.TestCase):
    def test(self):
        items = [Item("foo", 10, 0)]
        updater = AgedBrieUpdater(items[0])
        updater.update_quality()
        print(items[0])

if __name__ == '__main__':
    unittest.main()