import openai

def summarize_reviews(api_key, full_prompt, engine="text-davinci-003", temperature=0.6, max_tokens=200):
    """
    Use OpenAI's GPT-3 to summarize reviews based on the provided full prompt.

    Parameters:
    - api_key (str): The OpenAI API key.
    - full_prompt (str): The full prompt including the reviews.
    - engine (str): The OpenAI GPT-3 engine to use.
    - temperature (float): Sampling temperature.
    - max_tokens (int): Maximum length of the output.

    Returns:
    - str: Summarized text
    """
    openai.api_key = api_key

    # Send the completion request to OpenAI API
    response = openai.Completion.create(
        engine=engine,
        prompt=full_prompt,
        temperature=temperature,
        max_tokens=max_tokens
    )
    
    return response.choices[0].text.strip()
