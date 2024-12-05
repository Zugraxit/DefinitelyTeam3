import keyword


class Data_reader:
    """Класс для получения данных"""
    def read_lines_from_file(self, file_path: str) -> list[str]:
        """
        Читает данные из файла и возвращает список строк.

        :param file_path: Путь к файлу
        :return: Список строк из файла
        """
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()  # Чтение всех строк из файла
                return [line.strip() for line in lines]  # Удаление символов новой строки и лишних пробелов
        except FileNotFoundError:
            print(f"Файл '{file_path}' не найден.")
            return []
        except Exception as e:
            print(f"Произошла ошибка: {e}")
            return []