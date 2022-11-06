from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS

# inisiasi objek flask
app = Flask(__name__)

# inisiasi objek flask restful
api = Api(app)

# inisiasi objek flask cors
CORS(app)

# inisiasi variable kosong
identitas = {}  # variable global

# membuat class resource


class ContohResource(Resource):
    def get(self):
        response = {
            "message": "METHOD GET",
            "data": identitas
        }
        return response

    def post(self):
        nama = request.form["nama"]
        umur = request.form["umur"]

        identitas["nama"] = nama
        identitas["umur"] = umur

        response = {"message": "Data ditambahkan"}
        return response


# setup resource
api.add_resource(ContohResource, '/api', methods=["GET", "POST"])

if __name__ == "__main__":
    app.run(debug=True, port=8000)
