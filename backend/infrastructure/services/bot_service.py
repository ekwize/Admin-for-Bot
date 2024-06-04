from aiogram import Bot
from infrastructure.schemas.utils_schemas import SBotMessage


class BotService:

    def __init__(self, bot: Bot):
        self._bot: Bot = bot

    async def send_message(self, data: SBotMessage) -> None:
        try:
            # if data.photo:
            #     await self._bot.send_photo(chat_id=data.chat_id, photo=data.photo, caption=data.text)
            await self._bot.send_message(chat_id=data.chat_id, text=data.text)

        except Exception as e:
            print('An error occurred while sending the message:', e)


