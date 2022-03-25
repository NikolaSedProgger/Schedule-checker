# School 947 Shedule Bot
### Как установить
Python3 должен быть уже установлен. Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
Рекомендуется использовать [virtualenv/venv](https://docs.python.org/3/library/venv.html)

### Как запустить?
Открываем консоль и запускаем бота командой 
```
python main.py 
```
Далее можем написать боту @Shedule947_bot
```
😺- 8М
        У класса 8М сейчас Физика -🤖
```
```
😺- а у 12М?
        Такого класса нету в расписании -🤖
😺- 12М
        У класса 12М нет сейчас уроков -🤖
```
### Как изменить расписание?
Заходим в файл ```shedule.xlsx```
И изменяем Уроки / Время / Классы в таблице
```
+-----------------------+------------------+------------------+------------------++
| Время                  | Класс 1         | Класс 2          | Класс 3           |
+-----------------------+------------------+------------------+-------------------+
| 08:00-09:10           | Алгебра          | Физика           | Программмирование |
+-----------------------+------------------+------------------+-------------------+
| 09:30-10:10           | Геометрия        | Физика           |                   |
+-----------------------+------------------+------------------+-------------------+
```

Так же можем загрузить свой файл с расписанием, но его придётся переименовать
```Расписание.xlsx``` -->  ```shedule.xlsx```
```
```
И привести к виду стандартного файла
```| от 08:00 до 09:10           | Алгебра          | Физика           | Программмирование |``` --->
```| 08:00-09:10           | Алгебра          | Физика           | Программмирование |```
