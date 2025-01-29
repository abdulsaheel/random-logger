import random
import time

# Sample log messages by level
DEBUG_MESSAGES = [
    "Debugging connection to the database.",
    "Querying database with parameters: {'user_id': 1234, 'filter': 'active'}",
    "Entering function: calculate_statistics()",
]

INFO_MESSAGES = [
    "Data processed successfully for user ID 4321.",
    "Scheduled task 'daily_backup' completed without errors.",
    "User session started for user ID 5678.",
]

WARNING_MESSAGES = [
    "API response time is slower than expected.",
    "Disk space running low: only 10% remaining.",
    "Memory usage is nearing the limit.",
]

ERROR_MESSAGES = [
    "Failed to load configuration file.",
    "Database connection lost. Retrying...",
    "Error processing user data for user ID 9876.",
]

CRITICAL_MESSAGES = [
    "System shutdown imminent: unable to recover from error.",
    "Data corruption detected in core database.",
    "Critical failure: unable to write to disk.",
]

# Function to print a random message from each level
def print_random_message():
    level = random.choice(['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'])
    message = ""
    
    if level == 'DEBUG':
        message = random.choice(DEBUG_MESSAGES)
    elif level == 'INFO':
        message = random.choice(INFO_MESSAGES)
    elif level == 'WARNING':
        message = random.choice(WARNING_MESSAGES)
    elif level == 'ERROR':
        message = random.choice(ERROR_MESSAGES)
    elif level == 'CRITICAL':
        message = random.choice(CRITICAL_MESSAGES)
    
    print(f"[{level}] {message}")

# Infinite loop to keep printing
try:
    while True:
        print_random_message()
        time.sleep(0.5)  # Fixed pause of 0.5 seconds
except KeyboardInterrupt:
    print("Logger service stopped by user.")
