# Пульт охраны банка
## Учебная задача dvmn.org, модуль django orm
### Описание
Работы с django orm на примере пульта охраны банка, показывает:
- список карт доступа
- список визитов по картам
- длительность визитов

### Установка и запуск
1. Скачайте код и перейдите в папку проекта.
    ```bash
    git clone https://github.com/n1k0din/n1k0din-django-orm-1
    ```  
    ```bash
    cd n1k0din-django-orm-1
    ```
2. Установите вирт. окружение.
    ```bash
    python -m venv venv
    ```
3. Активируйте.
    ```bash
    venv\Scripts\activate.bat
    ```
    или
    ```bash
    source venv/bin/activate
    ```
4. Установите необходимые пакеты.
    ```bash
    pip install -r requirements.txt
    ```
5. Подготовьте переменные окружения:
  - `DB_HOST=адрес_хоста_базы_данных` (пр. `localhost`)
  - `DB_PASSWORD=пароль_базы_данных`
  - `DJANGO_SECRET_KEY=секретный_ключ_django` (пр. `REPLACE_ME`)
  - `DJANGO_DEBUG=режим_отладки` (`True` или `False`)
  - `ALLOWED_HOSTS=список_ваших_сайтов` (пр. `localhost,127.0.0.1,mysite.com`).

6. Запустите (пример: на всех интерфейсах, порт 8080)
  ```bash
  python python manage.py runserver 0.0.0.0:8080
