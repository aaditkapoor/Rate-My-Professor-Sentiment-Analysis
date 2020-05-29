# Rate-My-Professor-Sentiment-Analysis
Tired of reading the reviews of each and every professor? We bring you the solution to your problem.  Our aim is to use Machine Learning to classify each review of a particular professor as POSITIVE (1) or NEGATIVE(0).

This is an app that performs sentiment analysis on each review of a given professor and then counts the number of positives and negatives and neutrals to get a tentative classified response.

# How it works?
- A Sentiment Analysis machine learning model was built that is used to classify a certain professor's reviews and then compares the positive and negative reviews to get an analysis. We have used Beautifulsoup4 to scrape the reviews from ratemyprofessors.com, we then perform basic text preprocessing to get the prediction.

# The Model
- The Model was trained and tested on the imdb-reviews dataset achieving an accuracy of 82-85% accuracy on the testing and the training test. We incurred a lot of overfitting in the beginning but after many attempts we developed a resonably good model architecture.

- Model Architecture is given in main.ipynb.

# Requirements
- Python3
- BeautifulSoup4
- Keras (Tensorflow)
- Numpy
- Pandas
- requests
- Django
- Heroku (hosting)

# Try it
- You can try the app at: http://rmpsentiment.herokuapp.com/
Examples: 
- <a href="http://rmpsentiment.herokuapp.com/classify/?review_page_link=https%3A%2F%2Fwww.ratemyprofessors.com%2FShowRatings.jsp%3Ftid%3D221852%26showMyProfs%3Dtrue"> Link 1 </a>
- <a href = "http://rmpsentiment.herokuapp.com/classify/?review_page_link=https%3A%2F%2Fwww.ratemyprofessors.com%2FShowRatings.jsp%3Ftid%3D57992">Link 2</a>

- Feel free to contact me at: aaditkapoor2000@gmail.com

# Future directions
- Make the model better
- Set a database collection system and post it on Kaggle
- Improve the user interface

# More Info
• https://www.linkedin.com/posts/aadit-kapoor-263504143_ratemyprofessorscom-find-and-rate-your-activity-6563942463843733505-Cvnf 

# LICENSE
- See LICENSE.md for more info.

