import employee_info

def test_employee_age_range():
    emp_list = [{"name": "John", "age": 30, "department": "Sales", "salary": 50000},
    {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},]
    result = employee_info.get_employees_by_age_range(24,31)
    assert emp_list == result
def test_average_salary():
    result = employee_info.calculate_average_salary()
    assert result == 60166.67
def test_get_employee_data():
    arr = [
    {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
     {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000},]
    result = employee_info.get_employees_by_dept('Marketing')
    assert arr == result
