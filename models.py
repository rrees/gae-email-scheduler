from google.appengine.ext import ndb
from google.appengine.ext import db

class ScheduledEmail(ndb.Model):
	to = db.ListProperty(db.Email)
	message = ndb.TextProperty(required=True)
	send_datetime = ndb.DateTimeProperty(required=True)
