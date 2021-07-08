def get_quality_updater(item):
    if item.name == 'Aged Brie':
        return AgedBrieUpdater()
    elif item.name == 'Sulfuras, Hand of Ragnaros':
        return SulfurasUpdater()
    elif item.name.startswith('Backstage passes'):
        return BackstagePassUpdater()
    elif item.name.startswith('Conjured'):
        return ConjuredUpdater()
    else:
        return QualityUpdater()


class QualityUpdater:
    def __init__(self):
        self.sell_in_delta = -1
        self.quality_upper_bound = 50
        self.quality_lower_bound = 0

    def calculate_update(self, item):
        return {
            "quality": self.calculate_quality(item),
            "sell_in": self.calculate_sell_in(item)
        }

    def calculate_quality(self, item):
        delta = self.calculate_quality_delta(item)
        potential_quality = item.quality + delta
        return self.enforce_boundaries(potential_quality)

    def calculate_quality_delta(self, item, base_rate=1):
        if item.sell_in > 0:
            return -base_rate
        else:
            return -base_rate * 2

    # made this method into a one-liner at Aryeh Leib's sugestion,
    # but this might not be what was intended...
    def enforce_boundaries(self, quality):
        return quality if self.quality_lower_bound <= quality <= self.quality_upper_bound else min([0, 50], key=lambda x: abs(x - quality))

    def calculate_sell_in(self, item):
        return item.sell_in + self.sell_in_delta


class ConjuredUpdater(QualityUpdater):
    def calculate_quality_delta(self, item):
        return super().calculate_quality_delta(item, 2)


class AgedBrieUpdater(QualityUpdater):
    def calculate_quality_delta(self, item):
        if item.sell_in > 0:
            return 1
        else:
            return 2


class BackstagePassUpdater(QualityUpdater):
    def calculate_quality_delta(self, item):
        if item.sell_in > 10:
            return 1
        elif 5 < item.sell_in <= 10:
            return 2
        elif 0 < item.sell_in <= 5:
            return 3
        elif item.sell_in <= 0:
            return item.quality * -1


class SulfurasUpdater(QualityUpdater):
    def __init__(self):
        self.sell_in_delta = 0
        self.quality_upper_bound = self.quality_lower_bound = 80

    def enforce_boundaries(self, quality):
        return self.quality_upper_bound