#!/usr/bin/python3
words=input('Enter words separated by comma: ').split(',')

words.sort()
print(','.join(words))