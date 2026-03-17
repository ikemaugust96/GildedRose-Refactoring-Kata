class ItemUpdater:
    def update(self, item):
        raise NotImplementedError("Subclasses must implement update().")

    def increase_quality(self, item, amount=1):
        item.quality = min(50, item.quality + amount)

    def decrease_quality(self, item, amount=1):
        item.quality = max(0, item.quality - amount)

    def decrease_sell_in(self, item):
        item.sell_in -= 1


class NormalItemUpdater(ItemUpdater):
    def update(self, item):
        self.decrease_quality(item, 1)
        self.decrease_sell_in(item)

        if item.sell_in < 0:
            self.decrease_quality(item, 1)


class AgedBrieUpdater(ItemUpdater):
    def update(self, item):
        self.increase_quality(item, 1)
        self.decrease_sell_in(item)

        if item.sell_in < 0:
            self.increase_quality(item, 1)


class BackstagePassUpdater(ItemUpdater):
    def update(self, item):
        self.increase_quality(item, 1)

        if item.sell_in < 11:
            self.increase_quality(item, 1)

        if item.sell_in < 6:
            self.increase_quality(item, 1)

        self.decrease_sell_in(item)

        if item.sell_in < 0:
            item.quality = 0


class SulfurasUpdater(ItemUpdater):
    def update(self, item):
        pass


class ConjuredUpdater(ItemUpdater):
    def update(self, item):
        self.decrease_quality(item, 2)
        self.decrease_sell_in(item)

        if item.sell_in < 0:
            self.decrease_quality(item, 2)


class ItemUpdaterFactory:
    @staticmethod
    def get_updater(item):
        if item.name == "Aged Brie":
            return AgedBrieUpdater()
        if item.name == "Backstage passes to a TAFKAL80ETC concert":
            return BackstagePassUpdater()
        if item.name == "Sulfuras, Hand of Ragnaros":
            return SulfurasUpdater()
        if item.name.startswith("Conjured"):
            return ConjuredUpdater()
        return NormalItemUpdater()