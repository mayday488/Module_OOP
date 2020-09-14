"""
Constant that represens the number of player lives.
Allowed attacks are assigned to the corresponding variables.
I
"""
NUMBER_OF_LIVES = 5
MAGE = "1"
WARRIOR = "2"
ROGUE = "3"
WIN_COMBINATIONS = [(MAGE, WARRIOR), (WARRIOR, ROGUE), (ROGUE, MAGE)]
ALLOWED_INPUTS = ("start", "help", "score", "rules", "exit")


def help_display():
    """
    When called, returns strings with the list of menu options.
    """
    print("--------------------")
    print("1. Enter 'start' to begin the game.\n"
          "2. Enter 'score' to check the highscore\n"
          "3. Enter 'rules to learn more about the game itself\n"
          "4. Enter 'help' if you need instructions\n"
          "5. Enter 'exit' to quit the game")
    print("--------------------")


def game_rules():
    """
    When called, prints the list of rules, indexes of each fighter
    and explains the win combination
    """
    print("--------------------")
    print("The game consists of rounds: attack and defence. "
          "During the round, players must choose a fighter from the "
          "list: Mage, Warrior and Rogue. Whose fighter is stronger - wins\n"
          "Each victory during the attack round gives you "
          "1 point to a score. Defeating an enemy gives 5 points. "
          "However whenever the enemy is defeated, "
          "a new one comes, stronger than the previous one."
          "If your opponent attacks you successfully, "
          "you will lose 1 life. When all lives are lost - game ends.\n"
          "So, what are you waiting for? Enter start, "
          "fill in your Name and let the fight begin!")
    print("--------------------")
    print("Epic Fight Game Controls:\n"
          "--------------------\n"
          "Enter 1 - for Mage, 2 - for Warrior, 3 - for Rogue")
    print("--------------------\n"
          "Epic Fight Game Rules Set:\n"
          "--------------------\n"
          "Mage beats Warrior, Warrior beats Rogue, Rogue beats Mage\n"
          "--------------------")


def show_score():
    """
    Gets the list of lines from scores.txt files.
    Put the list in cycle and prints each element separately.
    """
    with open ("scores.txt", "r") as scores_file:
        scores_list = scores_file.read().split('\n')
        for item_of_scores in scores_list:
            print("--------------------")
            print(item_of_scores)
