### **Random Logger**

This project provides a simple Python-based logging utility that generates random log messages at various log levels (DEBUG, INFO, WARNING, ERROR, CRITICAL). It simulates typical log messages that might be encountered in real-world applications, such as database connections, system errors, and performance warnings. 

The script runs in an infinite loop, continuously logging messages to a file. It is designed to be easily run in a Docker container, ensuring that the logging service can be deployed consistently across environments.

### **Features:**

- **Random log generation:** Logs messages at different log levels (DEBUG, INFO, WARNING, ERROR, CRITICAL) randomly.
- **Customizable log file location:** The log file location can be configured via an environment variable (`LOG_FILE`).
- **Docker support:** The project includes a Dockerfile for easy containerization and deployment.
- **Continuous logging:** The script runs in a loop, logging messages indefinitely, simulating a long-running application.

### **Usage:**

- **Local Python Execution:** 
  1. Clone the repo.
  2. Install dependencies with `pip install -r requirements.txt` (if applicable).
  3. Run the logger with `python logger.py`.

- **Docker Execution:**
  1. Build the Docker image with `docker build -t random-logger .`.
  2. Run the container with `docker run -d --name random-logger random-logger`.
  
### **Customization:**

- You can modify the log messages and their frequency by editing the `logger.py` file.
- Customize the log file path by setting the `LOG_FILE` environment variable.