# Самоцветы скоро пропадут. Тебе потребуется помощь!

# findItems() возвращает массив предметов.
items = hero.findItems()

# Получи первый самоцвет из массива.
# Не забудь, что первый индекс равен 0.
gem0 = items[0]

# # Скажи Бруно получить gem0
hero.say("Bruno " + gem0)

# Ты можешь ссылаться на самоцвет без переменной
hero.say("Matilda " + items[1])

# Создай переменную для последнего самоцвета, items[2]:
gem2 = items[2]
# Передвинься к этому самоцвету с помощью moveXY()
hero.moveXY(gem2.pos.x, gem2.pos.y)
