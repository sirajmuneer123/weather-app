from django.shortcuts import render
from weatherApp.weather_search import run_query

# Create your views here.
from django.http import HttpResponse
import json
def index(request):

    result_list = []

    if request.method == 'POST':
    	#query = request.POST.get('query', False)
        query = request.POST['query'].strip()
        #print 'hello............................................'+query
        if query:
            # Run our Bing function to get the results list!
            result_list = run_query(query)
            return HttpResponse(json.dumps({'result_list': result_list}))

    return render(request, 'weatherApp/index.html', {'result_list': result_list})