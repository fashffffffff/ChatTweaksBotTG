# 🎯 Пошаговая инструкция: Деплой на Render.com

## Шаг 1: Создайте аккаунт на GitHub

1. Перейдите на [GitHub.com](https://github.com)
2. Нажмите "Sign up" и зарегистрируйтесь
3. Подтвердите email

## Шаг 2: Создайте репозиторий

1. На GitHub нажмите зеленую кнопку "New" (или "+" → "New repository")
2. Заполните:
   - Repository name: `telegram-mention-bot`
   - Description: `Telegram bot для упоминания всех участников`
   - Выберите "Public"
   - ✅ Поставьте галочку "Add a README file"
3. Нажмите "Create repository"

## Шаг 3: Загрузите файлы на GitHub

### Вариант А: Через веб-интерфейс (проще)

1. На странице вашего репозитория нажмите "Add file" → "Upload files"
2. Перетащите все файлы из папки `c:/projects/bot`:
   - `bot.py`
   - `requirements.txt`
   - `Procfile`
   - `runtime.txt`
   - `render.yaml`
   - `.gitignore`
3. Внизу страницы нажмите "Commit changes"

### Вариант Б: Через Git (если установлен)

Откройте командную строку в папке проекта и выполните:

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/ВАШ_USERNAME/telegram-mention-bot.git
git push -u origin main
```

## Шаг 4: Зарегистрируйтесь на Render

1. Перейдите на [Render.com](https://render.com)
2. Нажмите "Get Started for Free"
3. Выберите "Sign up with GitHub"
4. Разрешите Render доступ к вашему GitHub

## Шаг 5: Создайте Web Service

1. На Render нажмите "New +" → "Web Service"
2. Нажмите "Connect account" если нужно
3. Найдите репозиторий `telegram-mention-bot` и нажмите "Connect"
4. Заполните настройки:
   - **Name:** `telegram-mention-bot` (или любое другое)
   - **Region:** Frankfurt (EU Central) - ближе к России
   - **Branch:** main
   - **Runtime:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python bot.py`
5. Выберите план **Free**
6. Нажмите "Create Web Service"

## Шаг 6: Дождитесь деплоя

1. Render начнет устанавливать зависимости и запускать бота
2. Это займет 2-3 минуты
3. Когда увидите "Your service is live 🎉" - бот запущен!
4. В логах должно появиться: "Бот запущен..."

## Шаг 7: Проверьте работу

1. Откройте Telegram
2. Найдите вашего бота
3. Добавьте его в группу
4. Сделайте администратором
5. Напишите `/start` - бот должен ответить!

## ✅ Готово!

Теперь ваш бот работает 24/7 на серверах Render!

## ⚠️ Важные моменты

**Бесплатный план Render:**
- Бот засыпает через 15 минут неактивности
- Просыпается автоматически при первом сообщении (занимает ~30 секунд)
- Это нормально для бесплатного плана

**Если хотите, чтобы не засыпал:**
- Используйте Railway.app (500 часов/месяц бесплатно)
- Или платный план Render ($7/месяц)

## 🔄 Как обновить бота?

1. Измените файлы на GitHub (через веб-интерфейс или git push)
2. Render автоматически обнаружит изменения и передеплоит бота
3. Подождите 2-3 минуты

## 🆘 Проблемы?

**Бот не запускается:**
- Проверьте логи на Render (вкладка "Logs")
- Убедитесь, что токен правильный в `bot.py`

**Бот не отвечает:**
- Подождите 30 секунд (может просыпаться)
- Проверьте, что сервис "Live" на Render

**Ошибка деплоя:**
- Проверьте, что все файлы загружены на GitHub
- Убедитесь, что `requirements.txt` содержит `python-telegram-bot==20.7`
