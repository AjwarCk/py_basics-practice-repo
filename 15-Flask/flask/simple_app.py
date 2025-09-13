from flask import Flask
'''
It creates an instance of the Flask class,
which will be your WSGI (web server gateway interface) application.

-- Workflow
[User's Browser] 
       |
       | 1. Makes HTTP request to URL (e.g., http://localhost:5000/)
       v
[Web Server / Flask Development Server] 
       |
       | 2. Receives request and passes it to WSGI interface
       v
[WSGI (Web Server Gateway Interface)] 
       |
       | 3. WSGI calls the Flask app (the 'app' object)
       v
[Flask App (app)]
       |
       | 4. Looks at route definitions to find matching route
       |    (e.g., "/" → welcome() function)
       v
[Route Function: welcome()]
       |
       | 5. Executes the function and returns a response
       v
[WSGI]
       |
       | 6. Passes the response back to the server
       v
[Web Server]
       |
       | 7. Sends the response (HTML/text) back to the browser
       v
[User's Browser]
       |
       | 8. Displays: "Welcome to this Flask Course."

'''

### WSGI Application
simple_app = Flask(__name__)

@simple_app.route("/")
def welcome():
    return "Welcome to the Flask course!"

if __name__ == "__main__":
    simple_app.run()
    