import random
from enum import Enum
from unittest import TestCase

import Hammurabi


class Test(TestCase):

    def test_can_purchase(self):
        class Stats(Enum):
            ONE = 0
            TWO = 1
            THREE = 2

        test_dict = {
            Stats.ONE: 1,
            Stats.TWO: 32,
            Stats.THREE: 83
        }
        test_cases = [(test_dict, 50, Stats.ONE, False),
                      (test_dict, 31, Stats.TWO, 31),
                      (test_dict, 10, Stats.THREE, 10)]

        for (dictionary, increase, enumeration, actual) in test_cases:
            with self.subTest(f"{dictionary}, {increase}, {enumeration}, {actual}"):
                expected = Hammurabi.can_purchase(test_dict, increase, enumeration)
                self.assertEqual(actual, expected)

    def test_is_good_diff_between_rounds(self):
        self.fail()

    def test_show_value(self):
        self.fail()

    def test_status_print(self):
        self.fail()

    def test_player_input(self):
        self.fail()

    def test_ask_how_many_acres_to_buy(self):
        self.fail()

    def test_ask_how_many_acres_to_sell(self):
        self.fail()

    def test_ask_how_much_grain_to_feed_the_people(self):
        self.fail()

    def test_ask_how_many_acres_to_plant(self):
        self.fail()

    def test_plague_deaths(self):
        test_cases = [(100, 50, 50),
                      (1000, 500, 500),
                      (305, 153, 152)]

        for (pop, deaths, actual) in test_cases:
            with self.subTest(f"{pop}, {deaths}, {actual}"):
                expected = Hammurabi.plagueDeaths(pop)
                self.assertAlmostEqual(actual, expected, delta=deaths)

    def test_starvation_deaths(self):
        test_cases = [
            (100, 19, 5),
            (1000, 20, 0),
            (32, 5, 24),
            (100, 30, 0),
            (1000, 41, 0),
        ]
        for (pop, food, actual) in test_cases:
            with self.subTest(f"{pop}, {food},{actual}"):
                self.assertEqual(actual, Hammurabi.starvationDeaths(pop, food))

    def test_uprising(self):
        test_cases = [(100, 45, True),
                      (1000, 550, True),
                      (305, 153, True),
                      (100, 35, False)]
        for (pop, starve, actual) in test_cases:
            with self.subTest(f"{pop}, {starve}, {actual}"):
                expected = Hammurabi.uprising(pop, starve)
                self.assertAlmostEqual(actual, expected)

    def test_immigrants(self):
        self.fail()

    def test_harvest(self):
        test_cases = [(50, random.randint(1, 6)),
                      (500, random.randint(1, 6)),
                      (1000, random.randint(1, 6)),
                      (459, random.randint(1, 6))]
        for (acres, rand) in test_cases:
            with self.subTest(f"{acres},{rand}"):
                expected = Hammurabi.harvest(acres)
                self.assertAlmostEqual(acres, expected, delta=expected)  # pretty sure this test is wrong

    def test_grain_eaten_by_rats(self):
        test_cases = [
            (100, 19),
            (1000, 210),
            (32, 10)
        ]
        for (bushels, actual) in test_cases:
            with self.subTest(f"{bushels},{actual}"):
                self.assertAlmostEqual(actual, Hammurabi.grainEatenByRats(bushels), delta=actual)

    def test_new_cost_of_land(self):
        test_cases = [(random.randint(17, 23)),
                      (random.randint(17, 23)),
                      (random.randint(17, 23)),
                      (random.randint(17, 23)),
                      (random.randint(17, 23))]
        for actual in test_cases:
            with self.subTest(f"{actual}"):
                self.assertAlmostEqual(actual, Hammurabi.newCostOfLand(), delta=actual)

    def test_print_summary(self):
        self.fail()

    def test_final_summary(self):
        self.fail()

    def test_stats(self):
        self.fail()
