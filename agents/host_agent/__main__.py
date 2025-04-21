# from .task_manager import run
from commonutil.a2a_serverCall import create_app
from .task_manager import run

app = create_app(agent=type("Agent", (), {"execute": run}))
if __name__ == "__main__":
    import uvicorn
    # Run the FastAPI app (A2A server) if this script is executed
    uvicorn.run(
        app,
        port=8000)