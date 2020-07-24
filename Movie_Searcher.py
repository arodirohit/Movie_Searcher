# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 12:27:55 2019

@author: Rohit Arodi
"""
import json
import urllib
import pprint
from PIL import Image
import requests
from io import BytesIO

pp = pprint.PrettyPrinter(indent=4)

#create the movie name (we need to replace space with "+" as seperator)
moviename = input("Enter the movie name\n")
moviename = "+".join(moviename.split() )

#api key is different for every person
apikey = '1b081533abc0d7833b0861183cb3f1b9'
url = 'https://api.themoviedb.org/3/search/movie?api_key='+apikey+'&query='+moviename
data = urllib.request.urlopen(url).read()

response = json.loads(data)
pp.pprint(response['results'][0])

#working with the image...we take the data from the json parse and pass it to the image url
image_path=response['results'][0]['poster_path']
image_url = 'https://image.tmdb.org/t/p/w500'+image_path
response = requests.get(image_url)
img = Image.open(BytesIO(response.content))
img.show()
