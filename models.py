from google.appengine.ext import ndb
from google.appengine.ext import db

class ScheduledEmail(ndb.Model):
	recipients = db.ListProperty(db.Email)
	subject = ndb.StringProperty(required=True)
	message = ndb.TextProperty(required=True)
	send_datetime = ndb.DateTimeProperty(required=True)
