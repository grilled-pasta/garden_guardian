# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_different_errors.py                            :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: alkonsta <alkonsta@student.codam.nl>      +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/11/19 19:44:02 by alkonsta         #+#    #+#              #
#    Updated: 2026/11/19 21:57:31 by alkonsta        ###   ########.nl        #
#                                                                             #
# *************************************************************************** #


class GardenError(Exception):

    def __init__(self, name: str, error: Exception) -> None:
        super().__init__(error)
        self.name: str = name


def garden_operations(operation_number: int) -> None:
    match operation_number:
        case 0:
            _ = int("abc")
        case 1:
            _ = int(100 / 0)
        case 2:
            _ = open("test").fileno()
        case 3:
            _ = open(None).fileno()
        case _:
            return


def main() -> None:
    print("=== Garden Error Types Demo ===")
    for i in range(0, 5):
        try:
            try:
                print(f"Testing operation {i}...")
                garden_operations(i)
                print("Operation completed successfully!")
            except ValueError as e:
                raise GardenError("ValueError", e) from e
            except ZeroDivisionError as e:
                raise GardenError("ZeroDivisionError", e) from e
            except FileNotFoundError as e:
                raise GardenError("FileNotFoundError", e) from e
            except TypeError as e:
                raise GardenError("TypeError", e) from e
        except GardenError as e:
            print(f"Caught {e.name}: {e}")

    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    main()
