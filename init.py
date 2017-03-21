#!/usr/bin/env python
# -*- coding: utf-8 -*-

# weatherlogr by Preston Cammarata (c) 2016

import tweepy, time, sys, urllib2, json;

# Variables
TOWN       = "North_Kingstown";  # Your town, with '_' replacing spaces
STATE      = "RI";               # Your state (ex: CA, RI, MA, etc.)
API_KEY    = "yourKeyHere"; # Your Wunderground API key

# Twitter API
CONSUMER_KEY    = 'yourKeyHere';
CONSUMER_SECRET = 'yourKeyHere';
ACCESS_KEY      = 'yourKeyHere';
ACCESS_SECRET   = 'yourKeyHere';

auth = tweepy.OAuthHandler ( CONSUMER_KEY, CONSUMER_SECRET );
auth.set_access_token ( ACCESS_KEY, ACCESS_SECRET );
api  = tweepy.API ( auth );


while ( 1 ):
	# Fetch the API
	_API       = urllib2.urlopen( 'http://api.wunderground.com/api/%s/geolookup/conditions/q/%s/%s.json' % ( API_KEY, STATE, TOWN ) );
	API        = json.loads ( _API.read ( ) );
	
	# Post to Twitter
	MESSAGE = "weather: %s temp: %s humidity: %s wind speed: %s" % ( API['current_observation']['weather'], API['current_observation']['temp_f'], API['current_observation']['relative_humidity'], API['current_observation']['wind_mph'] );
	try:
		print "[weatherlogr] logged to twitter";
		api.update_status ( MESSAGE );
	except:
		print "[weatherlogr] did not log to twitter, it was a duplicate."
		pass
	time.sleep ( 3600 );


# Close the API connection
_API.close( );
