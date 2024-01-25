import os
from transformers import pipeline, set_seed
from dotenv import load_dotenv

# Load Hugging Face API token from .env file for security reasons
load_dotenv()
huggingface_token = os.getenv('HUGGINGFACE_TOKEN')

# Validate that the Hugging Face API token is loaded
if not huggingface_token:
    raise ValueError("Hugging Face API token not found. Please store it in a .env file.")

# Initialize the pipelines for various tasks
# Xenova/gpt-3.5-turbo for text generation
generator = pipeline('text-generation', model='Xenova/gpt-3.5-turbo', use_auth_token=huggingface_token)
# Sentiment analysis pipeline for understanding the emotional tone of the interpretation
sentiment_analyzer = pipeline('sentiment-analysis')
# Named entity recognition pipeline for identifying entities in the metaphor interpretation
ner = pipeline('ner')

set_seed(42)  # Set seed for reproducibility

def interpret_metaphor(metaphor):
    """
    Function to interpret a nominal metaphor using advanced NLP techniques.
    
    Args:
    metaphor (str): The metaphor in the format 'X is Y'.
    
    Returns:
    dict: The model's interpretation, sentiment analysis, and named entities recognized.
    """
    # Generate a detailed interpretation of the metaphor
    prompt = f"Explain the metaphor: '{metaphor}' in a detailed and insightful manner."
    interpretation = generator(prompt, max_length=100, num_return_sequences=1)[0]['generated_text']
    
    # Perform sentiment analysis on the generated interpretation
    sentiment = sentiment_analyzer(interpretation)
    
    # Perform named entity recognition on the generated interpretation
    entities = ner(interpretation)
    
    # Consolidate results into a single dictionary
    results = {
        'interpretation': interpretation,
        'sentiment': sentiment,
        'named_entities': entities
    }
    
    return results

# Example usage of the function with a sample metaphor
sample_metaphor = "a door is a beginning"
results = interpret_metaphor(sample_metaphor)

# Print the detailed results
print("Interpretation:")
print(results['interpretation'])
print("\nSentiment Analysis:")
print(results['sentiment'])
print("\nNamed Entities Recognized:")
for entity in results['named_entities']:
    print(f" - {entity['word']}, Type: {entity['entity']}")

