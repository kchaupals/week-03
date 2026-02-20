# A part of the task

numberList = [1,2,3,4,5,6]

numberList.append(7) # Adds int 7 to end of the list
numberList.append(12) # Adds int 12 after int 7
numberList.pop(0) # Removes index 0 value from list

# Sets variables for the loop
numberSum = 0 # Sets the starting SUM as 0
listCount = 0 # Sets the list count as 0
evenNumList = [] # Creates empty list for even numbers
oddNumList = [] # Creates empty list for odd numbers
for number in numberList: # For Loop that goes trough list and summs up all the int values 
    numberSum += number
    listCount = listCount + 1
    if number %2 == 0:
        evenNumList.append(number)
    else:
        oddNumList.append(number)

averageNum = round(numberSum / listCount, 1)

print('*** --- Saraksti ---  ***')
print(f'*** Summa: {numberSum}, Vidējais: {averageNum}')
print(f'*** Pāra skaitļi: {evenNumList}')
print(f'*** Nepāra skaitļi: {oddNumList}')
print(f'*** Pirmie 3: {numberList[slice(0,3)]}, Pēdējie 2: {numberList[slice(-2, None)]}') # Outputs first 3, Last 2 elements from list 
print(f'*** Katrs 2: {numberList[slice(None, None, 2)]}') # Outputs elements gap by two from list

# B part of the task
print('*** --- Vārdnīcas ---  ***')

gradeList = {"Anna":85,"Jānis":72,"Līga":95}
gradeList["Valters"] = 92 # Adds new student to dictionary
gradeList.pop("Līga") # Removes "Līga" from dictionary
gradeList["Līga"] = 95 # Adds "Līga" back to dictionary
gradeList["Jānis"] = 75 # Changes value of "Jānis" in dictionary

for name, grade in gradeList.items():
    print(f'*** {name} : {grade}')

topStud = max(gradeList, key=gradeList.get) # Finds the highest value grade in dictionary returns entry name
topGrade = gradeList[topStud] # Returns grade value for topStud
print(f'*** Labākais students: {topStud} ({topGrade})')

# C part of the task
print('*** --- Kombinācijas ---  ***')
studentList = [{"name": "Anna", "grade": 85},{"name": "Jānis", "grade": 72}, {"name": "Līga", "grade": 95}, {"name": "Valters", "grade": 92}]
topStudents = []
for student in studentList:
    if student["grade"] >= 80: # Collects all the passed data and stores matching one in dictionary topStudents
        topStudents.append({"name": student["name"], "grade": student["grade"]})
print('***--- Studenti ar atzīmi >= 80 ---')
for index, student in enumerate(topStudents, start= 1): # Sets enumerate to start with 1, if not passed index value will be starting as 0
    print(f'*** {index}. {student["name"]} - {student["grade"]}')