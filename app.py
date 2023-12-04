from flask import Flask, render_template,jsonify

app = Flask(__name__)

jobs=[
  {'id':1,
   'location':'Thimphu',
   'title':"Software Engineer",
   'company':"Google",
   'salary':"Nu.100000"
  },
  {'id':2,
   'location':'Phuentsholing',
   'title':"Software Engineer",
   'company':"Facebook",
   'salary':"Nu.200000"
  },
  {'id':3,
   'location':'Paro',
   'title':"Software Engineer",
   'company':"Tweeter",
   'salary':"Nu.150000"
  },
  {'id':4,
   'location':'Trashigang',
   'title':"Software Engineer",
   'company':"Techpark",
   
  },
  
]

@app.route('/')
def index():
  return render_template('home.html', jobs=jobs)

@app.route('/jobs')
def job_list():
  return jsonify(jobs)




if __name__ == '__main__':
  app.run("0.0.0.0", debug=True)