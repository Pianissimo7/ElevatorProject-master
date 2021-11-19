import csv
import json
import sys
from Building import Building
from Elevator import Elevator
from CallForElevator import CallForElevator


# receives a path to a json file that contains a building's data.
# returns a building object containing the json's values.
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


# receives a path to a csv file containing a list of calls.
# returns an array of CallForElevator objects representing the calls in the csv file specified.
def parse_csv(csv_path):
    calls_ = []
    with open(csv_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for rows in csv_reader:
            call = CallForElevator(rows[1], rows[2], rows[3], rows[4], -1)
            calls_.append(call)
        csv_file.close()
    return calls_


# receives a path to an output csv file and a list of calls.
# writes to the output the content of the calls.
def csv_output_writer(pathcsv, calls):
    with open(pathcsv, 'w', newline='') as file:
        csv_writer = csv.writer(file)
        for call in calls:
            row = call.output()
            if len(row) != 0:
                csv_writer.writerow(row)
        file.close()


# receives a building of type Building, call of type CallForElevator and call_max_length of type int
# returns the call after updating it's elev value to be one of the elevators in building
def allocate(building, call, call_max_length):
    building.elevators = sorted(building.elevators, key=lambda x: x.CloseTime + x.OpenTime + x.StartTime + x.StopTime - abs(call.dest - call.src) / x.Speed)
    margin = call_max_length / len(building.elevators)
    call_length = abs(int(call.dest) - int(call.src))
    elev_index = int(call_length / margin)
    if elev_index >= len(building.elevators) - 1:
        elev_index -= 1
    # load balancing algorithm
    # if one elevator has too many calls allocated to it, some calls should be given to elevators with less calls
    average = sum([x.call_amount for x in building.elevators]) / len(building.elevators)
    min_calls_elevator_index = min_calls(building)
    if building.elevators[elev_index].call_amount * 0.9 > average and elev_index < min_calls_elevator_index:
        elev_index = min_calls_elevator_index

    call.elev = building.elevators[elev_index].ID
    building.elevators[elev_index].call_amount += 1
    return call


# receives a building of type Building.
# returns an int representing the elevator with the lowest amount of calls assigned to it.
def min_calls(building):
    _min = building.elevators[0].call_amount
    index = 0
    for x in range(len(building.elevators)):
        if building.elevators[x].call_amount < _min:
            _min = building.elevators[x].call_amount
            index = x
    return index


# main function
# receives 3 arguments: a building path, a calls path and a path to the output file
if __name__ == '__main__':
    cmd_args = sys.argv[1:]
    building_path = cmd_args[0]
    calls_path = cmd_args[1]
    output_path = cmd_args[2]

    _building = parse_json(building_path)
    _calls = parse_csv(calls_path)
    _max = max([abs(x.dest - x.src) for x in _calls])
    for _call in _calls:
        _call = allocate(_building, _call, _max)
    csv_output_writer(output_path, _calls)
