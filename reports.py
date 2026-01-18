from sorting import heap_sort

def get_full_sorted_list(library):
    """Полный список книг, отсортированный по автору (↑), году (↓), количеству экземпляров (↓)"""
    if not library.books:
        return []

    def compare_books(a, b):
        if a.author != b.author:
            return -1 if a.author < b.author else 1

        if a.year != b.year:
            return 1 if a.year < b.year else -1

        if a.copies != b.copies:
            return 1 if a.copies < b.copies else -1

        return 0

    return heap_sort(library.books.copy(), compare_books)


def get_books_by_author(library, author):
    """Список книг определенного автора, отсортированный по издательству (↓) и названию (↑)"""
    if not library.books:
        return []

    author_books = []
    for book in library.books:
        if book.author == author:
            author_books.append(book)

    if not author_books:
        return []

    def compare_books(a, b):
        if a.publisher != b.publisher:
            return 1 if a.publisher < b.publisher else -1

        if a.title != b.title:
            return -1 if a.title < b.title else 1

        return 0

    return heap_sort(author_books, compare_books)


def get_books_by_years_range(library, n1, n2):
    """Список книг, выпущенных в период с N1 до N2 года,
    отсортированный по году выпуска (↓) и автору (↑)"""
    if not library.books:
        return []

    filtered_books = []
    for book in library.books:
        if n1 <= book.year <= n2:
            filtered_books.append(book)

    if not filtered_books:
        return []

    def compare_books(a, b):
        if a.year != b.year:
            return 1 if a.year < b.year else -1

        if a.author != b.author:
            return -1 if a.author < b.author else 1

        return 0

    return heap_sort(filtered_books, compare_books)


def print_books(books, title):
    """Вывести список книг с заголовком"""
    print(f"\n{'=' * 100}")
    print(f"{title} (всего: {len(books)})")
    print('=' * 100)
    if books:
        print(f"{'Автор':20} | {'Название':25} | {'Издательство':15} | {'Год':4} | {'Страниц':7} | {'Экз.':5}")
        print('-' * 100)

        for book in books:
            print(book)
    else:
        print("Книги не найдены или база данных пуста")


def show_database_info(library, filename):
    """Показать информацию о базе данных"""
    import os
    
    print("\n" + "=" * 60)
    print("ИНФОРМАЦИЯ О БАЗЕ ДАННЫХ БИБЛИОТЕКИ")
    print("=" * 60)

    if not library.books:
        print("База данных пуста")
        return

    print(f"Всего книг: {len(library.books)}")

    authors = {}
    for book in library.books:
        if book.author in authors:
            authors[book.author] += 1
        else:
            authors[book.author] = 1

    print(f"\nВсего авторов: {len(authors)}")
    print("Количество книг по авторам:")
    for author, count in sorted(authors.items()):
        print(f"  {author}: {count} книг")

    years = {}
    for book in library.books:
        if book.year in years:
            years[book.year] += 1
        else:
            years[book.year] = 1

    print(f"\nДиапазон годов: от {min(years.keys())} до {max(years.keys())}")
    print("Количество книг по годам:")
    for year in sorted(years.keys()):
        print(f"  {year}: {years[year]} книг")

    total_pages = sum(book.pages for book in library.books)
    total_copies = sum(book.copies for book in library.books)
    print(f"\nОбщее количество страниц: {total_pages}")
    print(f"Общее количество экземпляров: {total_copies}")

    if os.path.exists(filename):
        file_size = os.path.getsize(filename)
        print(f"\nФайл данных: {filename}")
        print(f"Размер файла: {file_size} байт")
