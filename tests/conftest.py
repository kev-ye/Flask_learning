import os
import tempfile

import pytest
from flaskr import create_app
from flaskr.db import get_db, init_db

with open(os.path.join(os.path.dirname(__file__), 'data.sql'), 'rb') as f:
	# print('debug: open path debug:', f'{ os.path.dirname(__file__) } + data.sql')
	_data_sql = f.read().decode('utf8')
	# print('debug: binary file:', _data_sql)


@pytest.fixture
def app():
	db_fd, db_path = tempfile.mkstemp()
	# print(f'debug: db_fd: { db_fd } --- db_path: { db_path }')

	app = create_app({
		'TESTING': True,
		'DATABASE': db_path,
	})

	with app.app_context():
		init_db()
		get_db().executescript(_data_sql)

	yield app

	os.close(db_fd)
	os.unlink(db_path)


@pytest.fixture
def client(app):
	# print('debug: in client(app)')
	return app.test_client()


@pytest.fixture
def runner(app):
	# print('debug: in runner(app)')
	return app.test_cli_runner()


class AuthActions(object):
	def __init__(self, client):
		self._client = client

	def login(self, username='test', password='test'):
		return self._client.post(
			'/auth/login',
			data={'username': username, 'password': password}
		)

	def logout(self):
		return self._client.get('/auth/logout')


@pytest.fixture
def auth(client):
	# print('debug client:', client)
	return AuthActions(client)



