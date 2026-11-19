#!/usr/bin/python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_first_exception.py                             :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: alkonsta <alkonsta@student.codam.nl>      +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/11/19 16:57:20 by alkonsta         #+#    #+#              #
#    Updated: 2026/11/19 16:57:59 by alkonsta        ###   ########.nl        #
#                                                                             #
# *************************************************************************** #


class TemperatureError(ValueError, TypeError):
    pass


def input_temperature(temp_str: str) -> int:
    try:
        return int(temp_str)
    except (ValueError, TypeError) as e:
        raise TemperatureError(
                f"input_temperature error: {e}"
                ) from e


def test_temperature() -> None:
    tests: list[str] = ["25", "abc"]
    for test in tests:
        try:
            print(f"\nInput data is '{test}'")
            res = input_temperature(test)
            print(f"Temperature is now {res}°C")
        except TemperatureError as e:
            print(f"Caught {e}")
    print("\nAll tests completed - program didn't crash!")


def main() -> None:
    print("=== Garden Temperature ===")
    test_temperature()


if __name__ == "__main__":
    main()
