import urllib2
import json
import string
key = '6d8888bcbd64042978374e8dc9c9069e'
def run_query(city):

	api_key= key
	new_city=city.replace(' ','-')
	url='http://api.openweathermap.org/data/2.5/forecast/city?units=metric&APPID='
	final_url=url + api_key + '&q=' + new_city
	json_obj=urllib2.urlopen(final_url)
	data = json.load(json_obj)
	d=data['list']
	f=d[0]
	data_list=[]
	data_list.append('city_name : ' + data['city']['name'])
	data_list.append('description : ' + f['weather'][0]['description'])
	for k,v in f['main'].iteritems():
		st=str(k)+' : '+str(v)
		data_list.append(st)
	print data['city']['name']
	return data_list