students = {
    "Lorenzo": [85, 90, 88],
    "Amelie": [78, 82, 84]
}

def calculate_average(grades):
    return sum(grades) / len(grades)

for student, grades in students.items():
    avg = calculate_average(grades)
    print(f"{student}'s average grade: {avg:.2f}")