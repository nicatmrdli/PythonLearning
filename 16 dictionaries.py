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
print(monthConversions["Mar"])

print(monthConversions.get("Luv", "Not a valid key"))
# Use ".get" to specify defualt value if a certain key is not found.
# Write comma after the value to write a string that can replace "None" on terminal.
# You can also use numbers instead of strings.


