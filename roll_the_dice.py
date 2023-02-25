# rzut kostką

import random


def roll_the_dice(dice_code):
    """
    Simulates rolling a dice with specified code and returns the result.
    Dice code has format 'NdM+/-K' where:
    - N is the number of dice to roll (default: 1)
    - M is the number of faces on each die
    - K is an optional modifier to the roll result (default: 0)
    """
    # Parse the dice code
    parts = dice_code.split('D')
    if len(parts) != 2:
        return 'Invalid dice code.'
    try:
        num_dice = int(parts[0]) if parts[0] else 1
        mod_idx = parts[1].find('+')
        if mod_idx == -1:
            mod_idx = parts[1].find('-')
        if mod_idx == -1:
            num_faces = int(parts[1])
            mod = 0
        else:
            num_faces = int(parts[1][:mod_idx])
            mod = int(parts[1][mod_idx:])
    except ValueError:
        return 'Invalid dice code.'

    # Roll the dice and apply the modifier
    if num_faces not in [3, 4, 6, 8, 10, 12, 20, 100]:
        return 'Invalid dice code.'
    rolls = [random.randint(1, num_faces) for _ in range(num_dice)]
    total = sum(rolls) + mod

    return total

# Test the function


print(roll_the_dice("2D10+10"))  # 12 to 30
print(roll_the_dice("D6"))  # 1 - 6
print(roll_the_dice("2D3"))  # 2 - 6
print(roll_the_dice("D12-1"))  # 0 - 11
print(roll_the_dice("DD34"))  # 'Invalid dice code.'
print(roll_the_dice("4-3D6"))  # 'Invalid dice code.'
print(roll_the_dice("2D6+10"))  # 12 - 22
