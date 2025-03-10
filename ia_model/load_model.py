import ollama


def get_model_response(prompt):
    response = ollama.chat(model="llama3.1", messages=[{
        "role": "user",
        "content": prompt
    }], options={
        "max_tokens": 400
    })
    return response["message"]["content"]