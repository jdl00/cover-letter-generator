import openai

from json import load


class ApiHandler():
    def __init__(self, key_path, job_desc, cv):
        self.__key_path = key_path
        self.__setup_openai_key()

        self.__job_desc = job_desc
        self.__cv = cv

    def __setup_openai_key(self):

        key = None
        with open(self.__key_path, 'r') as key_file:
            json = load(key_file)
            key = json["OPENAI_API_KEY"]

        openai.api_key = key

    def generate_prompt(self):
        prompt = f"Generate me a cover letter using the following job description: {self.__job_desc}.\n"
        prompt += f"Using the information from my CV: {self.__cv}."

        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=1000,
            n=1,
            stop=None,
            temperature=1.0,
        )

        print(response.choices[0].text.strip())
