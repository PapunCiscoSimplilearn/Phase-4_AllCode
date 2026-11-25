class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_employee(self):
        print("Employee Name:", self.name)
        print("Salary:", self.salary)


class Developer(Employee):
    def __init__(self, name, salary, technology):
        super().__init__(name, salary)
        self.technology = technology

    def display_technology(self):
        print("Technology:", self.technology)


class Manager(Employee):
    def __init__(self, name, salary, team):
        super().__init__(name, salary)
        self.team = team

    def display_team(self):
        print("Team:", self.team)


class SeniorDeveloper(Developer):
    def mentor(self):
        print(self.name, "is mentoring the development team.")


class WorkFromHome:
    def work_remotely(self):
        print(self.name, "can work remotely.")


class TechnicalLead(Developer, WorkFromHome):
    def lead_project(self):
        print(self.name, "is leading a project.")


def main():
    print("Single inheritance: Developer inherits Employee")
    developer = Developer("Irfan", 80000, "Python")
    developer.display_employee()
    developer.display_technology()

    print("\nHierarchical inheritance: Developer and Manager inherit Employee")
    manager = Manager("Amina", 100000, "Platform")
    manager.display_employee()
    manager.display_team()

    print("\nMultilevel inheritance: SeniorDeveloper inherits Developer")
    senior_developer = SeniorDeveloper("Ravi", 110000, "Java")
    senior_developer.display_employee()
    senior_developer.display_technology()
    senior_developer.mentor()

    print("\nMultiple inheritance: TechnicalLead inherits Developer and WorkFromHome")
    technical_lead = TechnicalLead("Sara", 120000, "Python")
    technical_lead.display_employee()
    technical_lead.work_remotely()

    print("\nHybrid inheritance: TechnicalLead combines single and multiple inheritance")
    technical_lead.lead_project()


if __name__ == "__main__":
    main()