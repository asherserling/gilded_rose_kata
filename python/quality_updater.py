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
    def update_quality(self):
        if self.item.quality < 50:
            increase = self.calculate_increase(self.item.sell_in)

            if not self.item.quality + increase > 50:
                self.item.quality += increase
            else:
                self.item.quality = increase

    def calculate_increase(self, sell_in):
        if sell_in > 0:
            return 1
        else:
            return 2


class SulfurasUpdater(QualityUpdater):
    def update_quality(self):
        pass

    def update_sell_in(self):
        pass


class BackstagePassUpdater(QualityUpdater):
    def update_quality(self):
        if self.item.sell_in > 0:
            increase = self.calculate_increase(self.item.sell_in)
            
            if not self.item.quality + increase > 50:
                self.item.quality += increase
            else:
                self.item.quality = 50

        elif self.item.sell_in <= 0:
            self.item.quality = 0

    def calculate_increase(self, sell_in):
        if sell_in > 10:
            return 1
        elif 5 < sell_in <= 10:
            return 2
        elif 0 < sell_in <= 5:
            return 3


class ConjuredUpdater(QualityUpdater):
    def update_quality(self):
        super().update_quality(base_rate=2)