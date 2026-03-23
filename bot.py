import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from telegram.error import TelegramError

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Токен бота
BOT_TOKEN = "8667992091:AAH51FCaFRjAa902x_pd6OKHgAAwPxK_tLM"

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик команды /help"""
    await update.message.reply_text(
        "📋 Команды бота:\n\n"
        "/all - упомянуть всех участников чата\n"
        "/help - показать эту справку\n\n"
        "💡 Также можно написать @all в любом сообщении, "
        "и бот автоматически упомянет всех участников.\n\n"
        "⚠️ Бот должен быть администратором группы."
    )

async def mention_all(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Упоминание всех участников чата"""
    chat = update.effective_chat
    
    # Проверка, что команда вызвана в группе
    if chat.type not in ['group', 'supergroup']:
        await update.message.reply_text(
            "⚠️ Эта команда работает только в группах!"
        )
        return
    
    try:
        # Получаем список администраторов
        admins = await context.bot.get_chat_administrators(chat.id)
        bot_is_admin = any(admin.user.id == context.bot.id for admin in admins)
        
        if not bot_is_admin:
            await update.message.reply_text(
                "⚠️ Бот должен быть администратором группы!"
            )
            return
        
        # Получаем количество участников
        member_count = await context.bot.get_chat_member_count(chat.id)
        
        # Формируем список упоминаний
        mentions = []
        
        for admin in admins:
            user = admin.user
            if not user.is_bot:
                if user.username:
                    mentions.append(f"@{user.username}")
                else:
                    mentions.append(f"[{user.first_name}](tg://user?id={user.id})")
        
        # Формируем и отправляем сообщение
        if mentions:
            mention_text = " ".join(mentions)
            message = f"📢 Внимание всем!\n\n{mention_text}"
            
            await update.message.reply_text(
                message,
                parse_mode='Markdown'
            )
            
            if len(mentions) < member_count:
                await update.message.reply_text(
                    f"ℹ️ Упомянуто {len(mentions)} из {member_count} участников."
                )
        else:
            await update.message.reply_text(
                "⚠️ Не удалось получить список участников."
            )
            
    except TelegramError as e:
        logger.error(f"Ошибка: {e}")
        await update.message.reply_text(
            f"❌ Произошла ошибка: {str(e)}"
        )

async def check_mention_all(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Проверка сообщений на наличие @all"""
    if update.message and update.message.text:
        if '@all' in update.message.text.lower():
            await mention_all(update, context)

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик ошибок"""
    logger.error(f"Ошибка: {context.error}")

def main():
    """Запуск бота"""
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Регистрируем обработчики команд
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("all", mention_all))
    
    # Обработчик текстовых сообщений для @all
    application.add_handler(MessageHandler(
        filters.TEXT & ~filters.COMMAND,
        check_mention_all
    ))
    
    # Обработчик ошибок
    application.add_error_handler(error_handler)
    
    logger.info("Бот запущен...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
