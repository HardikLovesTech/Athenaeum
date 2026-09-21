import httpx

from app.core.config import (
    OpenRouterApiKey,
    OpenRouterModel,
)


OpenRouterUrl = "https://openrouter.ai/api/v1/chat/completions"

def GenerateAnswer(
        Query:str,
        Context: str,
) -> str:
    Prompt =     Prompt = f"""
Answer the user's question using only the provided context.

If the context does not contain enough information to answer the question,
say that the information is not available in the provided documents.

Context:
{Context}

Question:
{Query}
""".strip()

    Headers = {
        "Authorization": f"Bearer {OpenRouterApiKey}",
        "Content-Type": "application/json"
    }

    Payload = {
        "model": OpenRouterModel,
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are Athenaeum, a research assistant. "
                    "Answer questions using the provided document context."
                ),
            },
            {
                "role":"user",
                "content":Prompt
            },
        ],
    }


    Response = httpx.post(
        OpenRouterUrl,
        headers=Headers,
        json=Payload,
        timeout=60.0
    )


    Response.raise_for_status()

    ResponseData = Response.json()

    return ResponseData["choices"][0]["message"]["content"]
