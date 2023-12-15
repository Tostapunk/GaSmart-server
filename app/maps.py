import openrouteservice


class DistanceMatrix(dict):
    def __init__(self):
        self.key = "5b3ce3597851110001cf6248c68555a1fd9b4d21809377d53c041bcd"
        self.client = openrouteservice.Client(self.key)

    def __get(self, usr_coord, distr_coord):
        coords = [usr_coord] + distr_coord
        print(f"COORDS: {coords}", flush=True)
        res = self.client.distance_matrix(
            locations=coords,
            profile="driving-car",
            metrics=["distance", "duration"],
            validate=False,
        )
        print(f"RES_MAT: {res}", flush=True)
        # return res["durations"][0]  # ritorna quando tempo ci si mette ad arrivare
        return res

    # Ritorna quanta distanza bisogna percorrere
    def get_distances(self, usr_coord, distr_coord):
        return self.__get(usr_coord, distr_coord)["distances"][0]

    # Ritorna quanto tempo ci si mette ad arrivare
    def get_durations(self, usr_coord, distr_coord):
        return self.__get(usr_coord, distr_coord)["durations"][0]
