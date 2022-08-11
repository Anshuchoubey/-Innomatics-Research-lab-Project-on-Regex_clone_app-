from flask import Flask, render_template ,request
import re

app = Flask(__name__)

#####################################
@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html')

####################################

@app.route('/search', methods = ['POST']) 
def search_funtion():
    string = request.form['in_1']
    regex_expression = request.form['in_2']
    count = re.findall( regex_expression, string)

    return render_template('search.html',s=string , r = regex_expression, a=len(count))

if __name__ == '__main__':
    app.run(debug=True)

