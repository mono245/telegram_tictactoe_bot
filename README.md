# Простой телеграм бот для игры в крестики-нолики

## Информация
Официального бота можно найти [здесь](https://t.me/okay_tictactoe_bot)\
**Бот НЕ работает 24/7!**\
_По техническим вопросам: [@o0ka1](https://t.me/o0ka1)_

### Требования к установке:
1. Python 3.11 и выше
2. Установленный git

### Установка:
1. Скопируйте репозиторий: `git clone https://github.com/mono245/telegram_tictactoe_bot.git`
2. Создайте файл .env рядом с bot.py в следующем формате:
```
BOT_TOKEN="your telegram token"
```
3. Перейдите в папку проекта в терминале: `cd ...`
4. (опционально) Создайте вирт. окружение: `python3 -m venv env`
5. И активируйте его (Windows): `env\Scripts\activate`, (Unix-подобные): `source env/bin/activate`
6. Установите зависимости: `pip3 install -r requirments.txt`
7. Готово :)

### Запуск:
1. Перейдите в терминале в папку bot к файлам bot.py, .env: `cd ...`
2. Запустите bot.py: (Windows) `python -m bot.bot`, (Unix-подобные): `python3 -m bot.bot`
3. Бот должен запуститься успешно :)