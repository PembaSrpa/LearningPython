student = {'name':'John', 'age':'21', 'courses':['Math', 'English']}
print(student)
print(student['courses'])
# print(student['phone'] error
print(student.get('courses'))
print(student.get('phone')) #prints none
print(student.get('phone', 'Not Found')) #prints Not Found
student['phone'] = '987192736'
student['name'] = 'Jane'
#to do all in one shot
student.update({'name': 'James', 'phone':'123'})
del student['courses'] #can also remove with pop
age= student.pop('age')
print(age)
print(student)

print(len(student))
print(student.keys())
print(student.values())
print(student.items())
