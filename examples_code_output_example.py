def csv_to_json(file_path):
    import csv, json
    with open(file_path) as f:
        return json.dumps(list(csv.DictReader(f)))
