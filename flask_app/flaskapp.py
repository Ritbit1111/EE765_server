from flask import Flask, render_template, redirect, url_for, Response, send_file
from forms import InputForm 
import pandas as pd
import numpy as np
import time
from flask_bootstrap import Bootstrap
app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = '45df45653df23224'

roll_list = ['rk', 'naren', 'yogesh', 'karan', '154076022','15D070032','15D070051', '15D070033' ,'160070049','160100059','16D070023','16D070024','16D070026','16D070030','16D070049','16D070059','16D070062','170070002','170070016','170070041','173074002','173074016','173074017','17D070020','17D070022','17D070039','17D070051','17D070054','17D070058','17D070060','17D070061','17D070063','183074002','183074009','183074017','183074018','183074022','183170012','183170021','184073001','184073004','18I170013','193070024','193070076','193076001','194076011','194366003','16D070027','16D070029']

@app.route("/home", methods = ['POST', 'GET'])
@app.route("/", methods = ['POST', 'GET'])
def home():
    form = InputForm()
    if form.validate_on_submit():
        roll = form.rollno.data
        points = form.points.data
        if roll in roll_list:
            s = np.random.weibull(0.5,points)
            df = pd.DataFrame({'Values':s})
            df.index.name = 'Index' 
            csv = df.to_csv()
            timestr = time.strftime("%m-%d@%H.%M.%S")
            filename = f'data_{roll}_{timestr}'
            return Response( csv, mimetype="text/csv", headers={"Content-disposition": "attachment; filename=%s.csv"%filename})
        else:
            return redirect(url_for('home'))
    return render_template('home.html', title='EE765',form = form)

if __name__ == "__main__":
    app.run(debug=True)
