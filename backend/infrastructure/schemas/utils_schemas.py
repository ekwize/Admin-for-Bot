from infrastructure.schemas.base_schema import Base


class SBotMessage(Base):
    """  
    Schema for sending a message to the user
    """
    chat_id: int | str
    text: str
    
