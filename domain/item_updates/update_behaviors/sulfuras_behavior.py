from domain.dtos.item import Item
from domain.item_updates.update_behaviors.item_behavior import ItemBehavior


class SulfurasBehavior(ItemBehavior):
    def update(self, item: Item) -> None:
        """Sulfuras does not change."""
