# -*- coding: utf-8 -*-

from domain.dtos.item import Item
from domain.enums.ItemName import ItemName

from domain.update_quality.generic_behavior import GenericBehavior
from domain.update_quality.item_behavior import ItemBehavior
from domain.update_quality.legacy_behavior import LegacyBehavior
from domain.update_quality.sulfuras_behavior import SulfurasBehavior


class GildedRose:
    def __init__(self, items: list[Item]):
        self.items = items

    def update_quality(self) -> None:
        items_map = self._items_map
        for item in self.items:
            items_map.get(item.name, GenericBehavior)().update(item)

    @property
    def _items_map(self) -> dict[str, type[ItemBehavior]]:
        return {
            ItemName.AGED_BRIE: LegacyBehavior,
            ItemName.BACKSTAGE: LegacyBehavior,
            ItemName.SULFURAS: SulfurasBehavior,
            ItemName.CONJURED: LegacyBehavior,
        }
