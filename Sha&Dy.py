# Import necessary libraries
import subprocess  # This library allows you to run external programs
import csv  # This library allows you to work with CSV files
import time

# Record the start time of the program execution
programStartTime = time.time()


# Function to run the executable with a username and pin and return the output
def runExe(username, pin):
    try:
        # Run the external program 'CrackMe.exe' with the provided username and pin as arguments
        out = subprocess.check_output(["CrackMe.exe", username, str(pin)], shell=True)
        # Convert the output from bytes to a string and remove any extra whitespace
        out = str(out, 'utf-8').strip()
        return out  # Return the program's output
    except subprocess.CalledProcessError as e:
        return str(e)  # Return an error message if there's an issue running the program

# Load the list of usernames from the CSV file
valid_usernames = []
with open('usernames.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        valid_usernames.extend(row)  # Add the usernames from the CSV file to the list

# Find valid username and pin combinations
valid_combinations = []
for username in valid_usernames:
    for pin in range(100, 1000):  # Try all 3-digit pins
        output = runExe(username, pin)  # Call the runExe function to check the combination
        if output == "User not found":
            break  # If the user is not found, move on to the next username
        elif output != "Incorrect Pin":
            valid_combinations.append((username, pin))  # If the pin is correct, add the combination to the list and move on to the next username
            break

# Print valid combinations
for username, pin in valid_combinations:
    print(f"Valid Combination: Username='{username}', Pin='{pin}'")  # Display the valid combinations found



# Calculate and print the time taken for the scan
print('Time taken:', time.time() - programStartTime)

# Call the runExe function with your values
output= runExe(username, pin)
print(output) # Print the result
