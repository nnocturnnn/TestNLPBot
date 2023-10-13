import requests
import os
import json
from utils.llm import chat_completion_request, messages

def execute_function_call(assistant_message):
    if assistant_message.get("function_call").get("name") == "get_current_weather":
        location = json.loads(assistant_message.get("function_call").get("arguments") )["location"]
        results = get_current_weather(location)
    else:
        results = f"Error: function {assistant_message['function_call']['name']} does not exist"

    return results
    

def get_current_weather(location):
    RAPID_API_KEY = os.getenv("RAPID_API_KEY")
    try:
        url = "https://weatherapi-com.p.rapidapi.com/current.json"

        querystring = {"q": location}
        print(f"\n>>>> got the querystring as: {querystring}")
        headers = {
            "X-RapidAPI-Key": RAPID_API_KEY,
            "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)
        response_json = response.json()
        print(f"\n>>>> got the RAPID API response as: \n{response_json}")
        return response_json
    except Exception as e:
        raise e
    
def get_natural_response(content):
    convert_prompt = f"convert this results from weather api to a natural english sentence: {content}"
    messages.append({"role": "user", "content": convert_prompt})
    convert_prompt_response = chat_completion_request(messages=messages)
    print(f"\n>>>> recieved message: {convert_prompt_response.json()}")
    new_assistant_message = convert_prompt_response.json()["choices"][0]["message"]
    messages.append(new_assistant_message)
    content = new_assistant_message["content"]
    print(f"\n>>>> natural response: \n{content}")
    return content