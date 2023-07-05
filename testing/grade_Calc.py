def calcGrade(module_marks):
    for i in module_marks:
          if module_marks[i] > 100 or module_marks[i] < 0:
            return "Invalid module mark. Mark must not be below 0 or exceed 100!"
    
    new_dict={}

    for key, value in module_marks.items():
            if value >= 70:
                new_dict[key] = "First"
            elif value >= 60 and value <= 69:
                new_dict[key] = "2:1"
            elif value >= 50 and value <= 59:
                new_dict[key] = "2:2"
            elif value >= 40 and value <= 49:
                new_dict[key] = "Third"
            elif value < 40:
                new_dict[key] = "Fail"
    return new_dict



