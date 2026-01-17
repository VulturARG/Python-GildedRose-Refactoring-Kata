from unittest import TestCase

from domain.dtos.item import Item
from domain.item_updates.update_behaviors.generic_behavior import GenericBehavior


class TestGenericBehavior(TestCase):
    def setUp(self):
        self.behavior = GenericBehavior()

    def test_sell_in_decrease_in_each_update(self):
        expected = 9
        item = Item(name="foo", sell_in=10, quality=10)
        self.behavior.update(item)
        self.assertEqual(expected, item.sell_in)

    def test_quality_decrease_in_each_update(self):
        expected = 9
        item = Item(name="foo", sell_in=10, quality=10)
        self.behavior.update(item)
        self.assertEqual(expected, item.quality)

    def test_quality_cant_be_less_than_zero(self):
        expected = 0
        item = Item(name="foo", sell_in=10, quality=0)
        self.behavior.update(item)
        self.assertEqual(expected, item.quality)

    def test_quality_decrease_double_each_update_if_sell_in_is_zero(self):
        expected = 8
        item = Item(name="foo", sell_in=0, quality=10)
        self.behavior.update(item)
        self.assertEqual(expected, item.quality)
