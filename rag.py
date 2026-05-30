import os
from anthropic import Anthropic
from dotenv import load_dotenv
from vector_storage import get_similar_incidents

load_dotenv(dotenv_path=".env")

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY")
)

message = client.messages.create(
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": "Hello, claude"
        }
    ],
    model="claude-opus-4-6"
)

print(message.content)

#next steps is to 
# call the get_similar_incidents function
# Build prompt that includes both the user's incident description and retrieved past incidents as context
# send it to claude
# return the response