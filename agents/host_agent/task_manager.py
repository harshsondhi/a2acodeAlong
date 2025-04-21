from .agent import execute
from commonutil.a2a_clientCall import call_agent

FLIGHT_URL = "http://localhost:8001/run"
BOOKING_URL = "http://localhost:8002/run"
ACTIVITIES_REVIEWS_URL = "http://localhost:8003/run"

async def run(payload):
    """
    Execute the task with the given payload.

    Args:
        payload (dict): The payload containing the task details.

    Returns:
        dict: The result of the task execution.
    """
    print("Executing task with payload:", payload)
    # Call the flight agent
    flight_response = await call_agent(FLIGHT_URL, payload)
    print("Flight response:", flight_response)
    # Call the stay agent
    stay_response = await call_agent(BOOKING_URL, payload)
    print("Stay response:", stay_response)
    # Call the activities agent
    activities_response = await call_agent(ACTIVITIES_REVIEWS_URL, payload)
    print("Activities response:", activities_response)
    
    flight_response = flight_response if isinstance(flight_response, dict) else {}
    stay_response = stay_response if isinstance(stay_response, dict) else {}
    activities_response = activities_response if isinstance(activities_response, dict) else {}
    
    
    # Combine the responses         
    combined_response = {
        "flights": flight_response.get("flights", "No flights returned."),
        "stay": stay_response.get("stays", "No stay options returned."),
        "activities": activities_response.get("activities", "No activities found.")
    }
    return combined_response
 