import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message

TOKEN = "BOT_TOKENINGIZNI_BU_YERGA_QOYING"

dp = Dispatcher()


@dp.message()
async def echo(message: Message):
    await message.send_copy(chat_id=message.chat.id)


async def main():
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
