from openai import OpenAI
from dotenv import load_dotenv
import os
from prompt_templates import few_shot_prompt

# Load environment variables
load_dotenv()

# Create OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_career_advice(profile):
    prompt = few_shot_prompt(profile)

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.4
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    profile = input("Enter your profile: ")
    advice = get_career_advice(profile)
    print("\nCareer Advice:\n")
    print(advice)
