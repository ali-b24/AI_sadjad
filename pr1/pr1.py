
def my_final_calculation(filename='students.txt'):
    with open(filename, 'r') as f:
        lines = f.readlines()
        grades = {}
        for line in lines:
            # spliting data
            data = line.strip().split(',')
            # lowering names
            name = data[0].lower()
            # reading exam grades minus 2 failed grade
            exam_grades = sorted([int(x) for x in data[1:6]])[2:]
            exam_avg = sum(exam_grades) / 4
            # reading assignment grades minus 1 failed grade
            assignment_grades = sorted([int(x) for x in data[7:10]])[1:]
            assignment_avg = sum(assignment_grades) / 3
            # reading midterm grade
            midterm = int(data[11])
            # reading final exam grade
            final = int(data[12])
            # defining the weight of exam
            exam_weight = 0.25
            # defining the weight of assignment
            assignment_weight = 0.25
            # defining the weight of midterm
            midterm_weight = 0.25
            # defining the weight of final exam
            final_weight = 0.25
            # calculation of total grade
            total_grade = (exam_avg * exam_weight) + (assignment_avg * assignment_weight) + (midterm * midterm_weight) + (final * final_weight)
            grades[name] = total_grade
            # final result
            if total_grade >= 60:
                grades[name] = 'pass'
            else:
                grades[name] = 'Failed'
        return grades
    
print(my_final_calculation())