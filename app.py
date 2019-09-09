import subprocess
def install(package):
    subprocess.call(['pip', 'install', package])
package = "flask"
install(package)
from flask import Flask, render_template, request
#from werkzeug.exceptions import BadRequest
import os
os.environ["KERAS_BACKEND"] = "tensorflow"
import model1
from timeit import default_timer as timer



app = Flask(__name__)
app.config['DEBUG'] = False

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/', methods=["GET","POST"])


def word_problem_solver():

    errors = []
    results = 0
    question = ""
    if request.method == "POST":
        try:
            questionText = request.form['question']

            #call model

			#question = "question_to_answer.txt"
            question = questionText

            print (question)
#train_model_for_operation_prediction.main(train,testfile,model,weights)
            t0 = timer()
            answer = model1.main_func(question)
            t1 = timer()
            time = t1 - t0
            #print (equation)

            print (answer)

            print(question)
            #results['question'] = questionText
            results = answer
        except Exception as e:
            print (e)
            errors.append(
                "Error occurred while processing your request....Please try again.."
            )
    return render_template('index.html', title="Welcome to Word Problem Solver", errors=errors, results=results,question=question,time=time)


if __name__ == '__main__':
    #port = int(os.environ.get('PORT',4503))
    #app.debug = True	
    #app.run(port=port)
    #app.run(debug = True)
    app.run(host='0.0.0.0', threaded=False)
    
    
    
    
    
