def get_positive_number(prompt, unit=""):
    """Запрашивает положительное число с обработкой некорректного ввода"""
    while True:
        try:
            value = float(input(f"{prompt} ({unit}): " if unit else prompt))
            if value <= 0:
                print("Введите положительное число")
            else:
                return value
        except ValueError:
            print("Некорректный ввод. Используйте числовые значения")

def calculate_molarity():
    """Расчет молярной концентрации (моль/л)"""
    print("\n Молярная концентрация")
    mass = get_positive_number("Масса вещества", "г")
    molar_mass = get_positive_number("Молярная масса", "г/моль")
    volume = get_positive_number("Объем раствора", "л")
    
    moles = mass / molar_mass
    concentration = moles / volume
    print(f"Результат: {concentration:.4f} моль/л")

def calculate_mass_fraction():
    """Расчет массовой доли (%)"""
    print("\n Массовая доля")
    while True:
        solute = get_positive_number("Масса вещества", "г")
        solution = get_positive_number("Масса раствора", "г")
        
        if solute > solution:
            print("Ошибка: Вещество не может весить больше раствора!")
            retry = input("Попробовать снова? (да/нет): ").lower()
            if retry != 'да':
                return
        else:
            break
    
    fraction = (solute / solution) * 100
    print(f"Результат: {fraction:.2f}%")

def calculate_molality():
    """Расчет моляльности (моль/кг)"""
    print("\n iceberg Моляльность")
    solute_mass = get_positive_number("Масса вещества", "г")
    molar_mass = get_positive_number("Молярная масса", "г/моль")
    solvent_mass = get_positive_number("Масса растворителя", "кг")
    
    moles = solute_mass / molar_mass
    molality = moles / solvent_mass
    print(f"Результат: {molality:.4f} моль/кг")

def main():
    """Главное меню программы"""
    while True:
        print("\n Выберите тип концентрации:")
        print("1. Молярность (моль/л)")
        print("2. Массовая доля (%)")
        print("3. Моляльность (моль/кг)")
        print("4. Выход")
        
        while True:
            choice = input("Введите номер (1-4): ").strip()
            if choice in {'1', '2', '3', '4'}:
                break
            print("Неверный выбор. Попробуйте еще раз")
        
        if choice == '4':
            print("Работа завершена!")
            break
        
        if choice == '1':
            calculate_molarity()
        elif choice == '2':
            calculate_mass_fraction()
        elif choice == '3':
            calculate_molality()
        
        # Запрос на повторение
        while True:
            again = input("\nХотите выполнить еще один расчет? (да/нет): ").lower()
            if again in ['да', 'нет']:
                break
            print("Введите 'да' или 'нет'")
        
        if again == 'нет':
            print("Работа завершена!")
            break

if __name__ == "__main__":
    main()

