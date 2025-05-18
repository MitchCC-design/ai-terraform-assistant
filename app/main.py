import os
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from openai import OpenAI

app = FastAPI()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.post("/prompt")
async def prompt_endpoint(request: Request):
    data = await request.json()
    prompt = data.get("request")
    if not prompt:
        return JSONResponse({"error": "No prompt provided."}, status_code=400)
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Change to "gpt-4o" if you want and have access
            messages=[
                {"role": "system", "content": "You are an AI assistant for Terraform and DevOps tasks."},
                {"role": "user", "content": prompt}
            ]
        )
        answer = response.choices[0].message.content
        return {"response": answer}
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)
