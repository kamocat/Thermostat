# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#	 http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START calendar_quickstart]
from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

def parse_date( text ):
	if ":" == text[-3:-2]:
		text = text[:-3]+text[-2:]
	elif "." == text[-5:-4]:
		text = text[:-5]+'+0000'
	result = datetime.datetime.strptime(  text, "%Y-%m-%dT%H:%M:%S%z")
	return( result )

def get():
	"""Shows basic usage of the Google Calendar API.
	Prints the start and name of the next 10 events on the user's calendar.
	"""
	creds = None
	# The file token.pickle stores the user's access and refresh tokens, and is
	# created automatically when the authorization flow completes for the first
	# time.
	if os.path.exists('token.pickle'):
		with open('token.pickle', 'rb') as token:
			creds = pickle.load(token)
	# If there are no (valid) credentials available, let the user log in.
	if not creds or not creds.valid:
		if creds and creds.expired and creds.refresh_token:
			creds.refresh(Request())
		else:
			flow = InstalledAppFlow.from_client_secrets_file(
				'credentials.json', SCOPES)
			creds = flow.run_local_server()
		# Save the credentials for the next run
		with open('token.pickle', 'wb') as token:
			pickle.dump(creds, token)

	service = build('calendar', 'v3', credentials=creds)

	# Call the Calendar API
	now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
#	print('Getting the upcoming 1 events')
	events_result = service.events().list(
		calendarId='es3ggcg3r4ga9ilfcrdmmd9dgs@group.calendar.google.com', 
		timeMin=now, maxResults=1, singleEvents=True, orderBy='startTime').execute()
	events = events_result.get('items', [])

	if not events:
		print('No upcoming events.')
		return 0
	event = events[0]	# Get first event
	now = datetime.datetime.now(datetime.timezone.utc)
	start = event['start'].get('dateTime')
	start = parse_date( start )
	end = event['end'].get('dateTime')
	end = parse_date( end )
	updated = event['updated']
	updated = parse_date( updated )
	updated = now - updated
	target = int( event['summary'] )
	if start <= now:
		#print("Heating to", target, "\tupdated", updated, "ago" )
		return target
	else:
		#print('Heater is off right now.')
		#print('Heating to', target, 'in', ((start-now).seconds)/60, "minutes" )
		return 0
		

if __name__ == '__main__':
	get()
# [END calendar_quickstart]
