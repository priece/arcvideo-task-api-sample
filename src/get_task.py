import requests
import json

# Replace with your own site URL and token
API_BASE_URL = "http://172.17.5.12/api/v8.0"
ACCESS_TOKEN = "t_848e7967e6d4c3c4638c057932873edb"

headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}

def get_task(task_id):
    """Get task details
    Args:
        task_id: Numeric task ID
    """
    url = f"{API_BASE_URL}/task/get/{task_id}"
    
    # Validate task_id is numeric
    if not isinstance(task_id, (int, float)) and not str(task_id).isdigit():
        print("Error: task_id must be a number")
        return None
        
    try:
        response = requests.get(
            url, 
            headers=headers
        )
        response.raise_for_status()
        print("Task details retrieved successfully:", response.json())
        return response.json()
    except requests.exceptions.RequestException as e:
        print("Failed to get task:", str(e))
        return None

if __name__ == "__main__":
    # Example usage:
    # task_id = "your_task_id_here"
    # get_task(task_id)
    
    # Or get task_id from user input
    task_id = input("Enter task ID to get details: ")
    if task_id.isdigit():
        get_task(int(task_id))
    else:
        print("Error: Task ID must be a number")