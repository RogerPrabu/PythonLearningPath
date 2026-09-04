import csv
from datetime import date
import validator
import generate_id
import logger

@logger.logger
def append_expense(description: str, cost: float, category: list[str]) -> tuple[bool, str]:
    if not (validator.validate_description(description) and
            validator.validate_categories(category) and
            validator.validate_cost(cost)):
            return (False, "Invalid Input")

    with open("data.csv", "a", newline="") as file:
        ptr = csv.writer(file)
        ptr.writerow([generate_id.generate_new_id(), date.today(), description, cost, str(category)])
        return (True, "Successfully Added Expense to Expense List.")

@logger.logger
def remove_expense(id: int) -> tuple[bool, str]:
    data = get_all_expenses()
    if data[0]:
        new_data = []
        found = False
        for i in data[1]:
            if int(i[0]) == id:
                found = True
                continue
            new_data.append(i)
        if found:
            with open('data.csv', 'w', newline="") as file:
                ptr = csv.writer(file)
                ptr.writerows(new_data)
                return (True, f"Successfully removed expense with ID: {id}")
        return (False, f"No expense with ID: {id} exists")
    return (False, f"Couldn't retrive data for deletion.")

@logger.logger
def modify_expense(id: int, description: str, cost: float, category: list[str]) -> tuple[bool, str]:
    data = get_all_expenses()
    if data[0]:
        for i in data[1]:
            if int(i[0]) == id:
                i[2], i[3], i[4] = description, cost, str(category)
                break
        else:
            return (False, f"Couldn't find expense data with ID: {id}")
        with open('data.csv', 'w', newline="") as file:
            ptr = csv.writer(file)
            ptr.writerows(data[1])
    else:
        return data

@logger.logger
def search_expenses(id: int) -> tuple[bool, str | list]:
    data = get_all_expenses()
    if data[0]:
        for i in data[1]:
            if int(i[0]) == id:
                return (True, i)
        else:
            return (False, f"Couldn't get expense with ID: {id}")
    else:
        return data

@logger.logger
def get_all_expenses() -> tuple[bool, str | list[list]]:
    try:
         with open("data.csv", "r") as file:
              data = csv.reader(file)
              return (True, list(data))
    except FileNotFoundError:
         return (False, "File 'data.csv' was not found.")

if __name__ == "__main__":
    print(append_expense("hhlloowoorld", 829.99, ["exp", "str"]))
    print(search_expenses(1))
