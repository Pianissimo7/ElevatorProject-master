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
    return calls_


def allocate(building_, call, call_max_length):
    margin = call_max_length / len(building_.elevators)
    call_length = abs(int(call.dest) - int(call.src))
    elev_index = int(call_length / margin)
    if elev_index >= len(building_.elevators) - 1:
        elev_index -= 1
    call.elev = elev_index
    return call


def find_max_length(calls):
    max_call_length = calls[0].dest - calls[0].src
    for call in calls:
        if call.dest - call.src > max_call_length:
            max_call_length = call.dest - call.src
    return max_call_length


def csv_output_writer(pathcsv, calls):
    with open(pathcsv, 'w', newline='') as file:
        csv_writer = csv.writer(file)
        for call in calls:
            row = call.output()
            if len(row) != 0:
                csv_writer.writerow(row)
        file.close()


# tester run command:
# java -jar Ex1_checker_V1.2_obf.jar 1111,2222,3333 Ex1_Buildings/B5.json output.csv logs/Calls_d_B5_log.csv
if __name__ == '__main__':
    building_path = "files/Ex1_Buildings/B5.json"
    output_path = "files/output.csv"
    calls_path = "files/Ex1_Calls/Calls_d.csv"
    _building = parse_json(building_path)
    _calls = parse_csv(calls_path)
    _max = find_max_length(_calls)
    i = 0;
    for _call in _calls:
        _call = allocate(_building, _call, _max)
        print(i, " ", _call, ",  ", _call.elev)
        i = i + 1
    csv_output_writer(output_path, _calls)

