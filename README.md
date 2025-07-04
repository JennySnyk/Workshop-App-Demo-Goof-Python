# Workshop App Demo - Goof (Python Edition)

This is a deliberately vulnerable Python Flask application designed for security demonstrations. It is a Python port of the original Node.js and .NET Goof apps.

## Features

- **To-Do List**: A simple, functional to-do list application.
- **SAST Vulnerabilities**: Common web application vulnerabilities for Snyk Code to find.
- **SCA Vulnerabilities**: Dependencies with known vulnerabilities for Snyk Open Source to find.

## Screenshot

![Application Screenshot](assets/screenshot.png)

## Getting Started

### Prerequisites

- Python 3

### Installation & Running the App

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/JennySnyk/Workshop-App-Demo-Goof-Python.git
    ```
2.  **Navigate to the project directory:**
    ```bash
    cd Workshop-App-Demo-Goof-Python
    ```
3.  **Create and activate a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
4.  **Install the dependencies:**
    ```bash
    python3 -m pip install -r requirements.txt
    ```
5.  **Run the application:**
    ```bash
    python3 app.py
    ```

The application will be available at `http://localhost:5001`.

## Vulnerability Details

- **Command Injection**: `vulnerabilities/cmd_injection`
- **SQL Injection**: `vulnerabilities/sqli`
- **Hardcoded Secret**: `vulnerabilities/hardcoded_secret`
- **Vulnerable Dependency**: `PyYAML==5.1` (High-Severity Deserialization Vulnerability)
- **Path Traversal**: `vulnerabilities/path_traversal`
- **Cross-Site Scripting (XSS)**: `vulnerabilities/xss`
- **Insecure Deserialization**: `vulnerabilities/insecure_deserialization`

## Disclaimer

**This application is for educational and demonstration purposes only. Do not deploy it in a production environment.**
