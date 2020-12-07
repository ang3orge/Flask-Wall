import pytest
from flask import Flask
from flask_wall import SimpleWall


@pytest.fixture
def app():
	flask_app = Flask(__name__)

	sw = SimpleWall()
	sw_no_callback = SimpleWall(status_code=307)
	sw_no_callback_or_status = SimpleWall()

	@sw.callback
	def simple_wall():
		return 'simple-wall', 503

	@flask_app.route('/')
	def index():
		return 'index', 200

	@flask_app.route('/pr-one')
	@sw.restrict
	def private_route_one():
		return 'private-route-one', 200

	@flask_app.route('/pr-two')
	@sw_no_callback.restrict
	def private_route_two():
		return 'private-route-two', 200

	@flask_app.route('/pr-three')
	@sw_no_callback_or_status.restrict
	def private_route_three():
		return 'private-route-three', 200

	yield flask_app


@pytest.fixture
def client(app):
	with app.test_client() as test_client:
		with app.app_context():
			yield test_client
