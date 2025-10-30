#Белякова 3 вариант
print("start code ...")
import json
import os
print("start code ...")

if os.path.exists("stars.json"):
    with open("stars.json", "r", encoding="utf-8") as f:
        stars = json.load(f)
else:
    stars = []

while True:
    print("Выберите пункт от 1 до 4:")
    print("1.Вывести все записи")
    print("2.Добавить запись")
    print("3.Удалить запись")
    print("4.Выйти")

    choice = input("Введите свой выбор:")

    if choice == "1":
        print("="*10 + "Все записи" + "="*10)
        if not stars:
            print("Записей нет")
        else:
            for star in stars:
                visible_str = "Видна без телескопа" if star["is_visible"] else "Не увидишь без телескопа"
                print(f"id: {star['id']}")
                print(f"Название:{star['name']}")
                print(f"Созвездие: {star['constellation']}")
                print(f"Видимость:{'visible_str'}")
                print(f"Радиус: {star['radius']}")
                print("-" * 50)

    elif choice == "2":
            new_id = max([s["id"] for s in stars], default=0) + 1
            name = input("Введите название звезды: ").strip()
            constellation = input("Введите созвездие: ").strip()
            is_visible_input = input(
                "Ваша звезда видна без телескопа? (да/нет): ").strip().lower()
            is_visible = True if is_visible_input in ("да") else False
            radius = float(input("Введите радиус звезды:"))
            new_star = {
                "id": new_id,
                "name": name,
                "constellation": constellation,
                "is_visible": is_visible,
                "radius": radius
            }
            stars.append(new_star)
            with open("stars.json", "w", encoding="utf-8") as f:
                json.dump(stars, f, ensure_ascii=False, indent=4)
            print("Запись добавлена")
            
    elif choice == "3":
            old_id = int(input("Введите id звезды для удаления:"))
            len_initial = len(stars)
            stars = [s for s in stars if s["id"] != old_id]
            if len(stars) == len_initial:
                print("="*10 + "Не найдено" + "=" * 10)
            else:
                with open("stars.json", "w", encoding="utf-8") as f:
                    json.dump(stars, f, ensure_ascii=False, indent=4)
                    print("Запись удалена")
    elif choice == "4":
        print("... end code")
        break
    else:
        print("Неправильный ввод")
print("... end code")
