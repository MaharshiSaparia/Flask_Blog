from flaskblog import create_app
from flaskblog import db
from gevent.pywsgi import WSGIServer

app = create_app()


@app.before_first_request
def create_tables():
    db.create_all()


if __name__ == '__main__':
    # Debug Development
    # app.run(debug=True)
    http_server = WSGIServer(('', 5000), app)
    http_server.serve_forever()
