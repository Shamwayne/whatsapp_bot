from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, request, redirect, session, flash, render_template

import logging
import chatbot

app = Flask(__name__)


@app.route('/login')
def login():
	return render_template('login.html')


@app.errorhandler(401)
def page_not_found(e):
	flash("Authentication Error: Failed to Login")
	return redirect(url_for('login'))


@app.errorhandler(500)
def internal_server_error(e):
	flash("Seems like an error occured", "danger")
	return render_template('errors/500.html')


@app.route('/forgot_password')
def forgot_password():
    return render_template('forgot_password.html')


@app.route("/whatsapp", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""

    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)

    # reply using our AIML chatbot
    ai_response = chatbot.reply_message(body) 

    # Start our TwiML response
    resp = MessagingResponse()

    # Add a message
    resp.message(ai_response)

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True, threaded=True)