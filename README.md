# Metaphor_interpreter info

---

# Metaphor Interpreter with NLP techniques

This project demonstrates the use of the `Xenova/gpt-3.5-turbo` model for interpreting nominal metaphors, such as "a door is a beginning". It leverages advanced Natural Language Processing (NLP) techniques including sentiment analysis and named entity recognition to provide a comprehensive understanding of metaphors.

## Features

- **Metaphor Interpretation**: Generates detailed interpretations of nominal metaphors.
- **Sentiment Analysis**: Analyzes the emotional tone of the interpretation (positive, negative, or neutral).
- **Named Entity Recognition**: Identifies and classifies named entities (like persons, organizations, locations, etc.) mentioned in the interpretation.

## Setup

### Prerequisites

- Python 3.x
- Internet connection (for API requests)
- Hugging Face account and API token

### Installation

1. **Clone the repository**:

   ```bash
   git clone <https://github.com/haratimo/MetaphorTaskStep>
   cd <MetaphorTaskStep>
   ```

2. **Set up a virtual environment** (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install required packages**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables**:
   - Store your Hugging Face API token in a `.env` file:
     ```
     HUGGINGFACE_TOKEN=your_hugging_face_api_token_here
     ```

## Usage

Run the script from your command line:

```bash
python metaphor_interpreter.py
```

## Project Structure

- `metaphor_interpreter.py`: Main Python script containing code for metaphor interpretation and advanced NLP techniques.
- `.env`: File containing environment variables (not tracked by Git for security).
- `requirements.txt`: File listing the dependencies for the project.
- `README.md`: This file, containing documentation for the project.

## Contributing

Contributions to improve the project are welcome. Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your_feature`).
3. Commit your changes (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature/your_feature`).
5. Create a new Pull Request.

## License

[MIT License](LICENSE)

---
