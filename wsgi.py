import imp

wsgi = imp.load_source('wsgi', 'streamlit_app.py')
application = wsgi.app
