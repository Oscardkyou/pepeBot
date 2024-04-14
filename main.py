from aiogram import Bot, Dispatcher
from config_data.config import load_config, Config
import asyncio
from handlers import user_handlers, other_handlers
from keyboards.main_menu import set_main_menu


async def main() -> None:
   config: Config = load_config()
   bot = Bot(token=config.tg_bot.token)
   dp = Dispatcher()
   await set_main_menu(bot)
   dp.include_router(user_handlers.router)
   dp.include_router(other_handlers.router)
   await bot.delete_webhook(drop_pending_updates=True)
   await dp.start_polling(bot)



asyncio.run(main())
