BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050
book: dict[int, str] = {}


# Функция, возвращающая строку с текстом страницы и ее размер
def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    end = ('.', ',', '!', '?', ':', ':')
    result = text[start: start + size]
    if len(result) + start != len(text):
        if result[-1] == '.' and text[len(result) + start] == '.' and text[len(result) + start + 1] != '.':
            result = result[:-3]
        elif result[-1] == '.' and text[len(result) + start] == '.' and text[len(result) + start + 1] == '.':
            result = result[:-2]
    while result[-1] not in end:
        result = result[:-1]
    return result, len(result)


# Функция, формирующая словарь книги
def prepare_book(path: str) -> None:
    with open(path, 'r', encoding='utf-8') as file:
        text = file.read()
        start = 0
        for i in range(len(text) // 1050 + 1):
            value = _get_part_text(text, start, PAGE_SIZE)
            book[i + 1] = value[0].lstrip('\n').lstrip()
            start += value[1]


prepare_book(BOOK_PATH)
