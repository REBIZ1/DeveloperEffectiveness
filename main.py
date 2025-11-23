from main.report import Report, REPORT_BUILDERS

def main():
    args = Report._get_arguments()
    name = args.report
    report_cls = REPORT_BUILDERS.get(name)

    if report_cls is None:
        print(f'Неизвестный отчет "{name}". Доступные: {", ".join(REPORT_BUILDERS.keys())}')
        return
    report = report_cls()
    report.create(args)

if __name__ == "__main__":
    main()