#!/usr/bin/env python3
import io
import sys
import pytest

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self._page_count = page_count

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")


    def set_page_count(self, new_page_count):
        if not isinstance(new_page_count, int) or new_page_count < 0:
            raise ValueError("page_count must be an integer")




pass
    
        