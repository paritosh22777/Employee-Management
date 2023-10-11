import random


def generateEmpID():
    return random.randint(100000, 999999)


def validateName(name):
    l = name.split(' ')
    if len(l) == 2:
        first_name = l[0]
        last_name = l[1]
        if last_name == '.' and first_name.isalpha() and first_name.istitle():
            return True
        if first_name.isalpha() and first_name.istitle() and last_name.isalpha() and last_name.istitle():
            return True
    return False


def validateEmail(email):
    if email.find('@') == -1 and email.find('.') == -1:
        return False
    return True


def validateUniqueEmail(EmployeeList, email):
    for i in EmployeeList:
        if i.email == email:
            return False
    return True


def validateSalary(sal):
    if str(sal).isdigit() and sal > 0:
        return True
    return False


def validateAge(age):
    if str(age).isdigit() and age > 18:
        return True
    return False


def validateGender(g):
    if g == 'M' or g == 'F':
        return True
    return False


def validateContactNo(phno):
    if len(phno) == 10 and phno.isdigit():
        return True
    return False


def validateUniqueContactNo(EmployeeList, phno):
    for i in EmployeeList:
        if i.phoneNo == phno:
            return False
    return True


def isLeapYear(year):
    if year % 400 == 0 and year % 100 == 0:
        return True
    if year % 4 == 0 and year % 100 != 0:
        return True
    return False


def validateDOB(dob):
    l = dob.split('/')
    if int(l[0]) >= 1 and int(l[0]) <= 31 and int(l[1]) >= 1 and int(l[1]) <= 12:
        if int(l[1]) == 2:
            if int(l[0]) > 29 or isLeapYear(int(l[2])) == False:
                return False
        return True
    return False


def validateDOJ(doj):
    return validateDOB(doj)


def validateDeptName(dept):
    departments = [
        'HR',
        'IT',
        'Sales and Marketing',
        'Finance',
        'Operations',
        'R&D',
        'Customer Support',
        'Product Management',
        'QA',
        'Administration',
        'Procurement',
        'Training and Development',
    ]

    if dept in departments:
        return True
    return False


def validateDesignation(desig):
    designations = [
        'CEO',
        'COO',
        'CFO',
        'CTO',
        'CMO',
        'CIO',
        'HR Manager',
        'IT Manager',
        'Sales Manager',
        'Marketing Manager',
        'Project Manager',
        'Team Lead',
        'Software Engineer',
        'Data Analyst',
        'Accountant',
        'Administrative Assistant',
        'Customer Support Representative',
        'Graphic Designer',
        'Quality Assurance Analyst',
        'Research and Development Engineer',
        'Product Manager',
        'Operations Manager',
        'Business Analyst',
        'Financial Analyst',
        'Legal Counsel',
        'Executive Assistant',
        'Network Administrator',
        'Systems Administrator',
        'Procurement Specialist',
        'Training and Development Specialist'
    ]

    if desig in designations:
        return True
    return False


def validatePan(pan):
    first_five = pan[0:5]
    last_digit = pan[9:10]
    digits = pan[6:9]
    if len(pan) == 10 and first_five.isalpha() and first_five.isupper() and digits.isdigit() and last_digit.isalpha() and last_digit.isupper():
        return True
    return False


def validateUniquePanId(EmployeeList, pan):
    for i in EmployeeList:
        if i.pan == pan:
            return False
    return True


def validateAadhaar(aadhaar):
    if len(aadhaar) == 12 and aadhaar.isdigit():
        return True
    return False


def validateUniqueAadhaarNo(EmployeeList, aadhaar):
    for i in EmployeeList:
        if i.aadhaar == aadhaar:
            return False
    return True
