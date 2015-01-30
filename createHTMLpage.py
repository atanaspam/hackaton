def createHTMLstring(imagesArr, text):
	templatePart1 = """
					<html>
					<body>
					"""
	templatePart2 = templatePart1 + '\n' + "<h1>" + text + "</h1>"
	templatePart3 = """
					</body>
					</html>
					"""
	for img in imagesArr:
		templatePart2 += '\n' + "<img src =" + '"' + img + '"' + "width=" + "142" + " height=" + "142" + ">"
	
	return templatePart2 + '\n' + templatePart3

def createHTML(htmlString, url, senderID):
	f = open(url + senderID + ".html", "w")
	f.write(htmlString)