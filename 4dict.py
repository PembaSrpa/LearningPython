# Demonstrates dictionary operations

student = {'name': 'John', 'age': '21', 'courses': ['Math', 'English']}
print(student)
print(student['courses'])           # Access value by key
# print(student['phone'])           # Error: key doesn't exist
print(student.get('courses'))       # Safe access
print(student.get('phone'))         # Returns None if key missing
print(student.get('phone', 'Not Found'))  # Default value if missing

student['phone'] = '987192736'      # Add new key-value
student['name'] = 'Jane'            # Update value

# Update multiple keys at once
student.update({'name': 'James', 'phone': '123'})

del student['courses']              # Delete key
age = student.pop('age')            # Remove and return value
print(age)
print(student)

print(len(student))                 # Number of keys
print(student.keys())               # List of keys
print(student.values())             # List of values
print(student.items())              # List of key-value pairs

for key in student:
    print(key)

for key, val in student.items():
    print(key, val)
