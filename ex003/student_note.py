# Create register for student 

student = dict()

student['name'] = str(input('Nome: '))
student['note'] = float(input(f'Note of {student["name"]}: '))

if student['note'] >= 7: 
   student['situation'] = 'Approve!'
elif 5 <=student['note'] < 7:
   student['situation'] = 'Recovery'
else: 
   student['situation'] = 'Reprove'   

print(student)
