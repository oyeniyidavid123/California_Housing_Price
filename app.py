# Initialize the app
app = flask.Flask(__name__)

@app.route("/", method=["GET","POST"])
def index():
    return render_template("index.html", beds=beds, baths=baths, city=city)

@app.route("/predict", methods=["POST"])
def predict():
   
    print(request.args)
    if(request.args):
        x_input, predictions = \   
            make_prediction(request.args['x_input'])
        print(x_input)

        return flask.render_template('predictor.html',
                                     price_input=x_input,
                                     prediction=predictions)
    else: 
        
        x_input, predictions = make_prediction('')
        return flask.render_template('predictor.html',
                                     price_input=x_input,
                                     prediction=predictions)
if __name__=="__main__":
   
    app.run(debug=False)
    
    app.run()