import os
from random import choice
import re
from flask import Flask, render_template, request

app = Flask(__name__)


def select_book():
    """
        select a file name from the list of files in the path ./books
    """
    list_of_books = os.listdir('./books')
    book_selected = choice(list_of_books)
    return book_selected


def getquote():
    book_name = select_book()
    path = f'./books/{book_name}'
    file = open(path, 'r')
    lines = file.readlines()
    # select the quote
    titles = [line for line in lines if re.match("##", line)]
    title = choice(titles)
    title_index = titles.index(title)
    # Get the quote until stop title
    quote_start_index = lines.index(title)
    stop_index = title_index + 1
    if stop_index < len(titles):
        stop_title = titles[stop_index]
        quote_stop_index = lines.index(stop_title)
        quote_list = lines[quote_start_index+1:quote_stop_index]
    else:
        quote_list = lines[quote_start_index+1:]
    # return quote
    quote = ""
    for text_line in quote_list:
        quote += text_line
    return book_name, title, quote


@app.route('/')
def index():
    app.logger.info('this is a test')
    book = 'This is the book title'
    quote = 'With supporting text below as a natural lead-in to additional content.'
    app.logger.info(f'this is the method {request.method}')
    book, title, quote = getquote()
    print(f'the book{book} and the quote{quote}')
    return render_template('index.html', book=book, quote=quote, title=title)


if __name__ == '__main__':
    app.debug = True
    app.run()
