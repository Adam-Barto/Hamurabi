from math import ceil
import random
from enum import Enum

line_break = '-' * 10
save_number = 0


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
    SAVED_NUMBER = 10


game_dict = {
    Stats.YEAR: 1,  # Current Round
    Stats.END: 5,
    Stats.PEOPLE: 100,
    Stats.BUSHELS: 2800,  # grain in storage
    Stats.ACRES: 1000,
    Stats.LAND_VAL: 19,  # bushels/acre
    Stats.LABOUR: 2  # How Many People are needed to Plant An Acre
}

win_dict = {
    'Did Win?': True,
    'How Much Did We Win?': 0,
    Stats.PEOPLE: 100,
    Stats.BUSHELS: 2800,  # grain in storage
    Stats.ACRES: 1000
}

last_round_dict = {
    Stats.PEOPLE: 0,
    Stats.BUSHELS: 0,  # grain in storage
    Stats.ACRES: 0
    #Stats.LAND_VAL: 0  # bushels/acre
}

curr_round_action_dict = {
    Stats.FEED: 0,
    Stats.SELL: 0,
    Stats.PLANTED: 0,
    Stats.SAVED_NUMBER: 0
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
            askHowMuchGrainToFeedThePeople()

            # lineBreak
            # status_print('CURRENTLY:')
            # lineBreak
            curr_round_action_dict[Stats.SELL] = 0
            askHowManyAcresToSell()
            if curr_round_action_dict.get(Stats.SELL) == 0:
                askHowManyAcresToBuy()

            # lineBreak
            # status_print('CURRENTLY:')
            # lineBreak

            # askHowManyAcresToBuy()

            # lineBreak
            # status_print('CURRENTLY:')
            # lineBreak

            askHowManyAcresToPlant()

            # The above should be moved to a Method Later
            print(line_break)
            # status_print('CURRENTLY MY LORD YOU HAVE:')
            if print_summary():
                break
            game_dict[Stats.YEAR] = game_dict[Stats.YEAR] + 1
            player_input('Press any Key to continue')
            print(line_break * 2)
            last_round_update()
        if win_dict.get('Did Win?'):
            for i in last_round_dict:
                if did_we_do_better_then_the_start(i):
                    print(f'GREAT HAMMURABI WE HAVE DONE WELL WITH {i.name}')
                    win_dict['How Much Did We Win?'] = win_dict.get('How Much Did We Win?') + 1
                else:
                    print(f'GREAT HAMMURABI WE HAVE LOST {i.name}')
            if win_dict.get('How Much Did We Win?') == 0:
                print(line_break * 2)
                print('HAMMURABI YOU FOOL, YOU ARE NOT READY FOR THE CROWN')
                print('I WILL BE A BETTER RULER THEN YOU EVER HAVE BEEN!')
            elif win_dict.get('How Much Did We Win?') == 1:
                print(line_break * 2)
                print('HAMMURABI YOU HAVE SURVIVED THE RATS')
                print('HONESTLY I AM IMPRESSED')
            elif win_dict.get('How Much Did We Win?') == 2:
                print(line_break * 2)
                print('GREAT HAMMURABI YOU HAVE DONE WELL')
                print('I AM PLEASED TO BE YOUR SERVANT')
            elif win_dict.get('How Much Did We Win?') == 3:
                print(line_break * 2)
                print('OH GREAT HAMMURABI YOU ARE THE LIGHT TO YOUR PEOPLE')
                print('YOUR FATHER COULD NOT BE MORE PROUD')
        else:
            print('HAMMURABI YOU FOOL, YOU ARE NOT READY FOR THE CROWN')
            print('I WILL BE A BETTER RULER THEN YOU EVER HAVE BEEN!')


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


def can_purchase(has_amount, amount_buying: int, stat: Stats):
    """
    :param has_amount: The Dictionary to focus on.
    :param amount_buying:  The Amount purchasing as an Int
    :param stats: The Enum Value
    :return: a good value.
    """
    value = amount_buying
    # print(value)
    if value > int(has_amount.get(stat)):
        print(f'YOU DO NOT HAVE {value} OF {stat.name}')
        print(f'YOU HAVE {has_amount.get(stat)} OF {stat.name}')
        return False
    else:
        return value


# Have you done a good job between rounds?
def did_we_do_better_then_the_start(value):
    if win_dict.get(value) is None:
        print(f'{value} is Not a Valid Key of last_round_dict!')
        return 'Break My Code so I can Fix it'
    if game_dict.get(value) < win_dict.get(value):
        return False
    elif game_dict.get(value) > win_dict.get(value):
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


def askHowManyAcresToBuy():
    """
    Ask player how many acres to sell and return the cost
    :param user_input:
    :return:
    """
    print(f'ACRES COST {game_dict[Stats.LAND_VAL]} BUSHELS EACH,')
    text = 'HOW MANY ACRES WOULD YOU LIKE TO BUY?'
    value = int(player_input(text))
    while type(can_purchase(game_dict, value, Stats.BUSHELS)) == bool:  # Shortening this breaks the code
        value = int(player_input(text))

    curr_round_action_dict[Stats.SELL] = can_purchase(game_dict, value, Stats.BUSHELS)

    purchased = curr_round_action_dict.get(Stats.SELL)
    print(
        f'YOU HAVE PURCHASED {purchased} ACRES EACH FOR A TOTAL OF '
        f'{purchased * game_dict[Stats.LAND_VAL]} BUSHELS')
    purchase(game_dict, Stats.ACRES, -purchased)
    purchase(game_dict, Stats.BUSHELS, purchased * game_dict[Stats.LAND_VAL])


def askHowManyAcresToSell():
    """
    Ask player how many acres to sell apply the cost into a saved value
    """
    print(f'ACRES SELL FOR {game_dict[Stats.LAND_VAL]} BUSHELS EACH,')
    text = 'HOW MANY ACRES WOULD YOU LIKE TO SELL?'
    value = int(player_input(text))
    while type(can_purchase(game_dict, value, Stats.ACRES)) == bool:  # Shortening this breaks the code
        value = int(player_input(text))

    curr_round_action_dict[Stats.SELL] = can_purchase(game_dict, value, Stats.ACRES)

    sold = curr_round_action_dict.get(Stats.SELL)
    print(f'YOU HAVE SOLD {sold} ACRES EACH FOR A TOTAL OF {sold * game_dict[Stats.LAND_VAL]} BUSHELS')
    purchase(game_dict, Stats.ACRES, sold)
    purchase(game_dict, Stats.BUSHELS, -sold * game_dict[Stats.LAND_VAL])


def askHowMuchGrainToFeedThePeople():
    """
    Takes User input and Applies it to Current Round Action Dictionary for Feed
    :param user_input:
    :return:
    """
    text = 'HOW MUCH WOULD YOU LIKE TO FEED YOUR PEOPLE?'
    value = int(player_input(text))
    while type(can_purchase(game_dict, value * game_dict[Stats.PEOPLE],
                            Stats.BUSHELS)) == bool:  # Shortening this breaks the code
        value = int(player_input(text))

    curr_round_action_dict[Stats.FEED] = can_purchase(game_dict, value, Stats.BUSHELS)

    transaction = curr_round_action_dict.get(Stats.FEED)
    print(f'YOU HAVE FED YOUR PEOPLE {transaction} BUSHEL(S) EACH')
    purchase(game_dict, Stats.BUSHELS, transaction)


def askHowManyAcresToPlant():
    """Ask player how many acres to plant with grain and returns that number
    Must have enough grain and people to do the planting. Left over grain goes to storage"""
    print(f'EACH ACRE NEEDS {game_dict.get(Stats.LABOUR)} PEOPLE TO PLANT')
    text = 'HOW MANY ACRES WOULD YOU LIKE TO PLANT?'
    value = int(player_input(text))
    while type(can_purchase(game_dict, value * game_dict[Stats.LABOUR], Stats.PEOPLE)) == bool:
        value = int(player_input(text))

    curr_round_action_dict[Stats.PLANTED] = can_purchase(game_dict, value * game_dict[Stats.LABOUR], Stats.PEOPLE)

    planted = curr_round_action_dict.get(Stats.PLANTED)
    print(f'YOU HAVE PLANTED {planted} ACRES OUT OF YOUR {game_dict[Stats.ACRES]} ACRES')
    purchase(game_dict, Stats.BUSHELS, planted)


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
    deaths = population - value
    if deaths < 0:
        return 0
    return population - value


def uprising(population, howManyPeopleStarved):
    """return True if 45% of people starve, auto-end game"""
    rebels = (howManyPeopleStarved / population) * 100 >= 45
    if rebels:
        win_dict['Did Win?'] = False
        print(line_break * 3)
        print("DEATH TO HAMMURABI")
        print(line_break * 3)
        return True
    else:
        return False


def immigrants(population, acresOwned, grainInStorage):
    """Nobody comes to city if subjects starving, don't call this method. If subjects happy calculate immigrants as
    (20 * _number of acres you have_ + _amount of grain you have in storage_) / (100 * _population_) + 1"""
    # come up with way to figure out whether or not population is happy
    value = (20 * (acresOwned + grainInStorage))
    moshulu_imms = (value // (100 * population) + 1) # (population // 10) *
    return int(moshulu_imms)


def harvest(acres):
    """choose randNum 1-6 inclusive, bushelsUsedAsSeed = acres * randNum"""
    # bushelsUsedAsSeed is redundant, removed from parameters for time being
    rand_num = random.randint(1, 6)
    bushels_harvested = acres * rand_num
    return bushels_harvested


def grainEatenByRats(bushels):
    """40% of rat infestation, rats eat 10%-30% of grain. Return number of bushel eaten, possibly 0"""
    if random.random() < 0.4:
        grain_eaten = ceil((random.randint(10, 30) * bushels) / 100)
        return grain_eaten
    else:
        return 0


def newCostOfLand():
    """Price of land is random from 17 to 23 bushels per acre. Return new price for next
    set of player decision to buy or sell land"""
    new_price = random.randint(17, 23)
    return new_price


def print_summary():
    if game_dict.get(Stats.YEAR) == game_dict.get(Stats.END):
        print('Game End')
        win_dict['Did Win?'] = False
        return True
    else:
        plague_deaths = plagueDeaths(game_dict.get(Stats.PEOPLE))
        if plague_deaths != 0:
            game_dict[Stats.PEOPLE] = game_dict.get(Stats.PEOPLE) - plague_deaths
            print(f'{plague_deaths} PEOPLE DIED FROM PLAGUE')

        bushels_harvested = harvest(curr_round_action_dict.get(Stats.PLANTED))
        if bushels_harvested != 0:
            game_dict[Stats.BUSHELS] = game_dict.get(Stats.BUSHELS) + bushels_harvested
            print(f'OH GREAT HAMMURABI WE HAVE HAD A HARVEST OF {bushels_harvested} BUSHELS')

        rat_food = grainEatenByRats(game_dict.get(Stats.BUSHELS))
        if rat_food != 0:
            game_dict[Stats.BUSHELS] = game_dict.get(Stats.BUSHELS) - rat_food
            print(f'OH GREAT HAMMURABI, {rat_food} BUSHELS HAVE BEEN EATEN BY RATS!')

        hungry_deaths = starvationDeaths(game_dict.get(Stats.PEOPLE), curr_round_action_dict.get(Stats.FEED))
        if hungry_deaths != 0:
            game_dict[Stats.PEOPLE] = game_dict.get(Stats.PEOPLE) - hungry_deaths
            print(f'{hungry_deaths} PEOPLE DIED DUE TO STARVATION!')
            if uprising(game_dict.get(Stats.PEOPLE), hungry_deaths):
                return True
        else:
            print('THE PEOPLE ARE SATISFIED WITH THEIR FOOD GREAT HAMMURABI!')
            peeps = immigrants(game_dict.get(Stats.PEOPLE), game_dict.get(Stats.ACRES), game_dict.get(Stats.BUSHELS))
            game_dict[Stats.PEOPLE] = game_dict.get(Stats.PEOPLE) + peeps
            print(f'{peeps} IMMIGRANTS HAVE COME TO OUR GREAT CITY GREAT HAMMURABI!')

        game_dict[Stats.LAND_VAL] = newCostOfLand()
        print(f'LAND NOW COSTS {game_dict[Stats.LAND_VAL]} BUSHELS')
        return False


if __name__ == '__main__':
    Hamurabi().play_game()
