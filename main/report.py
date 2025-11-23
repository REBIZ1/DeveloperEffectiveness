import os
import argparse
import csv
from .file_handler import process_files
from tabulate import tabulate


class Report:
    """
    Основной класс для работы с отчетами
    """

    @staticmethod
    def _save_report(data: list[tuple], filename: str, headers: list[str]):
        """
        Сохраняет отчет в csv файл
        """
        try:
            reports_dir = 'reports'
            os.makedirs(reports_dir, exist_ok=True)
            filepath = os.path.join(reports_dir, f'{filename}.csv')

            with open(filepath, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(headers)
                writer.writerows(data)
        except Exception as e:
            print(f'Ошибка при сохранении {filename}.csv: {e}')

    @staticmethod
    def _get_arguments() -> argparse.Namespace:
        """
        Разбирает аргументы (--files, --report, --save)
        Все аргументы являются необязательными:
        - если не указан --files, автоматически берутся все .csv файлы из директории data/;
        - если не указан --report, используется отчет 'performance';
        - если указать --save, будет созднач .csv файл с отчетом.
        """
        parser = argparse.ArgumentParser(description='Скрипт для создания отчета')
        parser.add_argument('--files', type=str, nargs='+', help='Имя или путь к csv файлам')
        parser.add_argument('--report', type=str, default='performance', help='Название отчета')
        # необязательный аргумент save для сохранения таблицы
        parser.add_argument('--save', action='store_true', help='Сохранение таблицы в .csv файл')

        args = parser.parse_args()
        # Добавил возможность не прописывать --files
        if not args.files:
            os.makedirs('data', exist_ok=True)
            args.files = [os.path.join('data', f) for f in os.listdir('data') if f.endswith('.csv')]

        return args

    def _create_report(self, headers: list[str], table: list[tuple], args: argparse.Namespace):
        """
        Создает отчет
        """
        # Сохранение для флага --save
        if args.save:
            self._save_report(table, args.report, headers)
        print(tabulate(table, headers=headers, tablefmt='simple', showindex=range(1, len(table) + 1)))
