
# OpenAI Chat Script

A simple Python script that allows you to have a one-time conversation with OpenAI's GPT-3.5-turbo model. The script sends your input to the AI and displays the response along with token usage statistics.

## Features

- Single-turn conversation with OpenAI's GPT-3.5-turbo
- Displays AI response
- Shows detailed token usage (prompt, completion, and total tokens)
- Uses environment variables for secure API key management

## What the Script Does

The script:
1. Loads your OpenAI API key from environment variables
2. Prompts you to enter a question
3. Sends your question to OpenAI's GPT-3.5-turbo model
4. Displays the AI's response
5. Shows token usage statistics for the conversation

## Prerequisites

- Python 3.7 or higher
- OpenAI API key

## Installation

1. **Clone or download the script** to your local machine

2. **Install required dependencies:**
   ```bash
   pip install openai python-dotenv
   ```

3. **Set up your OpenAI API key:**
   
   **Option A: Using .env file (Recommended)**
   - Create a `.env` file in the same directory as your script
   - Add your OpenAI API key:
     ```
     OPENAI_API_KEY=your_api_key_here
     ```
   
   **Option B: Using environment variable**
   - Set the environment variable directly:
     ```bash
     # Windows
     set OPENAI_API_KEY=your_api_key_here
     
     # macOS/Linux
     export OPENAI_API_KEY=your_api_key_here
     ```

## Getting an OpenAI API Key

1. Go to [OpenAI's website](https://platform.openai.com/)
2. Sign up or log in to your account
3. Navigate to the API section
4. Create a new API key
5. Copy the key and use it in your `.env` file or environment variable

## Usage

1. **Run the script:**
   ```bash
   python your_script_name.py
   ```

2. **Enter your question** when prompted

3. **View the response** and token usage statistics

## Example Output

```
🔹 Chat with OpenAI 🔹

👉 Enter your question: What is the capital of France?

=== Assistant Reply ===

The capital of France is Paris.

=== Token Usage ===
Prompt Tokens     : 15
Completion Tokens : 8
Total Tokens      : 23
```

## Dependencies

- `openai` - Official OpenAI Python client library
- `python-dotenv` - For loading environment variables from .env file

## Security Notes

- Never commit your `.env` file to version control
- Keep your OpenAI API key secure and don't share it publicly
- Consider adding `.env` to your `.gitignore` file if using git

## Troubleshooting

**"No module named 'openai'" error:**
- Make sure you've installed the dependencies: `pip install openai python-dotenv`

**"API key not found" error:**
- Verify your `.env` file is in the correct directory
- Check that your API key is correctly formatted in the `.env` file
- Ensure there are no extra spaces around the API key

**"Invalid API key" error:**
- Verify your API key is correct and active
- Check that you have sufficient credits in your OpenAI account

## Cost Considerations

This script uses OpenAI's paid API. Each request will consume tokens based on:
- Input length (your question)
- Output length (AI response)
- Model used (GPT-3.5-turbo)

Monitor your usage on the OpenAI dashboard to avoid unexpected charges.
