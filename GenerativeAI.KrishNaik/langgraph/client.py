from langchain_mcp_adapters import MultiServiceMCPClient

import os
import dotenv
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langgraph.prebuilt import create_react_agent 

load_dotenv()


import asyncio 

async def main():
    client = MultiServiceMCPClient(
        "math": {
            "command" : "python",
            "args":["mathserver.py"]
            "transport" : "stdio"

        },
        "weather" :{
            "url" : "http:localhost:8000/mcp",
            "transport" : "streamable_http"
        }
    )

    os.environ["GEMINI_API_KEY"] = os.getenv("GEMINI_API_KEY")
    model = init_chat_model(
    "gemini-2.5-flash",
    model_provider="google_genai")

    agent= create_react_agent(
             model,tools
    )

    math_response = await agent.invoke({
        "messages" : {{"role":"user", "content": "what is (3 + 5) x 12"}}
    })

    print("Math response:" ,math_response['messages'][-1].content)

asyncio.run(main())

