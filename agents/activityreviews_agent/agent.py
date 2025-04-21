from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
import json


suggestion_agent = Agent(
    name="activityreviews_agent",
    model=LiteLlm("openai/gpt-4o"),
    #api_key="",
    description="Suggest interesting activities for user at the destination.",
    instruction=(""" 
                 Given a destination, suggest interesting activities for the user to do there.
                 For each activity, provide name, a brief description , price estimation and duration in hours
                 Respond in plain English(not in json). Keep it cocise and well-formatted
                 """)
    
)

session_threads = InMemorySessionService()
runner = Runner(
    agent=suggestion_agent,
    session_service=session_threads,
    app_name="activityreviews_app",
)

USER_ID="user_activity"
SESSION_ID="session_activity"

async def execute(request):
    session_threads.create_session(
        app_name="activityreviews_app",
        user_id=USER_ID,
        session_id=SESSION_ID,
    )
    
    prompt = (
        f""" 
        User wants to know about activities in {request['destination']}.
        User's budget is {request['budget']}.
        User's travel dates are from {request['start_date']} to {request['end_date']}.
        Suggest 2-3 activities for the user to do there.
        For each activity, provide name, a brief description , price estimation and duration in hours.
        Respond in JSON format using the key 'activities' with a list of activity objects.
        """
    )
    
    message = types.Content(
        role="user",
        parts=[
            types.Part(
                text=prompt
            )
        ],
    )
    
    async for event in runner.run_async(user_id=USER_ID, session_id=SESSION_ID, new_message=message):
        if event.is_final_response:
            response_text = event.content.parts[0].text
            try:
                parsed = json.loads(response_text)
                if "activities" in parsed and isinstance(parsed["activities"], list):
                    return {"activities": parsed["activities"]}
                else:
                    print("❌ 'activities' key missing or not a list in response JSON")
                    return {"activities": response_text}  # fallback to raw text
            except json.JSONDecodeError as e:
                print("❌ JSON parsing failed:", e)
                print("Response content:", response_text)
                return {"activities": response_text}  # fallback to raw text   
            
    
    
