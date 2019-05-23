DEBUG = False # Turns on debugging features in Flask. Make sure DEBUG is set to False in production. Leaving it on will allow users to run arbitrary Python code on your server.
BCRYPT_LOG_ROUNDS = 12 # Configuration for the Flask-Bcrypt extension
MAIL_FROM_EMAIL = "john@example.com" # For use in application emails

SQLALCHEMY_ECHO = False