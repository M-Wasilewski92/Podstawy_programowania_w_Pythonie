from random import randint
import re


def main():
    """
    Ask user to choose ono or two dice types to roll. Checks if input is valid.
    Make rolls for user according to provided pattern.
    Make rolls for computer with random chosen dice.
    Add rolls result to score.
    Ends the game when score is 2001 or higher.
    :rtype: str
    :return: Message who won.
    """

    player_1 = 0
    player_2 = 0
    while True:
        dice = get_dice()
        roll = roll_dice(dice)
        if roll == 7:
            print("You rolled 7 :(")
            roll = roll // 7
        if roll == 11:
            print("You rolled 11 :)")
            roll = roll * 11
        player_1 += roll
        print(f"You rolled: {roll}")
        roll = roll_dice(get_computer_dice())
        if roll == 7:
            print("Computer rolled 7 :)")
            roll = roll // 7
        if roll == 11:
            print("Computer rolled 11 :(")
            roll = roll * 11
        player_2 += roll
        print(f"Player 2 rolled: {roll} ")
        print("_" * 20)
        print(f"Your score: {player_1}")
        print(f"Computer score: {player_2}")
        print("_" * 20)
        if player_1 >= 2001:
            return print("You WON!!!")
        elif player_2 >= 2001:
            return print("Computer Won :( ")



def roll_dice(dice_choice):
    """
    Makes rolls according to provided parameters and returns sum of rolls results int.
    :param dice_choice: list of 1 or two dice parameter
    :return: int
    """
    if len(dice_choice) > 1:
        for dice in dice_choice:
            get_int = re.findall('[0-9]+$', dice)
            results = []
            for i in get_int:
                roll = randint(1, int(i))
                results.append(roll)
            return sum(results)
    else:
        get_int = re.search('[0-9]+$', dice_choice[0])
        result = []
        for i in range(2):
            roll = randint(1, int(get_int.group()))
            result.append(roll)
            return sum(result)



def get_dice():
    """Ask user to choose dice then return list with chosen dice"""
    allowed_pattern = ['D3', 'D4', 'D6', 'D8', 'D10', 'D12', 'D20', 'D100',
                       '2D3', '2D4', '2D6', '2D8', '2D10', '2D12', '2D20', '2D100']
    while True:
        print("Chose dice to roll!")
        dice_type = input("Allowed dice: 'D3' 'D4' 'D6' 'D8' 'D10' 'D12' 'D20' 'D100'\n")
        dice_type = re.findall('2?D[0-9]+', dice_type)
        if dice_type:
            if len(dice_type) > 1:
                if dice_type[0] and dice_type[1] in allowed_pattern:
                    return dice_type
            elif dice_type[0] in allowed_pattern:
                return dice_type
        else:
            print("Its not valid dice Choice")

def get_computer_dice():
    """Randomly take two dice patterns and return them as list"""
    allowed_choices = ['D3', 'D4', 'D6', 'D8', 'D10', 'D12', 'D20', 'D100']
    choice = []
    for i in range(2):
        get_random_index = randint(0, 7)
        choice.append(allowed_choices[get_random_index])
    return choice

if __name__ == '__main__':
    main()
