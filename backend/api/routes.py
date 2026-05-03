from fastapi import APIRouter
from backend.services.prescription import create_prescription, create_multi_drug_schedule
from backend.schemas.prescription_schema import ScheduleRequest, MultiDrugScheduleRequest


router = APIRouter()

@router.get("/")
def read_root():
    return {"message": "Welcome to the Smart Prescription API!"}

@router.post("/prescription", response_model=dict, summary="Generate a prescription schedule")
def generate_prescription(request: ScheduleRequest):
    return create_prescription(request.drug_name, request.frequency, request.duration, request.start_hour)

@router.post("/multi-drug-schedule", response_model=list, summary="Generate a combined schedule for multiple drugs")
def generate_multi_drug_schedule(request: MultiDrugScheduleRequest):
    return create_multi_drug_schedule(request.drugs)