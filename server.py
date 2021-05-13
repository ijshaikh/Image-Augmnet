from flask import Flask , render_template , send_file, jsonify
app = Flask(__name__)
from write_into_image import ImageGenerator



@app.route('/')
def hello_world():
    return render_template("home.html")

@app.route("/created/<image_name>")
def return_image(image_name):
    filename = "created/"+image_name
    return send_file(filename, mimetype='image/png')


@app.route("/api/generate/image/<int:type>/<string:name>",methods=['POST','GET'])
def createImage(type,name):
    path = ImageGenerator(type,name)
    return jsonify(url=path)

app.run(debug=True)