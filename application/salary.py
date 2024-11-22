import random

def calculate_salary(tax_rate=13, bonus=12000, min_salary=30000, max_salary=90000):
    """
    Функция для расчета зарплаты сотрудника с учетом налогов и бонусов,
    bonus: бонус к зарплате
    min_salary: минимальная зарплата для генерации случайной зарплаты
    max_salary: максимальная зарплата для генерации случайной зарплаты
    return: итоговая зарплата после вычета налогов и добавления бонуса
    """
    # Генерация случайной зарплаты в заданном диапазоне
    random_salary = round(random.uniform(min_salary, max_salary), 2)
    
    # Рассчитываем налог
    tax = random_salary * (tax_rate / 100)
    
    # Рассчитываем итоговую зарплату
    final_salary = random_salary - tax + bonus
    
    return final_salary

if __name__ == "__main__":
    # Пример использования функции calculate_salary
    salary = calculate_salary(tax_rate=13, bonus=5000, min_salary=2000, max_salary=3000)
    print(f"Итоговая зарплата сотрудника: {salary:.2f}")



