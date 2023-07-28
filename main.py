import os

from helpers.cv_parser import CvParser
from helpers.job_description_scraper import JobDescriptionScraper
from helpers.api_handler import ApiHandler


class CoverLetterGenerator():
    """Main cover letter generator.

    Raises:
        Exception: The cv files cannot be found.
        Exception: The Open AI key cannot be located.
    """

    CONST_CV_PATH = os.path.abspath(os.path.join("resources", "cv"))
    CONST_KEY_PATH = os.path.abspath(os.path.join("resources", "key"))
    CONST_EXIT_KEY = 'e'

    def __init__(self):
        """Creates an instance of the main application
        """
        self.__setup_cv_names()
        self.__setup_api_key()

    def __setup_cv_names(self):
        """Looks for the cv files.

        Raises:
            Exception: The Open AI key cannot be located.
        """
        self.__cvs = [file.name for file in os.scandir(self.CONST_CV_PATH)]
        if not self.__cvs:
            raise Exception("Failed to locate any cv files.")

    def __setup_api_key(self):
        """Sets up the API keys.

        Raises:
            Exception: The key file could not be located.
        """
        keys = [file.name for file in os.scandir(self.CONST_KEY_PATH)]
        if not keys or len(keys) > 1:
            raise Exception("Failed to locate any key file.")
        self.__api_key_path = os.path.join(self.CONST_KEY_PATH, keys[0])

    def __choice_selection(self):
        """Selects the choice of cv to use.

        Returns:
            int: The chosen cv index to be used.
        """
        selected = None
        while True:
            selected = input()
            try:
                selected = int(selected)
                if (selected >= 0 and
                        selected <= len(self.__cvs) - 1):
                    return selected
                print("Selected option is not in valid range.")
            except ValueError:
                print("selected was not a number.")

    def __main(self):
        """Main function to be called responsible for program execution.

        Returns:
            boolean: Whether the program should exit.
        """
        start_option = input("Press 'e' to exit. Enter to continue.\n")
        if start_option.lower() == 'e':
            return True

        print("Located CVs: Select an option")
        for idx, name in enumerate(self.__cvs):
            print(f"{idx}: {name.split('.')[0]}")

        selected_cv = self.__cvs[self.__choice_selection()]
        cv_path = os.path.join(self.CONST_CV_PATH, selected_cv)

        cv_parser = CvParser(cv_path)
        parsed_cv = cv_parser.parse()
        print(parsed_cv)

        job_url = input("Enter the job url.")
        job_desc_scraper = JobDescriptionScraper(job_url)
        job_desc = job_desc_scraper.get_description()
        print(job_desc)

        openai_api = ApiHandler(self.__api_key_path, job_desc, parsed_cv)
        openai_api.generate_prompt()

    def main(self):
        """Wrapper for the main function.
        """
        exit = False
        while True:
            exit = self.__main()

            if exit:
                break


if __name__ == "__main__":
    cover_letter_generator = CoverLetterGenerator()
    cover_letter_generator.main()
