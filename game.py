"""
Importing various constants that defines behaviour of certain functions in the game.
Importing the main game classes: Enemy and Player,
they are used to create object instances.
Importing custom exception that aids to game sustainability
"""
from OOP_Module.settings import ALLOWED_INPUTS, help_display, game_rules, show_score
from OOP_Module.models import Enemy, Player
from OOP_Module.exceptions import EnemyDown, GameOver, GameQuit, UserInputChecker


def play():
    """
    Main game function. Received player object and creates enemy object.
    Within infinite loop calls attack/defence method until player's lives = 0.
    Once *lives* attribute == 0, game ends.
    Various exceptions are called within the game to control the process:
    1. EnemyDown - creates new enemy if the current instance is dead.
    2. GameQuit - ends the game if the user enters *exit*
    3. UserInputChecker - checks user's input
    """
    game_level = 5
    enemy_object = Enemy(game_level)
    while player_object.lives != 0:
        try:
            print(f"{player_object.attack(enemy_object)}."
                  f" Your score is: {player_object.score}")
            print("-----------------------------------")
            print(f"{player_object.defence(enemy_object)}."
                  f" Number of lives left: {player_object.lives}")
            print("-----------------------------------")
        except EnemyDown:
            print("Good Job! Enemy defeated but new one is approaching.")
            player_object.score += 5
            game_level += 1
            enemy_object = Enemy(game_level)
            print(f'New enemy with lives {enemy_object.lives} is here')
        except GameQuit:
            raise GameQuit
        except UserInputChecker:
            print("Please enter the correct value:\n"
                  "1 - for Mage\n"
                  "2 - for Warrior\n"
                  "3 - for Rogue\n"
                  "'exit' to quit the game")
            continue


if __name__ == "__main__":
    player_object = Player(name=input("Please enter your name: "))
    while True:
        user_input = (
            input("To learn the rules of the game, enter *rules*\n"
                  "Enter *start* to commence playing.\n"
                  "To see other menu options, enter *help*: "))
        if user_input == "start":
            try:
                play()
            except KeyboardInterrupt:
                print("Thank you for playing")
            except GameOver:
                print("Enemy hit successfully. You have no lives left.\n")
                if player_object.score == 1:
                    with open("scores.txt", "a+") as scores_file:
                        scores_file.write(f"{player_object.name}"
                                          "scored {player_object.score} point\n")
                    print("-----------------------------------")
                    print("{},you died game and scored {} \
                    point".format(player_object.name, player_object.score))
                else:
                    with open("scores.txt", "a+") as scores_file:
                        scores_file.write(f"{player_object.name} \
                        scored {player_object.score} points\n")
                    print("-----------------------------------")
                    print("{},you died game and scored {} \
                    points".format(player_object.name, player_object.score))
            except GameQuit:
                print("Game over")
                break
            finally:
                print("Goodbye")
        elif user_input == "help":
            help_display()
            continue
        elif user_input == "rules":
            game_rules()
            continue
        elif user_input == "score":
            show_score()
            continue
        elif user_input == "exit":
            print("Goodbye")
            break
        elif user_input != ALLOWED_INPUTS:
            print("Enter enter one of the correct values:\n"
                  "1. start\n"
                  "2. help\n"
                  "3. rules"
                  "3. score\n"
                  "4. exit")
