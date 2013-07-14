#!/usr/bin/env python
# Licensed by "Do whatever you want License" 1.0
import bottle

DEBUG = True

@bottle.route('/')
@bottle.jinja2_view('helloworld')
def helloworld():
    data = {
            'greeting': 'Hello World'
            }
    return data


app = bottle.default_app()
bottle.run(server='gae', app=app, debug=DEBUG)
