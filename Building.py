class Building:
    def __init__(self, min_floor, max_floor, elevators):
        self.min_floor = min_floor
        self.max_floor = max_floor
        self.elevators = elevators

    def __str__(self):
        return ", ".join([
            str(self.min_floor),
            str(self.max_floor),
            "".join(["[", ", ".join(["".join(['{', str(x), '}']) for x in self.elevators]), "]"])])

