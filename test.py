#-*-coding:utf-8 -*-
import pandas as pd
import numpy as np
import re

from nltk.stem.wordnet import WordNetLemmatizer
lem = WordNetLemmatizer()

word='conducive to'
print(lem.lemmatize(word,"v"))


