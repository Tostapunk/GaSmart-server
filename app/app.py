from flask import Flask
from csv_parser import Distributori

app = Flask(__name__)
distributori = Distributori()


@app.route("/")
def index():
    return "Per fare la chiamata vai a /get/coordinate/raggio/num_risultati/"


@app.route("/get/<coord>/<int:radius>/<carburante>/<int:num_res>/<float:kml>/<sort>")
@app.route("/get/")
def get(
    coord="45.74782102240776,12.102949475152739",
    radius=8.5,
    carburante="Benzina",
    num_res=5,
    kml=26.672,
    sorting_key="distanza",
):
    coord = coord.split(",")
    coord = [float(coord[1]), float(coord[0])]
    return (
        distributori.get(coord, radius, carburante, num_res, kml, sorting_key),
        200,
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
