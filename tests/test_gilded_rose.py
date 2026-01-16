# -*- coding: utf-8 -*-
from unittest import TestCase

from domain.item_updates.gilded_rose import GildedRose
from domain.dtos.item import Item


class GildedRoseTest(TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)
