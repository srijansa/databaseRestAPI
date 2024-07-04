from flask import Flask, request
#Json rule: everything needs to be inside a list, it is a string of text, it is not a python dictionary 
#A python dictionary needs to be returned as a string to make it a JSON 
#Change python keywords and values so they match the JSON Standard (ed. True to true)
#Changing the whole thing into a string so that our API can return
#If it is less prettified it's fine- it will just save us bytes of data 

database=[
    {
        "name":"employees",
        "data":[
            {
                "name":"Srijan Sareen",
                "course":"Computer Science & Engineering"
            }
        ]
    }
]
app=Flask(__name__)

@app.get("/database")
def get_data():
    return {"database":database} 

@app.post("/database")
def post_data():
    requested_data=request.get_json()
    new_data_entry={"name": requested_data["name"], "course":[]}
    database.append(new_data_entry)
    return new_data_entry, 201

@app.post("/database/<string:name>/entry")
def post_data_to_database(name):
    request_data=request.get_json()
    for database_name in database:
        print(database_name)
        if database_name["name"]==name:
            new_entry={"name": request_data["emp_name"], "course":request_data['course']}
            database[database_name].append(new_entry)
            return new_entry, 201
    return {"message", "Database not found"}, 404

@app.get("/database/<string:name>")
def get_data_by_name(name):
    for data in database:
        print(data)
        if data["name"]==name:
            return data
    return {"data":"Data Not Found."}, 404