import random
from enum import Enum

line_break = '-' * 10


# starter variables
class Stats(Enum):
    YEAR = 0
    PEOPLE = 1
    BUSHELS = 2
    ACRES = 3
    LAND_VAL = 4
    END = 5


game_dict = {
    Stats.YEAR: 1,  # Current Round
    Stats.END: 10,
    Stats.PEOPLE: 100,
    Stats.BUSHELS: 2800,  # grain in storage
    Stats.ACRES: 1000,
    Stats.LAND_VAL: 19  # bushels/acre
}

last_round_dict = {
    Stats.PEOPLE: 0,
    Stats.BUSHELS: 0,  # grain in storage
    Stats.ACRES: 0,
    Stats.LAND_VAL: 0  # bushels/acre
}


# people = 100
# bushels = 2800  # grain in storage
# acres = 1000
# land_val = 19  # bushels/acre
# year = 10  # rounds


class Hamurabi(object):
    def play_game(self):
        print
        "Let's play!"
        print(line_break * 2)
        print('OH GREAT HAMMURABI, YOU HAVE ASCENDED TO THE THRONE!')
        last_round_update()

        while (game_dict.get(Stats.YEAR) <= game_dict.get(Stats.END)):
            print(f'OH GREAT HAMMURABI, IT IS YEAR {game_dict.get(Stats.YEAR)} OF YOUR GLORIOUS RULE!\n'
                  f'WHAT IS IT THAT YOU WISH TO DO?')
            status_print('CURRENTLY:')

            if can_purchase(*askHowMuchGrainToFeedThePeople()):

                print('you can do it')

            last_round_update()
            game_dict[Stats.YEAR] = game_dict[Stats.YEAR] + 1

    ## lots more functions here...


def purchase(stat: Stats, value: int):
    game_dict[stat] = game_dict[stat] - value


# Updates Last Round Dictionary
def last_round_update():
    for i in last_round_dict:
        last_round_dict[i] = game_dict.get(i)


def can_purchase(amount_buying, stats: Stats):
    has_amount = game_dict[stats]
    if amount_buying <= has_amount:
        purchase(stats, amount_buying)
        return True
    else:
        return False


# Have you done a good job between rounds?
def is_good_diff_between_rounds(value):
    if last_round_dict.get(value) is None:
        print(f'{value} is Not a Valid Key of last_round_dict!')
        return 'Break My Code so I can Fix it'
    if game_dict.get(value) < last_round_dict.get(value):
        return False
    elif game_dict.get(value) > last_round_dict.get(value):
        return True
    else:
        return None


def show_value(value: int, value_name: str) -> None:
    """
    Given a value, displays the amount of that value
    :param value:
    :param value_name: The NAME of the value in a string
    :return: None
    """
    print(f'YOU HAVE {value} {value_name}')


def status_print(text: str) -> None:
    """
    Prints out the Status
    :param: text This will be printed out.
    :return:
    """
    print(text)
    print(line_break)
    show_value(game_dict.get(Stats.PEOPLE), 'PEOPLE')
    show_value(game_dict.get(Stats.BUSHELS), 'BUSHELS')
    show_value(game_dict.get(Stats.ACRES), 'ACRES')


def menu_display():
    player_input('HOW MUCH WOULD YOU LIKE TO FEED YOUR PEOPLE?')


def player_input(text='Placeholder') -> str:
    """
    Takes a string from the code to decide what to display, then returns input.
    :param text: The string in question.
    :return: returns a string, so be sure to convert it for the variables
    """
    return input(text + ' ')


def askHowManyAcresToBuy():
    """Ask player how many acres to buy and return that number"""
    print('HOW MANY ACRES WOULD YOU LIKE TO BUY?')
    print(f'EACH ACRE COSTS {game_dict.get(Stats.LAND_VAL)} BUSHELS')
    return player_input('HOW MANY ACRES WOULD YOU LIKE TO BUY?')


def askHowManyAcresToSell(acres_owned):
    """Ask player how many acres to sell and return that number"""
    pass


def askHowMuchGrainToFeedThePeople():
    """Ask player how much grain to feed people and return that number, and what Value to Modify"""
    return int(player_input('HOW MUCH WOULD YOU LIKE TO FEED YOUR PEOPLE?')), Stats.BUSHELS


def askHowManyAcresToPlant(acresOwned, population, bushels):
    """Ask player how many acres to plant with grain and returns that number
    Must have enough grain and people to do the planting. Left over grain goes to storage"""
    pass


def plagueDeaths(population):
    """15% chance of plague each year, return that number, possibly 0"""
    pass


def starvationDeaths(population, bushelsFedToPeople):
    """Each subject needs 20 bushels to survive, more makes them happy but not necessary
    No benefit to happy subjects. Return number of starvation deaths, possibly 0 """
    pass


def uprising(population, howManyPeopleStarved):
    """return True if 45% of people starve, auto-end game"""
    pass


def immigrants(population, acresOwned, grainInStorage):
    """Nobody comes to city if subjects starving, don't call method. If subjects happy calculate immigrants as
    (20 * _number of acres you have_ + _amount of grain you have in storage_) / (100 * _population_) + 1"""
    pass


def harvest(acres, bushelsUsedAsSeed):
    """choose randNum 1-6 inclusive, bushelsUsedAsSeed = acres * randNum"""
    pass


def grainEatenByRats(bushels):
    """40% of rat infestation, rats eat 10%-30% of of grain. Return number of bushel eaten, possibly 0"""
    pass


def newCostOfLand():
    """Price of land is random from 17 to 23 bushels per acre. Return new price for next
    set of player decision to buy or sell land"""
    pass


def print_summary():
    """
    This will be used to display the difference between values
    :return:
    """
    pass


def finalSummary():
    """Print final summary of game he usual evaluation is based on how many people starved,
    and how many acres per person you end up with for example"""
    pass


if __name__ == '__main__':
    Hamurabi().play_game()
