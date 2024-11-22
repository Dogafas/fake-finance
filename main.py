from datetime import datetime
from application.db.people import get_employees
from application.salary import calculate_salary
from dateutil.relativedelta import relativedelta
import locale


def print_previous_month():
    """для ознакомления с модулем datetime (нужно достать прошлый месяц(а))"""    
    locale.setlocale(locale.LC_TIME, 'ru_RU')
    current_date = datetime.now()
    previous_month_date = current_date - relativedelta(months=1)
    previous_month_str = previous_month_date.strftime("%B %Y")
    return previous_month_str
    

if __name__ == "__main__":
    print(f'ВЕДОМОСТЬ ВЫДАННОЙ ЗАРАБОТНОЙ ПЛАТЫ ООО "ФЕЙК" ЗА {print_previous_month()} г.')
    employees = get_employees()
    for employee in employees:
        print(f"Таб.№: {employee['id']}, ФИО: {employee['ФИО']}, Должность: {employee['Специальность']}, Выплачено: {calculate_salary():.2f}, руб.")
    print(f"Отчёт чёрной бухгалтерии сформирован на {datetime.now().strftime('%d.%m.%Y')}г.")


