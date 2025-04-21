import httpx
async def call_agent(agent_url: str, payload: dict) -> dict:
    """
    Call the agent with the given payload.

    Args:
        agent_url (str): The URL of the agent to call.
        payload (dict): The payload to send to the agent.

    Returns:
        dict: The response from the agent.
    """
    async with httpx.AsyncClient() as client:
        response = await client.post(agent_url, json=payload, timeout=60)
        response.raise_for_status()
        return response.json()