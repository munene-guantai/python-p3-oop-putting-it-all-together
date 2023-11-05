#!/usr/bin/env python3

from book import Book

import io
import sys
import pytest

class TestBook:
    '''Book in book.py'''

    def test_has_title_and_page_count(self):
        '''has the title and page_count passed into __init__, and values can be set to new instance.'''
        book = Book("And Then There Were None", 272)
        assert book._page_count == 272
        assert(book.title == "And Then There Were None")

    def test_requires_int_page_count(self):
        '''prints "page_count must be an integer" if page_count is not an integer.'''
        book = Book("And Then There Were None", 272)

        with pytest.raises(ValueError) as exc_info:
            book.set_page_count("not an integer")

        assert "page_count must be an integer" in str(exc_info.value)

    def test_can_turn_page(self):
        '''outputs "Flipping the page...wow, you read fast!" when method turn_page() is called'''
        book = Book("The World According to Garp", 69)
        captured_out = io.StringIO()
        sys.stdout = captured_out
        book.turn_page()
        sys.stdout = sys.__stdout__
        assert(captured_out.getvalue() == "Flipping the page...wow, you read fast!\n")
