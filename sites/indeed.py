# headline_selector = 'span[class="company"]'
# headline_selector = 'div > span'
headline_selector = 'h2 > a'

url = 'https://www.indeed.ca/jobs?q=developer&l=Vancouver%2C+BC'


def get_headline_url(element):
    return 'https://ca.indeed.com' + element.attrs['href']
