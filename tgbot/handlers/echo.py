from aiogram import types, Router, F
from aiogram.filters import StateFilter
from aiogram.utils.markdown import hcode

echo_router = Router()


@echo_router.message(F.text, StateFilter(None))
async def bot_echo(message: types.Message):
    await message.answer(hcode(message.text))
