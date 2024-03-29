Flask - HTML/CSS - DB
	How To Make a Web Application Using Flask in Python 3
	https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3



Flask setup

	- need to use installer (versus embeddable package) to reinstall Python
	  this is because virtual env is not available in python embeddable package
		- follow https://www.codingforentrepreneurs.com/guides/install-python-on-windows/
	
	- create a virtual env
		- python -m venv [environment_name]
			C:\a\z_jiajia\amsterdam\2024_02\computational_social_science\2_assignments\x>python -V
			Python 3.12.2

			C:\a\z_jiajia\amsterdam\2024_02\computational_social_science\2_assignments\x>pip -V
			pip 24.0 from C:\a\tool\python-3.12.2\Lib\site-packages\pip (python 3.12)

			C:\a\z_jiajia\amsterdam\2024_02\computational_social_science\2_assignments\x>python -m venv my_venv
			C:\a\z_jiajia\amsterdam\2024_02\computational_social_science\2_assignments\x>
	
	- activate virtual env
		C:\a\z_jiajia\amsterdam\2024_02\computational_social_science\2_assignments\x>my_venv\Scripts\activate
		
		(my_venv) C:\a\z_jiajia\amsterdam\2024_02\computational_social_science\2_assignments\x>
	
	- deactivate from virtual env

		(my_venv) C:\a\z_jiajia\amsterdam\2024_02\computational_social_science\2_assignments\x>deactivate
		
		C:\a\z_jiajia\amsterdam\2024_02\computational_social_science\2_assignments\x>

	- install flask
		(my_venv) C:\a\z_jiajia\amsterdam\2024_02\computational_social_science\2_assignments\x>pip install flask
		
	- check if flask is installed successfully	
		(my_venv) C:\a\z_jiajia\amsterdam\2024_02\computational_social_science\2_assignments\x>python -c "import flask; print(flask.__version__)"
		<string>:1: DeprecationWarning: The '__version__' attribute is deprecated and will be removed in Flask 3.1. Use feature detection or 'importlib.metadata.version("flask")' instead.
		3.0.2

	- install dotenv
		- so that environment variables can be created

		(my_venv) C:\a\z_jiajia\amsterdam\2024_02\computational_social_science\2_assignments\x>pip install python-dotenv



DB
	- for SQLite (sqlite3), there is no need to install SQLite database separately
		- this is because
			- SQLite is an embedded database (not a standard database)
			- it is already included inside the Python sqlite3 lib (from `pip install`)
				- https://stackoverflow.com/questions/24410124/does-python-sqlite3-library-need-sqlite-to-be-installed
				
	- how to view database, table, data in SQLite3?
		- install `DB Browser for SQLite`
			- https://sqlitebrowser.org/
				DB Browser for SQLite


Web Application
---------------------------------------------------------------------
	- need to create .env for each app
		- need to set
			- port number
			- app name

	- for simple web page
	-- 1_hello
		- create .env file under project folder (C:\a\z_jiajia\amsterdam\2024_02\computational_social_science\2_assignments\x\flash_blog\1_hello\.env)
			.env
				FLASK_APP=hello
				FLASK_ENV=development
				FLASK_RUN_PORT=8000

		- run flask (under project folder)
			(my_venv) C:\a\z_jiajia\amsterdam\2024_02\computational_social_science\2_assignments\x\flash_blog>1_hello\flask run
			* Serving Flask app 'hello'
			* Debug mode: off
			WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
			* Running on http://127.0.0.1:8000
			Press CTRL+C to quit

		- go to browser, run
			http://localhost:8000

	- for more advanced web page
	-- 2_app_basic
	-- 3_app_jinja_bootstrap
	-- 4_app_jinja_bootstrap_sqlite
	-- 5_app_all_crud

	- Jinja template app
		- create .env file under project folder (C:\a\z_jiajia\amsterdam\2024_02\computational_social_science\2_assignments\x\flash_blog\2_app_basic\.env)
			.env
				FLASK_APP=app
				FLASK_ENV=development
				FLASK_RUN_PORT=5000

		- need to add templates/index.html under 2_app_basic

		- run flask (under project folder)
			(my_venv) C:\a\z_jiajia\amsterdam\2024_02\computational_social_science\2_assignments\x\flash_blog>2_app_basic\flask run
			* Serving Flask app 'app'
			* Debug mode: off
			WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
			* Running on http://127.0.0.1:5000
			Press CTRL+C to quit

		- go to browser, run
			http://localhost:5000

	- DB
	-- sqlite
		- 4_app_jinja_bootstrap_sqlite

		- need to create database and table first
			- executing init_db.sql will automatically create DB (database.db) and table (posts)
				- python init_db.py

		- create .env file under project folder (C:\a\z_jiajia\amsterdam\2024_02\computational_social_science\2_assignments\x\flash_blog\4_app_jinja_bootstrap_sqlite\.env)
			.env
				FLASK_APP=app
				FLASK_ENV=development
				FLASK_RUN_PORT=5002

		- run flask (under project folder)
			(my_venv) C:\a\z_jiajia\amsterdam\2024_02\computational_social_science\2_assignments\x\flash_blog>4_app_jinja_bootstrap_sqlite\flask run
			* Serving Flask app 'app'
			* Debug mode: off
			WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
			* Running on http://127.0.0.1:5002
			Press CTRL+C to quit

		- go to browser, run
			http://localhost:5002

		- after running the app,
			- a database.db file will be created

	CRUD
		- 5_app_all_crud

		- create .env file under project folder (C:\a\z_jiajia\amsterdam\2024_02\computational_social_science\2_assignments\x\flash_blog\5_app_all_crud\.env)
			.env
				FLASK_APP=app
				FLASK_ENV=development
				FLASK_RUN_PORT=5003

		- NO need to create database because of adding db table auto detection and initialization

		- full run steps:
			- deactivate virtual environment
				(my_venv) C:\a\z_jiajia\amsterdam\2024_02\computational_social_science\2_assignments\web_python\flask_example>my_venv\Scripts\deactivate
				C:\a\z_jiajia\amsterdam\2024_02\computational_social_science\2_assignments\web_python\flask_example>
			
			- activate virtual environment
				C:\a\z_jiajia\amsterdam\2024_02\computational_social_science\2_assignments\web_python\flask_example>my_venv\Scripts\activate
				(my_venv) C:\a\z_jiajia\amsterdam\2024_02\computational_social_science\2_assignments\web_python\flask_example

			- go to 5_app_all_crud and run flask
				(my_venv) C:\a\z_jiajia\amsterdam\2024_02\computational_social_science\2_assignments\web_python\flask_example>cd flask_blog\5_app_all_crud

				(my_venv) C:\a\z_jiajia\amsterdam\2024_02\computational_social_science\2_assignments\web_python\flask_example\flask_blog\5_app_all_crud>flask run
				* Serving Flask app 'app'
				* Debug mode: off
				WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
				* Running on http://127.0.0.1:5003
				Press CTRL+C to quit

			- go to browser, run
				http://localhost:5003

		- after running the app,
			- a database.db file will be created / updated
				- can use `DB Browser for SQLite` to open / view database.db
					- C:\a\z_jiajia\amsterdam\2024_02\computational_social_science\2_assignments\web_python\flask_example\flask_blog\5_app_all_crud\database.db
		
		