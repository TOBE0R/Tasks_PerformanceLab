import json


def generate_report(values_path: str, tests_path: str, report_path: str):
    with open(values_path, 'r') as input_file:
        values_data = json.load(input_file)

    with open(tests_path, 'r') as input_file:
        tests_data = json.load(input_file)

    values_dict = {item['id']: item['value'] for item in values_data['values']}
    
    def fill_values(data):
        if isinstance(data, dict):
            if 'value' in data:
                data['value'] = values_dict.get(data['id'], 'unknown')
            for value in data.values():
                fill_values(value)
        elif isinstance(data, list):
            for item in data:
                fill_values(item)

    fill_values(tests_data)

    with open(report_path, 'w') as output_file:
        json.dump(tests_data, output_file, indent=2)


if __name__ == "__main__":
    generate_report(values_path = 'task3\\values.json', tests_path = 'task3\\tests.json', report_path = 'task3\\report.json')