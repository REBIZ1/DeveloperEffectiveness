# DeveloperEffectiveness

Скрипт читает файлы с данными о закрытых задачах и формирует отчеты.

---

## Установка и запуск проекта

### 1. Клонирование репозитория
```
git clone git@github.com:REBIZ1/DeveloperEffectiveness.git
```

### 2. Создание и активация виртуального окружения 
```
# Создаём venv
python -m venv .venv

# Активируем
# Windows:
.venv\Scripts\activate
# macOS / Linux:
source .venv/bin/activate
```

### 3. Установка зависимостей
```
pip install -r requirements.txt
```

---

## Функциональность

### Параметры:

- **--files**, принимает название файлов. Необязательный параметр, в случае если он не передан данные берутся из /data;
- **--report**, принимает тип отчета. Необязательный параметр, в случае если он не передан значение = 'performance';
- **--save**, в случае если параметр передан сохраняет таблицу в csv файл.

### Примеры запуска:

#### С параметрами:
```
python main.py --files data/employees1.csv data/employees2.csv --report performance --save
```

<img width="321" height="180" alt="image" src="https://github.com/user-attachments/assets/2e37b4d0-b53a-4c7e-a462-3399388b3eca" />



#### Без параметров:
```
python main.py
```

<img width="313" height="176" alt="image" src="https://github.com/user-attachments/assets/668e80b7-57cc-4ac0-b3db-a500203c9d95" />



