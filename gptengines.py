from openai import OpenAI

client = OpenAI(api_key='sk-W96H70nLh1osY96bAXi5T3BlbkFJ5NHhzmOQeSAy4EZ0X01Hpi')

# Set your OpenAI API key

# Use the create method with an empty prompt to get available engines
response = client.completions.create(prompt="", n=1, stop=None)

# Print the available engines
for choice in response.choices:
    print("Engine ID:", choice['model'])
    print("Engine Name:", choice['model'])
    print("-------------")
