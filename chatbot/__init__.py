# -*- coding: utf-8 -*-
# Name      : Shamu Shingai
# Reg Number: R157690W
# Program   : CTH
"""
This is a prototype based on the xml retrieval based Artificial Intelligence
Markup Language (AIML) integrated with the Flask framework for web based
customer support help.

The prototype is in part for the feasibility and usability study for my
HCT260 Major Project proposal.

For the full project i will be using the python Natural Language Toolkit and
Patterns module as they provide more capability for understanding and parsing
language into more structured code for more convinient data retrieval
"""
import aiml
import sys

# Create a Kernel object to start up the chatbot
kern = aiml.Kernel()

#load a precompiled "brain" that was created from a previous run
# This speeds up the chatbot initialisation a LOT
brainLoaded = False
forceReload = False

#creates brain if it wasn't before, otherwise loads the saved brain
while not brainLoaded:
	if forceReload or (len(sys.argv) >= 2 and sys.argv[1] == "reload"):
		kern.bootstrap(learnFiles="std-startup.xml", commands="load aiml b")
		brainLoaded = True
		kern.saveBrain("test_ai.brn") #save brain for later runs
	else:
		# Attempt to load the brain file.  If it fails, fall back on the Reload
		# method.
		try:
			# The optional branFile argument specifies a brain file to load.
			kern.bootstrap(brainFile = "test_ai.brn")
			brainLoaded = True
		except:
			forceReload = True

kern.setBotPredicate('master', 'Shingai M Shamu')#sets AIML var </master> to me!
kern.setBotPredicate('name', 'AdamBot')#sets AIML var </master> to me!


def reply_message(message):
	chat_reply = kern.respond(message)
	return chat_reply