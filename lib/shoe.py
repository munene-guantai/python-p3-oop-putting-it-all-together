#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
        self.available = True

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"


    def set_size(self, new_size):
        if not isinstance(new_size, int):
            print("size must be an integer.")
            raise ValueError("size must be an integer")
        else:
            self._size = new_size

    

        
    pass