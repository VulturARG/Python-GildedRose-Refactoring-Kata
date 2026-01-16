from abc import ABC, abstractmethod

from domain.dtos.item import Item


class ItemBehavior(ABC):
    @abstractmethod
    def update(self, item: Item) -> None:
        """Update Items."""
