# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_finally_block.py                               :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: alkonsta <alkonsta@student.codam.nl>      +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/11/19 22:24:38 by alkonsta         #+#    #+#              #
#    Updated: 2026/11/19 23:10:59 by alkonsta        ###   ########.nl        #
#                                                                             #
# *************************************************************************** #

from ex3.errors import PlantError


def water_plant(plant_name: str) -> None:
    if not plant_name or not plant_name[0].isupper():
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    print(f"Watering {plant_name}: [OK]")


def test_watering_system(plants: list[str]) -> None:
    try:
        print("Opening watering system")
        for plant_name in plants:
            water_plant(plant_name)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print("... ending tests and returning to main")
    finally:
        print("Closing watering system")


def main() -> None:
    print("=== Garden Watering System ===")
    print("\nTesting valid plants...")
    test_watering_system(["Tomato", "Lettuce", "Carrots"])
    print("\nTesting invalid plants...")
    test_watering_system(["Tomato", "lettuce", "carrots"])
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    main()
