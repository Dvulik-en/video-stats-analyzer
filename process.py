import csv


def load_data(file_paths):
    """
    Загружаем данные из списка CSV-файлов в единый список словарей.
    Преобразуем числовые поля 'ctr' и 'retention_rate' из строкового типа в float.
    """
    all_data = []

    # Итерируемся по списку путей к файлам
    for file_path in file_paths:
        with open(file_path, mode='r', encoding='UTF-8', newline='') as f:
            reader = csv.DictReader(f)

            # Читаем файл построчно и формируем список данных
            for row in reader:
                # Преобразуем строковые значения из CSV в числа для дальнейшей фильтрации
                row['ctr'] = float(row['ctr'])
                row['retention_rate'] = float(row['retention_rate'])

                all_data.append(row)

    return all_data