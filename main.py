import os
from models import Library
from file_operations import load_from_file
from ui import print_menu, add_book_interactive, remove_book_interactive, show_authors, show_years_range
from reports import get_full_sorted_list, get_books_by_author, get_books_by_years_range, print_books, show_database_info

def main():
    FILENAME = "books.txt"
    library = Library()
    
    # Загрузка данных из файла
    if os.path.exists(FILENAME):
        load_from_file(FILENAME, library)
    else:
        print(f"Файл '{FILENAME}' не найден. Программа будет работать без данных.")
        print("Пожалуйста, создайте файл books.txt с данными о книгах.")
        print("Формат каждой строки: Автор;Название;Издательство;Год;Страниц;Экземпляров")

    # Приветственное сообщение
    if library.books:
        print("\n" + "=" * 60)
        print("ДОБРО ПОЖАЛОВАТЬ В СИСТЕМУ УПРАВЛЕНИЯ БИБЛИОТЕКОЙ")
        print("=" * 60)
        print(f"Загружено {len(library.books)} книг из файла '{FILENAME}'")
        print("Для просмотра отчетов выберите пункты 1-3 в меню")
    else:
        print("\nВнимание: База данных пуста.")
        print("Создайте файл books.txt или добавьте книги через меню.")

    while True:
        print_menu()
        choice = input("\nВыберите действие (1-9): ")

        if choice == '1':
            # Отчет 1
            sorted_books = get_full_sorted_list(library)
            print_books(sorted_books, "ПОЛНЫЙ СПИСОК ВСЕХ КНИГ (Автор↑, Год↓, Экз.↓)")

        elif choice == '2':
            # Отчет 2
            if library.books:
                show_authors(library)
                author_input = input("\nВведите фамилию автора или номер: ")
                
                # Проверка, является ли ввод числом
                if author_input.isdigit():
                    authors = sorted(set(book.author for book in library.books))
                    idx = int(author_input) - 1
                    if 0 <= idx < len(authors):
                        author_input = authors[idx]
                    else:
                        print("Неверный номер")
                        continue

                author_books = get_books_by_author(library, author_input)
                print_books(author_books, f"КНИГИ АВТОРА: {author_input} (Издательство↓, Название↑)")
            else:
                print("База данных пуста.")

        elif choice == '3':
            # Отчет 3
            if library.books:
                show_years_range(library)
                try:
                    n1 = int(input("Введите начальный год (N1): "))
                    n2 = int(input("Введите конечный год (N2): "))

                    if n1 > n2:
                        n1, n2 = n2, n1
                        print(f"Годы поменяны местами: {n1}-{n2}")

                    year_books = get_books_by_years_range(library, n1, n2)
                    print_books(year_books, f"КНИГИ ЗА ПЕРИОД {n1}-{n2} (Год↓, Автор↑)")

                except ValueError:
                    print("Ошибка: введите корректные годы")
            else:
                print("База данных пуста.")

        elif choice == '4':
            add_book_interactive(library, FILENAME)

        elif choice == '5':
            remove_book_interactive(library, FILENAME)

        elif choice == '6':
            if os.path.exists(FILENAME):
                load_from_file(FILENAME, library)
            else:
                print(f"Файл {FILENAME} не найден.")

        elif choice == '7':
            from file_operations import save_to_file
            if library.books:
                save_to_file(FILENAME, library)
            else:
                print("Нет данных для сохранения.")

        elif choice == '8':
            show_database_info(library, FILENAME)

        elif choice == '9':
            print("\nСпасибо за использование системы управления библиотекой!")
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")

        input("\nНажмите Enter для продолжения...")


if __name__ == "__main__":
    main()
