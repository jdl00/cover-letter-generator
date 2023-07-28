from requests import get
from bs4 import BeautifulSoup
from re import sub


class JobDescriptionScraper():
    """Class that scrapes the linkedin job posting for the descriptions
    """

    # Constants used by the scraper
    CONST_PARSER = 'html.parser'

    # These constants will have to be updated if linkedIns' format changes
    CONST_ELEMENT = "div"
    CONST_DIV_CLASS = {
        "class": (
            "show-more-less-html__markup "
            "show-more-less-html__markup--clamp-after-5 "
            "relative overflow-hidden"
        )
    }

    def __init__(self, job_url):
        """Generates an instance of the scraper

        Args:
            job_url (str): The url string (must contain http/s prefix)
        """
        self.__job_url = job_url

    def get_description(self):
        """Scrapes the website for the job description."""

        # Gets the pages html
        page = get(self.__job_url)
        if page.status_code != 200:
            assert False, "Failed to get URL"

        # Initialises and parses the html
        soup = BeautifulSoup(page.content, self.CONST_PARSER)
        results = soup.find(self.CONST_ELEMENT, self.CONST_DIV_CLASS)
        if not results:
            assert False, "Failed to find the id"

        # Remove the html and apply regex to just get the words
        job_description = results.get_text(separator="\n")
        return sub(r'\W+', ' ', job_description)


''' EXAMPLE USAGE OF CLASS
# Initialises the scraper.
job_desc_scraper = JobDescriptionScraper(
    "https://www.linkedin.com/jobs/view/3670702809")

# Scrapes and gets the job description.
job_description = job_desc_scraper.get_description()
'''
