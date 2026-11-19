# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_raise_exception.py                             :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: alkonsta <alkonsta@student.codam.nl>      +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/11/19 19:02:24 by alkonsta         #+#    #+#              #
#    Updated: 2026/11/19 19:43:20 by alkonsta        ###   ########.nl        #
#                                                                             #
# *************************************************************************** #


TEMP_MIN: int = 0
TEMP_MAX: int = 40


class TemperatureError(ValueError):
    pass


def input_temperature(temp_str: str) -> int:
    try:
        temp: int = int(temp_str)
    except (ValueError, TypeError) as e:
        raise TemperatureError(e) from e
    if temp < TEMP_MIN:
        raise TemperatureError(
                f"{temp}°C is too cold for plants" +
                f" (min {TEMP_MIN}°C)"
                )
    elif temp > TEMP_MAX:
        raise TemperatureError(
                f"{temp}°C is too hot for plants" +
                f" (max {TEMP_MAX}°C)"
                )
    return temp


def test_temperature() -> None:
    tests: list[str] = ["25", "abc", "-100", "50"]
    for test in tests:
        try:
            print(f"\nInput data is '{test}'")
            res = input_temperature(test)
            print(f"Temperature is now {res}°C")
        except TemperatureError as e:
            print(f"Caught input_temperature error: {e}")
    print("\nAll tests completed - program didn't crash!")


def main() -> None:
    print("=== Garden Temperature Checker ===")
    test_temperature()


if __name__ == "__main__":
    main()
