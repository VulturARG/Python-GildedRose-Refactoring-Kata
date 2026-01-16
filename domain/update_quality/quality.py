from abc import ABC, abstractmethod

from domain.dtos.item import Item


class Quality(ABC):
    @abstractmethod
    def update(self, item: Item) -> None:
        """Update the quality of Items."""
