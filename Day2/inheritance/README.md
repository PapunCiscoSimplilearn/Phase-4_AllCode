# Inheritance in Python

Inheritance is an object-oriented programming concept where a child class receives the attributes and methods of a parent class. It supports code reuse, reduces duplication, improves organization, and makes classes easier to extend.

## Employee example

`Employee` is the parent class. It stores an employee's name and salary and defines `display_employee()`. `Developer` and `Manager` are child classes that add their own data and methods while reusing the employee behavior.

In `class Developer(Employee)`, `Developer` inherits from `Employee`. The call `super().__init__(name, salary)` runs the parent constructor, so the child does not need to repeat the code that assigns the common fields. A developer can call `display_employee()` directly and can also define its own methods, such as `display_technology()`.

## Inheritance types

| Type | Meaning | Example in `main.py` |
| --- | --- | --- |
| Single | One child inherits from one parent. | `Developer` inherits from `Employee`. |
| Multiple | One child inherits from multiple parents. | `TechnicalLead` inherits from `Developer` and `WorkFromHome`. |
| Multilevel | A class inherits through a chain of parent classes. | `SeniorDeveloper` inherits from `Developer`, which inherits from `Employee`. |
| Hierarchical | Multiple child classes inherit from one parent. | `Developer` and `Manager` inherit from `Employee`. |
| Hybrid | A combination of inheritance types. | `TechnicalLead` combines the employee/developer chain with multiple inheritance. |

## Run the example

From the workspace root, run:

```bash
python3 Day2/inheritance/main.py
```

The first example prints:

```text
Employee Name: Irfan
Salary: 80000
Technology: Python
```