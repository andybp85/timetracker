import Harvest
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True)


#Harvest.HarvestStatus().get()
#u'up'
#harvest = Harvest.Harvest("https://yst.harvestapp.com", "EMAIL", "PASSWORD")
##data = {"notes":"test note", "project_id":"PROJECT_ID","hours":"1.0", "task_id": "TASK_ID"}
##harvest.add(data)
##data['notes'] = "another test"
##harvest.update("ENTRY_ID", data)
#harvest.get_today()
