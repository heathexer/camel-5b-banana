import banana_dev as banana

p = {
    "prompt": "tell me something"
}

api_key = ""
model_key = ""

out = banana.run(api_key, model_key, p)
print(out["modelOutputs"])