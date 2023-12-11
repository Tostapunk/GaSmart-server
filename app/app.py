from flask import Flask
from csv_parser import Distributori

app = Flask(__name__)
distributori = Distributori()


@app.route("/")
def index():
    return "Per fare la chiamata vai a /get/coordinate/raggio/num_risultati/"


# @app.route("/get/<coord>/<int:radius>/<int:num_res>/<order_type>/")
@app.route("/get/<coord>/<int:radius>/<int:num_res>/")
@app.route("/get/")
def get(
    coord="45.74782102240776,12.102949475152739",
    radius=8.5,
    num_res=5,
    order_type="min_distance",
):
    coord = coord.split(",")
    coord = [float(coord[1]), float(coord[0])]
    return (
        distributori.get(coord, num_res, radius),
        200,
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
