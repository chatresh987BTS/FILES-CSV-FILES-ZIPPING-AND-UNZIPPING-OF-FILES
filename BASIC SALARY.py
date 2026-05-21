CALCULATE THE BASIC SALARY OF THE EMPLOYEE USING CSV FILES.
import csv
def create_employee_csv(filename):
    headers = ["Employee ID", "Name", "Basic Pay"]
    employees = [["E001", "X", 150000],["E002", "Y", 180000],["E003", "Z", 170000],["E004", "A", 160000],["E005", "B", 140000]]
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(employees)
    print(f"Success: '{filename}' created with 5 records!")
if __name__ == "__main__":
    create_employee_csv("employees.csv")
    def cal_sal(basic_pay):
        hra = 0.20 * basic_pay
        da = 0.10 * basic_pay
        return basic_pay + hra + da
    def disp_emp(filename):
        print(f"{'ID':<8} {'Name':<12} {'Basic Pay':<12} {'Total Salary':<12}")
        print("-" * 48)
        with open(filename, "r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                emp_id = row["Employee ID"]
                name = row["Name"]
                basic_pay = float(row["Basic Pay"])
                total_salary = cal_sal(basic_pay)
                print(f"{emp_id:<8} {name:<12} ₹{basic_pay:<11.2f} ₹{total_salary:<11.2f}")
            print("-" * 48)
    if __name__ == "__main__":
        disp_emp("employees.csv")
