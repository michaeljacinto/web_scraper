"""
This module houses a single function used to return a dictionary of text and urls
from a URL

It uses the bs4, and requests packages from PyPI
"""
import requests
import bs4

from typing import Callable
from typing import Dict


def get_element_urls(site_url: str, element_selector: str, get_url: Callable[[bs4.Tag], str]) -> Dict[str, str]:
    """
    This function retrieves specified url and returns a dictionary of the
    content of the elements and an associated URL.

    The page elements are specified using the CSS Selector and the associated
    URL's are determined using the function argument.

    Args:
        site_url:
            this is the page from which to extract the desired element text

        element_selector:
            this is the css selector used to identify the page elements that
            whose text would like to extract

        get_url:
            a function that gets the url related to the passed bs4 tag

    Returns:
        dictionary indexed by element text containing the related urls

    Examples
        >>> get_element_urls('https://www.bcit.ca',
        ...                  '#bcitlogo a span.bcitlogo_wordmark',
        ...                  lambda tag: 'https://www.bcit.ca{}'.format(tag.parent.attrs['href']))
        {'British Columbia Institute of Technology': 'https://www.bcit.ca/'}

    """
    user_agent = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'}

    front_page = requests.get(site_url, headers=user_agent).content
    parseable_page = bs4.BeautifulSoup(front_page, 'html.parser')

    elements = {element.contents[0]: get_url(element)
                for element in parseable_page.select(element_selector)}

    return elements
