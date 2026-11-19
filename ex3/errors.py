# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    errors.py                                         :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: alkonsta <alkonsta@student.codam.nl>      +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/11/19 23:07:30 by alkonsta         #+#    #+#              #
#    Updated: 2026/11/19 23:09:42 by alkonsta        ###   ########.nl        #
#                                                                             #
# *************************************************************************** #

class GardenError(Exception):

    def __init__(self, msg: str = "Unknown Garden Error") -> None:
        super().__init__(msg)


class PlantError(GardenError):
    def __init__(self, msg: str = "Unknown Plant Error") -> None:
        super().__init__(msg)


class WaterError(GardenError):
    def __init__(self, msg: str = "Unknown Water Error") -> None:
        super().__init__(msg)
