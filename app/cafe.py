import datetime
from app.errors import (NotWearingMaskError,
                        NotVaccinatedError, OutdatedVaccineError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        number = 0
        if visitor["wearing_a_mask"] is False:
            number += 1
            raise NotWearingMaskError(f"Visitor {visitor["name"]} "
                                      f"is not wearing a mask.")
        if "vaccine" not in visitor.keys():
            number += 1
            raise NotVaccinatedError(f"Visitor {visitor["name"]} "
                                     f"is not vaccinated.")
        elif visitor["vaccine"]["expiration_date"] < datetime.date.today():
            number += 1
            raise OutdatedVaccineError(f"Visitor {visitor["name"]} "
                                       f"has an outdated vaccine.")
        if number == 0:
            return f"Welcome to {self.name}"
