from .task_manager import run
from commonutil.a2a_serverCall import create_app

app = create_app(agent=type("Agent", (), {"execute": run}))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8002)