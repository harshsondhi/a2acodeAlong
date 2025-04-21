from .agent import execute

async def run(payload):
    """
    Run the task manager with the given payload.

    Args:
        payload (dict): The payload to send to the agent.

    Returns:
        dict: The response from the agent.
    """
    return await execute(payload)