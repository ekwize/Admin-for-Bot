from fastapi import APIRouter, Depends
from typing import Annotated

from api.dependencies import bot_service

from infrastructure.schemas.utils_schemas import SBotMessage
from infrastructure.services.bot_service import BotService


router = APIRouter(prefix="/utils", tags=["User Utils"])


@router.post("/user/message/", response_model=None)
async def send_user_message(
    data: SBotMessage,
    bot_service: Annotated[BotService, Depends(bot_service)]
) -> None:
    await bot_service.send_message(data)

