import json
from datetime import datetime

NOTES_FILE = "notes.json"

def load_notes():
    try:
        with open(NOTES_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("\nОшибка декодирования JSON.")
        return []
    except Exception as e:
        print(f"\nПроизошла ошибка: {e}")
        return []

def save_notes(notes):
    try:
        with open(NOTES_FILE, "w") as file:
            json.dump(notes, file, indent=4)
    except Exception as e:
        print(f"\nПроизошла ошибка при сохранении заметок: {e}")

def get_available_id(notes):
    available_ids = [note["id"] for note in notes if note["id"] is not None]
    return max(available_ids) + 1 if available_ids else 1

def add_note():
    try:
        title = input("Введите заголовок заметки: ")
        content = input("Введите содержание заметки: ")
        created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        notes = load_notes()
        new_id = get_available_id(notes)
        notes.append({"id": new_id, "title": title, "content": content, "created_at": created_at})
        save_notes(notes)
        print("\nЗаметка успешно сохранена.")
    except Exception as e:
        print(f"Произошла ошибка при добавлении заметки: {e}")

def show_notes():
    try:
        notes = load_notes()
        if notes:
            for note in notes:
                if note["id"] is not None:
                    print(f"\nID: {note['id']}, Title: {note['title']}, Content: {note['content']}, Created at: {note['created_at']}")
        else:
            print("\nНет заметок.")
    except Exception as e:
        print(f"\nПроизошла ошибка при отображении заметок: {e}")

def delete_note():
    try:
        id_to_delete = int(input("Введите ID заметки для удаления: "))
        notes = load_notes()
        for note in notes:
            if note["id"] == id_to_delete:
                note["id"] = None  
                save_notes(notes)
                print("\nЗаметка успешно удалена.")
                return
        print("\nЗаметка с таким ID не найдена.")
    except ValueError:
        print("\nНекорректный ввод ID заметки.")
    except Exception as e:
        print(f"\nПроизошла ошибка при удалении заметки: {e}")

def edit_note():
    try:
        note_id = int(input("Введите ID заметки для редактирования: "))
        notes = load_notes()
        for note in notes:
            if note['id'] == note_id:
                title = input("Введите новый заголовок заметки: ")
                content = input("Введите новое содержание заметки: ")
                note['title'] = title
                note['content'] = content
                note['last_modified_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                save_notes(notes)
                print("\nЗаметка успешно отредактирована.")
                return
        print("\nЗаметка с таким ID не найдена.")
    except ValueError:
        print("\nНекорректный ввод ID заметки.")
    except Exception as e:
        print(f"\nПроизошла ошибка при редактировании заметки: {e}")

def display_note_by_id(note_id):
    try:
        notes = load_notes()
        for note in notes:
            if note["id"] == note_id:
                print(f"\nID: {note['id']}, Title: {note['title']}, Content: {note['content']}, Created at: {note['created_at']}")
                return
        print("\nЗаметка с таким ID не найдена.")
    except Exception as e:
        print(f"\nПроизошла ошибка при отображении заметки: {e}")

def main():
    while True:
        print("\nВыберите действие:")
        print("1. Просмотреть список заметок")
        print("2. Добавить новую заметку")
        print("3. Удалить заметку")
        print("4. Редактировать заметку")
        print("5. Просмотреть конкретную заметку")
        print("6. Выйти")
        choice = input("Введите номер действия: ")
        if choice == "1":
            show_notes()
        elif choice == "2":
            add_note()
        elif choice == "3":
            delete_note()
        elif choice == "4":
            edit_note()
        elif choice == "5":
            note_id = int(input("Введите ID заметки для просмотра: "))
            display_note_by_id(note_id)
        elif choice == "6":
            print("До свидания!")
            break
        else:
            print("Некорректный ввод. Пожалуйста, выберите номер действия из списка.")

if __name__ == "__main__":
    main()