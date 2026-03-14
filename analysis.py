import csv
import io

data = """name,department,salary,active,years,city
Alice,Finance,72000,Yes,5,Stockholm
Bob,Engineering,95000,Yes,3,Oslo
Carol,HR,61000,Yes,7,Stockholm
Dan,Finance,83000,No,2,Copenhagen
Eve,Engineering,105000,Yes,6,Stockholm
Frank,HR,58000,Yes,1,Oslo
Grace,Finance,91000,Yes,9,Copenhagen
Henry,Engineering,88000,No,4,Stockholm
Iris,HR,64000,Yes,3,Copenhagen
Jack,Finance,77000,Yes,8,Oslo
Karen,Engineering,112000,Yes,11,Stockholm
Leo,HR,69000,Yes,5,Copenhagen
Maria,Finance,54000,No,1,Oslo
Nick,Engineering,98000,Yes,7,Copenhagen
Olivia,HR,73000,Yes,6,Stockholm"""

reader = csv.DictReader(io.StringIO(data))
employees = list(reader)

total = 0
employee_counter = 0

for emp in employees:
    if emp["active"] == "Yes":
        total = total + int(emp["salary"])
        employee_counter = employee_counter + 1

average_salary = total / employee_counter

print("Total:", total)
print("Average:", average_salary)