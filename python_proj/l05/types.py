week = ("Monday","Tuesday","Wensday")
print(week[1])
week2 = "Thresday", "friday"
# week3 = "suturday"
# print(week3)
# full_week = []
# full_week.append(week)
# print(full_week)
a,b = week2
print(a,b)
x,y,z = "пн","вт","ср"
print()

pupils = {"Карл Маркс","Aльберт Эйнштейн","Султанмурад","Ч.Дарвин","Карл Маркс"}
print(pupils)
if "Карл Маркс" in pupils:
	print("Победил")
else:
	print("Забудь")

madteam = {"Карл Маркс","Альберт Эйнштейн","Джон Нэш","Доналбд Трамп"}
print(pupils & madteam)
print(pupils | madteam)
print(madteam - pupils)

films = {"Люся": "Люся получает супермозг","Безумный макс": "Земля преаратилась в пустыню - комунизм Победил","Защитники":"Наш ответ западу! "}
print(films["Защитники"])
films["Люся"] = "Теряет мозг"
print(films)
films[7] = "жесьокий фильм про семь грехов"
print(films[7])
films["Чел1","Чел2"] = "Слив"
print(films ["Чел1","Чел2"])

for key in films:
	if key =="Люся":
	    print("Позор")

for desc in films.valeues():
	print(desc)

for name, desc in films.iteam():
	print("фильм" + str(name) + "о" + str(desc))


