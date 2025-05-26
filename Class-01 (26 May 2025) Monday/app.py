from flask import Flask , request , jsonify

app = Flask(__name__)


dict = []

@app.route("/" , methods=["POST" , "GET"])
def homeAPI(): 
    if request.method == "POST":

        data = request.get_json()

        first_name = data.get("first_name")
        Last_name = data.get("Last_name")
        field = data.get("field")

        dict.append(
            {
            "first_name": first_name , 
            "Last_name" : Last_name ,
            "field" : field
            }
        )

        return "Appended elements in dictionary ..."

    return dict    


app.run(debug=True)