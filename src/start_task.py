import requests
import json

# Replace with your own site URL and token
API_BASE_URL = "http://172.17.5.12/api/v8.0"
ACCESS_TOKEN = "t_848e7967e6d4c3c4638c057932873edb"

headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}

def start_task(task_id):
    """Start a task
    Args:
        task_id: Numeric task ID
    """
    url = f"{API_BASE_URL}/task/start"
    
    # Validate task_id is numeric
    if not isinstance(task_id, (int, float)) and not str(task_id).isdigit():
        print("Error: task_id must be a number")
        return None
        
    try:
        response = requests.post(
            url, 
            json={"id": int(task_id)}, 
            headers=headers
        )
        response.raise_for_status()
        print("Task started successfully:", response.json())
        return response.json()
    except requests.exceptions.RequestException as e:
        print("Failed to start task:", str(e))
        return None

if __name__ == "__main__":
    # Example usage:
    # task_id = "your_task_id_here"
    # start_task(task_id)
    
    # Or get task_id from user input
    task_id = input("Enter task ID to start: ")
    if task_id.isdigit():
        start_task(int(task_id))
    else:
        print("Error: Task ID must be a number")