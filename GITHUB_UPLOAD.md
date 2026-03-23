# 📤 Как загрузить бота на GitHub (через веб-интерфейс)

## Шаг 1: Создайте аккаунт на GitHub

1. Откройте [GitHub.com](https://github.com)
2. Нажмите **"Sign up"** (Зарегистрироваться)
3. Введите email, пароль, username
4. Подтвердите email

## Шаг 2: Создайте новый репозиторий

1. После входа нажмите зеленую кнопку **"New"** (или значок "+" → "New repository")
2. Заполните форму:
   - **Repository name:** `telegram-mention-bot` (или любое другое имя)
   - **Description:** `Telegram bot для упоминания всех участников`
   - **Public** - оставьте выбранным
   - ✅ Поставьте галочку **"Add a README file"**
3. Нажмите **"Create repository"**

## Шаг 3: Загрузите файлы

1. На странице вашего репозитория нажмите **"Add file"** → **"Upload files"**

2. Перетащите эти файлы из папки `c:/projects/bot` в окно браузера:
   - `bot.py`
   - `requirements.txt`
   - `Procfile`
   - `runtime.txt`
   - `render.yaml`
   - `.gitignore`
   - `DEPLOY_GUIDE.md`

3. Внизу страницы в поле "Commit changes" напишите: `Добавил файлы бота`

4. Нажмите зеленую кнопку **"Commit changes"**

## Шаг 4: Готово!

Теперь все файлы загружены на GitHub. Вы увидите их список на странице репозитория.

## Шаг 5: Деплой на Render.com

1. Откройте [Render.com](https://render.com)
2. Нажмите **"Get Started for Free"**
3. Выберите **"Sign up with GitHub"**
4. Разрешите Render доступ к GitHub
5. Нажмите **"New +"** → **"Web Service"**
6. Найдите ваш репозиторий `telegram-mention-bot` и нажмите **"Connect"**
7. Настройки:
   - **Name:** `telegram-mention-bot`
   - **Region:** Frankfurt (EU Central)
   - **Branch:** main
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python bot.py`
8. Выберите план **"Free"**
9. Нажмите **"Create Web Service"**

## Шаг 6: Дождитесь запуска

- Render установит зависимости и запустит бота (2-3 минуты)
- Когда увидите "Your service is live 🎉" - бот работает!
- В логах должно быть: "Бот запущен..."

## ✅ Проверка

1. Откройте Telegram
2. Найдите вашего бота
3. Добавьте в группу
4. Сделайте администратором
5. Напишите `/help` - бот должен ответить!

---

## 🔄 Как обновить бота в будущем?

1. Откройте ваш репозиторий на GitHub
2. Нажмите на файл, который хотите изменить (например, `bot.py`)
3. Нажмите значок карандаша (Edit)
4. Внесите изменения
5. Нажмите "Commit changes"
6. Render автоматически обновит бота через 2-3 минуты

---

**Всё! Ваш бот теперь работает 24/7 бесплатно! 🎉**
