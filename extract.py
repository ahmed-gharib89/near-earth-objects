"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    # Done: Load NEO data from the given CSV file.
    neos = []
    with open(neo_csv_path, "r") as f:
        reader = csv.reader(f)
        # Discard header row
        try:
            next(reader)
        except StopIteration:
            pass

        # Loop over remaining rows and create NearEarthObjects
        for row in reader:
            try:
                info = {
                    "designation": row[3],
                    "name": row[4],
                    "diameter": float(row[15]) if row[15] else float("nan"),
                    "hazardous": True if row[7] == "Y" else False,
                }
                neo = NearEarthObject(**info)
                neos.append(neo)
            except ValueError as e:
                print(e)

    return neos


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param neo_csv_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    # Done: Load close approach data from the given JSON file.
    approaches = []
    with open(cad_json_path, "r") as f:
        cad_data = json.load(f)

    data = cad_data["data"]
    for row in data:
        try:
            info = {
                "designation": row[0],
                "time": row[3],
                "distance": float(row[4]),
                "velocity": float(row[7]),
            }
            approache = CloseApproach(**info)
            approaches.append(approache)
        except ValueError as e:
            print(e)

    return approaches
