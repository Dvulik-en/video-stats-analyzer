def filter_clickbait(data):
    """
    Фильтрует список видео, оставляя только те, что соответствуют критериям кликбейта
    (высокий CTR и низкое удержание), и сортирует их по убыванию CTR.
    """
    filtered_data = []

    # Проходим по всем видео и отбираем те, что подходят под условия
    for row in data:
        # Критерии кликбейта: CTR выше 15%, а удержание менее 40%
        if row['ctr'] > 15 and row['retention_rate'] < 40:
            filtered_data.append(row)

    # Сортируем результат по CTR от большего к меньшему,
    # чтобы самые «агрессивные» кликбейты оказались в начале списка
    filtered_data.sort(key=lambda x: x['ctr'], reverse=True)

    return filtered_data