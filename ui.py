from models import Book
from file_operations import load_from_file, save_to_file
from reports import get_full_sorted_list, get_books_by_author, get_books_by_years_range, print_books, show_database_info
import os

def print_menu():
    """Вывести меню программы"""
    print("\n" + "=" * 60)
    print("БИБЛИОТЕКА - система управления книгами")
    print("=" * 60)
    print("1. Показать все книги (отчет 1)")
    print("2. Найти книги по автору (отчет 2)")
    print("3. Найти книги по году выпуска (отчет 3)")
    print("4. Добавить новую книгу")
    print("5. Удалить книгу")
    print("6. Обновить данные из файла")
    print("7. Сохранить данные в файл")
    print("8. Показать информацию о базе данных")
    print("9. Выход")
    print("-" * 60)


def add_book_interactive(library, filename):
    """Интерактивное добавление книги"""
    print("\n" + "=" * 60)
    print("ДОБАВЛЕНИЕ НОВОЙ КНИГИ")
    print("=" * 60)

    try:
        author = input("Автор: ")
        if not author:
            print("Ошибка: автор не может быть пустым")
            return

        title = input("Название: ")
        if not title:
            print("Ошибка: название не может быть пустым")
            return

        publisher = input("Издательство: ")
        if not publisher:
            print("Ошибка: издательство не может быть пустым")
            return

        year = int(input("Год выпуска: "))
        if year < 0 or year > 2100:
            print("Ошибка: неверный год")
            return

        pages = int(input("Количество страниц: "))
        if pages <= 0:
            print("Ошибка: количество страниц должно быть положительным")
            return

        copies = int(input("Количество экземпляров: "))
        if copies < 0:
            print("Ошибка: количество экземпляров не может быть отрицательным")
            return

        new_book = Book(author, title, publisher, year, pages, copies)
        library.add_book(new_book)
        print(f"Книга '{new_book.title}' добавлена в библиотеку")

        save_choice = input("Сохранить изменения в файл? (да/нет): ")
        if save_choice.lower() == 'да':
            save_to_file(filename, library)

    except ValueError as e:
        print(f"Ошибка ввода: {e}")
    except Exception as e:
        print(f"Ошибка: {e}")


def remove_book_interactive(library, filename):
    """Интерактивное удаление книги"""
    if not library.books:
        print("База данных пуста. Нечего удалять.")
        return

    print("\n" + "=" * 60)
    print("УДАЛЕНИЕ КНИГИ")
    print("=" * 60)

    print("Список книг:")
    for i, book in enumerate(library.books, 1):
        print(f"{i:3}. {book.author:20} | {book.title:25} | {book.publisher:15} | {book.year}")

    try:
        choice = input("\nВыберите способ удаления:\n1. По номеру из списка\n2. По параметрам\nВаш выбор (1/2): ")

        if choice == '1':
            book_num = int(input("Введите номер книги для удаления: "))
            if 1 <= book_num <= len(library.books):
                removed_book = library.books.pop(book_num - 1)
                print(f"Книга '{removed_book.title}' удалена из библиотеки")

                save_choice = input("Сохранить изменения в файл? (да/нет): ")
                if save_choice.lower() == 'да':
                    save_to_file(filename, library)
            else:
                print("Неверный номер книги")

        elif choice == '2':
            print("\nВведите параметры книги для удаления:")
            author = input("Автор: ")
            title = input("Название: ")
            publisher = input("Издательство: ")
            year = int(input("Год выпуска: "))

            if library.remove_book(author, title, publisher, year):
                print("Книга удалена из библиотеки")
                save_choice = input("Сохранить изменения в файл? (да/нет): ")
                if save_choice.lower() == 'да':
                    save_to_file(filename, library)
            else:
                print("Книга не найдена")

        else:
            print("Неверный выбор")

    except ValueError as e:
        print(f"Ошибка ввода: {e}")
    except Exception as e:
        print(f"Ошибка: {e}")


def show_authors(library):
    """Показать список авторов"""
    if not library.books:
        print("База данных пуста.")
        return
    
    authors = sorted(set(book.author for book in library.books))
    print("\nДоступные авторы:")
    for i, author in enumerate(authors, 1):
        print(f"{i}. {author}")


def show_years_range(library):
    """Показать диапазон годов"""
    if not library.books:
        print("База данных пуста.")
        return
    
    years = sorted(set(book.year for book in library.books))
    print(f"\nДоступные годы: от {years[0]} до {years[-1]}")
