'''A virtual environment is a tool used to isolate specific Python environments on a single machine, allowing you to work on multiple projects with different dependencies and packages without conflicts. This can be especially useful when working on projects that have conflicting package versions or packages that are not compatible with each other. here it allows a user to install like different pythons in the same pc with different dependencies and versions . this is helpful for the collaborative task.'''


# Create a virtual environment
python -m venv myenv

# Activate the virtual environment (Linux/macOS)
source myenv/bin/activate

# Activate the virtual environment (Windows)
myenv\Scripts\activate.bat

# Activate the virtual environment (Windows - powershell)
myenv\Scripts\activate.ps


# to install the module or package with a specific version
pip3 install pandas==1.3.5 (version)

# Deactivate the virtual environment
deactivate
# Remove the virtual environment
rm -rf myenv

# Output the list of installed packages and their versions to a file to send someone
pip freeze > requirements.txt

# Install the packages listed in the requirements.txt file in a different pc.
pip install -r requirements.txt

