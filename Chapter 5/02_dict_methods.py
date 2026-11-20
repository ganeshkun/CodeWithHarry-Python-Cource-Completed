marks = {
"Harry": 100,
"Shubam": 56,
"Rohan": 23

}

print(marks.items())  # Returns a list of tuples containing key-value pairs
print(marks.keys())   # Returns a list of all keys in the dictionary
print(marks.values()) # Returns a list of all values in the dictionary

# marks.update({"Rohan": 50})  # Updates the value of the key "Rohan" to 50

print(marks)  # Prints the updated dictionary

print(marks.get("Shubham"))  # Returns the value as none
print(marks["Harry"])  # Returns the value as error

print(marks.pop("Rohan"))  # Removes the key "Rohan" and returns its value  