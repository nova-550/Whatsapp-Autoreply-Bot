from openai import OpenAI

# pip imstall openai
# if you saved the key under a different environment variable name,you can do something like : 
client = OpenAI(
    api_key="API key" #Enter your API Key
)

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        ("role": "system", "content": "You are a person named shiv who is an engineering student. He is from India. You analyze chat history and respond like Shiv"),
        ("role": "user", "content": "")
    ]
)

print(completion.choices[0].message.content)