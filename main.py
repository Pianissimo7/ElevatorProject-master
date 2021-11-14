import csv
import json
from Building import Building
from Elevator import Elevator
from CallForElevator import CallForElevator


def parse_json(json_path):
    with open(json_path) as f:
        data = json.load(f)

        elevators = [Elevator(
            e["_id"],
            e["_speed"],
            e["_minFloor"],
            e["_maxFloor"],
            e["_closeTime"],
            e["_openTime"],
            e["_startTime"],
            e["_stopTime"])
            for e in data["_elevators"]]
        building_ = Building(data["_minFloor"], data['_maxFloor'], elevators)
        f.close()
    return building_


def parse_csv(csv_path):
    calls_ = []
    with open(csv_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for rows in csv_reader:
            call = CallForElevator(rows[1], rows[2], rows[3], rows[4], -1)
            calls_.append(call)
        csv_file.close()

    for call in calls_:
        print(call)
    return calls_


if __name__ == '__main__':
    path1 = "files/Ex1_Buildings/B1.json"
    building = parse_json(path1)
    path2 = "files/Ex1_Calls/Calls_a.csv"
    calls = parse_csv(path2)
