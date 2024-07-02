import PyPDF2
import sys
import os

for file in os.listdir(os.curdir):
    if file.endswith('.pdf'):
        print(file)