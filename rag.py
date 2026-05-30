import os
from anthropic import Anthropic
from dotenv import load_dotenv
from vector_storage import get_similar_incidents, store_incidents_in_db

load_dotenv()
store_incidents_in_db()

user_input = "Server is returning 500 errors" #needs to be changed later on once the cli is built to take in user input
similar_incidents = get_similar_incidents(user_input)

def claude_response():
    client = Anthropic(
        api_key=os.environ.get("ANTHROPIC_API_KEY")
    )
    
    agentic_prompt = f"""
    You are an SRE agent that is responsible for assisting in incident response. Your job is to assist in finding a root cause
    for what the user is asking. You will be concise in your responses and only provide the necessary details. If you do not have the data to properly respond, say so. 
    Do not make anything up. 

    current incident: {user_input}

    Similar past incidents:
    {similar_incidents}

    Based on the result of these past incidents, suggest the most likely root cause and possible troubleshooting steps.
    """
    message = client.messages.create(
        max_tokens=1024,
        messages = [
            {
                "role": "user",
                "content": agentic_prompt,
            }
        ],
        model="claude-opus-4-6",
    )
    print(message.content[0].text)


claude_response()
