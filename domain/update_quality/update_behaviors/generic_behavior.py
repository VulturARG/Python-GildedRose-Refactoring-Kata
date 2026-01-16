from domain.dtos.item import Item
from domain.update_quality.update_behaviors.item_behavior import ItemBehavior


class GenericBehavior(ItemBehavior):
    def update(self, item: Item) -> None:
        self._set_sell_in(item=item)
        self._set_quality(item=item)

    def _set_sell_in(self, item: Item) -> None:
        item.sell_in -= 1

    def _set_quality(self, item: Item) -> None:
        quality_decrease = 1 if item.sell_in >= 0 else 2
        item.quality = item.quality - quality_decrease if item.quality > 0 else 0
