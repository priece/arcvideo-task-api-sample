import requests
import json

# Replace with your own site URL and token
API_BASE_URL = "http://172.17.5.12/api/v8.0"
ACCESS_TOKEN = "t_848e7967e6d4c3c4638c057932873edb"
# Modify task.json file with your task data
TASK_FILE = "task.json"

headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}

def create_task():
    """Create a new task"""
    url = f"{API_BASE_URL}/task/create"
    
    # Load task data from JSON file
    try:
        with open(TASK_FILE, "r", encoding="utf-8") as f:
            task_data = json.load(f)
    except FileNotFoundError:
        print("Error: task.json file not found")
        return None
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in task.json")
        return None
    
    try:
        response = requests.post(url, json=task_data, headers=headers)
        response.raise_for_status()
        print("Task created successfully:", response.json())
        return response.json()
    except requests.exceptions.RequestException as e:
        print("Failed to create task:", str(e))
        return None

if __name__ == "__main__":
    create_task()
