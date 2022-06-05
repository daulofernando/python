#!/usr/bin/env python3
"""Hello world em varios idiomas :) 

Esse script exibe um hello world em diferentes idiomas na tela! 

"""
__version__ = "0.1"
__author__ = "daulo"
__license__ = "Unlicense"

import os

current_lang = os.getenv("LANG","en_US")[:5]

msg = "Hello, World!"

if (current_lang == "pt_BR"):
    msg = "Olá, Mundo!"
elif (current_lang == "it_IT"):
    msg = "Ciao, Mondo!"
    
print(msg)