from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from .preprocess import *
from .classify import *
from .Scraper import *
from keras.models import load_model

#build the model (initlize the model)
model = build_model()


# home request
def home(request):
	return render_to_response('index.html')



# show all the reviews
def show_reviews(request):
	review_page_link = request.GET.get("review_page_link","")
	preprocess = PreProcess(review_page_link)
	preprocess.process()
	return HttpResponse(preprocess.reviews)



# classify
def classification(request):
	review_page_link = request.GET.get("review_page_link","")
	preprocess = PreProcess(review_page_link)
	preprocess.process()

	vectorized_reviews = preprocess.return_vectorized_reviews()
	print (vectorized_reviews)
	if preprocess.is_applicable: # Should be in the shape (*,100)
		results = get_results(model, vectorized_reviews)
		pos = results['pos']
		neg = results['neg']
		analysis = results['analysis']
		if results:
			return render_to_response("classification.html", {"pos":pos, "neg":neg, "analysis":analysis, "count":preprocess.count, "name":preprocess.name, "review_page_link":review_page_link})
		else:
			return HttpResponse("Error in processing! Try again")
	else:
		return HttpResponse("Insufficient number of review! Please try another professor.")
		return HttpResponseRedirect("/")

	
	