# loading_cargo.py
"""Program that uses a possible heuristic to optimally divide the crates between two trucks from
a randomly generated cargo list with total weight entered by the user."""
import random
from itertools import combinations


def loading_cargo():
    """Load the cargo between two trucks."""
    try:
        sum_cargo = int(input('Enter any number for the sum of the cargo: '))
    except ValueError:
        print('The number to be entered for the sum of the cargo must be an integer')
    else:
        # Decides how to distribute the cargo
        if sum_cargo % 2 == 0:
            half_weight_cargo = sum_cargo // 2
        else:
            half_weight_cargo = sum_cargo // 2 + 1

        # Load the cargo randomly
        cargo = []
        while sum(cargo) < sum_cargo:
            crate = random.randint(1, half_weight_cargo)
            if sum(cargo) + crate <= sum_cargo:
                cargo.append(crate)

        print(f'Cargo {cargo} has a sum of {sum(cargo)}')

        # Determines the possible cargo combinations
        cargo_size = (len(cargo))
        crate_distribution = []
        for n in range(cargo_size, 0, -1):
            crate_distribution += list(combinations(cargo, n))

        # Determines from the list of combinations which have a sum less than or equal to half the weight of the cargo
        half_cargo = []
        for crate_set in crate_distribution:
            if sum(crate_set) <= half_weight_cargo:
                half_cargo.append(list(crate_set))

        # Load the truck 1
        truck1 = []
        for crate in half_cargo:
            if sum(truck1) < sum(crate):
                truck1 = crate

        # Determines the cargo not introduced into the truck 1
        remaining_cargo = cargo.copy()
        for crate in truck1:
            remaining_cargo.remove(crate)

        # Load the truck 2
        truck2 = []
        remaining_cargo.sort(reverse=True)
        for crate in remaining_cargo:
            if crate + sum(truck2) <= half_weight_cargo:
                truck2.append(crate)

        print(f'Truck 1 {sorted(truck1)} has a sum of {sum(truck1)}')
        print(f'Truck 2 {sorted(truck2)} has a sum of {sum(truck2)}')


if __name__ == '__main__':
    loading_cargo()
