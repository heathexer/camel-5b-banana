import torch
import os

from potassium import Potassium, Request, Response

from transformers import pipeline

app = Potassium("my_app")

# @app.init runs at startup, and loads models into the app's context
@app.init
def init():
    model = pipeline(model='Writer/camel-5b-hf', device_map="auto", max_new_tokens=100)
   
    context = {
        "model": model
    }

    return context

# @app.handler runs for every call
@app.handler()
def handler(context: dict, request: Request) -> Response:
    prompt = request.json.get("prompt")
    model = context.get("model")
    outputs = model(prompt)

    return Response(
        json = {"outputs": outputs}, 
        status=200
    )

if __name__ == "__main__":
    app.serve()