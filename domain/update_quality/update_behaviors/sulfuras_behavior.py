from domain.dtos.item import Item
from domain.update_quality.update_behaviors.item_behavior import ItemBehavior


class SulfurasBehavior(ItemBehavior):
    def update(self, item: Item) -> None:
        """Sulfuras does not change."""
