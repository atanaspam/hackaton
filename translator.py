import urllib2
import simplejson
import time

def getImage(word):
	url = ('https://ajax.googleapis.com/ajax/services/search/images?' +
			'v=1.0&q='+ word +'&userip=INSERT-USER-IP&start=0')

	request = urllib2.Request(url, None, {'Referer': 'google.com'})
	response = urllib2.urlopen(request)

	results = simplejson.load(response)
	return results["responseData"]["results"][0]["url"]

def textToImages(text):
	wordsDict = {}
	textArr = text.split()

	for i in range(0, len(textArr)):
		if not textArr[i] in wordsDict:
			wordsDict[textArr[i]] = getImage(textArr[i])
		textArr[i] = wordsDict[textArr[i]]

	return textArr