import csv
import pytest
from src.file_handler import process_files

@pytest.fixture
def csv_files(tmp_path):
    """
    Создает 2 csv файла и возвращает их пути
    """
    file1 = tmp_path / 'employees1.csv'
    file2 = tmp_path / 'employees2.csv'

    with open(file1, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['name', 'position', 'completed_tasks', 'performance', 'experience_years'])
        writer.writerow(['David Chen', 'Mobile Developer', '36', '4.6', '3'])
        writer.writerow(['Elena Popova','Backend Developer','43','4.8','4'])
    with open(file2, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['name', 'position', 'completed_tasks', 'performance', 'experience_years'])
        writer.writerow(['Alex Ivanov','Backend Developer','45','4.8','5'])
        writer.writerow(['Maria Petrova','Frontend Developer','38','4.7','4'])

    return file1, file2

def test_process_files_single_csv(csv_files):
    """
    Должен корректно читать один csv файл и вернуть список словарей
    """
    file, _ = csv_files
    rows = process_files([str(file)])

    assert isinstance(rows, list)
    assert len(rows) == 2
    assert rows[0] == {
        'name': 'David Chen',
        'position': 'Mobile Developer',
        'completed_tasks': '36',
        'performance': '4.6',
        'experience_years': '3',
    }
    assert rows[1]['name'] == 'Elena Popova'
    assert rows[1]['performance'] == '4.8'

def test_process_files_multiple_csv(csv_files):
    """
    Должен объединять строки из нескольких csv файлов
    """
    file1, file2 = csv_files
    rows = process_files([str(file1), str(file2)])

    assert len(rows) == 4
    names = [row['name'] for row in rows]
    assert names == [
        'David Chen',
        'Elena Popova',
        'Alex Ivanov',
        'Maria Petrova',
    ]

def test_process_files_empty_list():
    """
    Пустой список файлов, вернет пустой список строк
    """
    rows = process_files([])
    assert rows == []

def test_process_files_not_csv(tmp_path):
    """
    Если передан не csv файл, вернет ValueError с текстом
    """
    wrong_file = tmp_path / 'text.txt'

    with open(wrong_file, 'w', encoding='utf-8') as file:
        file.write('text')

    with pytest.raises(ValueError) as e:
        process_files([str(wrong_file)])

    msg = str(e.value)
    assert 'Ошибка при обработке файла' in msg
    assert 'Поддерживаются только .csv файлы!' in msg

def test_process_files_missing_file():
    """
    Если файл не найден, FileNotFoundError с текстом
    """
    file = 'test.csv'

    with pytest.raises(FileNotFoundError) as e:
        process_files([file])

    assert str(e.value) == 'Файл "test.csv" не найден'