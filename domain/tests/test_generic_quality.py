from unittest import TestCase

from domain.dtos.item import Item
from domain.update_quality.generic_quality import GenericQuality


class TestGenericQuality(TestCase):
    def setUp(self):
        self.generic_quality = GenericQuality()

    def test_sell_in_decrease_in_each_update(self):
        expected = 9
        item = Item(name="foo", sell_in=10, quality=10)
        self.generic_quality.update(item)
        self.assertEqual(expected, item.sell_in)

    def test_quality_decrease_in_each_update(self):
        expected = 9
        item = Item(name="foo", sell_in=10, quality=10)
        self.generic_quality.update(item)
        self.assertEqual(expected, item.quality)

    def test_quality_cant_be_less_than_zero(self):
        expected = 0
        item = Item(name="foo", sell_in=10, quality=0)
        self.generic_quality.update(item)
        self.assertEqual(expected, item.quality)

    def test_quality_decrease_double_each_update_if_sell_in_is_zero(self):
        expected = 8
        item = Item(name="foo", sell_in=0, quality=10)
        self.generic_quality.update(item)
        self.assertEqual(expected, item.quality)
