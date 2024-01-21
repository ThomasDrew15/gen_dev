from openai import OpenAI

client = OpenAI(api_key='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')

# Set your OpenAI API key

def generate_joke(prompt):
    try:
        response = client.completions.create(
            model="gpt-3.5-turbo-instruct",
            prompt=prompt,
            max_tokens=100)

        return response.choices[0].text.strip()

    except Exception as e:
        print(f"Error generating joke with GPT-3: {e}")
        return None

# Example usage
prompt = "Tell me a joke:"
joke = generate_joke(prompt)

if joke:
    print("Generated Joke:", joke)
