# Площадка для сбора пожертвований на разные проекты: "Кошачий благотворительный фонд"

<details>
  <summary>Оглавление</summary>
  <ul>
    <li>
      <a href="#описание"> Описание</a>
      <ul>
          <li><a href="#проекты">Проекты</a></li>
          <li><a href="#пожертвования">Пожертвования</a></li>
          <li><a href="#пользователи">Пользователи</li>
      </ul>
    </li>
    <li>
      <a href="#используемые-библиотеки-и-пакеты">Используемые библиотеки и пакеты</a>
    </li>
    <li><a href="#инструкция-по-развёртыванию-проекта">Инструкция по развёртыванию проекта</a></li>
  </ul>
</details><br>


## **Описание**
***

Фонд собирает пожертвования на различные целевые проекты: на медицинское обслуживание, на обустройство и тд.

#### *Проекты*

В Фонде может быть открыто несколько целевых проектов. У каждого проекта есть название, описание и сумма, которую планируется собрать. После того как нужная сумма собрана — проект закрывается.
Пожертвования в проекты поступают по принципу First In, First Out: все пожертвования идут в проект, открытый раньше других; когда этот проект набирает необходимую сумму и закрывается — пожертвования начинают поступать в следующий проект.

#### *Пожертвования*

Каждый пользователь может сделать пожертвование и сопроводить его комментарием. Пожертвования не целевые: они вносятся в фонд, а не в конкретный проект. Каждое полученное пожертвование автоматически добавляется в первый открытый проект, который ещё не набрал нужную сумму. Если пожертвование больше нужной суммы или же в Фонде нет открытых проектов — оставшиеся деньги ждут открытия следующего проекта. При создании нового проекта все неинвестированные пожертвования автоматически вкладываются в новый проект.

#### *Пользователи*

Целевые проекты создаются администраторами сайта. 
Любой пользователь может видеть список всех проектов, включая требуемые и уже внесенные суммы. Это касается всех проектов — и открытых, и закрытых.
Зарегистрированные пользователи могут отправлять пожертвования и просматривать список своих пожертвований.

<br>

## **Используемые библиотеки и пакеты:**
***

Язык программирования: Python 3.9, реализация FastAPI

библиотеки и пакеты:

    aiofiles==0.8.0; python_version >= '3.6' and python_version < '4'
    aiogoogle==4.2.0
    aiohttp==3.8.1; python_version >= '3.6'
    aiosignal==1.2.0; python_version >= '3.6'
    aiosqlite==0.17.0
    alembic==1.7.7
    anyio==3.6.1
    asgiref==3.5.2
    async-timeout==4.0.2; python_version >= '3.6'
    attrs==21.4.0
    bcrypt==3.2.2
    cachetools==5.2.0; python_version ~= '3.7'
    certifi==2022.5.18.1
    cffi==1.15.0
    charset-normalizer==2.0.12
    click==8.1.3
    cryptography==37.0.2
    dnspython==2.2.1
    email-validator==1.2.1
    faker==12.0.1
    fastapi-users-db-sqlalchemy==4.0.3
    fastapi-users[sqlalchemy]==10.0.4
    fastapi==0.78.0
    flake8==4.0.1
    freezegun==1.2.1
    frozenlist==1.3.0; python_version >= '3.7'
    google-auth==2.8.0
    greenlet==1.1.2
    h11==0.13.0
    httptools==0.4.0
    idna==3.3
    iniconfig==1.1.1
    lock==2018.3.25.2110
    makefun==1.13.1
    mako==1.2.0
    markupsafe==2.1.1
    mccabe==0.6.1
    mixer==7.2.2
    multidict==6.0.2; python_version >= '3.7'
    packaging==21.3; python_version >= '3.6'
    passlib[bcrypt]==1.7.4
    pluggy==1.0.0
    py==1.11.0
    pyasn1-modules==0.2.8
    pyasn1==0.4.8
    pycodestyle==2.8.0
    pycparser==2.21
    pydantic==1.9.1
    pyflakes==2.4.0
    pyjwt[crypto]==2.3.0
    pyparsing==3.0.9
    pytest-asyncio==0.18.3
    pytest-freezegun==0.4.2
    pytest-pythonpath==0.7.4
    pytest==6.2.5
    python-dateutil==2.8.2
    python-dotenv==0.20.0
    python-multipart==0.0.5
    pyyaml==6.0
    requests==2.27.1
    rsa==4.8; python_version >= '3.6'
    six==1.16.0
    sniffio==1.2.0
    sqlalchemy==1.4.36
    starlette==0.19.1
    toml==0.10.2
    tonyg-rfc3339==0.1
    typing-extensions==4.2.0
    urllib3==1.26.9
    uvicorn[standard]==0.17.6
    watchgod==0.8.2
    websockets==10.3
    yarl==1.7.2; python_version >= '3.6'
<br>

## **Инструкция по развёртыванию проекта**
***

1. **Клонировать репозиторий и перейти в него в командной строке:**

```
git clone git@github.com:amirsvc/QRkot_spreadsheets.git
```

```
cd QRkot_spreadsheets
```

2. **Cоздать и активировать виртуальное окружение:**

```
python3 -m venv venv
```

- Если у вас Linux/macOS

  ```
  source venv/bin/activate
  ```

- Если у вас windows

  ```
  source venv/scripts/activate
  ```

3. **Установить зависимости из файла requirements.txt:**

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

4. **База данных и переменные окружения:**

В проекте используется база данных SQLite

Пример заполнения файла .env

```
APP_TITLE=Благотворительный фонд поддержки котиков QRKot
APP_DESCRIPTION=Фонд собирает пожертвования на различные проекты для котиков
DATABASE_URL=sqlite+aiosqlite:///./fastapi.db
SECRET=hufurnfriwnfmv
FIRST_SUPERUSER_EMAIL=admin@mail.com
FIRST_SUPERUSER_PASSWORD=Admin123
TYPE=service_account
PROJECT_ID=dsfuhsdgsdg-392014
PRIVATE_KEY_ID=847hs7hfs7g64gh7w9grhsgsdf
PRIVATE_KEY="-----BEGIN PRIVATE KEY-----\....\n-----END PRIVATE KEY-----\n"
CLIENT_EMAIL=dsfuhsdgsdg-service@dsfuhsdgsdg-345354.iam.gserviceaccount.com
CLIENT_ID=2452345234523452345
AUTH_URI=https://accounts.google.com/o/oauth2/auth
TOKEN_URI=https://oauth2.googleapis.com/token
AUTH_PROVIDER_X509_CERT_URL=https://www.googleapis.com/oauth2/v1/certs
CLIENT_X509_CERT_URL=https://www.googleapis.com/robot/v1/metadata/x509/dsfuhsdgsdg-service%40dsfuhsdgsdg-345354.iam.gserviceaccount.com
EMAIL=mail@mail.com
```

5. **Запуск проекта:**

Создаем базу данных

```
alembic upgrade head
```

Запускаем проект

```
uvicorn app.main:app --reload
```

Открываем Redoc проекта по адресу:

http://127.0.0.1:8000/docs

***
<h4 align="center">
Разработчик: <a href="https://github.com/amirsvc">Амир Исиналинов</a>
</h4