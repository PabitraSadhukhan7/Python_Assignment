class Employee:
    def __init__(self, name, years_of_service):
        self.name = name
        self.years_of_service = years_of_service

    def salary(self):
        return 1500 + 100 * self.years_of_service

class Manager(Employee):

    def salary(self):
        return 2500 + 120 * self.years_of_service

database = {
    "Rahul": Employee("Rahul", 3),
    "Bikash": Employee("Bikash", 1),
    "Rajan": Manager("Rajan", 10),
    "Priya": Manager("Priya", 3)
}
table = []

total_salary = 0

for name, obj in database.items():
    sal = obj.salary()
    table.append([name, sal])
    total_salary += sal
print("Name\tSalary")
for row in table:
    print(row[0], "\t", row[1])

average_salary = total_salary / len(database)

print("\nTable Format:")
print(table)

print("\nAverage Salary =", average_salary)