print("Student Records Manager")
print("-----------------------")

students = [
    {"name": "Alice", "score": 85},
    {"name": "Ben", "score": 72},
    {"name": "Cathy", "score": 90},
    {"name": "David", "score": 45},
    {"name": "Ella", "score": 58}
]

total_score = 0
pass_count = 0
fail_count = 0
results = []

print()
print("Student Records")
print("---------------")

for student in students:
    name = student["name"]
    score = student["score"]

    if score >= 50:
        result = "Pass"
        pass_count += 1
    else:
        result = "Fail"
        fail_count += 1

    student["result"] = result
    results.append(result)
    total_score += score

    print(f"Name: {name}, Score: {score}, Result: {result}")

average_score = total_score / len(students)
unique_results = set(results)

print()
print("Summary Report")
print("--------------")
print(f"Number of students: {len(students)}")
print(f"Average score: {average_score:.2f}")
print(f"Students passed: {pass_count}")
print(f"Students failed: {fail_count}")
print(f"Unique result categories: {unique_results}")

print()
print("Updated Student Data")
print("--------------------")

for student in students:
    print(student)







