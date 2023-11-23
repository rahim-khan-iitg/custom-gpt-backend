from flask import Flask,render_template,jsonify,request
from flask_cors import CORS
from pipelines.chat_pipeline import ChatModel,QueryModel
app=Flask(__name__)
CORS(app)
@app.route('/',methods=['GET',"POST"])
def home():
    return render_template("./index.html")

@app.route("/chat",methods=['GET','POST'])
def chat():
    if request.method=='POST':
        content=request.get_json()
        chat_model=ChatModel()
        response=chat_model.chat(content['question'])
        return jsonify(response)
    return "hello"
@app.route("/query",methods=['GET','POST'])
def query():
    if request.method=='POST':
        content=request.get_json()
        query_model=QueryModel()
        response=query_model.chat(content['question'])
        return jsonify(response)
    return "hello"
if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000,debug=False)