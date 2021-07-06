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
        delta = self.calculate_delta(self.item.sell_in)
        potential_quality = self.item.quality + delta
        bounded_quality = self.enforce_boundaries(potential_quality)
        self.item.quality = bounded_quality

    def update_sell_in(self):
        self.item.sell_in -= 1

    def calculate_delta(self, sell_in):
        if sell_in > 0:
            return -1
        else:
            return -2

    def enforce_boundaries(self, quality):
        if 0 <= quality <= 50:
            return quality
        elif quality < 0:
            return 0
        else:
            return 50


class ConjuredUpdater(QualityUpdater):
    def calculate_delta(self, sell_in):
        if sell_in > 0:
            return -2
        else:
            return -4


class AgedBrieUpdater(QualityUpdater):
    def calculate_delta(self, sell_in):
        if sell_in > 0:
            return 1
        else:
            return 2


class BackstagePassUpdater(QualityUpdater):
    def calculate_delta(self, sell_in):
        if sell_in > 10:
            return 1
        elif 5 < sell_in <= 10:
            return 2
        elif 0 < sell_in <= 5:
            return 3
        elif sell_in <= 0:
            return self.item.quality * -1


class SulfurasUpdater(QualityUpdater):
    def update_quality(self):
        pass

    def update_sell_in(self):
        pass
