#!/usr/bin/env python3

class MyString:
    def __init__(self, value=""):
        if isinstance(value, str):
            self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if isinstance(value, str):
            self._value = value
        else:
            print("The value must be a string.")

    def is_sentence(self):
        return self.value.endswith('.')
        
    def is_question(self):
        return self.value.endswith('?')
    
    def is_exclamation(self):
        return self.value.endswith('!')
    
    def count_sentences(self):
        count = 0
        i = 0
        while i < len(self.value):
            if self.value[i] in '.!?':
                count += 1
                # ignorer les ponctuations répétées
                while i + 1 < len(self.value) and self.value[i + 1] in '.!?':
                    i += 1
            i += 1
        return count