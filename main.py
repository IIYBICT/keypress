# -*- coding:utf-8 -*-
# @Author  : IIYBICT
# @Time      :2025/9/18 21:22
import sys
import time

from pynput import keyboard
from pynput.keyboard import Key


class KeyboardService:
    def __init__(self):
        self.keyboardController = keyboard.Controller()

    def press(self, key):
        try:
            special_key = getattr(Key, key)
            self.keyboardController.press(special_key)
        except AttributeError:
            self.keyboardController.press(key)

    def release(self, key):
        try:
            special_key = getattr(Key, key)
            self.keyboardController.release(special_key)
        except AttributeError:
            self.keyboardController.release(key)

    def type(self, text):
        self.keyboardController.type(text)

if __name__ == '__main__':
    keyboardService = KeyboardService()

    if len(sys.argv) > 1:
        inputType = sys.argv[1]
        inputKey = sys.argv[2]
        if inputType == 'press':
            keyboardService.press(inputKey)
        elif inputType == 'release':
            keyboardService.release(inputKey)
        else:
            print('Invalid type argument')
    else:
        print('Please provide a type argument')


