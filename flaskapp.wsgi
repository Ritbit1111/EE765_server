import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/home/riteshkr/sandbox/")

from bokeh_flask_app import app as application
