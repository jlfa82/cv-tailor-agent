from abc import ABC, abstractmethod

class MessagingClient(ABC): 

    @abstractmethod
    async def send_message(self, chat_id:str, text:str) -> None: 
        """Send a text to a user""" 
        pass

    @abstractmethod
    async def send_file(self, chat_id:str, file_path:str, caption: str=None) -> None: 
        """Send a file to a user"""
        pass

    @abstractmethod
    async def send_question(self, chat_id: str, question: str) -> None: 
        """Send a question to a user and wait for the response"""
        pass 
    