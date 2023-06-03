import gpt4all
from fastapi import FastAPI
from pydantic import BaseModel, Field


class Query(BaseModel):
    id: str
    prompt: str
    stream: bool = True


print("Loading the model ...")
model = gpt4all.GPT4All("ggml-mpt-7b-chat.bin")
print("Loaded")

app = FastAPI()


@app.post("/llm/api/v1/completion")
async def complete(query: Query):
    return model.generate(query.prompt, streaming=query.stream)
