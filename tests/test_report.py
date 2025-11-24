import csv
from types import SimpleNamespace
from src.report import Report, ReportPerformance


def test_build():
    """
    _build_table должен:
    - сгруппировать по position,
    - посчитать средний performance,
    - отсортировать по performance по убыванию.
    """
    rows = [
        {'position': 'Backend', 'performance': '4.0'},
        {'position': 'Backend', 'performance': '5.0'},
        {'position': 'Frontend', 'performance': '3.0'},
    ]

    table = ReportPerformance._build_table(rows)
    assert table == [
        ('Backend', 4.5),
        ('Frontend', 3.0),
    ]

def test_save_report(tmp_path, monkeypatch):
    """
    _save_report должен создавать директорию reports и записывать туда csv файл
    """
    monkeypatch.chdir(tmp_path)
    data = [
        ('Backend', 4.5),
        ('Frontend', 3.0),
    ]
    headers = ['position', 'performance']

    Report._save_report(data, 'performance', headers)
    reports_dir = tmp_path / 'reports'
    filepath = reports_dir / 'performance.csv'

    assert reports_dir.is_dir()
    assert filepath.is_file()

    with filepath.open('r', encoding='utf-8', newline='') as file:
        reader = csv.reader(file)
        rows = list(reader)
    assert rows[0] == headers
    assert rows[1] == ['Backend', '4.5']
    assert rows[2] == ['Frontend', '3.0']


def test_report_performance_create(monkeypatch):
    """
    create() должен:
    - вызвать process_files с args.files,
    - собрать таблицу через _build_table,
    - передать headers и table в _create_report.
    """
    called = {}
    def fake_process_files(files):
        called['files'] = files
        return [
            {'position': 'Backend', 'performance': '4.0'},
            {'position': 'Backend', 'performance': '5.0'},
            {'position': 'Frontend', 'performance': '3.0'},
        ]
    monkeypatch.setattr('src.report.process_files', fake_process_files)

    captured = {}
    def fake_create_report(self, headers, table, args):
        captured['headers'] = headers
        captured['table'] = table
        captured['args'] = args
    monkeypatch.setattr(ReportPerformance, '_create_report', fake_create_report)

    args = SimpleNamespace(
        files=['dummy1.csv', 'dummy2.csv'],
        report='performance',
        save=False,
    )
    report = ReportPerformance()
    report.create(args)

    assert called['files'] == args.files
    assert captured['headers'] == ['position', 'performance']
    assert captured['table'] == [
        ('Backend', 4.5),
        ('Frontend', 3.0),
    ]
    assert captured['args'] is args
