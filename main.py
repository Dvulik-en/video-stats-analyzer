import argparse
from process import load_data
from report import filter_clickbait
from tabulate import tabulate

def main():
    # Настройка CLI: задаем аргументы для запуска программы
    parser = argparse.ArgumentParser()
    parser.add_argument('--files', nargs='+')
    parser.add_argument('--report', default='clickbait')
    args = parser.parse_args()

    # Загружаем данные из всех указанных файлов
    data = load_data(args.files)

    # Выбор логики отчета в зависимости от аргумента --report
    result = []
    if args.report == 'clickbait':
        result = filter_clickbait(data)

    # Форматирование и вывод результата
    if result:
        # Оставляем только нужные колонки для итоговой таблицы
        clean_result = [
            {'title': row['title'], 'ctr': row['ctr'], 'retention_rate': row['retention_rate']}
            for row in result
        ]
        # Вывод данных в виде таблицы с сеткой
        print(tabulate(clean_result, headers={'title': 'title', 'ctr': 'CTR %', 'retention_rate': 'retention_rate %'}, tablefmt='grid'))
    else:
        print("По заданным критериям ничего не найдено.")

if __name__ == "__main__":
    main()