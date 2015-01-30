import translator
import createHTMLpage
import time
import webbrowser

def main(text, url, senderID):
	images = translator.textToImages(text)

	htmlString = createHTMLpage.createHTMLstring(images,text)
	createHTMLpage.createHTML(htmlString, url, senderID)