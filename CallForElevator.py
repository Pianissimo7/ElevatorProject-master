class CallForElevator:
    # constructor.
    def __init__(self, time, src, dest, state, elev):
        self.time = time
        self.src = int(src)
        self.dest = int(dest)
        self.state = state
        self.elev = elev
        self.type = (int(dest) - int(src)) / abs(int(dest) - int(src))

    # returns a list representing a line in a csv file as it should be written in the output file.
    def output(self):
        return "Elevator call", self.time, str(self.src), str(self.dest), 3, str(self.elev)

    # toString.
    def __str__(self):
        return ", ".join([
            str(self.time),
            str(self.src),
            str(self.dest),
            str(self.state),
            str(self.elev),
            str(self.type)])
