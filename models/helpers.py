import os
from datetime import datetime
from passlib.hash import pbkdf2_sha256
from db import Chats, db_session
from jinja2 import Template


def export_to_aiml():
    """ converts the rows in the table into an aiml dataset """

    aiml_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'template.aiml')
    aiml_data = open(aiml_file, 'r').read()
    template = Template(aiml_data)
    all_chats = db_session.query(Chats).all()
    generated_template = template.stream(chats=all_chats).dump('chat-data.aiml')