from flask import *
import os
import project

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/result.html', methods=['POST', 'GET'])
def success():
    if request.method == 'POST':
        fname = request.files['file']
        # print(fname)
        # print(f.filename)
        fname.save(os.path.join("static", fname.filename))

        # dog,lifespan=proj.myfunc(fname)
        dog, lifespan = project.find_dog(
            os.path.join("static", fname.filename))
            
        return render_template('result.html', name=dog, name2=lifespan, name3=fname.filename)


if __name__ == "__main__":
    app.run(debug=True)


# source env/bin/activate
