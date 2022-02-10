from flask import Flask,render_template,request
import model as m
mk=0
app = Flask(__name__)
linkpred=0
@app.route("/",methods=['GET','POST'])
def helloworld():
    global mk
    if request.method=='POST':
        link=request.form["link"]
        linkpred= m.summaryPredictions(link)
        mk=linkpred
         
       
        
    return render_template("index.html",linkp=mk)
       
       
 

# if __name__=="__main__":
#     app.run(debug=True)
if __name__ == '__main__':
    app.debug = True
    app.run()