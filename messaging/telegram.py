from telegram import Bot 
from messaging.base import MessagingClient 

class TelegramClient(MessagingClient): 
    

    def __init__(self, token: str): 
        self.bot = Bot(token=token) 

    async def send_message(self, chat_id: str, text: str) -> None: 
        await self.bot.send_message(chat_id=chat_id, text=text) 

    async def send_file(self, chat_id: str, file_path: str, caption: str = None) -> None: 
        with open(file_path, "rb") as f: 
            await self.bot.send_document(
                chat_id=chat_id, 
                document=f, 
                caption=caption
                ) 

    async def send_question(self, chat_id: str, question: str) -> None: 
        await self.bot.send_message(
            chat_id=chat_id, 
            text=f"❓ {question}"
            ) 
        