


uvicorn agents.host_agent.__main__:app --port 8000 &
uvicorn agents.flight_agent.__main__:app --port 8001 &
uvicorn agents.booking_agent.__main__:app --port 8002 &      
uvicorn agents.activityreviews_agent.__main__:app --port 8003 &
streamlit run travel_ui.py