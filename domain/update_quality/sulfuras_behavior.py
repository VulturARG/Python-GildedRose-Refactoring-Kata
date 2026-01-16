from domain.dtos.item import Item
from domain.update_quality.item_behavior import ItemBehavior


class SulfurasBehavior(ItemBehavior):
    def update(self, item: Item) -> None:
        """Sulfuras does not change."""
