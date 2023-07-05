from flask import Flask, request, jsonify
from flask import Response
import json
from gradeCalc import calcGrade
app = Flask(__name__)

@app.route('/')
def get_grade():
    module_1 = request.args.get('module_1')
    module_2 = request.args.get('module_2')
    module_3 = request.args.get('module_3')
    module_4 = request.args.get('module_4')
    module_5 = request.args.get('module_5')

    mark_1 = request.args.get('mark_1')
    mark_2 = request.args.get('mark_2')
    mark_3 = request.args.get('mark_3')
    mark_4 = request.args.get('mark_4')
    mark_5 = request.args.get('mark_5')
    
    if not module_1:
        r = "Module 1 is missing"
        response = Response(response=r, status =400)
        return response
    
    if not module_2:
        r = "Module 2 is missing"
        response = Response(response=r, status =400)
        return response
    
    if not module_3:
        r = "Module 3 is missing"
        response = Response(response=r, status =400)
        return response
    
    if not module_4:
        r = "Module 4 is missing"
        response = Response(response=r, status =400)
        return response

    if not module_5:
        r = "Module 5 is missing"
        response = Response(response=r, status =400)
        return response

    if not mark_1:
        r = "Mark 1 is missing"
        response = Response(response=r, status =400)
        return response

    if not mark_2:
        r = "Mark 2 is missing"
        response = Response(response=r, status =400)
        return response

    if not mark_3:
        r = "Mark 3 is missing"
        response = Response(response=r, status =400)
        return response

    if not mark_4:
        r = "Mark 4 is missing"
        response = Response(response=r, status =400)
        return response
    
    if not mark_5:
        r = "Mark 5 is missing"
        response = Response(response=r, status =400)
        return response

    try:
        mark1 = int(mark_1)
        mark2 = int(mark_2)
        mark3 = int(mark_3)
        mark4 = int(mark_4)
        mark5 = int(mark_5)
    except ValueError:
        r = "Invalid module mark, must be a number"
        response = Response(response=r, status=400)
        return response
    
    module_marks = {module_1: int(mark_1), module_2: int(mark_2),
    module_3: int(mark_3), module_4: int(mark_4),
    module_5: int(mark_5)}

    marks = calcGrade(module_marks)
    r = {
        "Modules and their Classifications": str(marks) 

    }
    reply = json.dumps(r)

    response = Response(response=reply, status=200, mimetype='application/json')
    response.headers["Content-Type"]="application/json"
    response.headers["Access-Control-Allow-Origin"]="*"

    return response

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
