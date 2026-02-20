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

gradeList = {"Anna":85,"Jānis":72,"Līga":95}
gradeList["Valters"] = 92 # Adds new student to dictionary
gradeList.pop("Līga") # Removes "Līga" from dictionary
gradeList["Līga"] = 95 # Adds "Līga" back to dictionary
gradeList["Jānis"] = 75 # Changes value of "Jānis" in dictionary

for name, grade in gradeList.items():
    print(f'{name} : {grade}')

topStud = max(gradeList, key=gradeList.get) # Finds the highest value grade in dictionary returns entry name
topGrade = gradeList[topStud] # Returns grade value for topStud
print(f'Labākais students: {topStud} ({topGrade})')