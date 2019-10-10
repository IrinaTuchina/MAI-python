# ==================
# ДЗ №1: простые типы данных, изменяемые и неизменяемые типы, работа со строками, списки

# Задание: сделайте анализ выгрузки квартир с ЦИАН:

# 1) Измените структуру данных, используемую для хранения данных о квартире. Сейчас квартира = список. Сделайте вместо этого квартира = словарь следующего вида: flat_info = {"id":flat[0], "rooms":flat[1], "type":flat[2], "price":flat[11]}. В задании используйте поля: идентификатор квартиры на ЦИАН, количество комнат, тип (новостройка или вторичка), стоимость

# 2) Подсчитайте количество новостроек, расположенных у каждого из метро

import csv

flats_list = list()
with open('output.csv', encoding="utf-8") as csvfile:
	flats_csv = csv.reader(csvfile, delimiter=';')
	flats_list = list(flats_csv)
header = flats_list.pop(0)


#first task
subway_dict = {}
for flat in flats_list:
	subway = flat[3].replace("м.", "")
	subway_dict.setdefault(subway, [])
	flat_info = {"id":int(flat[0]), "rooms":int(flat[1]), "type":(flat[2]), "cost":int(flat[11])}
	subway_dict[subway].append(flat_info)

#second task
subwayWithNewBuldings = []
flat_type = "новостройка"
for subway in subway_dict:
	numberOfNewBuildings = 0
	for flat in subway_dict[subway]:
		if flat["type"] == flat_type:
			numberOfNewBuildings = numberOfNewBuildings + 1
	subway_and_numberOfNewBuildings = {f"{subway}":f"{numberOfNewBuildings}"}
	subwayWithNewBuldings.append(subway_and_numberOfNewBuildings)

print(f"Data type is '{flat_type}'\n")
for undergroundAndNumberOfNewBuildings in subwayWithNewBuldings:
	print(f"subway: {undergroundAndNumberOfNewBuildings} new buildings:")