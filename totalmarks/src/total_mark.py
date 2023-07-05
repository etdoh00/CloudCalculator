def t_marks(module_marks):
    total = 0
    for k in module_marks:
        total += module_marks[k]
    for i in module_marks:
        if module_marks[i] > 100 or module_marks[i] < 0:
            return "Invalid module mark. Mark must not be below 0 or exceed 100!"
    return total
