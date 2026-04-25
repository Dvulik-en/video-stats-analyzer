import sys
import os


# Добавляем путь к родительской папке в список мест, где Python ищет модули
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from report import filter_clickbait


def test_filter_clickbait_logic():
    # Готовим данные с разными случаями
    test_data = [
        # Видео, которое НЕ является кликбейтом (низкий CTR)
        {'title': 'Нормальное', 'ctr': 10.0, 'retention_rate': 50.0},

        # Видео, которое ЯВЛЯЕТСЯ кликбейтом (CTR > 15, Retention < 40)
        {'title': 'Кликбейт!', 'ctr': 20.0, 'retention_rate': 30.0},

        # Пограничный случай: CTR ровно 15 (не должен попасть)
        {'title': 'На грани', 'ctr': 15.0, 'retention_rate': 20.0}
    ]

    # Вызываем функцию
    result = filter_clickbait(test_data)

    # Проверяем, что попало в отчет
    assert len(result) == 1
    assert result[0]['title'] == 'Кликбейт!'

    # Проверяем, что пограничное видео НЕ попало
    titles = [row['title'] for row in result]
    assert 'На грани' not in titles