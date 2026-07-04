import os
from datetime import datetime


# ==========================
# Save Report
# ==========================

def save_report(filename, data):

    with open(filename, "w", encoding="utf-8") as file:
        file.write(data)


# ==========================
# Write Activity Log
# ==========================

def write_log(activity):

    # Project root directory
    project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Logs folder
    log_folder = os.path.join(project_dir, "logs")

    # Create logs folder if it doesn't exist
    os.makedirs(log_folder, exist_ok=True)

    # Log file
    log_file = os.path.join(log_folder, "history.txt")

    # Current date and time
    now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    # Write activity
    with open(log_file, "a", encoding="utf-8") as file:
        file.write(f"[{now}] {activity}\n")