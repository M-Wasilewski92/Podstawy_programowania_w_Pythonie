import re, random
def main():
    """Ask user for a pattern. Checks if input is valid.
       Make rolls according to provided pattern.
    :rtype: str
    :return: Dice roll value for proper dice pattern, 'Wrong Input'
    """
    allowed_dice = ['D3', 'D4', 'D6', 'D8', 'D10', 'D12', 'D20', 'D100']
    while True:
        pattern = input('How many and what dice are we rolling?\n')

        if re.search('^[0-9]*D[0-9]+\+?[0-9]?', pattern):
            rolls = re.search("^[0-9]+", pattern)
            rolls = int(rolls.group()) if rolls else 1

            dice_type = re.search("D[0-9]+", pattern)
            if dice_type.group() not in allowed_dice:
                return print("I can't roll that type of dice, please provide correct input")
            dice_type = re.search("[0-9]+", dice_type.group())
            dice_type = int(dice_type.group())

            bonus = re.search("[+-][0-9]+", pattern)
            bonus= int(bonus.group()) if bonus else 0

            for roll, result in enumerate(dice_simulator(dice_type=dice_type, rolls=rolls, bonus=bonus)):
                print(f"Roll {roll + 1}: {result} ")
            continue
        else:
             print("I can't roll that, please provide correct input")

def dice_simulator(dice_type, rolls, bonus):
    """Returns list of rolls made with provided parameters"""
    results = []
    for i in range(rolls):
        result = random.randint(1, dice_type)
        result += bonus
        if result < 0:
            result = 0
        results.append(result)
    return results

if __name__ == '__main__':
    main()
