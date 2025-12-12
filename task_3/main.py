#Белякова 3 вариант
import json
import os

def load_file():
    if os.path.exists("stars.json"):
        with open("stars.json", "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        return []

def save_file(stars):
    try:
     with open("stars.json", "w", encoding="utf-8") as f:
        json.dump(stars, f, ensure_ascii=False, indent=4)
    except Exception as e:
        raise ValueError(f"Ошибка сохранения данных:{e}")

def all_stars(stars):
     print("="*10 + "Все записи" + "="*10)
     if not stars:
            print("Записей нет")
     else:
            for star in stars:
                visible_str = "Видна без телескопа" if star["is_visible"] else "Не увидишь без телескопа"
                print(f"id: {star['id']}")
                print(f"Название:{star['name']}")
                print(f"Созвездие: {star['constellation']}")
                print(f"Видимость:{visible_str}")
                print(f"Радиус: {star['radius']}")
                print("-" * 50)

def star_by_field(stars):
    try:
        star_id = int(input("Введите id нужной звезды:"))
        if star_id <= 0:
            raise ValueError("Число должно быть положительное!")
        for star in stars:
            found = [star for star in stars if star['id'] == star_id]
            if not found:
                print("Не найдено!")
            else:
                star = found[0]
                visible_str = "Видна без телескопа" if star["is_visible"] else "Не увидишь без телескопа"
                print(f"id: {star['id']}")
                print(f"Название:{star['name']}")
                print(f"Созвездие: {star['constellation']}")
                print(f"Видимость:{visible_str}")
                print(f"Радиус: {star['radius']}")
                print("-" * 50)
    except ValueError as e:
        print(f"Ошибка:{e}")

def add_star(stars):
    try:
        new_id = max([s["id"] for s in stars], default=0) + 1
        name = input("Введите название звезды: ").strip()
        if not name:
            raise ValueError("Строка не может быть пустой!")
        constellation = input("Введите созвездие: ").strip()
        if not constellation:
            raise ValueError("Не оставляйте строку пустой!")
        is_visible_input = input("Ваша звезда видна без телескопа? (да/нет): ").strip().lower()
        if is_visible_input not in ['да','нет']:
            raise ValueError("Введите 'да' или 'нет'!")
        is_visible = True if is_visible_input in ("да") else False
        radius = float(input("Введите радиус звезды:"))
        if radius <= 0:
            raise ValueError("Радиус должен быть положительным!")
        new_star = {
                "id": new_id,
                "name": name,
                "constellation": constellation,
                "is_visible": is_visible,
                "radius": radius
            }
        stars.append(new_star)
        save_file(stars)
        print("Запись добавлена")
    except ValueError as e:
        print(f"Ошибка ввода данных:{e}")

def delete_star_by_field(stars):
    try:
        old_id = int(input("Введите id звезды для удаления:")) 
        if old_id <= 0:
            raise ValueError ("Число должно быть положительным!")  
        len_initial = len(stars)
        stars = [s for s in stars if s["id"] != old_id]
        if len(stars) == len_initial:
            print("="*10 + "Не найдено" + "=" * 10)
        else:
            save_file(stars)
        print("Запись удалена")
        return stars
    except ValueError as e:
        print(f"Ошибка при удалении:{e}")

def menu_choice(choice):
    choice_num = int(choice)
    if choice_num <1 or choice_num > 5:
        raise ValueError("Ваедите число от 1 до 5!")
    return choice_num

def main():
    try:
        stars = load_file()
        print(f"Данные успешно загрузились!")
    except ValueError as e:
        print(f"Ошибка {e}")
        stars = []
    while True:
        print("Выберите пункт от 1 до 5:")
        print("1.Вывести все записи")
        print("2.Вывести запись по полю")
        print("3.Добавить запись")
        print("4.Удалить запись по полю")
        print("5.Выйти из программы")
        try:
            choice = input("Введите свой выбор:")
            choice_num = menu_choice(choice)
            if choice_num == 1:
                all_stars(stars)
            elif choice_num == 2: 
                star_by_field(stars)     
            elif choice_num == 3:
                add_star(stars)
            elif choice_num == 4:
                delete_star_by_field(stars)
            elif choice_num == 5:
                print("Выход из программы...")
                break 
        except ValueError as e:
            print(f"Ошибка ввода:{e}")
if __name__ == "__main__":
    main()

    