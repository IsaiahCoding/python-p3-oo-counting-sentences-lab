#!/usr/bin/env python3

class MyString:
  def __init__(self, value = ""):
    self.value = value
    
  @property
  def value(self):
    return self._value
  @value.setter
  def value(self, str_value):
    if isinstance(str_value, str):
      self._value = str_value
    else: print("The value must be a string.")
    
  def is_sentence(self):
    return self._value.endswith(".")
  def is_question(self):
    return self._value.endswith("?")
  def is_exclamation(self):
    return self._value.endswith("!")
  def count_sentences(self):
    value = self.value
    for punc in ["?", "!"]:
      value = value.replace(punc, ".")
    sentences = [letter for letter in value.split(".")if letter]
    return len(sentences)
  
  pass
