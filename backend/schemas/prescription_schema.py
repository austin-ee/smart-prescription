from pydantic import BaseModel, field_validator
from typing import List
from enum import Enum


class ScheduleRequest(BaseModel):
    drug_name: str
    frequency: str
    duration: int
    start_hour: int


    @field_validator("drug_name")
    def validate_drug_name(cls, value):
        if not value.strip() or len(value.strip()) == 0:
            raise ValueError("drug_name cannot be empty")
        return value.strip()

    @field_validator("start_hour")
    def validate_start_hour(cls, value):
        if not (0 <= value <= 23):
            raise ValueError("start_hour must be between 0 and 23")
        return value

    @field_validator("duration")
    def validate_duration(cls, value):
        if value <= 0:
            raise ValueError("duration must be a positive integer")
        return value

    @field_validator("frequency")
    def validate_frequency(cls, value):
        valid_frequencies = {"OD", "BD", "TDS", "QID"}
        if value.upper() not in valid_frequencies:
            raise ValueError(f"frequency must be one of {valid_frequencies}")
        return value.upper()
     

class MultiDrugScheduleRequest(BaseModel):
    drugs: List[ScheduleRequest]

    @field_validator("drugs")
    def validate_drugs(cls, value):
        if not value or len(value) == 0:
            raise ValueError("drugs list cannot be empty")
        return value