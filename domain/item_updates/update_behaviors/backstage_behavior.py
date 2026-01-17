from domain.dtos.item import Item
from domain.enums.backstage_limit import BackstageLimit
from domain.enums.quality_limit import QualityLimit
from domain.item_updates.update_behaviors.item_behavior import ItemBehavior


class BackstageBehavior(ItemBehavior):
    def update(self, item: Item) -> None:
        self._set_sell_in(item=item)
        self._set_quality(item=item)

    def _set_sell_in(self, item: Item) -> None:
        item.sell_in -= 1

    def _set_quality(self, item: Item) -> None:
        if item.sell_in < 0:
            item.quality = QualityLimit.MINIMUM.value
            return

        item.quality = item.quality + self._get_quality_increase(item=item)
        item.quality = (
            item.quality if item.quality <= QualityLimit.MAXIMUM else QualityLimit.MAXIMUM.value
        )

    def _get_quality_increase(self, item: Item) -> int:
        if item.sell_in >= BackstageLimit.INTERMEDIUM:
            return 1

        if item.sell_in >= BackstageLimit.FINAL:
            return 2

        return 3
