import csv

def process_files(files: list[str]) -> list[dict[str, str]]:
    """
    Обрабатывает файлы и возвращает список словарей
    """
    rows = []

    for file in files:
        try:
            if not file.endswith('.csv'):
                raise ValueError('Поддерживаются только .csv файлы!')
            with open(file, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    rows.append(row)
        except FileNotFoundError:
            raise FileNotFoundError(f'Файл "{file}" не найден')
        except ValueError as e:
            raise ValueError(f'Ошибка при обработке файла {file}: {e}')
    return rows
