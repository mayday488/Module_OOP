"""
Importing random module, so that Enemy class object's attack
could be determined randomly.
Importing various constants that are later used during the object
initiation and functions
Importing exceptions to control the game process
"""
from random import randint
from OOP_Module.settings import NUMBER_OF_LIVES, WIN_COMBINATIONS
from OOP_Module.exceptions import EnemyDown, GameOver, GameQuit, UserInputChecker


class Enemy:
    """
    One of two main classes. Creates object of the second player.
    Methods are run automatically.
    """
    def __init__(self, level):
        self.level = level
        self.lives = level

    @staticmethod
    def select_attack():
        """
        Returns a random number between one and three
        """
        return randint(1, 3)

    def decrease_lives(self):
        """
        Reduces the number of object lives. When life becomes 0 raises
        EnemyDown exception.
        Exception creates new instance of the object.
        """
        self.lives -= 1
        if self.lives:
            return self.lives
        raise EnemyDown  # exception must be places here


class Player:
    """
    Player class. Name is determined by the user.
    Other attributes are constants contained in the settings file.
    """
    allowed_attacks = ("1", "2", "3")

    def __init__(self, name):
        """
        Attributes: name, score, allowed_attacks.
        allowed_attacks is constant, located in the settings.py file.
        Constructor receives player name. Score is always 0
        """
        self.name = name
        self.score = 0
        self.lives = NUMBER_OF_LIVES

    def decrease_lives(self):
        """
        Reduces the number of object lives. When life becomes 0 raises
        GameOver exception.
        Exception ends the program and writes object score into a file.
        """
        self.lives -= 1
        if self.lives:
            return self.lives
        raise GameOver

    @staticmethod
    def fight(attack, defence):
        """
        Returns the result of the round:
        - 0 if there it was a draw
        -1 if the attack was unsuccessful
        1 if the attack was successful.
        """
        if attack == defence:
            return 0
        elif (attack, defence) in WIN_COMBINATIONS:
            return 1
        else:
            return -1

    def attack(self, enemy_obj):
        """
        Receives input from Player object (1, 2, 3), selects enemy attack from enemy_obj object.
        Calls the fight() method.
        If the result of the battle is 0, prints "It's a draw!".
        If 1 = "You attacked successfully!" and calls decrease_lives() method.
        If -1 returns "You missed!"
        If the user enters *exit*, calls GameQuit exception.
        If the user input is not in allowed_attacks or *exit*,calls UserInputChecker exception
        """
        player_attack = str(input("Time to attack! Choose your fighter: "))
        if player_attack == "exit":
            raise GameQuit
        if player_attack not in self.allowed_attacks and player_attack != "exit":
            raise UserInputChecker

        enemy_attack = enemy_obj.select_attack()
        fight_result = self.fight(player_attack, enemy_attack)

        if fight_result == 0:
            return "It's a draw!"
        elif fight_result == 1:
            enemy_obj.decrease_lives()
            self.score += 1
            return "You attacked successfully!"
        elif fight_result == -1:
            return "Unfortunately, you've missed!"

    def defence(self, enemy_obj):
        """
        Method is same as the attack() method, but when the fight method called,Enemy object input is transferred first.
        If the result of the battle is 0, prints "It's a draw!".
        If 1 = ""Enemy attack was successful!" and calls decrease_lives() of the Player.
        If -1 returns "Enemy missed!"
        """
        player_attack = str(input("Defend yourself! Choose your fighter: "))
        if player_attack == "exit":
            raise GameQuit
        if player_attack not in self.allowed_attacks and player_attack != "exit":
            raise UserInputChecker

        enemy_attack = enemy_obj.select_attack()
        fight_result = self.fight(enemy_attack, player_attack)

        if fight_result == 0:
            return "It's a draw!"
        if fight_result == 1:
            self.decrease_lives()
            return "Enemy attack was successful!"
        if fight_result == -1:
            return "Enemy missed"
