'''Drazdon Fenton'''
import time
import os
import random

import scoring
import constants
import scorecard
import playing


# TODO: write main AFTER you have written and tested each function
def main():
    '''Lab 1, Problem 1 Yahtzee'''
    """
    create a list of lists for the scorecard
    set userTurn to false
    call resetScorecard

    while there are still empty items in either scorecard
        swap players
        call updateScorecard
        call displayScorecard
        if it's the user's turn
            print a message and pause briefly
            call userPlay
        else
            print a message and pause breifly
            call computerPlay
        end if
     end while
     call updateScorecard
     call displayScorecard
     determine who won and display a message

    """
    print("Yahtzee!")
    print("\nTo select the dice to keep, just type the indices (0 thru 4) for the list of dice. Example: 0 2 4")
    print("\nTo designate a move, type the number from the Yahtzee game board (0 thru 12). example: 8 for a Fullhouse\n")
    scoreCard = [[], []]
    userTurn = False
    scorecard.resetScorecard(scoreCard)
    while constants.EMPTY in scoreCard[constants.USER][constants.ONES:constants.SUBTOTAL] or constants.EMPTY in scoreCard[constants.COMPUTER][constants.ONES:constants.SUBTOTAL]:
        if not userTurn:
            userTurn = True
        else:
            userTurn = False
        scorecard.updateScorecard(scoreCard)
        scorecard.displayScorecards(scoreCard)
        if userTurn:
            print("It is your turn.")
            playing.userPlay(scoreCard[0])
        else:
            print("It is the computers turn.")
            playing.computerPlay(scoreCard[1])
        #time.sleep(1)

    scoreCard.updateScorecard(scoreCard)
    scoreCard.displayScorecards(scoreCard)
    if scoreCard[constants.USER][constants.TOTAL] >= scoreCard[constants.COMPUTER][constants.TOTAL]:
        print("You Won!")
    else:
        print("Sorry, you lost.")



# this block is the same all of the time
# when the name of the file is main, call main
if __name__ == '__main__':
    main()
