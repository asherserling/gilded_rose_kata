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
    def update_item_n_times(self, item, n):
        quality_updater = get_quality_updater(item)

        temp = item
        for i in range(n):
            updated_values = quality_updater.calculate_update(temp)
            temp = Item(
                temp.name,
                updated_values['sell_in'],
                updated_values['quality']
            )
        
        return temp

    def test_updates_standard_item_before_sell_date(self):
        item = Item(name="+5 Dexterity Vest", sell_in=10, quality=20)

        updated_item = self.update_item_n_times(item, 10)

        self.assertEqual(10, updated_item.quality)

    def test_updates_standard_item_after_sell_date(self):
        item = Item(name="+5 Dexterity Vest", sell_in=10, quality=20)
        
        updated_item = self.update_item_n_times(item, 11)

        self.assertEqual(8, updated_item.quality)

    def test_standard_item_never_less_than_zero(self):
        item = Item(name="+5 Dexterity Vest", sell_in=10, quality=20)

        updated_item = self.update_item_n_times(item, 1000)

        self.assertEqual(0, updated_item.quality)
        
    def test_aged_brie_increases_until_50(self):
        item = Item(name="Aged Brie", sell_in=2, quality=0)
        
        updated_item = self.update_item_n_times(item, 1000)

        self.assertEqual(50, updated_item.quality)

    def test_sulfuras_always_80_and_sell_in_stays_same(self):
        item = Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80)
        
        updated_item = self.update_item_n_times(item, 1000)

        self.assertEqual(80, updated_item.quality)
        self.assertEqual(0, updated_item.sell_in)

    def test_backstage_pass_increases_correctly_before_10(self):
        item = Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=11, quality=49)
        
        updated_item = self.update_item_n_times(item, 1)

        self.assertEqual(50, updated_item.quality)

    def test_backstage_pass_increases_correctly_at_10(self):
        item = Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49)
        
        updated_item = self.update_item_n_times(item, 1)

        self.assertEqual(50, updated_item.quality)

    def test_backstage_pass_increases_correctly_at_5(self):
        item = Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49)
        
        updated_item = self.update_item_n_times(item, 1)

        self.assertEqual(50, updated_item.quality)

    def test_backstage_pass_worthless_after_concert(self):
        item = Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=0, quality=49)
        
        updated_item = self.update_item_n_times(item, 1)

        self.assertEqual(0, updated_item.quality)

    def test_conjured_decreases_correctly_before_sale_by(self):
        item = Item(name="Conjured Mana Cake", sell_in=3, quality=6)
        
        updated_item = self.update_item_n_times(item, 1)

        self.assertEqual(4, updated_item.quality)

    def test_conjured_decreases_correctly_after_sale_by(self):
        item = Item(name="Conjured Mana Cake", sell_in=3, quality=10)

        updated_item = self.update_item_n_times(item, 4)

        self.assertEqual(0, updated_item.quality)

if __name__ == '__main__':
    unittest.main()