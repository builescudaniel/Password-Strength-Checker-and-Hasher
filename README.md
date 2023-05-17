# Password-Strength-Checker-and-Hasher
"Password Strength Checker and Hasher" is a Python script designed to evaluate password robustness and generate its SHA256 hash. It checks length, character diversity, and common sequence avoidance to ensure password strength, providing an additional layer of security with password encryption.

This Python script checks the strength of a password. It assesses the password based on several criteria:
- Length of the password (at least 8 characters)
- Presence of at least one digit
- Presence of at least one uppercase letter
- Presence of at least one lowercase letter
- Presence of at least one special character
- Absence of common sequences (e.g., "123", "abc", "password", "admin", "qwerty")
- Absence of repeated characters
- After these checks, the script will classify the password as either "Strong password" or "Weak password".

Additionally, the script hashes the password using SHA256.

# How to Use

Clone this repository to your local machine. You can then run the script using a Python interpreter. The script will prompt you to enter a password. For security reasons, the password will not be displayed as you type it. After you've entered the password, the script will display its strength and its SHA256 hash.

# Setting Up a Virtual Environment (Optional)

If you wish to run the script in a virtual environment, you can do so using venv. This is generally a good practice as it isolates the script and its dependencies from your global Python environment. To set up a virtual environment:

Navigate to the directory where the script is located.
Create a virtual environment: ```python3 -m venv env```
Activate the virtual environment:
On macOS and Linux: ```source env/bin/activate```
On Windows: ```.\env\Scripts\activate```
Your virtual environment is now active and you can run the script.

# Requirements
This script requires Python 3. No external libraries are required.
