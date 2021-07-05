def get_quality_updater(item):
    if item.name == 'Aged Brie':
        return AgedBrieUpdater(item)
    elif item.name == 'Sulfuras, Hand of Ragnaros':
        return SulfurasUpdater(item)
    elif item.name.startswith('Backstage passes'):
        return BackstagePassUpdater(item)
    elif item.name.startswith('Conjured'):
        return ConjuredUpdater(item)
    else:
        return QualityUpdater(item)


class QualityUpdater:
    def __init__(self, item):
        self.item = item

    def update(self):
        self.update_quality()
        self.update_sell_in()

    def update_quality(self, base_rate=1):
        if self.item.quality > 0:
            if self.item.sell_in > 0:
                self.item.quality -= base_rate
            else:
                 self.item.quality -= base_rate * 2

    def update_sell_in(self):
        self.item.sell_in -= 1


class AgedBrieUpdater(QualityUpdater):
    def __init__(self, item):
        super().__init__(item)

    def update_quality(self):
        if self.item.quality < 50:
            self.item.quality += 1


class SulfurasUpdater(QualityUpdater):
    def update_quality(self):
        pass

    def update_sell_in(self):
        pass


class BackstagePassUpdater(QualityUpdater):
    def update_quality(self):
        if self.item.sell_in > 0 and self.item.quality < 50:
            if self.item.sell_in > 10:
                self.item.quality += 1
            elif self.item.sell_in > 5:
                self.item.quality += 2
            else:
                self.item.quality += 3
        elif self.item.sell_in <= 0:
            self.item.quality = 0


class ConjuredUpdater(QualityUpdater):
    def update_quality(self):
        super().update_quality(base_rate=2)
