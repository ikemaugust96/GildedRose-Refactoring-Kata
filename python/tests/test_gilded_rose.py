# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_conjured_item_decreases_quality_by_two_before_sell_date(self):
        items = [Item("Conjured Mana Cake", 10, 20)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(18, items[0].quality)

    def test_conjured_item_decreases_quality_by_four_after_sell_date(self):
        items = [Item("Conjured Mana Cake", 0, 20)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(16, items[0].quality)

    def test_conjured_item_quality_never_goes_below_zero_before_sell_date(self):
        items = [Item("Conjured Mana Cake", 5, 1)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(0, items[0].quality)

    def test_conjured_item_quality_never_goes_below_zero_after_sell_date(self):
        items = [Item("Conjured Mana Cake", 0, 3)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(0, items[0].quality)

        
if __name__ == '__main__':
    unittest.main()
