#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 11:08:25 2021

@author: cerivera
"""
# Trabajo realizado por Carlos ELías Rivera Mercado: A01656451
# y por Andrés Eugenio Martínez Sánchez: A01656442

class VigenereCipher():

    def __init__(self, key):
        self.alphabet = 'abcdefghijklmnopqrstuvwxyz'
        self.key = key

    def onEncrypt(self, plaintext):
        ciphertext = ''
        counter = 0
        for char in plaintext:
            if(char.lower() in self.alphabet): # exist in dictionary
                char_key = self.key[counter % len(self.key)]
                pos_key = self.alphabet.index(char_key.lower())
                new_index = (self.alphabet.index(char.lower()) + pos_key) % len(self.alphabet)
                new_char =  self.alphabet[new_index].upper() if char.isupper() else  self.alphabet[new_index]
                ciphertext+=new_char
                counter+=1
            else:
                ciphertext+=char
        return ciphertext

    def onDecrypt(self, ciphertext):
        plaintext = ''
        counter = 0
        for char in ciphertext:
            if(char.lower() in self.alphabet):
                char_key = self.key[counter % len(self.key)]
                pos_key = self.alphabet.index(char_key.lower())
                new_index = (self.alphabet.index(char.lower()) - pos_key) % len(self.alphabet)
                new_char =  self.alphabet[new_index].upper() if char.isupper() else  self.alphabet[new_index]
                plaintext+=new_char
                counter+=1
            else:
                plaintext+=char
        return plaintext