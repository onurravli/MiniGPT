import json
import requests


class MiniGPT:
    def __init__(self, key):
        self.key = key

    def chat(self, model, role, content, temp: float = 1):
        if not (model and role and content and self.key):
            return json.dumps({
                "error": "Some of arguments are missing."
            })
        if temp > 2.0 or temp < 0.0:
            return json.dumps({
                "error": "Enter a valid temperature."
            })
        res = requests.post(
            url="https://api.openai.com/v1/chat/completions",
            json={
                "model": model,
                "messages": [{"role": role, "content": content}],
                "temperature": temp
            },
            headers={
                "Authorization": f"Bearer {self.key}",
                "Content-Type": "application/json"
            })
        try:
            return json.dumps({
                "response": res.json()['choices'][0]['message']['content']
            })
        except KeyError as keyError:
            return json.dumps({
                "error": f"An error occurred on the OpenAI side: {keyError}"
            })
        except (KeyboardInterrupt, EOFError):
            return json.dumps({
                "exiting": "with exit code 0."
            })
