monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}
# Always make sure to use "{}" for dictionary

print(monthConversions["Mar"])
# Use this code to access your dictionary

print(monthConversions.get("Aug"))
# This is another way to access you dictionary

print(monthConversions.get("Luv", "Not a valid key"))
# Use ".get" to specify default value if a certain key is not found in the dictionary.
# Write comma after the value to write a string that can replace "None" on terminal.
# You can also use numbers instead of strings.


