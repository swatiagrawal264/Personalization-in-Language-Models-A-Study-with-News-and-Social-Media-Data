import json
import requests

# Function to interact with ChatGPT using the OpenAI API
def ask_chatgpt(question, api_key):
    url = "https://api.openai.com/v1/engines/davinci/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "prompt": question,
        "max_tokens": 150
    }
    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        json_response = response.json()
        if "choices" in json_response and len(json_response["choices"]) > 0 and "text" in json_response["choices"][0]:
            return json_response["choices"][0]["text"].strip()
        else:
            print("Unexpected response format from OpenAI API.")
    else:
        print(f"Error: {response.status_code} - {response.text}")
    return None

# Example usage to read the dataset and interact with ChatGPT for each item
api_key = "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"  # Replace with your actual API key
file_path = "/Users/medhagoel/Downloads/Compsci646/Final_project/dev_questions_tweet.json"

# Read the dataset
with open(file_path, 'r') as file:
    data = json.load(file)

# Check if the expected structure is found
if isinstance(data, dict) and 'golds' in data and isinstance(data['golds'], list):
    # Loop through the 'golds' field and interact with ChatGPT for each item
    for item in data['golds']:
        if isinstance(item, dict) and 'id' in item:
            question = f"Can you categorize this article? {item['id']}"  # Customize the prompt/question as needed
            response = ask_chatgpt(question, api_key)
            if response is not None:
                print(f"Article ID: {item['id']} - Predicted Category: {response}")
        else:
            print("Each item in 'golds' field should be a dictionary with an 'id' field.")
else:
    print("Dataset format is not as expected. Ensure it has 'golds' field as a list of dictionaries.")





