import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = os.getenv("TOKEN")

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
            InlineKeyboardButton("⚙️ Status", callback_data="status")
        ],
        [
            InlineKeyboardButton("🔧 API", callback_data="api"),
            InlineKeyboardButton("⏱ Time", callback_data="time")
        ],
        [
            InlineKeyboardButton("⚡ FAST", callback_data="fast"),
            InlineKeyboardButton("⭐ BEST", callback_data="best")
        ]
    ]

    await update.message.reply_text(
        "🎮 *PAINEL DE SALAS FF*",
        reply_markup=InlineKeyboardMarkup(teclado),
        parse_mode="Markdown"
    )

async def menu_botoes(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "4x4":
        await query.edit_message_text("🎮 *4x4 Personalizado*", parse_mode="Markdown")

    elif query.data == "top":
        await query.edit_message_text("🔥 *Top mais jogado*", parse_mode="Markdown")

    elif query.data == "historico":
        await query.edit_message_text("📜 *Histórico*", parse_mode="Markdown")

    elif query.data == "salas":
        await query.edit_message_text("🟢 *Salas Ativas*", parse_mode="Markdown")

    elif query.data == "saldo":
        await query.edit_message_text("💰 *Seu saldo*\nR$ 0,00", parse_mode="Markdown")

    elif query.data == "status":
        await query.edit_message_text("⚙️ *Sistema*\n🟢 Online", parse_mode="Markdown")

    elif query.data == "api":
        await query.edit_message_text("🔧 *API conectada*", parse_mode="Markdown")

    elif query.data == "time":
        await query.edit_message_text("⏱ *Tempo padrão*\n5 minutos", parse_mode="Markdown")

    elif query.data == "fast":
        await query.edit_message_text("⚡ *FAST ativado*", parse_mode="Markdown")

    elif query.data == "best":
        await query.edit_message_text("⭐ *BEST ativado*", parse_mode="Markdown")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(menu_botoes))

    print("🤖 Bot rodando...")
    app.run_polling()

if __name__ == "__main__":
    main()
