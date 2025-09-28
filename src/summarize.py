import json
from openai import OpenAI

client = OpenAI(
    api_key="",
)

try:
    with open("../static/ds_data.json") as file:
        cs_data = json.load(file)
    for entry in cs_data:
        text_to_summarize = entry["description"]
        prompt=f"Summarize the provided text in one concise sentence: {text_to_summarize}."
        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "developer", "content": "You are an assistant that specializes in summarizing text. "},
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
        )
        print(f"SUMMARIZED TEXT: {completion.choices[0].message.content}\n")
except Exception as e:
    print(f"The following error occured: {e}")