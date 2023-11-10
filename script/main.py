# Импорт библиотек
import pandas as pd
import bar_chart_race as bcr

# Загрузка данных из CSV-файла
df = pd.read_csv('Pollution.csv', dtype={'year': str})

# Установка столбца 'year' в качестве индекса DataFrame
df = df.set_index('year')

# Путь к файлу для сохранения видео
output_file_path = 'Pol_bar_race.mp4'

# Создание bar chart race с определенными параметрами
bcr.bar_chart_race(
    df=df,  # DataFrame с данными
    title='Атмосфераға ластаушы заттардың шығарындылары\nВыброcы в атмосферу загрязняющих веществ',  # Заголовок видео
    orientation='h',  # Ориентация: горизонтальная
    sort='desc',  # Сортировка данных в нисходящем порядке
    n_bars=17,  # Количество столбцов, отображаемых в каждый момент времени
    steps_per_period=40,  # Количество шагов (кадров) на каждый период данных
    period_length=2000,  # Длительность каждого периода в миллисекундах
    filename=output_file_path,  # Путь и имя файла для сохранения видео
    figsize=(16, 9),  # Размер фигуры
    cmap='Pastel1',  # Цветовая карта
    bar_kwargs={'alpha': 0.7},  # Прозрачность столбцов
    filter_column_colors=True,  # Разрешить изменение цвета столбцов в процессе анимации
    title_size=20,  # Размер шрифта заголовка
    bar_label_size=15,  # Размер шрифта для названий регионов
    tick_label_size=15  # Размер шрифта для числа населения
)
