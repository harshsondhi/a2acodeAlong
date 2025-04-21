from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types


booking_agent = Agent(
    name="booking_agent",
    description="A booking agent that can help you find a hotel or stay option.",
    model=LiteLlm("openai/gpt-4o"),
    #api_key="",
    instruction=(
        """ 
        Given a destination, travel dates, and any budgets, sugget 2-3 hotels or stay option.
        Include hotel name, price per night and location, ensure suggestions are with in budget.
        If the user has not provided a budget, suggest hotels that are within a reasonable price range.
        If the user has not provided travel dates, suggest hotels that are available for the next 30 days.
        If the user has not provided a destination, suggest hotels in popular tourist destinations.
        """
    )
    
)

session_service=InMemorySessionService()

runner = Runner(
    agent=booking_agent,
    session_service=session_service,
    app_name="booking_app"
)

USER_ID = "user_booking"
SESSION_ID = "session_booking"
async def execute(request):
    session_service.create_session(
        user_id=USER_ID,
        session_id=SESSION_ID,
        app_name="booking_app"
    )
    prompt = (
        """ 
        User is staying in {request['destination']} from {request['start_date']} to {request['end_date']} 
        with a budget of {request['budget']}. Suggest stay options.
        """
    )
    
    message = types.Content(role="user", parts=[types.Part(text=prompt)])
    
    async for event in runner.run_async(user_id=USER_ID, session_id=SESSION_ID, new_message=message):
        if event.is_final_response():
            return {"stays": event.content.parts[0].text}