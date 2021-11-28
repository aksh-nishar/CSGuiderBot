from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

API_KEY = "2142160935:AAEGjTuZrHdNmLrGwVimS_OLs-qSfV-fd6c"

bot = Bot(token=API_KEY)
dp = Dispatcher(bot)

what_is_bot_button = KeyboardButton("What is CSGuider Bot?")
why_we_created_bot_button = KeyboardButton("Why we created this bot?")
important_note_button = KeyboardButton("\U00002757\U00002757Important Note\U00002757\U00002757")
go_to_guides_button = KeyboardButton("Go to Guides")

top_menu_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(what_is_bot_button)
top_menu_keyboard.add(why_we_created_bot_button)
top_menu_keyboard.add(important_note_button)
top_menu_keyboard.add(go_to_guides_button)

ai_and_ml_button = KeyboardButton("AI and ML Guide")
cyber_security_button = KeyboardButton("Cyber Security Guide")
game_development_button = KeyboardButton("Game Development Guide")
software_development_button = KeyboardButton("Software Development Guide")
blockchain_button = KeyboardButton("Blockchain Guide")
cloud_computing_button = KeyboardButton("Cloud Computing Guide")
networking_button = KeyboardButton("Networking Guide")
graphic_designing_button = KeyboardButton("Graphic Designing Guide")
data_science_button = KeyboardButton("Data Science Guide")
robotics_and_hardware_button = KeyboardButton("Robotics and Hardware Guide")
back_button = KeyboardButton("Back")
back_to_top_menu_button = KeyboardButton("Main Menu")

guides_menu_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(ai_and_ml_button, cyber_security_button)
guides_menu_keyboard.add(game_development_button, software_development_button)
guides_menu_keyboard.add(blockchain_button, cloud_computing_button)
guides_menu_keyboard.add(networking_button, graphic_designing_button)
guides_menu_keyboard.add(data_science_button, robotics_and_hardware_button)
guides_menu_keyboard.add(back_button, back_to_top_menu_button)

skills_required_button = KeyboardButton("Skills Required")
courses_button = KeyboardButton("Courses")
books_button = KeyboardButton("Books")
certifications_button = KeyboardButton("Certifications")
degrees_button = KeyboardButton("Degrees")
jobs_button = KeyboardButton("Jobs")

ai_and_ml_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(skills_required_button, courses_button)
ai_and_ml_keyboard.add(books_button, certifications_button)
ai_and_ml_keyboard.add(degrees_button, jobs_button)
ai_and_ml_keyboard.add(back_button, back_to_top_menu_button)


@dp.message_handler(commands=['start', 'help'])
async def welcome(message: types.Message):
    if message.is_command():
        await message.reply("Hello, Welcome to CSGuider Bot", reply_markup=top_menu_keyboard)
    else:
        await message.reply(message.text + " is not a recognized command, please enter /start")


@dp.message_handler()
async def main_keyboard_answer(message: types.Message):

    ai_and_ml_on = False
    cyber_security_on = False
    game_development_on = False
    software_development_on = False
    blockchain_on = False
    cloud_computing_on = False
    networking_on = False
    graphic_designing_on = False
    data_science_on = False
    robotics_and_hardware_on = False

    if message.text == "What is CSGuider Bot?":
        pass
    elif message.text == "Why we created this bot?":
        pass
    elif message.text == "\U00002757\U00002757Important Note\U00002757\U00002757":
        pass
    elif message.text == "Go to Guides":
        await message.answer("Guides", reply_markup=guides_menu_keyboard)
    elif message.text == "AI and ML Guide":
        await message.answer("AI and ML Guide", reply_markup=ai_and_ml_keyboard)
        if message.text == "Skills Required":
            pass
        elif message.text == "Courses":
            pass
        elif message.text == "Books":
            pass
        elif message.text == "Certifications":
            pass
        elif message.text == "Degrees":
            pass
        elif message.text == "Jobs":
            pass
        elif message.text == "Back":
            await message.answer("Back", reply_markup=guides_menu_keyboard)
        elif message.text == "Main Menu":
            await message.answer("Main Menu", reply_markup=guides_menu_keyboard)
        else:
            await message.answer("Not a recognized command, select one of the buttons")
    elif message.text == "Cyber Security Guide":
        cyber_security_on = True
        pass
    elif message.text == "Game Development Guide":
        game_development_on = True
        pass
    elif message.text == "Software Development Guide":
        software_development_on = True
        pass
    elif message.text == "Blockchain Guide":
        blockchain_on = True
        pass
    elif message.text == "Cloud Computing Guide":
        cloud_computing_on = True
        pass
    elif message.text == "Networking Guide":
        networking_on = True
        pass
    elif message.text == "Graphic Designing Guide":
        graphic_designing_on = True
        pass
    elif message.text == "Data Science Guide":
        data_science_on = True
        pass
    elif message.text == "Robotics and Hardware Guide":
        robotics_and_hardware_on = True
        pass
    elif message.text == "Back":
        await message.answer("Back", reply_markup=top_menu_keyboard)
    elif message.text == "Main Menu":
        await message.answer("Main Menu", reply_markup=top_menu_keyboard)
    else:
        await message.answer("Not a recognized command, select one of the buttons")


executor.start_polling(dp)
