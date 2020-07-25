headline_company = '[class="topictitle_retailer"]'
headline_selector = '[class="topic_title_link"]'


url = 'https://forums.redflagdeals.com/hot-deals-f9/'


def get_headline_url(element):
    return 'https://forums.redflagdeals.com' + element.attrs['href']
