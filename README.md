# Prompt Engineering Agent

A sophisticated AI-powered tool designed to help users craft better and more effective prompts for large language models. This application provides an interactive interface for prompt optimization and refinement.

## Features

- Interactive web interface powered by Gradio
- Real-time prompt analysis and suggestions
- Integration with OpenAI's powerful language models
- User-friendly prompt editing and refinement tools
- Instant feedback on prompt quality and effectiveness

## Prerequisites

- Python 3.7 or higher
- OpenAI API key
- Internet connection

## Installation

1. Clone the repository:
```bash
git clone https://github.com/erminhurem/Prompt-engineering-agent.git
cd Prompt-engineering-agent
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Configuration

1. Create a `.env` file in the root directory of the project
2. Add your OpenAI API key to the `.env` file:
```
OPENAI_API_KEY="your_api_key_here"
```

> ⚠️ **Important**: Never commit your `.env` file or expose your API key publicly.

## Usage

1. Start the application:
```bash
python app.py
```

2. Open your web browser and navigate to the local address shown in the terminal (typically http://localhost:7860)

3. Enter your prompt in the input field and use the various tools available to refine and improve it

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

If you encounter any problems or have questions, please open an issue in the repository.

## Acknowledgments

- Built with [Gradio](https://www.gradio.app/)
- Powered by [OpenAI](https://openai.com/) language models
