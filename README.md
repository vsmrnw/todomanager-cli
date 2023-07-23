# Задание

Сделать две консольные программы для планировщика дел

**Первая**: спрашивает у юзера какое задание он хочет добавить. Вводится название и планируемое время в виде день.месяц. Естественно, если пользователь в декабре написал задачу на январь - это на следующий год. Так же чтобы можно было написать "завтра" или "послезавтра"

**Вторая программа**: выдает 5 следующих дел и 5 последних, которые прошли. Считается относительно текущей даты. Так же чтобы можно было в консоли параметром ввести на какой день считать вместо сегодняшнего.

Что тебе понадобится

* Вынести общий код в отдельный модуль
* Разобраться как будешь сохранять данные (json или sqlite на выбор)
* Разобраться с аргументами командной строки (модуль Argparse)
* Разобраться с модулем datetime.

**Усложнения:**

* Использовать sqlite или json опрделеяется настройками программы
* Сделать UI (веб или десктоп), работающий с тем же хранилищем