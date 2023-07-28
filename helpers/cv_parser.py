from PyPDF2 import PdfReader


class CvParser():
    """Class that parses the cv and returns the text.
    """

    def __init__(self, file_name):
        """Creates an instance of the parser.

        Args:
            file_name (str): The CV to be parsed.
        """
        self.__file_name = file_name

    def parse(self):
        """Parse and return the text.

        Returns:
            str: The parsed cv.
        """

        text = ""
        with open(self.__file_name, 'rb') as pdf_file_obj:
            pdf_reader = PdfReader(pdf_file_obj)
            for page in pdf_reader.pages:
                text += page.extract_text()
        return text
