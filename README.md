## Установка

1. Клонировать репозиторий
```bash
git clone <repository_url>
```

2. Создать и активировать виртуальное окружение
```bash
python -m venv .venv
```

Windows:
```bash
.venv\Scripts\activate
```

Linux/macOS:
```bash
source .venv/bin/activate
```

3. Установить зависимости
```bash
pip install -r requirements.txt
```

4. Скопировать `.env.example` в `.env`
Windows:
```bash
copy .env.example .env
```

Linux/macOS:
```bash
cp .env.example .env
```

5. Сгенерировать Django secret key
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

6. Вставить сгенерированный ключ в `.env`
```env
SECRET_KEY=ваш-сгенерированный-ключ
```

## Задания
1. Результат выполнения задания 1 находится в файле `task_1.py`. Запуск:
```bash
python task_1.py
```
В процессе работы скрипта будут выводиться отладочные сообщения, по которым можно будет понять, что происходит.

2. Для просмотра результата выполнения задания 2 см. файлы `core/views.py`, `core/urls.py` и `core/templates/objects_list.html`. Для ознакомления с таблицей:
```bash
python manage.py runserver
```
Перейти по адресу: `http://127.0.0.1:8000/core/objects/`.

3. Результат выполнения задания 3 находится в файле `task_3.py`. Запуск:
```bash
python task_3.py
```
Итоговый файл будет находиться по пути `core/docs/test_json.txt`. 
P.S. Я исходил из той логики, что в случае, если у версии документа удалены все родители, данная версия будет удалена, но при этом сам документ, у которого не останется версий, удалён не будет.

4. Результат выполнения задания 4 находится в файле `task_4.py`. Запуск:
```bash
python task_4.py
```
Итоговый файл будет находиться по пути `core/docs/test.txt`. 
