import os
import re

BOOK_PATH = '/home/newage/projects-wsl/bookbot/book/book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}

# Функция, возвращающая строку с текстом страницы и ее размер


# МОЯ РЕАЛИЗАЦИЯ
# def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
#     end = [',', '.', '!', ':', ';', '?']

#     len_out = min(size + start, len(text))

#     if text[len_out-1] in end and text[len_out-2] not in end:
#         return text[start:len_out], len_out-start

#     if text[len_out-1] in end and (text[len_out-2] in end or text[len_out] in end):
#         while text[len_out-1] in end and (text[len_out-2] in end or text[len_out] in end):
#             len_out = len_out - 1

#         if text[len_out-1] not in end:
#             while text[len_out-1] not in end:
#                 len_out = len_out - 1
#         return text[start:len_out], len_out-start

#     if text[len_out-1] not in end:
#         while text[len_out-1] not in end:
#             len_out = len_out - 1

#         return text[start:len_out], len_out-start


def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    edit_text = re.sub(r'[.,!?:;]\.+$', '', text[start:start+size])
    edit_text = re.findall(r'(?s).+[.,!?:;]', edit_text)
    return *edit_text, len(*edit_text)


# Не удаляйте эти объекты - просто используйте
PAGE_SIZE = 1050


# Дополните эту функцию, согласно условию задачи
def prepare_book(path: str) -> None:
    with open(path, "r") as f:
        text = f.read()

        x = 0
        i = 1
        y = 0

        while x < len(text):
            text_out, y = _get_part_text(text, x, PAGE_SIZE)
            text_out = re.sub(r'[\r\t\0]', '', text_out)
            text_out = re.sub(r'^\s+', '', text_out)
            x = x + y
            book[i] = text_out
            i = i + 1


# Вызов функции prepare_book для подготовки книги из текстового файла
prepare_book(os.path.join(os.getcwd(), BOOK_PATH))
