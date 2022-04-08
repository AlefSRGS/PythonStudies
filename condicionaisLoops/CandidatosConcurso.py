entry = input()
values = entry.split()
total_candidates = int(values[0])
cut_grade = float(values[1])

candidates_grades = dict()

for i in range(total_candidates):
    entry = input()
    values = entry.split()
    candidates_grades[values[0]] = float(values[1])


sorted_grades_candidates = list()
for candidate, grade in candidates_grades.items():
    sorted_grades_candidates.append([grade, candidate])

sorted_grades_candidates.sort(reverse=True)

has_separator = False
for i in range(len(sorted_grades_candidates)):
    grade_candidate = sorted_grades_candidates[i]
    grade = grade_candidate[0]
    candidate = grade_candidate[1]
    if grade < cut_grade and not has_separator:
        print('------------------------------')
        has_separator = True

    print('#{0} - {1} - {2:.1f}'.format(i+1, candidate, grade))
