"""
Declare a dictionary with any key-value pair of items/elements
Print the dictionary in console
Update the dictionary with two different key-value pair items
Print the dictionary in console again
"""

biodata = {
    'name': 'Fisayo',
    'age': 21,
    'marital_status': 'single',
    'occupation': 'Test Automation Engineer'
}

print(biodata)

updateDict = biodata.update({'complexion': 'Dark', 'Bestie': 'Diane'})
print(biodata)