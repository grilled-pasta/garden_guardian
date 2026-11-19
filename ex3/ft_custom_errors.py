# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_custom_errors.py                               :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: alkonsta <alkonsta@student.codam.nl>      +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/11/19 21:58:23 by alkonsta         #+#    #+#              #
#    Updated: 2026/11/19 23:09:53 by alkonsta        ###   ########.nl        #
#                                                                             #
# *************************************************************************** #

from ex3.errors import GardenError, PlantError, WaterError


def plant_error() -> None:
    raise PlantError("The tomato plant is wilting!")


def water_error() -> None:
    raise WaterError("Not enough water in the tank!")


# def main() -> None:
#     print("=== Custom Garden Errors Demo ===")
#
#     try:
#         print("\nTesting PlantError...")
#         plant_error()
#     except PlantError as e:
#         print(f"Caught PlantError: {e}")
#
#     try:
#         print("\nTesting WaterError...")
#         water_error()
#     except WaterError as e:
#         print(f"Caught WaterError: {e}")
#
#     print("\nTesting catching all garden errors...")
#     try:
#         plant_error()
#     except GardenError as e:
#         print(f"Caught GardenError: {e}")
#
#     try:
#         water_error()
#     except GardenError as e:
#         print(f"Caught GardenError: {e}")
#
#     print("\nAll custom error types work correctly!")

def main() -> None:
    print("=== Custom Garden Errors Demo ===")

    errors = [
           ("PlantError", plant_error, PlantError),
           ("WaterError", water_error, WaterError)
           ]

    for name, func, error_type in errors:
        print(f"\nTesting {name}...")
        try:
            func()
        except error_type as e:
            print(f"Caught {name}: {e}")

    print("\nTesting catching all garden errors...")

    for _, func, _ in errors:
        try:
            func()
        except GardenError as e:
            print(f"Caught GardenError: {e}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    main()
