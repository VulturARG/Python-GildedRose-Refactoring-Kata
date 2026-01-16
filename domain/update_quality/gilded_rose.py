# -*- coding: utf-8 -*-
from domain.enums.backstage_limit import BackstageLimit
from domain.enums.quality import Quality


class GildedRose:
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if (
                item.name != "Aged Brie"
                and item.name != "Backstage passes to a TAFKAL80ETC concert"
            ):
                if item.quality > Quality.MINIMUM:
                    if item.name != "Sulfuras, Hand of Ragnaros":
                        item.quality = item.quality - 1
            else:
                if item.quality < Quality.MAXIMUM:
                    item.quality = item.quality + 1
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        if item.sell_in <= BackstageLimit.INTERMEDIUM:
                            if item.quality < Quality.MAXIMUM:
                                item.quality = item.quality + 1
                        if item.sell_in <= BackstageLimit.FINAL:
                            if item.quality < Quality.MAXIMUM:
                                item.quality = item.quality + 1

            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1

            if item.sell_in >= 0:
                continue

            if item.name != "Aged Brie":
                if item.name != "Backstage passes to a TAFKAL80ETC concert":
                    if item.quality > Quality.MINIMUM:
                        if item.name != "Sulfuras, Hand of Ragnaros":
                            item.quality = item.quality - 1
                else:
                    item.quality = item.quality - item.quality
            else:
                if item.quality < Quality.MAXIMUM:
                    item.quality = item.quality + 1
