from faker import Faker

def get_employees(num_employees=10):
    """
    Функция для генерации списка с данными о фейковых сотрудниках
    """
    fake = Faker('ru_RU')
    employees = []
    
    for _ in range(num_employees):
        employee = {
            "id": fake.random_int(min=1, max=1000),
            "ФИО": fake.name(),
            "Специальность": fake.job(),
            "Дата рождения": fake.date_of_birth(minimum_age=18, maximum_age=65).strftime("%d-%m-%Y"),
            "ИНН": fake.random_int(min=1000000000, max=9999999999),
            "Адрес": fake.address(),
            "Почта": fake.email(),
            "Телефон": fake.phone_number(),
            "Опыт работы": fake.random_int(min=1, max=20), 
                    }
        employees.append(employee)
    
    return employees

if __name__ == "__main__":
    # Пример использования функции get_employees
    employees_list = get_employees(5)
    for employee in employees_list:
        print(employee)
