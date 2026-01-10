import os
from models import Book


def load_from_file(filename, library):
    """Загрузить книги из текстового файла"""
    library.books = []
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()

            for i, line in enumerate(lines, 1):
                line = line.strip()
                if line and not line.startswith('#'):
                    if ';' in line:
                        parts = line.split(';')
                    else:
                        if ',' in line:
                            parts = line.split(',')
                        elif '\t' in line:
                            parts = line.split('\t')
                        else:
                            print(f"Пропущена строка {i}: неправильный формат")
                            continue

                    if len(parts) >= 6:
                        try:
                            author = parts[0].strip()
                            title = parts[1].strip()
                            publisher = parts[2].strip()
                            year = int(parts[3].strip())
                            pages = int(parts[4].strip())
                            copies = int(parts[5].strip())

                            library.books.append(Book(author, title, publisher, year, pages, copies))
                        except ValueError as e:
                            print(f"Ошибка в строке {i}: {e}")
                            continue
                    else:
                        print(f"Пропущена строка {i}: недостаточно данных (нужно 6 полей)")

        print(f"Загружено {len(library.books)} книг из файла '{filename}'")
        return True

    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        library.books = []
        return False


def save_to_file(filename, library):
    """Сохранить книги в текстовый файл"""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            for book in library.books:
                line = f"{book.author};{book.title};{book.publisher};" \
                       f"{book.year};{book.pages};{book.copies}\n"
                f.write(line)
        print(f"Данные сохранены в файл '{filename}'")
        return True
    except Exception as e:
        print(f"Ошибка при сохранении файла: {e}")
        return False
