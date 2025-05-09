import datetime
import flask
import logging


######################
## initialization
######################
app = flask.Flask(__name__)
start = datetime.datetime.now()

log = logging.getLogger('werkzeug')
log.disabled = True


######################
## routes
######################
@app.route('/', methods=['GET'])
def root():
  logging.warning('main route accessed')
  return flask.jsonify({'message': 'flask app root/'})

@app.route('/healthz', methods=['GET'])
def healthz():
  now = datetime.datetime.now()
  logging.warning('healthz route accessed')
  return flask.jsonify({'message': f'up and running since {(now - start)}'})

@app.errorhandler(404)
def page_not_found(error):
    logging.error(f"404 Error: {error}")
    return flask.jsonify({'message': 'Route not found'}), 404

######################
if __name__ == '__main__':
######################
  app.run(debug=True, host='0.0.0.0', port=5000)