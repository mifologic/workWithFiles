import pandas as pd

df = pd.read_excel('file_example_XLSX_10.xlsx')
print('Заголовки файла')
print(df.columns.values.tolist())  # вывод заголовков в виде списка
print('\n Данные колонки по имени')
print(df['Category'].values.tolist())  # вывод данных из определённой колонки
print('\n Все значения в виде списка объектов')
print(df.to_dict('records'))  #  вывод значений файла в виде списка объектов
