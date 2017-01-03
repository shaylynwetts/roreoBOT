#==============================================================================
# TODO: comments; top comments and general comments
#
# TODO: general functions list
#	- parse for language for timing out
#	- basic input output commands & cycle them output
#		* links
#		* commission info & availability
#		* drawing programs
#		* tablet
#		* requests info
#	- chat log
#	- loyalty (revlo type functionality)
#	- song requests
#	- links to other streamers
#	- uptime
#	- request stream functionality (gotta determine how to go about this)
#
#==============================================================================
from Setup import *
from Functions import *
from Configure import RATE

import string
import time

sock = openSocket()
joinRoom(sock)

while True:
	readLine = sock.recv(1024).decode("utf-8")

	if readLine == "PING :tmi.twitch.tv\r\n":
		print("PINGed")
		sock.send("PONG :tmi.twitch.tv\r\n")
		print("PONGed\n")
	else:
		username = getUsername(readLine)
		message = getMessage(readLine)
		print(username + ": " + message)
		if message == "!links\r\n":
			printLinks(sock)

	time.sleep(1 / RATE)
#==============================================================================
#   Sample of responding to a specific string in a message
#           if "string" in message:
#               sendMessage(s, "response")
#==============================================================================