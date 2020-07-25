"""
This module houses a single function for generating an HTML blog like page
given a nested dictionary of web sites, text, and urls.

This module uses the jinja2 template library to generate the html page. This
module isn't a standard module and needs to be installed from PyPI.
"""

import jinja2
import datetime


def gen_page(content: dict) -> str:
    """
    This function generates an HTML index page given a nested dictionary of web
    sites, text, and urls.

    Args:
        content: a nested set of dictionaries in the form

                content = { 'site1_name': { 'content1_text': 'content1_url',
                                            'content2_text': 'content2_url' },
                            'site2_name': { 'content1_test': 'content1_url',
                                            'content2_text': 'content2_url' } }


    Returns:
        A string containing an HTML page consisting of a set of links based on the
        site names, text, and urls in the content parameter.

    Examples:

        >>> test_content = { 'site_1':
        ...                   { 'site 1 text data 1': 'https://site1.org/data1.html',
        ...                    'site 1 text data 2': 'https://site1.org/data2.html' },
        ...                  'site_2':
        ...                   { 'site 1 text data 1': 'https://site1.org/data1.html',
        ...                     'site 1 text data 2': 'https://site1.org/data2.html' }
        ...                 }
        >>> print(gen_page(test_content)) #doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
        <!DOCTYPE html>
                                 <html lang="en">
                                     <head>
                                         <meta charset="UTF-8">
                                         <title>My News</title>
                                     </head>
                                     <body>
        ...
                                             <h2> site_1 </h2>
                                             <ol>
                                                     <li><a href="https://site1.org/data1.html">site 1 text data 1</a></li>
                                                     <li><a href="https://site1.org/data2.html">site 1 text data 2</a></li>
                                             </ol>
                                             <h2> site_2 </h2>
                                             <ol>
                                                     <li><a href="https://site1.org/data1.html">site 1 text data 1</a></li>
                                                     <li><a href="https://site1.org/data2.html">site 1 text data 2</a></li>
                                             </ol>
                                     </body>
                                 </html>

    """
    page_template = jinja2.Template('<!DOCTYPE html> \n \
                                    <html lang="en"> \n \
                                        <head> \n \
                                            <meta charset="UTF-8"> \n \
                                            <title>My News</title> \n \
                                        </head> \n \
                                        <body> \n \
                                            <h1>My News: {{ date_string }}</h1> \n \
                                            {% for news_source in headlines.keys()  %} \n \
                                                <h2> {{ news_source }} </h2> \n \
                                                <ol> \n \
                                                    {% for headline in headlines[news_source].keys() %} \n \
                                                        <li><a href="{{ headlines[news_source][headline] }}">{{ headline }}</a></li> \n \
                                                    {% endfor %} \n \
                                                </ol> \n \
                                            {% endfor %} \n \
                                        </body> \n \
                                    </html>')

    today_string = datetime.date.today().strftime("%B %d %Y")

    return page_template.render(headlines=content, date_string=today_string)

