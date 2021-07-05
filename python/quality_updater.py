def get_quality_updater(item):
    if item.name == 'Aged Brie':
        return AgedBrieUpdater(item)
    elif item.name == 'Sulfuras, Hand of Ragnaros':
        return SulfurasUpdater(item)
    elif item.name == 'Backstage passes to a TAFKAL80ETC concert':
        return BackstagePassUpdater(item)
    else:
        return QualityUpdater(item)


class QualityUpdater:
    def __init__(self, item):
        self.item = item

    def update_quality(self):
        self.update_quality()
        self.update_sell_in()

    def update_quality(self):
        if self.item.quality > 0:
            if self.item.sell_in > 0:
                self.item.quality -= 1
            else:
                 self.item.quality -= 2

    def update_sell_in(self):
        self.item.sell_in -= 1


class AgedBrieUpdater(QualityUpdater):
    def __init__(self, item):
        super().__init__(item)

    def update_quality(self):
        if self.item.quality < 50:
            self.item.quality += 1

    def update_sell_in(self):
        self.item.sell_in -= 1

class SulfurasUpdater(QualityUpdater):
    def update_quality(self):
        pass

    def update_sell_in(self):
        pass


class BackstagePassUpdater(QualityUpdater):
    def update_quality(self):
        if self.item.sell_in > 10:
            self.item.quality += 1
        elif 5 < self.item.sell_in <= 10:
            self.item.quality += 2
        elif 0 < self.item.sell_in <= 5:
            self.item.quality += 3
        elif self.item.sell_in <= 0:
            self.item.quality = 0


class ConjuredUpdater(QualityUpdater):
    def update_quality(self):
        return
