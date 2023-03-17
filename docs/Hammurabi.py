import random

# starter variables
people = 100
bushels = 2800  # grain in storage
acres = 1000
land_val = 19  # bushels/acre


class Hamurabi(object):
    def play_game(self):
        print
        "Let's play!"
    ## lots more functions here...

def askHowManyAcresToBuy(price, bushels) :
    """Ask player how many acres to buy and return that number"""
    pass

def askHowManyAcresToSell(acres_owned) :
    """Ask player how many acres to sell and return that number"""
    pass

def askHowMuchGrainToFeedThePeople(bushels) :
    """Ask player how much grain to feed people and return that number"""
    pass

def askHowManyAcresToPlant(acresOwned, population, bushels) :
    """Ask player how many acres to plant with grain and returns that number
    Must have enough grain and people to do the planting. Left over grain goes to storage"""
    pass

def plagueDeaths(population) :
    """15% chance of plague each year, return that number, possibly 0"""
    pass

def starvationDeaths(population, bushelsFedToPeople) :
    """Each subject needs 20 bushels to survive, more makes them happy but not necessary
    No benefit to happy subjects. Return number of starvation deaths, possibly 0 """
    pass

def uprising(population, howManyPeopleStarved) :
    """return True if 45% of people starve, auto-end game"""
    pass

def immigrants(population, acresOwned, grainInStorage) :
    """Nobody comes to city if subjects starving, don't call method. If subjects happy calculate immigrants as
    (20 * _number of acres you have_ + _amount of grain you have in storage_) / (100 * _population_) + 1"""
    pass

def harvest(acres, bushelsUsedAsSeed) :
    """choose randNum 1-6 inclusive, bushelsUsedAsSeed = acres * randNum"""
    pass

def grainEatenByRats(bushels) :
    """40% of rat infestation, rats eat 10%-30% of of grain. Return number of bushel eaten, possibly 0"""
    pass

def newCostOfLand() :
    """Price of land is random from 17 to 23 bushels per acre. Return new price for next
    set of player decision to buy or sell land"""
    pass

def printSummary() :
    """Print summary of the year"""
    pass

def finalSummary() :
    """Print final summary of game he usual evaluation is based on how many people starved,
    and how many acres per person you end up with for example"""



if __name__ == '__main__':
    Hamurabi().play_game()
