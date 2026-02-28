class Company:
    def __init__(self, name):
        self.name = name
        self.employees = {}

    class Employee:
        def __init__(self, name, empno, city, state):
            self.name = name
            self.empno = empno
            self.city = city
            self.state = state
        
    def add_employee(self, emp):
        self.employees.append(emp)


e = Company("TCS")

employee_data = [
    {"name": "Madhu",  "empno": 101, "city": "Chennai",   "state": "Tamil Nadu"},
    {"name": "Alice",  "empno": 102, "city": "Bangalore",  "state": "Karnataka"},
    {"name": "Bob",    "empno": 103, "city": "Mumbai",     "state": "Maharashtra"}
]

print(f"Company: {e.name}")

for emp in employee_data:
    print(f"Employee Name: {emp['name']}, Emp No: {emp['empno']}, City: {emp['city']}, State: {emp['state']}")