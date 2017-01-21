# Run a test server.
from app import app
from app.mod_ncm import controllers
app.run(host='127.0.0.1', port=5000, debug=True)
