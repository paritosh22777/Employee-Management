from validate import *


class Employee:
    def __init__(self, id, name, email, sal, age, gender, phoneNo, address, city, dob, doj, dept, desig, pan, aadhaar):
        self.id = id
        self.name = name
        self.email = email
        self.sal = sal
        self.age = age
        self.gender = gender
        self.phoneNo = phoneNo
        self.address = address
        self.city = city
        self.dob = dob
        self.doj = doj
        self.dept = dept
        self.desig = desig
        self.pan = pan
        self.aadhaar = aadhaar

    def display(self):
        print("ID: ", self.id)
        print("Name: ", self.name)
        print("Email: ", self.email)
        print("Salary: Rs.", self.sal)
        print("Age: ", self.age, "years")
        print("Gender: ", self.gender)
        print("Contact number: ", self.phoneNo)
        print("Address: ", self.address)
        print("City: ", self.city)
        print("Date of birth: ", self.dob)
        print("Date of joining: ", self.doj)
        print("Department name: ", self.dept)
        print("Designation: ", self.desig)
        print("PAN ID: ", self.pan)
        print("Aadhaar number: ", self.aadhaar)
        print("")


EmployeeList = []
SalaryList = []


while True:
    print("1. Press 1 to add the record")
    print("2. Press 2 to display the record")
    print("3. Press 3 to delete the record")
    print("4. Press 4 to update the record")
    print("5. Press 5 to search the record")
    print("6. Press 6 to display the employee details with highest salary")
    print("7. Press 7 to display the employee details with lowest salary")
    print("8. Press 8 to exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        id = generateEmpID()
        while True:
            name = input("Enter employee name (name should be in 'FirstName LastName'. If LastName does not exist, enter '.'): ")
            if validateName(name):
                break
            else:
                print("Invalid name format.")
        while True:
            f = 2
            email = input("Enter employee email: ")
            if (validateEmail(email)):
                if validateUniqueEmail(EmployeeList, email):
                    break
                else:
                    f = 1
            else:
                f = 2
            if f == 1:
                print("Email already present.")
            else:
                print("Invalid email entered.")
        while True:
            salary = int(input("Enter employee salary: "))
            if (validateSalary(salary)):
                SalaryList.append(salary)
                break
            else:
                print("Invalid salary entered.")
        while True:
            age = int(input("Enter employee age: "))
            if (validateAge(age)):
                break
            else:
                print("Invalid age entered.")
        while True:
            gender = input("Enter 'M' for male or 'F' for female: ")
            if gender == 'M':
                gender = 'Male'
            if gender == 'F':
                gender == 'Female'
            if (validateGender(gender)):
                break
            else:
                print("Invalid gender entered.")
        while True:
            f = 2
            phoneNo = input("Enter mobile number: ")
            if validateContactNo(phoneNo):
                if validateUniqueContactNo(EmployeeList, phoneNo):
                    break
                else:
                    f = 1
            else:
                f = 2
            if f == 1:
                print("Mobile number already present.")
            else:
                print("Invalid mobile number entered.")
        address = input("Enter the address: ")
        city = input("Enter city: ")
        while True:
            dob = input("Enter date of birth (in DD/MM/YYY): ")
            if validateDOB(dob):
                break
            else:
                print("Invalid date entered.")
        while True:
            doj = input("Enter date of joining (in DD/MM/YYY): ")
            if (validateDOJ(doj)):
                break
            else:
                print("Invalid date entered.")
        while True:
            dept = input("Enter the department: ")
            if (validateDeptName(dept)):
                break
            else:
                print("Department does not exist.")
        while True:
            desig = input("Enter the designation: ")
            if (validateDesignation(desig)):
                break
            else:
                print("Designation does not exist.")
        while True:
            f = 2
            pan = input("Enter the PAN ID: ")
            if (validatePan(pan)):
                if validateUniquePanId(EmployeeList, pan):
                    break
                else:
                    f = 1
            else:
                f = 2
            if f == 1:
                print("PAN ID already present.")
            else:
                print("Invalid PAN ID entered.")
        while True:
            f = 2
            aadhaar = input("Enter the Aadhaar number: ")
            if (validateAadhaar(aadhaar)):
                if validateUniqueAadhaarNo(EmployeeList, aadhaar):
                    break
                else:
                    f = 1
            else:
                f = 2
            if f == 1:
                print("Aadhaar number already present.")
            else:
                print("Invalid Aadhaar number entered.")
        print("Employee having employee id", id, "inserted.")
        print("")
        obj = Employee(id, name, email, salary, age, gender, phoneNo,
                       address, city, dob, doj, dept, desig, pan, aadhaar)
        EmployeeList.append(obj)    
    elif choice == 2:
        if len(EmployeeList) == 0:
            print("No employee details exists.")
        else:
            for i in EmployeeList:
                i.display()
    elif choice == 3:
        if len(EmployeeList) == 0:
            print("No employee details exists.")
        else:
            inputID = int(
                input("Enter the employee ID for which the record has to be deleted: "))
            flag = False
            for i in EmployeeList:
                if i.id == inputID:
                    flag = True
                    break
            if flag:
                EmployeeList.remove(i)
                print("Details of employee with ID", inputID, "deleted.")
            else:
                print("Employee with id", inputID, "not found.")
        print("")
    elif choice == 4:
        if len(EmployeeList) == 0:
            print("No employee details exists.")
        else:
            while True:
                print("1. Enter 1 to update name of employee")
                print("2. Enter 2 to update address of employee")
                print("3. Enter 3 to update DOB of employee")
                print("4. Enter 4 to update salary of employee")
                print("5. Enter 5 to exit")
                updateChoice = int(input("Enter the option: "))
                if updateChoice == 1:
                    inputID = int(input("Enter the employee id:"))
                    flag = False
                    for i in EmployeeList:
                        if i.id == inputID:
                            flag = True
                            break
                    if flag:
                        updatedName = input("Enter the new employee name: ")
                        i.name = updatedName
                        print("Employee name updated.")
                    else:
                        print("Employee with id", inputID, "does not exist.")
                elif updateChoice == 2:
                    # 
                    inputID = int(input("Enter the employee id:"))
                    for i in EmployeeList:
                        if i.id == inputID:
                            updatedAddress = input(
                                "Enter the new employee address: ")
                            i.address = updatedAddress
                            print("Address of employee updated.")
                elif updateChoice == 3:
                    inputID = int(input("Enter the employee id:"))
                    for i in EmployeeList:
                        if i.id == inputID:
                            updatedDOB = input(
                                "Enter the new date of birth of the employee: ")
                            i.dob = updatedDOB
                            print("Date of birth with employee ID", inputID,"updated.")
                elif updateChoice == 4:
                    print(
                        "1. Enter 1 to update the salary of specific employee by employee id.")
                    print(
                        "2. Enter 2 to update the salary of all employees working in specific department.")
                    print("3. Enter 3 to update the salary of all employees")
                    print("4. Enter 4 to exit")
                    updateSalaryChoice = int(input("Enter the option: "))
                    if updateSalaryChoice == 1:
                        inputID = int(input("Enter the employee id: "))
                        for i in EmployeeList:
                            if i.id == inputID:
                                inputSalary = int(input("Enter the salary: "))
                                i.sal = inputSalary
                                print("Salary of employee with ID", inputID, "updated.")
                    elif updateSalaryChoice == 2:
                        inputDept = input("Enter the department: ")
                        for i in EmployeeList:
                            if i.dept == inputDept:
                                inputSalary = int(input("Enter the salary: "))
                                i.sal = inputSalary
                                print("Salary of employees with department", inputDept, "updated.")
                    elif updateSalaryChoice == 3:
                        inputSalary = int(input("Enter the salary: "))
                        for i in EmployeeList:
                            i.sal = inputSalary
                            print("Salary of all the employees updated.")
                    elif updateSalaryChoice == 4:
                        break
                    else:
                        print("Invalid choice entered.")
                    print("")
                elif updateChoice == 5:
                    break
                else:
                    print("Invalid choice")
        print("")
    elif choice == 5:
        if len(EmployeeList) == 0:
            print("No employee details exists.")
        else:
            while True:
                print("1. Enter 1 to search the details of specific employee by employee id")
                print("2. Enter 2 to search by employee name")
                print("3. Enter 3 to search by Department name")
                print("4. Enter 4 to exit")
                searchChoice = int(input("Enter the choice: "))
                if searchChoice == 1:
                    inputID = int(input("Enter the employee ID: "))
                    for i in EmployeeList:
                        if i.id == inputID:
                            i.display()
                        else:
                            print("Employee ID is invalid.")
                elif searchChoice == 2:
                    inputName = input("Enter the employee name: ")
                    for i in EmployeeList:
                        if i.name == inputName:
                            i.display()
                        else:
                            print("Employee name is invalid.")
                elif searchChoice == 3:
                    inputDept = input("Enter the employee department: ")
                    for i in EmployeeList:
                        if i.dept == inputDept:
                            i.display()
                        else:
                            print("Employee department is invalid.")
                elif searchChoice == 4:
                    break
                else:
                    print("Invalid search choice.")
        print("")
    elif choice == 6:
        if len(SalaryList) == 0:
            print("Employee list is empty. Please enter the records in the list.")
        else:
            maxSal = max(SalaryList)
            print("Details of employees with maximum salary:")
            for i in EmployeeList:
                if i.sal == maxSal:
                    i.display()
        print("")
    elif choice == 7:
        if len(SalaryList) == 0:
            print("Employee list is empty. Please enter the records in the list.")
        else:
            minSal = min(SalaryList)
            print("Details of employees with minimum salary:")
            for i in EmployeeList:
                if i.sal == minSal:
                    i.display()
        print("")
    elif choice == 8:
        print("Program terminated successfully.")
        break
    else:
        print("Invalid choice entered.")