import os
from transformers import pipeline, set_seed
from dotenv import load_dotenv

# Load Hugging Face API token from .env file for security reasons
load_dotenv()
huggingface_token = os.getenv('HUGGINGFACE_TOKEN')

# Validate that the Hugging Face API token is loaded
if not huggingface_token:
    raise ValueError("Hugging Face API token not found. Please store it in a .env file.")

# Initialize the Xenova/gpt-3.5-turbo model from Hugging Face
# We use the 'text-generation' pipeline for generating text based on the input metaphor.
generator = pipeline('text-generation', model='Xenova/gpt-3.5-turbo', use_auth_token=huggingface_token)
set_seed(42)  # Set seed for reproducibility

def interpret_metaphor(metaphor):
    """
    Function to interpret a nominal metaphor using the Xenova/gpt-3.5-turbo model.
    
    Args:
    metaphor (str): The metaphor in the format 'X is Y'.
    
    Returns:
    str: The model's interpretation or explanation of the metaphor.
    """
    # Create a prompt for the model to generate text based on the metaphor
    prompt = f"Explain the metaphor: '{metaphor}' in a detailed and insightful manner."
    
    # Generate a response from the model based on the prompt
    response = generator(prompt, max_length=100, num_return_sequences=1)
    
    # Return the generated text as the model's interpretation of the metaphor
    return response[0]['generated_text']

# Example usage of the function with a sample metaphor
sample_metaphor = "a door is a beginning"
interpretation = interpret_metaphor(sample_metaphor)

# Print the model's interpretation of the metaphor
print(interpretation)
