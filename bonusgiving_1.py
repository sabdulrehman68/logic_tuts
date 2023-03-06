
class Employee:
    def __init__(self,employee_name,designation,salary,overTimeContribution, overTimeStatus=False):
        self.employee_name = employee_name
        self.designation = designation
        self.salary = salary
        self.overTimeContribution = overTimeContribution
        self.overTimeStatus = overTimeStatus

class Organization():
    def __init__(self,employee_list):
        self.employee_list = employee_list

    def elegible(self,threshold):
        sum = 0
        for employee in self.employee_list:   
            for i in employee.overTimeContribution.values():
                sum+=i
            if sum >= threshold:
                employee.overTimeStatus = True
        
        return employee.overTimeStatus

    def bonus(self,rate):
        sum = 0
        total_bonus = 0
        for employee in self.employee_list:
            for i in employee.overTimeContribution.values():
                sum+=i
            if employee.overTimeStatus == True:
                bonus_offered = rate * sum
        total_bonus += bonus_offered
        return total_bonus

if __name__ == "__main__":
    
    employeeCount = int(input())
    employeeList = []

    
    for employee in range(0,employeeCount):
        employeeName = str(input())
        designation = str(input())
        salary = int(input())
        overtimeMonths = int(input())
        
        overtimeDict ={}

        for month in range(0,overtimeMonths):
           
            key = str(input())
            val = int(input())

            overtimeDict[key] = val

        employeeList.append(Employee(employeeName, designation,salary, overtimeDict,overTimeStatus=False))    
    
    newOrg = Organization(employeeList)

  
    overtimeThreshold = int(input())

    isEligible = newOrg.elegible(overtimeThreshold)

    bonusRate = int(input())

    # Calculate Bonus    
    for employee in employeeList:
        
        total_bonus = newOrg.bonus(bonusRate)

    # Print data of each employee
    for employee in employeeList:
        print(f"{employee.employee_name} {employee.overTimeStatus}")
        


    if isEligible:
            print(total_bonus)






    
    





