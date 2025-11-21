import csv

def process_files(*args):
    """
    Рассчитывает среднюю эффективность по позициям
    Принимает csv файлы
    Возвращает отсортированный список кортежей
    """
    data = {}

    for file in args:
        try:
            with open(file, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    data.setdefault(row['position'], []).append(float(row['performance']))
        except FileNotFoundError as e:
            print(f'Ошибка, файл "{file}" не найден!: {e}')
            return None

    # вычисляем среднее значение по позиции
    data = {k: round(sum(v) / len(v), 2) for k, v in data.items()}
    # сортируем и возвращаем список кортежей
    data = sorted(data.items(), key=lambda x: x[1], reverse=True)
    return data
