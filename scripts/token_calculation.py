import pandas as pd

# Function to estimate the number of tokens in a given text
def calculate_tokens(text):
    return len(text.split()) + text.count('.') + text.count(',') + text.count('!') + text.count('?')

# Function to split the dataframe into smaller chunks
def split_dataframe(df, text_column, max_tokens):
    chunks = []
    current_chunk = []
    current_token_count = 0
    
    for _, row in df.iterrows():
        review = row[text_column]
        tokens = calculate_tokens(review)
        
        if current_token_count + tokens <= max_tokens:
            current_chunk.append(row)
            current_token_count += tokens
        else:
            chunks.append(pd.DataFrame(current_chunk))
            current_chunk = [row]
            current_token_count = tokens

    if current_chunk:
        chunks.append(pd.DataFrame(current_chunk))

    return chunks

# Main function to check and split the DataFrame
def check_and_split_dataframe(df, column_name, prompt_length, max_tokens_for_completion):
    # Reduce the maximum tokens per chunk to provide a buffer
    buffer = 1150  # You can adjust this buffer
    max_context_length = 4097 - prompt_length - max_tokens_for_completion - buffer
    
    if calculate_tokens(' '.join(df[column_name])) > max_context_length:
        return split_dataframe(df, column_name, max_context_length)
    else:
        return [df]

# Example usage
# prompt_length = len("Your prompt template".format(reviews=''))
# max_tokens_for_completion = 200
# chunks = check_and_split_dataframe(df, 'text_column', prompt_length, max_tokens_for_completion)


# Example usage:
# Assuming 'df' is your DataFrame and 'text_column' is the name of the column to check
# prompt_length = len("Your prompt template here".format(reviews=''))
# max_tokens_for_completion = 200  # Set this based on your specific needs
# chunks = check_and_split_dataframe(df, 'text_column', prompt_length, max_tokens_for_completion)


# Example usage, assuming 'my_dataframe' is your DataFrame and 'column_to_check' is the name of the column to check:
# Replace 'prompt_length' with the actual length of your prompt
# prompt_length = len("Analyze the reviews and provide a summary and a list of the top 5 praised aspects or features: ")
# max_tokens_for_completion = 200  # Adjust according to your completion settings
# chunks = check_and_split_dataframe(my_dataframe, column_to_check, prompt_length, max_tokens_for_completion)

# Output the result and number of tokens for each chunk
# for i, chunk in enumerate(chunks):
#     print(f"Chunk {i+1} (size: {len(chunk)} rows):")
#     print(chunk.head(), '\n')  # Print the first few rows of the chunk
#     num_tokens = calculate_tokens(' '.join(chunk[column_to_check]))
#     print(f"Number of tokens in chunk {i+1}: {num_tokens}\n")
