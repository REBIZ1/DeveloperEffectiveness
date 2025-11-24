import sys
from main import main
from src.report import REPORT_BUILDERS

def test_main_invalid_report(capsys, monkeypatch):
    """
    Если указан неизвестный отчет.
    """
    monkeypatch.setattr(sys, 'argv', ['main.py', '--report', 'unknown_report'])
    main()
    captured = capsys.readouterr()

    assert 'Неизвестный отчет "unknown_report"' in captured.out
    assert 'Доступные: performance' in captured.out

def test_main_valid_report(capsys, monkeypatch):
    """
    Если передан правильный отчет.
    """
    monkeypatch.setattr(sys, 'argv', ['main.py', '--report', 'performance'])

    called = {}
    def fake_create(self, args):
        called['report'] = args.report
    monkeypatch.setattr(REPORT_BUILDERS['performance'], 'create', fake_create)
    main()

    assert called['report'] == 'performance'
    captured = capsys.readouterr()
    assert 'Неизвестный отчет' not in captured.out
    assert 'Доступные:' not in captured.out