from bottle import route, run
import bottle

@route('/')
def index():
    return '<h3>Hello my Bottle!</h3>'

app = bottle.default_app()
