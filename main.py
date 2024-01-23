import asyncio
from aiogram import Bot, Dispatcher, types
from config import TOKEN
from handlers import router
from menu_commands import private

ALLOWED_UPDATES = ['message, edited_message']

bot = Bot(token=TOKEN)
dp = Dispatcher()

dp.include_router(router)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    # await bot.delete_my_commands(scope=types.BotCommandScopeAllPrivateChats())
    await bot.set_my_commands(commands=private, scope=types.BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)

if __name__ == '__main__':
    asyncio.run(main())