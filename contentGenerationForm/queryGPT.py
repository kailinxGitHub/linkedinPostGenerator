from dotenv import load_dotenv
load_dotenv()
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

def query(temperature, max_tokens, context, content):
    # customer input message
    prompt = """
            Role: You are an excellent copyrighter. You are writing a LinkedIn post for a client, writing in a professional, captivating, and joyful tone.
            Context: {context}
            Task: Use moderate amount of emojis with short emoji bulletpoints, short paragraphs and a call to action at the end, write about {content}
            """

    completion = client.chat.completions.create(
        model = "gpt-3.5-turbo-0125",
        messages = [
            {"role": "user", "content": prompt.format(context=context, content=content)}
        ],
        temperature = temperature,
        max_tokens = max_tokens
    )
    return completion.choices[0].message.content

# print(query(temperature=1.0, max_tokens=100, context="I am a college student studying computer science, passionate about the software engineering and want to share my experience with everyone. ", content="After a long journey and a list of rejections from searching for research assistant roles, my expertise have finally been acknolwedged by a professor. I am now a research assistant at Northeastern, working on a project that I wont disclose yet. Just sharing to tell everyone that if you keep trying your best, you will eventually get what you want."))