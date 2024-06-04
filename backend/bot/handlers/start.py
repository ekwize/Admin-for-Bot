from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from infrastructure.schemas.user_schemas import SUserCreate
from services import user_service
from messages.start_message import start_message


router = Router(name="Base")


@router.message(Command(commands=['start']))
async def start(message: Message, state: FSMContext):
    """ 
    Process the startup message 
    and save the user information in the database
    """

    user = await user_service().get_single(id=message.from_user.id)

    if not user:
        user_data = SUserCreate(
            id=message.from_user.id,
            first_name=message.from_user.first_name,
            last_name=message.from_user.last_name,
            full_name=message.from_user.full_name,
            is_premium=message.from_user.is_premium,
            username=message.from_user.username,
            language_code=message.from_user.language_code,
        )
        await user_service().create(user_data)

        await message.answer(
            text=start_message(
                first_name=message.from_user.first_name,
                user_exists=False
            ),
            parse_mode="HTML"
        )
        return

    await message.answer(
        text=start_message(
            first_name=message.from_user.first_name,
            user_exists=True
        ),
        parse_mode="HTML"
    )






 

