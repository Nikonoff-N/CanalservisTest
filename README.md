# CanalservisTest
<h3> Тестовое задание от компании КаналСервис</h3>
Необходимо разработать скрипт на языке Python 3, 

который будет выполнять следующие функции:

1. Получать данные с документа при помощи Google API, сделанного в [Google Sheets](https://docs.google.com/spreadsheets/d/1f-qZEX1k_3nj5cahOzntYAnvO4ignbyesVO7yuBdv_g/edit) (необходимо копировать в свой Google аккаунт и выдать самому себе права).
2. Данные должны добавляться в БД, в том же виде, что и в файле –источнике, с добавлением колонки «стоимость в руб.»
    
    a. Необходимо создать DB самостоятельно, СУБД на основе PostgreSQL.
    
    b. Данные для перевода $ в рубли необходимо получать по курсу [ЦБ РФ](https://www.cbr.ru/development/SXML/).
    
3. Скрипт работает постоянно для обеспечения обновления данных в онлайн режиме (необходимо учитывать, что строки в Google Sheets таблицу могут удаляться, добавляться и изменяться).

Дополнения, которые дадут дополнительные баллы и поднимут потенциальный уровень оплаты труда:

1. a. Упаковка решения в docker контейнер
    
    b. Разработка функционала проверки соблюдения «срока поставки» из таблицы. В случае, если срок прошел, скрипт отправляет уведомление в Telegram.
    
    c. Разработка одностраничного web-приложения на основе Django или Flask. Front-end React.
    

На сегодня выполнил задачи 1-3

Для запуска скрипта запустите файл main.py.
Так же с скрипте dbWorker необходим подключить корректную базу данных. (В моём проекте используется локальная)
!FileNotFoundError: [Errno 2] No such file or directory: 'credentials.json'
Если выскочила такая ошибка, значит вы запустили скрипт не из папки script и он не мжет найти файл с ключами
Скопируйте путь к папке script и выполните сd [путь к папке]
На выполнение 1 -3 задачи ушло около 6 часов ( пришлось научиться работать с Google API)

Выполнил 4.а задание
Правда контейнер не будет работать, так как нужен правильный адресс БД. Даже если я смогу прокинуть его для своего компьютера через 192.168.0.1. Не факт что это сработает на компьютере проверяющего.
На установку Docker и пляски с бубном ушло 2 часа

Выполнил задание 4.б
Скрипт проверяет про какие заказы он еще не сообщал сегодня, про все новые он пишет в телеграмм канал https://t.me/+nMpDrn6S4bdhYTcy.
При желании, легко можно прописать любой канал.
На создание канала, создание токена для бота и скрипта в 15 строчек ушел час.

Выполнил задание 4.в.
Прописан одностраничное веб-приложение на Django. Фронтенд на HTML5+bootstrap. Я могу выучить React, но время ограничено.
Опять же для корректной работы необходимо прописать корректный адресс БД.
На создание веб-приложения ушло 2 часа.
