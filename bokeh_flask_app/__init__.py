from flask import Flask, render_template, redirect, url_for, Response
from forms import InputForm 
import numpy as np
import pandas as pd

from figure import get_weibull, get_normal, get_exponential, get_lognormal, plot
from bokeh.layouts import row, column, gridplot
from bokeh.embed import server_document
from bokeh.models import ColumnDataSource, Slider
from bokeh.plotting import Figure, ColumnDataSource
from bokeh.server.server import Server
from bokeh.themes import Theme
from tornado.ioloop import IOLoop

app = Flask(__name__)

app.config['SECRET_KEY'] = '45df45653df23224'
def modify_doc(doc):

    layout = plot(400, 400)
    doc.add_root(layout)
#
    doc.theme = Theme(filename="theme.yaml")
#

roll_list = ['154076022','15D070032','15D070051', '15D070033' ,'160070049','160100059','16D070023','16D070024','16D070026','16D070030','16D070049','16D070059','16D070062','170070002','170070016','170070041','173074002','173074016','173074017','17D070020','17D070022','17D070039','17D070051','17D070054','17D070058','17D070060','17D070061','17D070063','183074002','183074009','183074017','183074018','183074022','183170012','183170021','184073001','184073004','18I170013','193070024','193070076','193076001','194076011','194366003','16D070027','16D070029']

@app.route("/home", methods = ['POST', 'GET'])
@app.route('/', methods=['GET', 'POST'])
def bkapp_page():
    form = InputForm()
    if form.validate_on_submit():
        roll = form.rollno.data
        points = form.points.data
        if roll in roll_list:
            s = np.random.weibull(0.5,points)
            df = pd.DataFrame({'Values':s})
            df.index.name = 'Index' 
            csv = df.to_csv()
            return Response( csv, mimetype="text/csv", headers={"Content-disposition": "attachment; filename=dwnld_csv.csv"})
        else:
            return redirect(url_for('bkapp_page'))
    script = server_document('http://localhost:5006/bkapp')
    return render_template("home.html",title='EE765', form=form, script=script)

def bk_worker():
    # Can't pass num_procs > 1 in this configuration. If you need to run multiple
    # processes, see e.g. flask_gunicorn_embed.py
    server = Server({'/bkapp': modify_doc}, io_loop=IOLoop(), allow_websocket_origin=["localhost:8000"])
    server.start()
    server.io_loop.start()

from threading import Thread
Thread(target=bk_worker).start()

if __name__ == '__main__':
    app.run(port=8000)
