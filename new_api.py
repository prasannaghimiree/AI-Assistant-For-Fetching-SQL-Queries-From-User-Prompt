from changed import a_Model
from dotenv import load_dotenv
import os
import json
# , db_user, db_pass,host,port,service
from flask import Flask, request
import time

load_dotenv(verbose=True)
db_user=os.getenv('DB_USER')
db_pass = os.getenv("DB_PASS")
host = os.getenv("HOST")
port = os.getenv("PORT")
service = os.getenv("SERVICE")

print(db_user, db_pass, host, port, service)



# Initialize the database connection using environment variables
db = a_Model(db_user, db_pass, host, port, service)

# ADMIN
# admin@123

# print(db)
app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to the AI Assistant API!!"



@app.route('/syn_assistant' , methods = ['POST','GET'])
def syn_assistant():
    # user = get_jwt_identity()
    
    data = request.get_json(force=True)
    # print(f"""{user["db_user"]}""")
    # db = ai_model_for_query.a_Model(``
    #  user["db_user"], user["db_pass"])  # intilization db
    # data={"text":"can you tell me the detailed amount sales of month shrawan"}
    
    output = db.fetch_query(data["text"], data["query_detect"], '01')
    output = json.dumps(output)
    jsonoutput = str("'''"+str(output)+"'''")
    return jsonoutput

# ss=syn_assistant("can you tell me the detailed amount sales of month shrawan")
# time_2 = time.time()
# timee = time_2 - time_1
# print(timee)
# print(ss)

#if __name__ == "__main__":
#     app.run(debug=True, host='0.0.0.0',port=4040)


if __name__ =="__main__":
    app.run(debug = True, host = '0.0.0.0', port = 6060)


