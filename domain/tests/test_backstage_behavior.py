from unittest import TestCase

from domain.dtos.item import Item
from domain.item_updates.update_behaviors.backstage_behavior import BackstageBehavior


class TestGenericBehavior(TestCase):
    def setUp(self):
        self.behavior = BackstageBehavior()

    def test_sell_in_decrease_in_each_update(self):
        expected = 9
        item = Item(name="foo", sell_in=10, quality=10)
        self.behavior.update(item)
        self.assertEqual(expected, item.sell_in)

    def test_quality_is_zero_if_sell_in_is_equal_than_zero(self):
        expected = 0
        item = Item(name="foo", sell_in=0, quality=15)
        self.behavior.update(item)
        self.assertEqual(expected, item.quality)

    def test_quality_is_zero_if_sell_in_is_lower_than_zero(self):
        expected = 0
        item = Item(name="foo", sell_in=-1, quality=15)
        self.behavior.update(item)
        self.assertEqual(expected, item.quality)

    def test_quality_increase_in_each_update(self):
        expected = 16
        item = Item(name="foo", sell_in=11, quality=15)
        self.behavior.update(item)
        self.assertEqual(expected, item.quality)

    def test_quality_increase_double_each_update_if_sell_in_is_equal_than_10(self):
        expected = 17
        item = Item(name="foo", sell_in=10, quality=15)
        self.behavior.update(item)
        self.assertEqual(expected, item.quality)

    def test_quality_increase_double_each_update_if_sell_in_is_less_than_10(self):
        expected = 17
        item = Item(name="foo", sell_in=6, quality=15)
        self.behavior.update(item)
        self.assertEqual(expected, item.quality)

    def test_quality_increase_triple_each_update_if_sell_in_is_equal_than_5(self):
        expected = 18
        item = Item(name="foo", sell_in=5, quality=15)
        self.behavior.update(item)
        self.assertEqual(expected, item.quality)

    def test_quality_increase_double_each_update_if_sell_in_is_less_than_5(self):
        expected = 18
        item = Item(name="foo", sell_in=4, quality=15)
        self.behavior.update(item)
        self.assertEqual(expected, item.quality)

    def test_quality_cant_be_great_than_50(self):
        expected = 50
        item = Item(name="foo", sell_in=12, quality=50)
        self.behavior.update(item)
        self.assertEqual(expected, item.quality)
