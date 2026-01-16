from domain.dtos.item import Item
from domain.enums.ItemName import ItemName
from domain.enums.backstage_limit import BackstageLimit
from domain.enums.quality_limit import QualityLimit
from domain.item_updates.update_behaviors.item_behavior import ItemBehavior


class LegacyBehavior(ItemBehavior):
    def update(self, item: Item) -> None:
        if item.name != ItemName.AGED_BRIE and item.name != ItemName.BACKSTAGE:
            if item.quality > QualityLimit.MINIMUM:
                if item.name != ItemName.SULFURAS:
                    item.quality = item.quality - 1
        else:
            if item.quality < QualityLimit.MAXIMUM:
                item.quality = item.quality + 1
                if item.name == ItemName.BACKSTAGE:
                    if item.sell_in <= BackstageLimit.INTERMEDIUM:
                        if item.quality < QualityLimit.MAXIMUM:
                            item.quality = item.quality + 1
                    if item.sell_in <= BackstageLimit.FINAL:
                        if item.quality < QualityLimit.MAXIMUM:
                            item.quality = item.quality + 1

        if item.name != ItemName.SULFURAS:
            item.sell_in = item.sell_in - 1

        if item.sell_in >= 0:
            return

        if item.name != "Aged Brie":
            if item.name != ItemName.BACKSTAGE:
                if item.quality > QualityLimit.MINIMUM:
                    if item.name != ItemName.SULFURAS:
                        item.quality = item.quality - 1
            else:
                item.quality = item.quality - item.quality
        else:
            if item.quality < QualityLimit.MAXIMUM:
                item.quality = item.quality + 1
