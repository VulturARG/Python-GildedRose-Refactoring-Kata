# -*- coding: utf-8 -*-
from typing import Callable

from domain.dtos.item import Item
from domain.enums.ItemName import ItemName

from domain.update_quality.generic_quality import GenericQuality
from domain.update_quality.temporal_quality import TemporalQuality


class GildedRose:
    def __init__(self, items: list[Item]):
        self.items = items

    def update_quality(self) -> None:
        items_map = self._items_map
        generic_quality = GenericQuality()
        for item in self.items:
            items_map.get(item.name, generic_quality.update)(item)

    @property
    def _items_map(self) -> dict[ItemName, Callable]:
        temporal_quality = TemporalQuality()
        return {
            ItemName.AGED_BRIE: temporal_quality.update,
            ItemName.BACKSTAGE: temporal_quality.update,
            ItemName.SULFURAS: temporal_quality.update,
            ItemName.CONJURED: temporal_quality.update,
        }
