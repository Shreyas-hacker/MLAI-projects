# import statements
from configparser import InterpolationSyntaxError
import random
import json
import pickle
from matplotlib.font_manager import json_dump
import numpy as np
import nltk
nltk.download('punkt')
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.optimizers import SGD

#actual code
lemmatizer = WordNetLemmatizer
intents = json.loads(open('Chat bot/intents.json').read())

words = []
classes = []
documents = []
ignore_letters = ['?','!','.',',']

for intent in intents['intents']: #list of dictionaries
    for pattern in intent['patterns']:
        word_list = nltk.word_tokenize(pattern)
        words.append(word_list)
        documents.append((word_list,intent['tag']))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

print(words)
print(documents)