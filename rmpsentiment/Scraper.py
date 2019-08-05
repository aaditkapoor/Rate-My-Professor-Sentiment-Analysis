"""
        Scraper class for RMP Sentiment Analysis
        scrapes the required web page to get informative queries.
"""

import os
import requests
import json
from bs4 import BeautifulSoup


class Scraper():


        """
                Intializes the scraper with the url.
        """

        def __init__(self, review_page_link): # should be exact url
                self.review_page_link = review_page_link
                resp = requests.get(review_page_link)
                if resp.status_code == 200:
                        self.content = resp.content
                        self.bsoup = BeautifulSoup(self.content,features="html.parser")

                        # get reviews
                        self.reviews = []
                        for review in self.bsoup.findAll("p", {"class": "commentsParagraph"}):
                                # perform some text preprocessing
                                self.reviews.append(review.getText().strip().lower())


                        self.count = len(self.reviews)
                        # get name
                        self.first_name = self.bsoup.find("span", {"class":"pfname"}).getText().strip()
                        self.last_name = self.bsoup.find("span", {"class":"plname"}).getText().strip()

                        print ("Status: ", resp.status_code)
                        print ("Retrieved %d reviews" % self.count)
                        print ("Scraped: ", self.review_page_link)

                else:
                        self.count = None
                        self.content = None
                        self.bsoup = None
                        self.reviews = None
                        self.first_name = None
                        self.last_name = None

        """
                get number of reviews.
        """
        def get_count(self):
                return self.count

        """
                get if reviews sufficient
        """
        def is_applicable(self):
                if self.count >=7:
                        return True
                else:
                        return False


        # check if there are reviews available
        def is_success(self):
                if self.count:
                        return True
                else:
         
                        return False
        # get first name
        def get_first_name(self):
                return self.first_name
        def get_last_name(self):
                return self.last_name
        # concat names
        def get_name(self):
                return self.first_name + " " + self.last_name

        def get_reviews(self):
                return self.reviews

        # return in a specified manner.
        def get_data(self):
        	# data in dict form
        	return {"name":self.get_name(), "count":self.get_count(), "is_success":self.is_success(), "reviews":self.get_reviews()}




