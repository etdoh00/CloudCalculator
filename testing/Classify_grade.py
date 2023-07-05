
def classifyGrade(module_marks):
    total = 0
    for k in (module_marks):
        if module_marks[k] > 100 or module_marks[k] < 0:
             return "Invalid module mark. Mark must not be below 0 or exceed 100!"
    for i in (module_marks):
        total+= module_marks[i]

    average = total/len(module_marks)
    if average >100 or average < 0:
        return "Invalid average. Must not be below 0 or exceed 100"

    if average >= 70:
        return("Classification is a first")
    elif average >=60 and average <= 69:
        return("Classification is a 2:1")
    elif average >=50 and average <= 59:
        return("Classfication is a 2:2")
    elif average >=40 and average <= 49:
        return("Classification is a third")
    elif average <40:
        return("No classification awarded, mark too low")    



