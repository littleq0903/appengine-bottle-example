#!/usr/bin/env python
# Licensed by "Do whatever you want License" 1.0
import bottle

from google.appengine.api import mail

DEBUG = True

@bottle.route('/')
@bottle.jinja2_view('helloworld')
def helloworld():
    data = {
            'greeting': 'Hello World'
            }
    return data


@bottle.route('/maildemo')
def sendmail():
    SENDER = 'littleq0903@gmail.com'
    RECIPIANT = 'colin@noderabbit.com'
    SUBJECT = 'Hello from Taipei.py'
    CONTENT = """
    <h1>Hello</h1>
    <p>Taipei.py Google Cloud Workshop</p>
    """
    
    mail.send_mail(sender=SENDER, to=RECIPIANT, subject=SUBJECT, body=CONTENT)
    return 'ok'


app = bottle.default_app()
bottle.run(server='gae', app=app, debug=DEBUG)
