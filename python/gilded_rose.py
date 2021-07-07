# -*- coding: utf-8 -*-
from quality_updater import get_quality_updater

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        self.items = map(
            self.update_item,
            self.items
        )
        
    def update_item(self, item):
        quality_updater = get_quality_updater(item)
        
        updated_values = quality_updater.calculate_update(item)

        return Item(
            item.name,
            updated_values['sell_in'],
            updated_values['quality']
        )

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
