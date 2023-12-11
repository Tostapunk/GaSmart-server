import openrouteservice


class DistanceMatrix(dict):
    def __init__(self):
        self.key = ""
        self.client = openrouteservice.Client(self.key)

    def get(self, usr_coord, distr_coord):
        coords = [usr_coord] + distr_coord
        res = self.client.distance_matrix(
            locations=coords,
            profile="driving-car",
            metrics=["distance", "duration"],
            validate=False,
        )
        return res["durations"][0]  # ritorna quando tempo ci si mette ad arrivare