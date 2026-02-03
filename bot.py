import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes
)

TOKEN = "8512936747:AAGxiCpgrMNvUN8HPt7T7Ynk3c3yeb5lTO8"
  # ou token direto

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    teclado = [
        [
            InlineKeyboardButton("🎮 4x4", callback_data="4x4"),
            InlineKeyboardButton("🔥 TOP", callback_data="top")
        ],
        [
            InlineKeyboardButton("📜 Histórico", callback_data="historico"),
            InlineKeyboardButton("🟢 Salas", callback_data="salas")
        ],
        [
            InlineKeyboardButton("💰 Saldo", callback_data="saldo"),
            InlineKeyboardButton("📊 Status", callback_data="status")
        ],
        [
            InlineKeyboardButton("🌐 API", callback_data="api"),
            InlineKeyboardButton("⏱ Time", callback_data="time")
        ],
        [
            InlineKeyboardButton("⚡ FAST", callback_data="fast"),
            InlineKeyboardButton("⭐ BEST", callback_data="best")
        ]
    ]

    await update.message.reply_text(
        "🎛 *PAINEL DE SALAS FF*",
        reply_markup=InlineKeyboardMarkup(teclado),
        parse_mode="Markdown"
    )

async def botoes(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(f"Você clicou em: {query.data}")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(botoes))

    app.run_polling()

if __name__ == "__main__":
    main()
