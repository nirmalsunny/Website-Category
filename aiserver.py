from functools import wraps
from flask import Flask
from flask import request, Response
from subprocess import call
from flask import render_template
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import random
from sklearn.feature_extraction.text import TfidfVectorizer
import sys
import os
from sklearn.linear_model import LogisticRegression

import math
import json
from collections import Counter

from pathlib import Path

mitphish = Flask(__name__)


def entropy(s):
	p, lns = Counter(s), float(len(s))
	return -sum(count / lns * math.log(count / lns, 2) for count in p.values())


def getTokens(input):
	tokensBySlash = str(input.encode('utf-8')).split('/')  # get tokens after splitting by slash
	allTokens = []
	for i in tokensBySlash:
		tokens = str(i).split('-')  # get tokens after splitting by dash
		tokensByDot = []
		for j in range(0, len(tokens)):
			tempTokens = str(tokens[j]).split('.')  # get tokens after splitting by dot
			tokensByDot = tokensByDot + tempTokens
		allTokens = allTokens + tokens + tokensByDot
	allTokens = list(set(allTokens))  # remove redundant tokens
	# if 'com' in allTokens:
	#    allTokens.remove(
	 #       'com')  # removing .com since it occurs a lot of times and it should not be included in our features
	return allTokens



def TL():
	allurls = Path("data.csv")  # path to our all urls file
	allurlscsv = pd.read_csv(allurls, ',', error_bad_lines=False)  # reading file
	allurlsdata = pd.DataFrame(allurlscsv)  # converting to a dataframe
	allurlsdata = np.array(allurlsdata)  # converting it into an array
	random.shuffle(allurlsdata)  # shuffling
	# print(allurlsdata)
	y = [d[1] for d in allurlsdata]  # all labels
	corpus = [d[0] for d in allurlsdata]  # all urls corresponding to a label (either good or bad)
	vectorizer = TfidfVectorizer(tokenizer=getTokens)
	x = vectorizer.fit_transform(corpus)  # get the X vector

	x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)  # split into training and testing set 80/20 ratio

	lgs = LogisticRegression(solver='liblinear', random_state=42, max_iter=120)  # using logistic regression
	lgs.fit(x_train, y_train)
	print(lgs.score(x_test, y_test))  # pring the score. It comes out to be 98%
	return vectorizer, lgs


@mitphish.route('/')
def homepage():
	return "MitPhish"


@mitphish.route('/test/<path:path>')
def show_index(path):
	X_predict = []
	X_predict.append(str(path))
	vectoriser, lggs = TL()
	X_predict = vectoriser.transform(X_predict)
	y_Predict = lggs.predict(X_predict)
	if str(y_Predict) == "['good']":
		decision = "good"
	else:
		decision = "bad"
	data = {'url': path, 'decision': decision, 'entropy': str(entropy(path))}
	return json.dumps(data, indent=4)


port = int(os.environ.get('PORT', 5000))
if __name__ == "__main__":
	mitphish.run(debug=True, threaded=True, port=port)

# vectorizer, lgs  = TL()
# checking some random URLs. The results come out to be expected. The first two are okay and the last four are malicious/phishing/bad

# X_predict = ['wikipedia.com','google.com/search=something','pakistanifacebookforever.com/getpassword.php/','www.radsport-voggel.de/wp-admin/includes/log.exe','ahrenhei.without-transfer.ru/nethost.exe','www.itidea.it/centroesteticosothys/img/_notes/gum.exe']

# X_predict = vectorizer.transform(X_predict)

# y_Predict = lgs.predict(X_predict)

# print(y_Predict)	#printing predicted values
