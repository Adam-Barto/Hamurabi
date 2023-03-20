import random
from enum import Enum
from io import StringIO
from unittest import TestCase
from unittest.mock import patch

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

    @patch('sys.stdout', new_callable=StringIO)
    def test_status_print(self, stdout_mock):
        class Stats(Enum):
            PEOPLE = 0
            BUSHELS = 1
            ACRES = 2

        Hammurabi.game_dict = {
            Stats.PEOPLE: 100,
            Stats.BUSHELS: 2800,
            Stats.ACRES: 1000
        }

        expected = 'THINGS\n' \
                   '----------\n' \
                   'YOU HAVE None PEOPLE\n' \
                   'YOU HAVE None BUSHELS\n' \
                   'YOU HAVE None ACRES\n'

        Hammurabi.status_print('THINGS')
        self.assertEqual(expected, stdout_mock.getvalue())

    @patch('Hammurabi.player_input', return_value='Test Time')
    def test_player_input(self, value):
        actual = 'Test Time'
        expected = Hammurabi.player_input()
        self.assertEqual(actual, expected)

    @patch('Hammurabi.player_input', return_value='10')
    def test_ask_how_many_acres_to_buy(self, value):
        actual = 10
        Hammurabi.askHowManyAcresToBuy()
        expected = Hammurabi.curr_round_action_dict.get(Hammurabi.Stats.SELL)
        self.assertEqual(actual, expected)

    @patch('Hammurabi.player_input', return_value='100')
    def test_ask_how_many_acres_to_buy2(self, value):
        actual = 100
        Hammurabi.askHowManyAcresToBuy()
        expected = Hammurabi.curr_round_action_dict.get(Hammurabi.Stats.SELL)
        self.assertEqual(actual, expected)

    @patch('Hammurabi.player_input', return_value='10')
    def test_ask_how_many_acres_to_sell(self, value):
        actual = 10
        Hammurabi.askHowManyAcresToSell()
        expected = Hammurabi.curr_round_action_dict.get(Hammurabi.Stats.SELL)
        self.assertEqual(actual, expected)

    @patch('Hammurabi.player_input', return_value='100')
    def test_ask_how_many_acres_to_sell2(self, value):
        actual = 100
        Hammurabi.askHowManyAcresToSell()
        expected = Hammurabi.curr_round_action_dict.get(Hammurabi.Stats.SELL)
        self.assertEqual(actual, expected)

    @patch('Hammurabi.player_input', return_value='10')
    def ask_how_much_grain_to_feed_the_people(self, value):
        actual = 10
        Hammurabi.askHowMuchGrainToFeedThePeople()
        expected = Hammurabi.curr_round_action_dict.get(Hammurabi.Stats.FEED)
        self.assertEqual(actual, expected)

    @patch('Hammurabi.player_input', return_value='100')
    def ask_how_much_grain_to_feed_the_people2(self, value):
        actual = 100
        Hammurabi.askHowMuchGrainToFeedThePeople()
        expected = Hammurabi.curr_round_action_dict.get(Hammurabi.Stats.FEED)
        self.assertEqual(actual, expected)

    @patch('Hammurabi.player_input', return_value='2')
    def test_askHowManyAcresToPlant1(self, value):
        actual = 2 * Hammurabi.game_dict.get(Hammurabi.Stats.LABOUR)
        Hammurabi.askHowManyAcresToPlant()
        expected = Hammurabi.curr_round_action_dict.get(Hammurabi.Stats.PLANTED)
        self.assertEqual(actual, expected)

    @patch('Hammurabi.player_input', return_value='10')
    def test_askHowManyAcresToPlant2(self, value):
        actual = 10 * Hammurabi.game_dict.get(Hammurabi.Stats.LABOUR)
        Hammurabi.askHowManyAcresToPlant()
        expected = Hammurabi.curr_round_action_dict.get(Hammurabi.Stats.PLANTED)
        self.assertEqual(actual, expected)

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
        test_cases = [(100, 1000, 100, 3),
                      (10, 10, 100, 3),
                      (100, 1000, 5000, 13),
                      (100, 1000, 2800, 8)
                      ]
        for (people, acres, food, actual) in test_cases:
            with self.subTest(f"{people}, {acres}, {food}, {actual}"):
                expected = Hammurabi.immigrants(people, acres, food)
                self.assertEqual(actual, expected)  # pretty sure this test is wrong

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

    def test_is_good_diff_between_rounds(self):
        class Stats(Enum):
            PEOPLE = 0
            BUSHELS = 1
            ACRES = 2

        Hammurabi.game_dict = {
            Stats.PEOPLE: 100,
            Stats.BUSHELS: 100,  # grain in storage
            Stats.ACRES: 100,
        }
        Hammurabi.win_dict = {
            Stats.PEOPLE: 100,
            Stats.BUSHELS: 50,  # grain in storage
            Stats.ACRES: 200,
        }
        test_cases = [(Stats.PEOPLE, None),
                      (Stats.BUSHELS, True),
                      (Stats.ACRES, False)
                      ]
        for (key, actual) in test_cases:
            with self.subTest(f"{key}, {actual}"):
                expected = Hammurabi.did_we_do_better_then_the_start(key)
                self.assertEqual(actual, expected)  # pretty sure this test is wrong

    # @patch('sys.stdout', new_callable=StringIO)
    # def test_print_summary(self):
    #     expected = 'YOU HAVE 2 THINGS\n'
    #     Hammurabi.show_value(2, 'THINGS')
    #     self.assertEqual(expected, stdout_mock.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_get_stats(self, stdout_mock):
        expected ='YOU HAVE 2 THINGS\n'
        Hammurabi.show_value(2, 'THINGS')
        self.assertEqual(expected, stdout_mock.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_get_stats2(self, stdout_mock):
        expected ='YOU HAVE 54 APPLES\n'
        Hammurabi.show_value(54, 'APPLES')
        self.assertEqual(expected, stdout_mock.getvalue())

