from fastapi import FastAPI
from workflow_registry import WorkflowRegistry
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@post("/example-usage")
def example_usage():
    registry = WorkflowRegistry()
    registry.publish(
        name="member_eligibility",
        version="1.0.0",
        env_config={
            "API_URL": "https://qa.example.com",
            "TIMEOUT_SECONDS": 10,
            "MAX_RETRIES": 3,
            "DEBUG_MODE": False
        }
    )