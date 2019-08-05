# preprocess data


from sklearn.svm import SVC
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from keras.models import load_model
from .Scraper import *


class PreProcess:
	def __init__(self, url):
		self.url = url


	def process(self):
		scraper = Scraper(self.url)
		self.reviews = scraper.get_reviews()
		self.data = scraper.get_data()
		self.count = scraper.get_count()
		self.name = scraper.get_name()
		self.is_applicable = scraper.is_applicable() # check is reviews compatiable

	def return_vectorized_reviews(self):
		# performing vectorizer
		vectorizer = CountVectorizer(stop_words=("english"),max_features=100) # to convert the main reviews into a matrix of shape[1]=100
		tfvect = TfidfVectorizer(stop_words="english", max_features=100)

		vect_r = vectorizer.fit_transform(self.reviews)
		return vect_r
