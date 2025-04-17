from openai import OpenAI

def extract_structured_data(client: OpenAI, model: str, system_prompt: str, user_prompt: str, temperature: float, max_tokens: int):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=temperature,
        max_tokens=max_tokens,
        response_format={"type": "json_object"} 
    )
    return response.choices[0].message.content, response.usage.total_tokens
