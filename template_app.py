from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, request, redirect
import logging

app = Flask(__name__)

@app.route("/whatsapp", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""

    # Start our TwiML response
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)

    # create response object
    resp = MessagingResponse()

    # Add your response logic here to send a message, here it's just "hello world"
    resp.message("hello world!")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)