#! /usr/bin/evn python3

def spam():
    bacon()

def bacon():
    raise Exception('これはエラーメッセージです')

spam()
