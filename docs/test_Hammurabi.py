from unittest import TestCase

import Hammurabi
class Test(TestCase):

    def test_can_purchase(self):
        Hammurabi.can_purchase()
        self.fail()

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

        for(pop, deaths, actual) in test_cases:
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
                      (100, 35, 35)]
        for (pop, starve, actual) in test_cases:
            with self.subTest(f"{pop}, {starve}, {actual}"):
                expected = Hammurabi.uprising(pop, starve)
                self.assertAlmostEqual(actual, expected)

    def test_immigrants(self):
        self.fail()

    def test_harvest(self):
        self.fail()

    def test_grain_eaten_by_rats(self):
        test_cases = [
            (100, 19, 5),
            (1000, 20, 0),
            (32, 5, 24)
        ]
        for (bushels, eaten, actual) in test_cases:
            with self.subTest(f"{bushels}, {eaten},{actual}"):
                self.assertEqual(actual, Hammurabi.grainEatenByRats(bushels))

        self.fail()

    def test_new_cost_of_land(self):
        self.fail()

    def test_print_summary(self):
        self.fail()

    def test_final_summary(self):
        self.fail()

    def test_stats(self):
        self.fail()
