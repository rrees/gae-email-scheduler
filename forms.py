import wtforms
from wtforms_appengine.ndb import model_form

import models

ScheduledEmailForm = model_form(models.ScheduledEmail, field_args={
        'subject' : {
            'label': "Subject",
        },
        'send_datetime': {
            'label': 'When',
            'validators': [wtforms.validators.DataRequired(),]
        }
})
