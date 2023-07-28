# Project: Automatic Cover Letter Generation with ChatGPT

## Table of Contents

1. [Description](#Description)
2. [Installation](#Installation)
3. [Usage](#Usage)
4. [Limitations](#Limitations)
5. [Contributing](#Contributing)
6. [License](#License)

## Description

This project leverages the capabilities of ChatGPT to generate custom cover letters based on job descriptions and a parsed CV. This is performed by first fetching the job description, parsing the CV text, and then feeding these inputs into the ChatGPT API call.

### Features

- Automatically fetch and parse job descriptions
- CV parsing to extract relevant skills, experiences, and personal details
- Integration with ChatGPT API to generate personalized and unique cover letters

## Installation

Before you begin, ensure you have met the following requirements:

- You have a working Python environment (Python 3.6 or higher is required)
- You have installed the necessary dependencies in `requirements.txt` file
- You have an OpenAI account and access to the GPT API

Clone the project using the following command:
`git clone https://github.com/your-username/cover-letter-generator.git`

## Usage

You can start using the application with the following command:

1. Copy the cv to be parsed to `resources/c`.
2. Generate the Open AI API key using the command.
   `python generate_api_key.py`
3. Start main.py using `python main.py`

## Limitations

There are currently some limitations including:

- Website scraper currently only works on LinkedIn
- Pdf parser struggles with some cv's formatting

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Please make sure to update tests as appropriate.

## License

This project uses the following license: [MIT License](https://opensource.org/licenses/MIT).
