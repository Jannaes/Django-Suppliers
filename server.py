from waitress import serve 

from suppliers.wsgi import application

if __name__ == '__main__':
    print("Open browser in http://localhost:8000")
    print("Shut down server with 'control + c'")
    serve(application, port='8000')