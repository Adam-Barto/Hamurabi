from math import ceil
import random
from enum import Enum

line_break = '-' * 10


# starter variables
class Stats(Enum):
    SELL = 0
    YEAR = 1
    PEOPLE = 2
    BUSHELS = 3
    ACRES = 4
    LAND_VAL = 5
    END = 6
    LABOUR = 7
    FEED = 8
    PLANTED = 9


game_dict = {
    Stats.YEAR: 1,  # Current Round
    Stats.END: 10,
    Stats.PEOPLE: 100,
    Stats.BUSHELS: 2800,  # grain in storage
    Stats.ACRES: 1000,
    Stats.LAND_VAL: 19,  # bushels/acre
    Stats.LABOUR: 1  # How Many People are needed to Plant An Acre
}

last_round_dict = {
    Stats.PEOPLE: 0,
    Stats.BUSHELS: 0,  # grain in storage
    Stats.ACRES: 0,
    Stats.LAND_VAL: 0  # bushels/acre
}

curr_round_action_dict = {
    Stats.FEED: 0,
    Stats.SELL: 0,
    Stats.PLANTED: 0
}


class Hamurabi(object):
    def play_game(self):
        print
        "Let's play!"
        print(line_break * 2)
        print('OH GREAT HAMMURABI, YOU HAVE ASCENDED TO THE THRONE!')
        last_round_update()

        while game_dict.get(Stats.YEAR) <= game_dict.get(Stats.END):
            print(f'OH GREAT HAMMURABI, IT IS YEAR {game_dict.get(Stats.YEAR)} OF YOUR GLORIOUS RULE!\n'
                  f'WHAT IS IT THAT YOU WISH TO DO?')
            status_print('CURRENTLY:')
            # This should be moved to a Method Later
            amount = askHowMuchGrainToFeedThePeople(int(player_input('HOW MUCH WOULD YOU LIKE TO FEED YOUR PEOPLE?')))
            if can_purchase(game_dict, *amount):
                transaction = curr_round_action_dict.get(Stats.FEED)
                print(f'YOU HAVE FED YOUR PEOPLE {transaction} BUSHEL(S) EACH')
                purchase(game_dict, Stats.BUSHELS, transaction)
            # lineBreak
            # status_print('CURRENTLY:')
            # lineBreak
            print(f'ACRES SELL FOR {game_dict[Stats.LAND_VAL]} BUSHELS EACH,')
            amount = askHowManyAcresToBuyAndSell(int(player_input('HOW MANY ACRES WOULD YOU LIKE TO SELL?')))
            if can_purchase(game_dict, *amount):
                sold = curr_round_action_dict.get(Stats.SELL)
                print(f'YOU HAVE SOLD {sold} ACRES EACH FOR A TOTAL OF {sold * game_dict[Stats.LAND_VAL]} BUSHELS')
                purchase(game_dict, Stats.ACRES, sold)
                purchase(game_dict, Stats.BUSHELS, -sold * game_dict[Stats.LAND_VAL])
            # lineBreak
            # status_print('CURRENTLY:')
            # lineBreak
            print(f'ACRES COST {game_dict[Stats.LAND_VAL]} BUSHELS EACH,')
            amount = askHowManyAcresToBuyAndSell(int(player_input('HOW MANY ACRES WOULD YOU LIKE TO BUY?')))
            if can_purchase(game_dict, *amount):
                sold = curr_round_action_dict.get(Stats.SELL)
                print(f'YOU HAVE PURCHASED {sold} ACRES EACH FOR A TOTAL OF {sold * game_dict[Stats.LAND_VAL]} BUSHELS')
                purchase(game_dict, Stats.ACRES, -sold)
                purchase(game_dict, Stats.BUSHELS, sold * game_dict[Stats.LAND_VAL])
            # lineBreak
            # status_print('CURRENTLY:')
            # lineBreak --START HERE ADAM
            # amount = askHowManyAcresToPlant(int(player_input('HOW MANY ACRES WOULD YOU LIKE TO PLANT?')))
            # if can_purchase(game_dict, *amount):
            #     sold = curr_round_action_dict.get(Stats.SELL)
            #     print(f'YOU HAVE PLANTED {sold} ACRES EACH FOR A TOTAL OF {sold * game_dict[Stats.LAND_VAL]} BUSHELS')
            #     purchase(game_dict, Stats.ACRES, -sold)
            #     purchase(game_dict, Stats.BUSHELS, sold * game_dict[Stats.LAND_VAL])
            # The above should be moved to a Method Later
            print_summary()

  #  Cool Cheese

            last_round_update()

            game_dict[Stats.YEAR] = game_dict[Stats.YEAR] + 1
            player_input('Press any Key to continue')
            print(line_break * 2)

        finalSummary()

    ## lots more functions here...


def purchase(dict: dict, stat: Stats, value: int):  # Issue Here, Need amounts
    """
    :param dict: The Dictionary
    :param stat: The Key
    :param value: The Reduction
    :return:
    """
    dict[stat] = dict[stat] - value


# Updates Last Round Dictionary
def last_round_update():
    for i in last_round_dict:
        last_round_dict[i] = game_dict.get(i)


def can_purchase(has_amount: dict, amount_buying: int, stats: Stats) -> bool:
    """
    :param has_amount: The Dictionary to focus on.
    :param amount_buying:  The Amount purchasing as an Int
    :param stats: The Enum Value
    :return: bool value
    """
    if has_amount[stats] == 0:  # This should hopefully never trigger in later versions.
        print(f'YOU DO NOT HAVE ANY {stats.name}')
        return False
    elif amount_buying <= has_amount[stats]:
        return True
    else:
        print(f'YOU DO NOT HAVE ENOUGH {stats.name}')
        return can_purchase(has_amount, int(player_input('MY LORD PLEASE GIVE ME A PROPER AMOUNT')), stats)


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
    show_value(game_dict.get(Stats.BUSHELS), Stats.BUSHELS.name)
    show_value(game_dict.get(Stats.ACRES), 'ACRES')


def player_input(text='text_not_submitted_for_input') -> str:
    """
    Takes a string from the code to decide what to display, then returns input.
    :param text: The string in question.
    :return: returns a string, so be sure to convert it for the variables
    """
    return input(text + ' ')


def askHowManyAcresToBuyAndSell(user_input):
    """
    Ask player how many acres to sell and return the cost
    :param user_input:
    :return:
    """
    curr_round_action_dict[Stats.SELL] = user_input  # * game_dict.get(Stats.LAND_VAL)
    return user_input, Stats.ACRES


def askHowMuchGrainToFeedThePeople(user_input: int):
    """
    Takes User input and Applies it to Current Round Action Dictionary for Feed
    :param user_input:
    :return:
    """
    curr_round_action_dict[Stats.FEED] = user_input
    return user_input*game_dict[Stats.PEOPLE], Stats.BUSHELS


def askHowManyAcresToPlant(user_input):
    """Ask player how many acres to plant with grain and returns that number
    Must have enough grain and people to do the planting. Left over grain goes to storage"""
    print('HOW MANY ACRES WOULD YOU LIKE TO PLANT')
    print(f'EACH ACRE NEEDS {0} BUSHELS TO PLANT AND {game_dict.get(Stats.LABOUR)} PEOPLE TO PLANT')
    # An issue here, The math is off, Reformat to Math change value
    return user_input * game_dict.get(Stats.BUSHELS), Stats.BUSHELS

def plagueDeaths(population):
    """15% chance of plague each year, killing 50% of population. Return that number, possibly 0"""
    if random.random() < 0.15:
        plague_pop = ceil(population * 0.5)
        return population - plague_pop
    else:
        return 0

def starvationDeaths(population, bushelsFedToPeople):
    """Each subject needs 20 bushels to survive, more makes them happy but not necessary
    No benefit to happy subjects. Return number of starvation deaths, possibly 0 """
    value = ceil((population * bushelsFedToPeople) / 20)
    return population - value


def uprising(population, howManyPeopleStarved):
    """return True if 45% of people starve, auto-end game"""
    rebels = ceil(howManyPeopleStarved / population) * 100 >= 45
    if rebels:
        return True
        print("DEATH TO HAMMURABI")
        print("GAME OVER")
    else :
        return False


def immigrants(population, acresOwned, grainInStorage):
    """Nobody comes to city if subjects starving, don't call method. If subjects happy calculate immigrants as
    (20 * _number of acres you have_ + _amount of grain you have in storage_) / (100 * _population_) + 1"""
    moshulu = ((20 * acresOwned) + grainInStorage) / ((100 * population) + 1)
    return moshulu


def harvest(acres, bushelsUsedAsSeed):
    """choose randNum 1-6 inclusive, bushelsUsedAsSeed = acres * randNum"""
    pass


def grainEatenByRats(bushels):
    """40% of rat infestation, rats eat 10%-30% of grain. Return number of bushel eaten, possibly 0"""
    if random.random() < 0.4:
        grain_eaten = ceil((random.randint(10, 30) * bushels) / 100)
        return bushels - grain_eaten
    else:
        return 0
def newCostOfLand():
    """Price of land is random from 17 to 23 bushels per acre. Return new price for next
    set of player decision to buy or sell land"""
    pass


def print_summary():
    hungry_deaths = starvationDeaths(game_dict[Stats.PEOPLE], curr_round_action_dict[Stats.FEED])
    game_dict[Stats.PEOPLE] = game_dict[Stats.PEOPLE] - hungry_deaths
    print(f'{hungry_deaths} People Died Due to Starvation')


def finalSummary():
    """Print final summary of game the usual evaluation is based on how many people starved,
    and how many acres per person you end up with for example"""
    pass


if __name__ == '__main__':
    Hamurabi().play_game()
