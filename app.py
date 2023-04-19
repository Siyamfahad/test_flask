from flask import Flask, request, redirect
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)

@app.route("/twilio", methods=['GET', 'POST'])
def twilio():
    resp = VoiceResponse()
    resp.say("Welcome, Dear Brother. Please say Good Morning.")
    with resp.gather(numDigits=1, action="/process-response") as gather:
        gather.say("Press 1 for Good Morning.")
    return str(resp)

@app.route("/process-response", methods=['GET', 'POST'])
def process_response():
    digit_pressed = request.values.get('Digits', None)
    if digit_pressed == '1':
        resp = VoiceResponse()
        resp.say("I am very happy.")
        return str(resp)
    else:
        return redirect('/twilio')

if __name__ == '__main__':
    app.run(debug=False)
