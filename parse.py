from flask import Flask, request
import simplejson
import main

app = Flask(__name__)
@app.route('/incoming', methods=['POST'])
def form():
    envelope = simplejson.loads(request.form.get('envelope'))
    from_address = envelope['from']
    print from_address
    text = request.form.get('text')
    print text
    main.main(text, "C:/Users/Atanas/Desktop/PythonBackEnd/emails/", from_address)    
    return "OK"
    
    
if __name__ == '__main__':
	app.run()
