# Statement for enabling the development environment
DEBUG = True

# Define the application directory
import os
from config_db import *

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED     = True

# Use a secure, unique and absolutely secret key for
# signing the data.
CSRF_SESSION_KEY = "o86dloe8dlpf987kw8s4i7d6f9gKU^R%JU%AD&O(&FP:7f8o654w5d"

# Secret key for signing cookies
SECRET_KEY = "L*&LO*WED%R^*TVOuiglub,gfrdyd79"
