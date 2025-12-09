import json

def get_newspaper_data():
    file_path = 'churnapp/data.json'  # Replace with correct path
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return {paper['name'].lower().replace(' ', ''): paper for paper in data}