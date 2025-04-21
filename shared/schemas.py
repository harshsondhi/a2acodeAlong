from pydantic import BaseModel, Field
class TravelRequest(BaseModel):
    """
    Schema for a travel request.
    """
    
    destination: str = Field(..., description="Destination of the travel")
    start_date: str = Field(..., description="Start date of the travel in YYYY-MM-DD format")
    end_date: str = Field(..., description="End date of the travel in YYYY-MM-DD format")
    budget: float = Field(..., description="Status of the travel request (e.g., pending, approved, rejected)")