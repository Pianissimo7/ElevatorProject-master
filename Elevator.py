class Elevator:
    def __init__(self, ID, speed, min_floor, max_floor, close_time, open_time, start_time, stop_time):

        self.ID = ID
        self.Speed = speed
        self.MinFloor = min_floor
        self.MaxFloor = max_floor
        self.CloseTime = close_time
        self.OpenTime = open_time
        self.StartTime = start_time
        self.StopTime = stop_time

    def __str__(self):
        return ", ".join([
            str(self.ID),
            str(self.Speed),
            str(self.MinFloor),
            str(self.MaxFloor),
            str(self.CloseTime),
            str(self.OpenTime),
            str(self.StopTime),
            str(self.StopTime)])
