# -*- coding: utf-8 -*-
import unittest

from quality_updater import get_quality_updater
from gilded_rose import Item

# items = [
#              Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
#              Item(name="Aged Brie", sell_in=2, quality=0),
#              Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
#              Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
#              Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
#              Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
#              Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
#              Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
#              Item(name="Conjured Mana Cake", sell_in=3, quality=6),  
#             ]

class UpdaterTest(unittest.TestCase):
    def test_updates_standard_item_before_sell_date(self):
        item = Item(name="+5 Dexterity Vest", sell_in=10, quality=20)
        quality_updater = get_quality_updater(item)

        for i in range(10):
            quality_updater.update()

        self.assertEqual(10, item.quality)

    def test_updates_standard_item_after_sell_date(self):
        item = Item(name="+5 Dexterity Vest", sell_in=10, quality=20)
        quality_updater = get_quality_updater(item)

        for i in range(11):
            quality_updater.update()

        self.assertEqual(8, item.quality)

    def test_standard_item_never_less_than_zero(self):
        item = Item(name="+5 Dexterity Vest", sell_in=10, quality=20)
        quality_updater = get_quality_updater(item)

        for i in range(1000):
            quality_updater.update()

        self.assertEqual(0, item.quality)
        
    def test_aged_brie_increases_until_50(self):
        item = Item(name="Aged Brie", sell_in=2, quality=0)
        quality_updater = get_quality_updater(item)
    
        for i in range(1000):
            quality_updater.update()

        self.assertEqual(50, item.quality)

    def test_sulfuras_always_80_and_sell_in_stays_same(self):
        item = Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80)
        quality_updater = get_quality_updater(item)

        for i in range(1000):
            quality_updater.update()

        self.assertEqual(80, item.quality)
        self.assertEqual(0, item.sell_in)

    def test_backstage_pass_increases_correctly_before_10(self):
        item = Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=11, quality=49)
        quality_updater = get_quality_updater(item)

        quality_updater.update()

        self.assertEqual(50, item.quality)

    def test_backstage_pass_increases_correctly_at_10(self):
        item = Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49)
        quality_updater = get_quality_updater(item)

        quality_updater.update()

        self.assertEqual(51, item.quality)

    def test_backstage_pass_increases_correctly_at_5(self):
        item = Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49)
        quality_updater = get_quality_updater(item)

        quality_updater.update()

        self.assertEqual(52, item.quality)

    def test_backstage_pass_worthless_after_concert(self):
        item = Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=0, quality=49)
        quality_updater = get_quality_updater(item)

        quality_updater.update()

        self.assertEqual(0, item.quality)

    def test_conjured_decreases_correctly_before_sale_by(self):
        item = Item(name="Conjured Mana Cake", sell_in=3, quality=6)
        quality_updater = get_quality_updater(item)

        quality_updater.update()

        self.assertEqual(4, item.quality)

    def test_conjured_decreases_correctly_after_sale_by(self):
        item = Item(name="Conjured Mana Cake", sell_in=3, quality=10)
        quality_updater = get_quality_updater(item)

        for i in range(4):
            quality_updater.update()

        self.assertEqual(0, item.quality)

if __name__ == '__main__':
    unittest.main()