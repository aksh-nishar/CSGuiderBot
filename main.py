# Diploma Final Year Project - CSGuider Telegram Bot
# Authors - Aksh Nishar, Kenneth Rodrigues, Khush Trivedi
# Created - December 2021

# Importing necessary classes from aiogram module
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# API KEY - got from Telegram's BotFather
API_KEY = "2142160935:AAEGjTuZrHdNmLrGwVimS_OLs-qSfV-fd6c"

# Bot class creates and initializes the bot
# Dispatcher class dispatches all kinds of updates to the Bot's registered handlers.
bot = Bot(token=API_KEY)
dp = Dispatcher(bot)

# Creating all the necessary buttons
what_is_bot_button = KeyboardButton("\U0001F937 What is CSGuider Bot? \U0001F937")
important_note_button = KeyboardButton("\U00002757\U00002757Important Notes\U00002757\U00002757")
go_to_guides_button = KeyboardButton("\U0001F4DA\U0001F4DA Go to Guides \U0001F4DA\U0001F4DA")
contact_us_button = KeyboardButton("\U0001F4E7 Contact Us \U0001F4E7")

ai_and_ml_button = KeyboardButton("\U00002699 AI and ML \U00002699")
cyber_security_button = KeyboardButton("\U0001F3AD Cyber Security \U0001F3AD")
game_development_button = KeyboardButton("\U0001F3AE Game Development \U0001F3AE")
software_development_keyboard = KeyboardButton("\U0001F5A5 Software Development \U0001F5A5")
blockchain_button = KeyboardButton("\U0001F517 Blockchain \U0001F517")
cloud_computing_button = KeyboardButton("\U00002601 Cloud Computing \U00002601")
networking_button = KeyboardButton("\U0001F4F6 Networking \U0001F4F6")
graphic_designing_button = KeyboardButton("\U0001F5BC Graphic Designing \U0001F5BC")
data_science_button = KeyboardButton("\U0001F4CA Data Science \U0001F4CA")
robotics_and_hardware_button = KeyboardButton("\U0001F916 Robotics and Hardware \U0001F916")
web_development_button = KeyboardButton("\U0001F310 Web Development \U0001F310")
front_end_development_button = KeyboardButton("\U00002B06 Front-End Web Development \U00002B06")
back_end_development_button = KeyboardButton("\U00002B07 Back-End Web Development \U00002B07")
application_development_button = KeyboardButton("\U0001F4BB Application Development \U0001F4BB")
android_development_button = KeyboardButton("\U0001F4F1 Android App Development \U0001F4F1")
ios_development_button = KeyboardButton("\U0001F4F2 IOS App Development \U0001F4F2")

skills_required_button = KeyboardButton("\U0001F530 Skills Required")
courses_button = KeyboardButton("\U0001F4BB Courses")
books_button = KeyboardButton("\U0001F4D6 Books")
certifications_button = KeyboardButton("\U0001F3C5 Certifications")
degrees_button = KeyboardButton("\U0001F393 Degrees")
jobs_button = KeyboardButton("\U0001F935 Jobs")
certifications_degrees_button = KeyboardButton("\U0001F393 Certifications/Degrees")
back_button = KeyboardButton("\U0001F519 Back")
back_to_top_menu_button = KeyboardButton("\U0001F51D Main Menu")

what_is_ai_and_ml_button = KeyboardButton("\U0001F937 What is AI and ML \U0001F937")
what_is_cyber_security_button = KeyboardButton("\U0001F937 What is Cyber Security \U0001F937")
what_is_game_development_button = KeyboardButton("\U0001F937 What is Game Development \U0001F937")
what_is_blockchain_button = KeyboardButton("\U0001F937 What is Blockchain \U0001F937")
what_is_cloud_computing_button = KeyboardButton("\U0001F937 What is Cloud Computing \U0001F937")
what_is_networking_button = KeyboardButton("\U0001F937 What is Networking \U0001F937")
what_is_graphic_designing_button = KeyboardButton("\U0001F937 What is Graphic Designing \U0001F937")
what_is_data_science_button = KeyboardButton("\U0001F937 What is Data Science \U0001F937")
what_is_robotics_and_hardware_button = KeyboardButton("\U0001F937 What is Robotics and Hardware \U0001F937")
what_is_front_end_development_button = KeyboardButton("\U0001F937 What is Front-End Web Development \U0001F937")
what_is_back_end_development_button = KeyboardButton("\U0001F937 What is Back-End Web Development \U0001F937")
what_is_android_app_development_button = KeyboardButton("\U0001F937 What is Android App Development \U0001F937")
what_is_ios_app_development_button = KeyboardButton("\U0001F937 What is IOS App Development \U0001F937")

# Creating all the necessary keyboards which will contain the buttons
top_menu_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(what_is_bot_button)
top_menu_keyboard.add(important_note_button)
top_menu_keyboard.add(go_to_guides_button)
top_menu_keyboard.add(contact_us_button)

guides_menu_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(ai_and_ml_button, cyber_security_button)
guides_menu_keyboard.add(game_development_button, software_development_keyboard)
guides_menu_keyboard.add(blockchain_button, cloud_computing_button)
guides_menu_keyboard.add(networking_button, graphic_designing_button)
guides_menu_keyboard.add(data_science_button, robotics_and_hardware_button)
guides_menu_keyboard.add(back_button, back_to_top_menu_button)

ai_and_ml_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(what_is_ai_and_ml_button)
ai_and_ml_keyboard.add(skills_required_button, courses_button)
ai_and_ml_keyboard.add(books_button, jobs_button)
ai_and_ml_keyboard.add(certifications_degrees_button)
ai_and_ml_keyboard.add(back_button, back_to_top_menu_button)

cyber_security_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(what_is_cyber_security_button)
cyber_security_keyboard.add(skills_required_button, courses_button)
cyber_security_keyboard.add(books_button, certifications_button)
cyber_security_keyboard.add(degrees_button, jobs_button)
cyber_security_keyboard.add(back_button, back_to_top_menu_button)

blockchain_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(what_is_blockchain_button)
blockchain_keyboard.add(skills_required_button, courses_button)
blockchain_keyboard.add(books_button, certifications_button)
blockchain_keyboard.add(degrees_button, jobs_button)
blockchain_keyboard.add(back_button, back_to_top_menu_button)

networking_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(what_is_networking_button)
networking_keyboard.add(skills_required_button, courses_button)
networking_keyboard.add(books_button, certifications_button)
networking_keyboard.add(degrees_button, jobs_button)
networking_keyboard.add(back_button, back_to_top_menu_button)

graphic_designing_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(what_is_graphic_designing_button)
graphic_designing_keyboard.add(skills_required_button, courses_button)
graphic_designing_keyboard.add(books_button, certifications_button)
graphic_designing_keyboard.add(degrees_button, jobs_button)
graphic_designing_keyboard.add(back_button, back_to_top_menu_button)

cloud_computing_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(what_is_cloud_computing_button)
cloud_computing_keyboard.add(skills_required_button, courses_button)
cloud_computing_keyboard.add(books_button, certifications_button)
cloud_computing_keyboard.add(degrees_button, jobs_button)
cloud_computing_keyboard.add(back_button, back_to_top_menu_button)

software_development_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(web_development_button)
software_development_keyboard.add(application_development_button)
software_development_keyboard.add(back_button, back_to_top_menu_button)

web_development_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(front_end_development_button)
web_development_keyboard.add(back_end_development_button)
web_development_keyboard.add(back_button, back_to_top_menu_button)

application_development_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(android_development_button)
application_development_keyboard.add(ios_development_button)
application_development_keyboard.add(back_button, back_to_top_menu_button)

data_science_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(what_is_data_science_button)
data_science_keyboard.add(skills_required_button, courses_button)
data_science_keyboard.add(books_button, certifications_button)
data_science_keyboard.add(degrees_button, jobs_button)
data_science_keyboard.add(back_button, back_to_top_menu_button)

game_development_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(what_is_game_development_button)
game_development_keyboard.add(skills_required_button, courses_button)
game_development_keyboard.add(books_button, certifications_button)
game_development_keyboard.add(degrees_button, jobs_button)
game_development_keyboard.add(back_button, back_to_top_menu_button)

robotics_and_hardware_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(what_is_robotics_and_hardware_button)
robotics_and_hardware_keyboard.add(skills_required_button, courses_button)
robotics_and_hardware_keyboard.add(books_button, certifications_button)
robotics_and_hardware_keyboard.add(degrees_button, jobs_button)
robotics_and_hardware_keyboard.add(back_button, back_to_top_menu_button)

front_end_development_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(what_is_front_end_development_button)
front_end_development_keyboard.add(skills_required_button, courses_button)
front_end_development_keyboard.add(books_button, certifications_button)
front_end_development_keyboard.add(degrees_button, jobs_button)
front_end_development_keyboard.add(back_button, back_to_top_menu_button)

back_end_development_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(what_is_back_end_development_button)
back_end_development_keyboard.add(skills_required_button, courses_button)
back_end_development_keyboard.add(books_button, certifications_button)
back_end_development_keyboard.add(degrees_button, jobs_button)
back_end_development_keyboard.add(back_button, back_to_top_menu_button)

android_development_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(what_is_android_app_development_button)
android_development_keyboard.add(skills_required_button, courses_button)
android_development_keyboard.add(books_button, jobs_button)
android_development_keyboard.add(certifications_degrees_button)
android_development_keyboard.add(back_button, back_to_top_menu_button)

ios_development_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(what_is_ios_app_development_button)
ios_development_keyboard.add(skills_required_button, courses_button)
ios_development_keyboard.add(books_button, jobs_button)
ios_development_keyboard.add(back_button, back_to_top_menu_button)

# Boolean values to identify which keyboard/guide user is interacting with
ai_and_ml_on = False
cyber_security_on = False
game_development_on = False
software_development_on = False
web_development_on = False
front_end_development_on = False
back_end_development_on = False
full_stack_development_on = False
application_development_on = False
android_development_on = False
ios_development_on = False
desktop_development_on = False
blockchain_on = False
cloud_computing_on = False
networking_on = False
graphic_designing_on = False
data_science_on = False
robotics_and_hardware_on = False


# Asynchronous functions are used. They cannot be avoided otherwise the code will break.
# await keyword is also used to prevent errors and to continuously wait for user's input.
@dp.message_handler(commands=['start'])
async def welcome(message: 'types.Message') -> None:
    """
    Function to handle the start command.

    :param message: To receive the commands from the user. If any other text is entered other than the specified
        command, an error message will be shown by the bot.
    :return: None
    """
    if message.is_command():
        await message.reply("Hello, Welcome to CSGuider Bot", reply_markup=top_menu_keyboard)
    else:
        await message.reply(message.text + " is not a recognized command, please enter /start")


@dp.message_handler()
async def main_keyboard_answer(message: 'types.Message') -> None:
    """
    Function which will handle all the commands of the bot, except the start command.

    :param message: To receive the commands from the user. If any other text is entered other than the specified
        commands, an error message will be shown by the bot.
    :return: None
    """
    # global keyword prevents the below variables to be used as local variables.
    global ai_and_ml_on, cyber_security_on, game_development_on, software_development_on, blockchain_on, \
        cloud_computing_on, networking_on, graphic_designing_on, data_science_on, robotics_and_hardware_on, \
        web_development_on, front_end_development_on, back_end_development_on, full_stack_development_on, \
        application_development_on, android_development_on, ios_development_on, desktop_development_on

    # if...elif...else ladder to handle all the commands
    if message.text == "\U0001F937 What is CSGuider Bot? \U0001F937":
        await message.answer("\U0001F4BB CSGuiderBot\n\n\n\
\U0001F4BB What is CSGuider Bot?\n\n\
CSGuider is a comprehensive guide to specialization within the Computer Science field.\n\n\
It is aimed at providing students with a list of possible opportunities within the Computer Science field along with \
providing them with resources related to these specialization fields with the help of a responsive UI.\n\n\
The following resources are included in the CSGuider Bot:\n\
\U00002666 Skills Required \n\
\U00002666 Courses\n\
\U00002666 Books\n\
\U00002666 Degrees\n\
\U00002666 Certifications\n\
\U00002666 Job Opportunities\n\n\
All these features are conveniently packed into an easy to use and interactive Telegram Bot ")

    elif message.text == "\U00002757\U00002757Important Notes\U00002757\U00002757":
        await message.answer("\U0001F6A9 All the resources provided in this bot will help you move from a \
beginner level with no knowledge to an intermediate level. However, to become an expert in any field you will \
need a lot of practice, real-world experience, a never-stop-learning attitude and staying up-to-date with trends.\n\n\
\U0001F6A9 A second important thing to remember is to do some research before enrolling in any course, \
certification, degree program or purchasing a book to find out if they are suitable for you, whether all \
prerequisites are met, and if the skills they are providing are what you need, so that you don't regret \
after buying them.")

    elif message.text == "\U0001F4DA\U0001F4DA Go to Guides \U0001F4DA\U0001F4DA":
        await message.answer("Guides", reply_markup=guides_menu_keyboard)

    elif message.text == "\U0001F4E7 Contact Us \U0001F4E7":
        await message.answer("If you have any questions, feel free to email any one of us: \n\n\
aksh.nishar@somaiya.edu\n\n\
kenneth.r@somaiya.edu\n\n\
khush.t@somaiya.edu")

    elif message.text == "\U00002699 AI and ML \U00002699":
        ai_and_ml_on = True
        await message.answer("\U00002699 AI and ML \U00002699", reply_markup=ai_and_ml_keyboard)

    elif message.text == "\U0001F3AD Cyber Security \U0001F3AD":
        cyber_security_on = True
        await message.answer("\U0001F3AD Cyber Security \U0001F3AD", reply_markup=cyber_security_keyboard)

    elif message.text == "\U0001F3AE Game Development \U0001F3AE":
        game_development_on = True
        await message.answer("Game Development", reply_markup=game_development_keyboard)

    elif message.text == "\U0001F5A5 Software Development \U0001F5A5":
        software_development_on = True
        await message.answer("\U0001F5A5 Software Development \U0001F5A5",
                             reply_markup=software_development_keyboard)

    elif message.text == "\U0001F310 Web Development \U0001F310":
        web_development_on = True
        await message.answer("\U0001F310 Web Development \U0001F310", reply_markup=web_development_keyboard)

    elif message.text == "\U00002B06 Front-End Web Development \U00002B06":
        front_end_development_on = True
        await message.answer("\U00002B06 Front-End Web Development \U00002B06",
                             reply_markup=front_end_development_keyboard)

    elif message.text == "\U00002B07 Back-End Web Development \U00002B07":
        back_end_development_on = True
        await message.answer("\U00002B07 Back-End Web Development \U00002B07",
                             reply_markup=back_end_development_keyboard)

    elif message.text == "\U0001F4BB Application Development \U0001F4BB":
        application_development_on = True
        await message.answer("\U0001F4BB Application Development \U0001F4BB",
                             reply_markup=application_development_keyboard)

    elif message.text == "\U0001F4F1 Android App Development \U0001F4F1":
        android_development_on = True
        await message.answer("\U0001F4F1 Android App Development \U0001F4F1",
                             reply_markup=android_development_keyboard)

    elif message.text == "\U0001F4F2 IOS App Development \U0001F4F2":
        ios_development_on = True
        await message.answer("\U0001F4F2 IOS App Development \U0001F4F2", reply_markup=ios_development_keyboard)

    elif message.text == "\U0001F517 Blockchain \U0001F517":
        blockchain_on = True
        await message.answer("\U0001F517 Blockchain \U0001F517", reply_markup=blockchain_keyboard)

    elif message.text == "\U00002601 Cloud Computing \U00002601":
        cloud_computing_on = True
        await message.answer("\U00002601 Cloud Computing \U00002601", reply_markup=cloud_computing_keyboard)

    elif message.text == "\U0001F4F6 Networking \U0001F4F6":
        networking_on = True
        await message.answer("\U0001F4F6 Networking \U0001F4F6", reply_markup=networking_keyboard)

    elif message.text == "\U0001F5BC Graphic Designing \U0001F5BC":
        graphic_designing_on = True
        await message.answer("Graphic Designing", reply_markup=graphic_designing_keyboard)

    elif message.text == "\U0001F4CA Data Science \U0001F4CA":
        data_science_on = True
        await message.answer("Data Science", reply_markup=data_science_keyboard)

    elif message.text == "\U0001F916 Robotics and Hardware \U0001F916":
        robotics_and_hardware_on = True
        await message.answer("Robotics and Hardware", reply_markup=robotics_and_hardware_keyboard)

    elif message.text == "\U0001F937 What is AI and ML \U0001F937":
        await message.answer("\U0001F6A9 Artificial Intelligence (AI) is a technology using which we can create \
intelligent systems that can simulate human intelligence. The Artificial intelligence system does not require to \
be pre-programmed, instead of that, they use such algorithms which can work with their own intelligence. It \
involves machine learning algorithms such as Reinforcement learning algorithm and deep learning neural networks. \
AI is being used in multiple places such as Siri, Google Assistant, AI in Chess playing, etc.\n\n\
\U0001F6A9 Machine Learning (ML) is a subfield of artificial intelligence, which enables machines to learn from \
past data or experiences without being explicitly programmed. Machine learning works on algorithm which learn by \
it's own using historical data. It works only for specific domains such as if we are creating a machine learning \
model to detect pictures of dogs, it will only give result for dog images, but if we provide a new data like cat \
image then it will become unresponsive. Machine learning is being used in various places such as for online \
recommender system, for Google search algorithms, Email spam filter, Facebook Auto friend tagging suggestion, etc.")

    elif message.text == "\U0001F937 What is Cyber Security \U0001F937":
        await message.answer("\U0001F6A9 Computer security, cyber security, or information technology security \
(IT security) is the protection of computer systems and networks from information disclosure, theft of \
or damage to their hardware, software, or electronic data, as well as from the disruption or misdirection \
of the services they provide.\n\nThe field is becoming increasingly significant due to the continuously expanding \
reliance on computer systems, the Internet and wireless network standards such as Bluetooth and Wi-Fi, and due \
to the growth of `smart` devices, including smartphones, televisions, and the various devices that constitute \
the `Internet of things`.")

    elif message.text == "\U0001F937 What is Game Development \U0001F937":
        await message.answer("\U0001F6A9 Game Development is the art of creating games and describes the design, \
development and release of a game. It may involve concept generation, design, build, test and release. \
While you create a game, it is important to think about the game mechanics, rewards, player engagement \
and level design.\n\nGame Development can be undertaken by a large Game Development Studio or by a single individual. \
It can be as small or large as you like. As long as it lets the player interact with content and is able to \
manipulate the game’s elements, you can call it a `game`.")

    elif message.text == "\U0001F937 What is Blockchain \U0001F937":
        await message.answer("\U0001F6A9 A blockchain is a growing list of records, called blocks, that are linked \
together using cryptography. Each block contains a cryptographic hash of the previous block, a timestamp, \
and transaction data (generally represented as a Merkle tree). The timestamp proves that the transaction data \
existed when the block was published in order to get into its hash. As blocks each contain information about the \
block previous to it, they form a chain, with each additional block reinforcing the ones before it. Therefore, \
blockchains are resistant to modification of their data because once recorded, the data in any given block cannot \
be altered retroactively without altering all subsequent blocks.\n\n Blockchains are typically managed by a \
peer-to-peer network for use as a publicly distributed ledger, where nodes collectively adhere to a protocol to \
communicate and validate new blocks. Although blockchain records are not unalterable as forks are possible, \
blockchains may be considered secure by design and exemplify a distributed computing system with high Byzantine \
fault tolerance.")

    elif message.text == "\U0001F937 What is Cloud Computing \U0001F937":
        await message.answer("\U0001F6A9 Cloud computing is the delivery of different services through the Internet. \
These resources include tools and applications like data storage, servers, databases, networking, and software. \
Rather than keeping files on a proprietary hard drive or local storage device, cloud-based storage makes it possible \
to save them to a remote database. As long as an electronic device has access to the web, it has access to the data \
and the software programs to run it. \n\nCloud computing is a popular option for people and businesses for a number of \
reasons including cost savings, increased productivity, speed and efficiency, performance, and security.")

    elif message.text == "\U0001F937 What is Networking \U0001F937":
        await message.answer("\U0001F6A9 A computer networking is a process of connecting two more than two \
computers with the purpose to share data, provide technical support, and to communicate. \n\n\
Internet is the technology that is used to connect different computer systems (located in different \
geographic location). Networking technology has revolutionized the world and created a new arena for the overall \
development of every nation.")

    elif message.text == "\U0001F937 What is Graphic Designing \U0001F937":
        await message.answer("\U0001F6A9 Graphic design is the profession and academic discipline whose activity \
consists in projecting visual communications intended to transmit specific messages to social groups, with specific \
objectives. Therefore, graphic design is an interdisciplinary branch of design whose foundations and objectives \
revolve around the definition of problems and the determination of objectives for decision-making, through creativity, \
innovation and lateral thinking along with manual or digital tools, transforming them for proper interpretation. \
This activity helps in the optimization of graphic communications.\n\nThe design work can be based on a customer’s \
demand, a demand that ends up being established linguistically, either orally or in writing, that is, that graphic \
design transforms a linguistic message into a graphic manifestation.")

    elif message.text == "\U0001F937 What is Data Science \U0001F937":
        await message.answer("\U0001F6A9 Data science is an interdisciplinary field that uses scientific methods, \
processes, algorithms and systems to extract knowledge and insights from noisy, structured and unstructured data, \
and apply knowledge and actionable insights from data across a broad range of application domains. Data science is \
related to data mining, machine learning and big data. \n\nData science is a `concept to unify statistics, data \
analysis, informatics, and their related methods` in order to `understand and analyze actual phenomena` with data. \
It uses techniques and theories drawn from many fields within the context of mathematics, statistics, computer \
science, information science, and domain knowledge. \n\nA data scientist is someone who creates programming code, and \
combines it with statistical knowledge to create insights from data.")

    elif message.text == "\U0001F937 What is Robotics and Hardware \U0001F937":
        await message.answer("\U0001F6A9 Robotics is the intersection of science, engineering and technology that \
produces machines, called robots, that substitute for (or replicate) human actions. A robot is the product of the \
robotics field, where programmable machines are built that can assist humans or mimic human actions. \n\n Robots were \
originally built to handle monotonous tasks (like building cars on an assembly line), but have since expanded well \
beyond their initial uses to perform tasks like fighting fires, cleaning homes and assisting with incredibly \
intricate surgeries. Each robot has a differing level of autonomy, ranging from human-controlled bots that carry \
out tasks that a human has full control over to fully-autonomous bots that perform tasks without any \
external influences.")

    elif message.text == "\U0001F937 What is Front-End Web Development \U0001F937":
        await message.answer("\U0001F6A9 Front-end web development is the development of the graphical user interface \
of a website, through the use of HTML, CSS, and JavaScript, so that users can view and interact with that website. \
It involves transforming the code built by backend developers into a graphical interface, making sure that the data \
is presented in an easy-to-read and -understand format. \n\nWithout frontend development, all you would see on a \
website or web application are undecipherable codes (unless you’re a developer, too, of course). But because of \
frontend developers, people with no coding background can easily understand and use web applications and websites.")

    elif message.text == "\U0001F937 What is Back-End Web Development \U0001F937":
        await message.answer("\U0001F6A9 Backend is the server-side of the website. It stores and arranges data, and \
also makes sure everything on the client-side of the website works fine. It is the part of the website that \
you cannot see and interact with. It is the portion of software that does not come in direct contact with \
the users.\n\nThe parts and characteristics developed by backend designers are indirectly accessed by users through \
a front-end application. Activities, like writing APIs, creating libraries, and working with system components \
without user interfaces or even systems of scientific programming, are also included in the backend.")

    elif message.text == "\U0001F937 What is Android App Development \U0001F937":
        await message.answer("\U0001F6A9 Android app development is a process in which mobile apps are developed \
for devices that run the Android operating system. Android apps are written with the help of languages such \
as Java, Kotlin and C++ languages with the Android Software Development Kit (SDK). Android was initially \
released in the year 2009 and is basically written in Java language.")

    elif message.text == "\U0001F937 What is IOS App Development \U0001F937":
        await message.answer("\U0001F6A9 IOS application development is the process of making mobile applications \
for Apple hardware, including iPhone, iPad and iPod Touch. The software is written in the Swift programming \
language or Objective-C and then deployed to the App Store for users to download.")

    elif message.text == "\U0001F530 Skills Required":
        if ai_and_ml_on:
            await message.answer("Some skills required to get into AI and ML are as follows:\n\n\n \
\U00002666 Applied Mathematics which include\n \
Linear algebra, probability, statistics, multivariate calculus, distributions like Poisson, normal, binomial, etc\
and some knowledge of Physics concepts.\n\
Mathematics for Machine Learning Course:\n\
https://www.youtube.com/playlist?list=PLmAuaUS7wSOP-iTNDivR0ANKuTUhEzMe4\n\n \
\U00002666 Computer Science Fundamentals and Programming\n \
CS concepts like data structures and algorithms, space and time complexity, programming languages like Python and R\
for ML and statistics, Spark and Hadoop for distributed computing, SQL for database management, Apache Kafka for\
data pre-processing, etc. Python libraries like NumPy, Pandas, Matplotlib, Scikit-Learn, Tensor-Flow, etc.\n\n \
\U00002666 Machine Learning algorithms\n \
Some common ones include Naïve Bayes Classifier, K Means Clustering, Support Vector Machine, Apriori Algorithm, \
Linear Regression, Logistic Regression, Decision Trees, Random Forests, etc.\n\
Machine Learning Algorithms:\n\
https://www.youtube.com/playlist?list=PLmAuaUS7wSOMsOj6PRpxQ4SiGEsCO349V\n\n \
\U00002666 Neural Networks\n \
Different types of neural networks like Feedforward Neural Network, Recurrent Neural Network, \
Convolutional Neural Network, Modular Neural Network, Radial basis function Neural Network, etc.\n\
Neural Networks Courses:\n\
https://www.youtube.com/results?search_query=neural+networks+course\n\n \
\U00002666 Natural Language Processing\n \
This is so that machines can understand and interpret the human language to eventually understand human \
communication in a better way. Natural Language Toolkit which is the most popular platform for creating \
applications relating to NLP.\n\
Natural Language Processing Courses:\n\
https://www.youtube.com/results?search_query=natural+language+processing+course\n\n \
\U00002666 Data Modeling and Evaluation\n \
Data modeling involves understanding the underlying structure of the data and then finding patterns that are \
not obvious to the naked eye. You also need to evaluate the data using an algorithm that is suitable for the data.\n\n\
\U00002666 Communication Skills\n \
That’s because while you understand the data and the insights obtained using machine learning better than anyone \
else, it is equally important that you can convey these insights to a non-technical team, your shareholders, \
or clients.")
        elif cyber_security_on:
            await message.answer("Some skills required to get into Cyber Security are as follows:\n\n\n \
\U00002666 Computer Networking Skills\n \
One of the most important skills to become an ethical hacker is networking skills. Understanding networks \
like DHCP, Subnetting, Network Protocols, and more will provide ethical hackers to explore the various interconnected \
computers in a network and the potential security threats that this might create, as well as how to handle \
those threats.\n\n\
\U00002666 Computer Skills\n\
Computer skills are knowledge and ability which allow one to use computers and related technology. \
Typically, basic computer skills include data processing, managing computer files, and creating presentations. \
Advanced computer skills include managing databases, programming, and running calculations in spreadsheets.\n\n\
\U00002666 Linux Skills\n\
The main reason to learn Linux for an ethical hacker is, in terms of security, Linux is more secure than any \
other operating system and there are many Linux distributions designed for cyber security that have a lot of \
pre-installed hacking tools\n\n\
\U00002666 Programming Skills\n\
Another most important skill to become an ethical hacker is Programming Skills. Depending on the type of \
security we are focusing on, an ethical hacker has to learn a lot of programming languages. It is not necessary \
to master all languages but he/she must at least understand the basic syntax and code.\n\n\
\U00002666 Basic Hardware Knowledge\n\
Suppose one wants to hack a machine that is controlled by a computer. First, he needs to know about the machine \
or how it works.  If one doesn't know about hardware, then how will he/she know how the motherboard works, \
how USBs to transfer data, or how CMOS or BIOS work together, etc.? So one must have basic hardware knowledge \
also to become an ethical hacker.\n\n\
\U00002666 Reverse Engineering\n\
Reverse Engineering is a process of recovering the design, requirement specifications, and functions of a product \
from an analysis of its code. In software security, reverse engineering is widely used to ensure that the system \
lacks any major security flaws or vulnerabilities. It helps to make a system robust, thereby protecting it from \
hackers and spyware.\n\
Reverse Engineering Courses:\n\
https://www.udemy.com/topic/reverse-engineering/\n\n\
\U00002666 Cryptography Skills\n\
Cryptography is the study and application of techniques for reliable communication in the presence of third parties \
called adversaries. Cryptography deals with converting a normal text/message known as plain text to a non-readable \
form known as ciphertext during the transmission to make it incomprehensible to hackers.\n\
Cryptography Courses:\n\
https://www.youtube.com/results?search_query=cryptography+course\n\n\
\U00002666 Database Skills\n\
DBMS is the crux of creating and managing all databases. Accessing a database where all the information is stored \
can put the company in a tremendous threat, so ensuring that this software is hack-proof is important.\n\n\
\U00002666 Problem-solving Skills\n\
Apart from the technical skills pointed above, an ethical hacker also must be a critical thinker and dynamic \
problem solver. They must be wanting to learn new ways and ensure all security breaches are thoroughly checked.")
        elif blockchain_on:
            await message.answer("Some skills required to get into Blockchain are as follows:\n\n\n \
\U00002666 Blockchain architecture. \n \
Blockchain developers should fully understand how blockchain works and the architecture on which it's based. They \
should be well versed in concepts such as cryptography, consensus, hash functions, distributed ledgers, smart \
contracts and any other concepts integral to understanding blockchain's inner workings. Developers should also be \
familiar with the four types of blockchain architecture: consortium, private, public and hybrid.\n\
Enterprise Blockchain Architect Course:https://www.udemy.com/course/enterprise-blockchain-architect-course/\n\n\
\U00002666 Cryptography. \n \
Effective cryptography is essential to providing a secure blockchain environment, and developers should have a strong \
foundation in cryptographic concepts and practices, including wallets, keys and digital signatures. \n\
Cryptography Course: https://www.udemy.com/course/cryptography/\n\n\
\U00002666 Data structures. \n\
The entire blockchain network consists of data structures. Each block can be considered a type of data structure that \
clusters transactions for the public ledger. Blockchain developers must routinely work with data structures and should \
understand how the blockchain network uses them. \n\
Data Structures Course: https://www.coursera.org/learn/data-structures\n\n\
\U00002666 Smart contracts. \n\
Smart contracts are self-executing contracts that enable two parties to exchange goods and services without an \
intermediary. Smart contracts have become a staple of blockchain implementations, and developers should have a \
thorough understanding of what they are and how they enforce business logic. \n\
Smart Contracts Course: https://www.coursera.org/learn/smarter-contracts\n\n\
\U00002666 Web development. \n\
Blockchain and web development go hand in hand, especially with blockchain's emphasis on decentralized applications. \
Blockchain developers should be experienced in all aspects of web development.\n\n\
\U00002666 Programming languages. \n\
Blockchain technologies often use different programming languages, depending on the platforms used to implement the \
blockchain environments. Although developers can't be experts in every language, they still need to be proficient in \
any number of them. Some of the more common languages used for blockchain include Java, C++, Python and JavaScript. \n")
        elif networking_on:
            await message.answer("In order to build a career in networking, one needs to develop skill and knowledge \
pertaining to the following topics: \n\n\n \
\U00002666 Internet\n\
Internet is a worldwide virtual networking medium that connects computers all across the world. Net is short for the \
internet and has millions of smaller networks that carry a huge array of information.\n\n\
\U00002666 Linux\n\
Linux is a Unix-like operating system. Just like Windows, Mac OS, and IOS, Linux is an operating system used by \
millions across the globe. Android itself is powered by the Linux operating system. \n\
Linux Course: https://www.udemy.com/course/linux-administration-bootcamp/\n\n\
\U00002666 Ethernet\n\
Ethernet refers to a system that connects a series of computers in a local area network (LAN). This is often done \
through ethernet cables, which plug into a router or other port in the modem in addition to the computer port.\n\n\
\U00002666 Network Security\n\
Here's how network security is used on computer network engineer resumes:\n\
Create and enforce network security policy.\n\
Analyzed data network documentation and assisted in communicating to management regarding the current operational \
status of networks.\n\
Appointed to Boundary Protection Technician, providing network security and monitoring firewall; opened firewall ports \
on case-by-case basis.\n\
Network Security Courses: https://www.coursera.org/courses?query=network%20security\n\n\
\U00002666 Assurance\n\
Here's how assurance is used on computer network engineer resumes:\n\
Performed information assurance vulnerability assessments on more than 12 ships.\n\
Implemented Information Assurance controls to ensure all resident information systems were safe and secure.\n\n\
\U00002666 Hardware\n\
Hardware is the physical part attached to a computer or other similar devices. Components are the internal parts of \
hardware which include RAM, hard drives, motherboard, and so on. External hardware devices which include, keyboard, \
mouse, printer, and so on are known as peripherals. All of these together are called computer hardware.\n\
Computer Hardware Course: https://www.coursera.org/learn/computer-hardware-software\n\n")
        elif graphic_designing_on:
            await message.answer("Some skills required to get into GRaphics Design are as follows:\n\n\n \
\U00002666 3D Design\n\
3D design is the process of using software to create a mathematical representation of a 3-dimensional object or shape. \
The created object is called a 3D model and these 3-dimensional models are used for computer-generated (CG) design. 3D \
design is used in a variety of industries to help artists shape, communicate, document, analyse and share their \
ideas.\n\
3D Design Courses: https://www.skillshare.com/browse/3d-design\n\n\
\U00002666 Digital Illustration (Adobe Illustrator)\n\
Illustrator is widely used by graphic designers, web designers, visual artists, and professional illustrators \
throughout the world to create high quality artwork. Illustrator includes many sophisticated drawing tools that \
can reduce the time need to create illustrations.\n\
Illustration Courses: https://www.skillshare.com/browse/illustration\n\n\
\U00002666 Adobe Photoshop \n\
Learning Photoshop for graphic design is an essential skill for anyone working or wanting to work in graphic design. \
Photoshop is the standard digital tool used a wide variety of graphic design roles, including print, web and \
interactive design, as well as video. Those looking to start a career in graphic design will need to learn Photoshop, \
but this is simply one step in the process of becoming a graphic designer. Learning Photoshop alone is not enough to \
become a graphic designer.\n\
Photoshop Course: https://www.skillshare.com/classes/Adobe-Photoshop-CC-%E2%80%93-Essentials-Training-Course/181044379\
3\n\n\
\U00002666 Logo Design \n\
Designers know the importance of a great first impression, which is why graphic designer logos are some of the most \
creative and compelling logos out there. At a glance, the right logo builds trust in your design skills and sets you \
apart from the competition. \n\
Logo Design Course: https://www.udemy.com/course/logodesign/\n\n\
\U00002666 Typography \n\
Graphic designers use typography to adjust the text within the design. This helps in creating content with a purpose. \
The planned use of typefaces allows the designers to make a design look aesthetic and pleasing. The designers have \
been using typefaces strategically to make a text readable and also to make an impression on viewers. Because of such \
designs with unique typography ideas, a brand can communicate with its audience in an effective way.\n\
Typography course: https://www.udemy.com/course/typographic-logos-typography-and-lettering-for-logo-design/\n\n\
\U00002666 Vector Graphics\n\
Vector graphics are computer images created using a sequence of commands or mathematical statements that place lines \
and shapes in a two-dimensional or three-dimensional space. In vector graphics, a graphic artist's work, or file, is \
created and saved as a sequence of vector statements. A vector graphic file describes a series of points to be \
connected. \n\
Vector Graphics Course: https://www.udemy.com/topic/vector-graphic/\n\n")
        elif cloud_computing_on:
            await message.answer("Some skills required to get into Cloud Computing are as follows:\n\n\n \
\U00002666 Understanding the Linux OS\n \
The first and foremost thing is to get good hands-on on a Linux operating system. Practicing Linux would help you \
as a cloud engineer, or as a cloud architect, you should have this fundamental understanding of your operating \
system.\n\n\
\U00002666 Programming Skills\n\
Having good programming skills is an essence while learning cloud. There are a few languages you need to be \
proficient with:\n\
* ASP.NET: Provide dynamic web pages and cutting-edge solutions across various browsers\n\
* SQL: Used to store, manipulate and process large data\n\
* Python: Used for developing serverless applications, especially in AWS.\n\
* Golang: Used for concurrency and parallelism management, especially when working with GCP\n\
* PHP: Used to automate websites or websites with multiple functions\n\
Having a good command of these languages will definitely help to master cloud computing in the desired way.\n\n\
\U00002666  Networking and Internet Protocols\n\
Working knowledge about how the internet works and networking is extremely crucial to cloud roles since it is \
based on provisioning centralized computing resources over the cloud. Engineers are required to work on network \
management like improving responsive networks as demanded by the user by automating procedure adjustments. \
Therefore, it is important to learn virtual networks and network fundamentals for cloud-centric roles.\n\n\
\U00002666 DevOps and Containerization\n\
DevOps is a combination of development and operations and is one of the most popular frameworks in the cloud. \
Recently, AWS DevOps has been highly in demand for people especially interested in AWS. Containerization means \
abstracting applications from one another in the cloud and it makes the applications very easy to deploy on the \
cloud. Therefore learning Docker or Kubernetes will give a good push towards being a good cloud engineer.\n\
Docker Tutorials:\n\
https://www.youtube.com/results?search_query=docker+tutorial\n\
Kubernetes Tutorials:\n\
https://www.youtube.com/results?search_query=kubernetes+tutorial\n\n\
\U00002666 Understanding Virtualization\n\
This means not depending upon personal individual hardware that faces problems when scaling but rather running \
application software on virtual machines. This reduces the hardware dependency and also aids in fault tolerance, \
making it one of the most desirable skills of a cloud engineer. Examples include AWS EC2 (Elastic Compute) and \
AWS Lambda.\n\
AWS Lambda Courses:\n\
https://www.udemy.com/topic/aws-lambda/\n\n\
\U00002666 Cloud Service Providers\n\
There are many cloud service vendors that offer storage, database, compute machine learning, and migration services \
but AWS is the leader being closely followed by Microsoft’s Azure. Knowing how different cloud providers work and \
ship resources to their clients will help you understand cloud computing in detail.\n\n\
\U00002666 Security and Recovery\n\
Cloud security is one of the most difficult subdomains in the cloud since it involves critical measures to be taken \
when there is a data breach or disaster recovery. It demands advanced skills in cyber security and cloud combined \
since any time the cloud resources are down, it can result in huge losses and unavailability of services to the \
client thereby affecting their business in turn.\n\n\
\U00002666 Web Services and API\n\
Cloud infrastructure is heavily based upon APIs and web services for the integration of applications on the \
internet. Some examples are XML, SOAP, WSDL, and other open standards are used to transfer and describe data \
and list services available. Gaining an understanding of these fundamentals can help you in your journey in \
the cloud.\n\
WebServices/API Testing by SoapUI-Groovy:\n\
https://www.udemy.com/course/soapui-with-groovy-with-realtime-projects/")
        elif data_science_on:
            await message.answer("Following are the skills that are required to pursue a career in Data Science:\n\
1.Data science requires you to have or develop skills in statistics.\n\
Introduction to Statistic :\n\
https://www.udemy.com/course/intro-to-statistics/\n\
Statistics for Data science and Business Analysis : \n\
https://www.udemy.com/course/statistics-for-data-science-and-business-analysis/\n\
Your collegtive destination for everything you need to know about Statistics in Data science :\n\
https://www.coursera.org/courses?query=statistics%20for%20data%20science\n\
Following are the skills that are required to pursue a career in Data Science:\n\n\
\U00002666Data science requires you to have or develop skills in statistics.\n\
One of the building blocks is statistics.Some even call machine learning glorified statistics.\
I do not completely agree with this argument but machine learning and statistics are closely related.\
The goal of data science is creating value out of data.\
The initial requirement for accomplishing this goal is to understand the data very well.\n\
Statistics can be considered as the most impactful tool to understand, interpret, evaluate the data.\
\n\n\
\U00002666 A person has to have or attain knowledge of Data science tools.\
The tools for data science are for analyzing data, creating aesthetic and interactive \
visualizations and creating powerful predictive models using machine learning algorithms.\n \
Most of the data science tools deliver complex data science operations in one place.\
Some of the Data science tools of 2021 are:\n\
SAS\n 2. Apache Hadoop\n 3. Excel\n 4. MongoDB\n 5. Python\n \
You'll find all the information you need to learn the Data science tools by clicking the Courses button down below.\
3.One needs to know how to best communicate with others whether it's at \
SAS\n 2. Apache Hadoop\n 3. Excel\n 4. MongoDB\n 5. Python\n \n\
\U00002666 One needs to know how to best communicate with others whether it's at\
work or with clients or even with the computer.\n\
Communication becomes a very crucial part of a person's life especially if he \
belongs to the industrial sector such as Computer Science or IT.\n\
You need to know how and when to communicate with people and maintain a clean reputation just the same.\
Here are some courses that will help you with your Communication skills better :\n\
Become more clear Concise and confident:\n\
https://www.skillshare.com/classes/Communication-Skills-Become-More-Clear-Concise-Confident/\n\
Powerful Speaking:\n\
https://www.udemy.com/course/powerful-speaking/\n\
\n4.Commendable knowledge in Quants and Business Acumen.\n\
You need to know how and when to communicate with people and maintain a clean reputation just the same.\n\n\
\U00002666 Commendable knowledge in Quants and Business Acumen.\n\
Good Business Acumen include the following things and qualities: \n\
*Leadership Skills\n\
*Financial acumen\n\
*Strategic thinking\n\
*Market orientation\n\
*Analytical skills\n\
*Problem-solving skills\n\
Some courses about business:\n\
Learn Business Acumen with Udemy:\n\
https://www.udemy.com/course/learn-business-acumen/\n\
Develop Business Acumen with LinkedIn:\n\
https://www.linkedin.com/learning/developing-business-acumen\n\
Business Acumen Training:\n\
https://www.acumenlearning.com/online-corporate\n\
\n5.Apart from all these skills one need to have a profound knowledge of Graphs and Statistical Graphs, Pie Charts.\
\n\
Mos of the times in Data Analysis graphs are use and till date they are considered to be the \
\n\U00002666Apart from all these skills one need to have a profound knowledge of Graphs and Statistical Graphs, \
Pie Charts.\n\n\
Most of the times in Data Analysis graphs are use and till date they are considered to be the \
best method of representing any sort of data in a pictorial form.\n\
Why use of graph is made is because it is easier to understand and it saves a lot of time that would be\
consumes if one opted to read the report of each and every financial year\
( in instance of a Company's share prices )   ")
        elif robotics_and_hardware_on:
            await message.answer("Some skills you need to learn before going into Robotics:\n\n\
\U00002666Math and Science:\n\
Robotics manufacturer RobotIQ describes mathematics as one of \
the only core robotics skills that you cannot learn as you go along.\n\
At a minimum, a strong background in several fields of\
mathematics and science are critical for a successful career in robotics:\n\n\
\U00002666Programming:\n\
While a career in robotics requires knowledge of popular \
programming languages such as C, C++, Python, and Java, there are \
some key differences between programming for robotics and \
programming to develop software or mobile applications.\n\
*Software applications tend to interact with other software \
applications, such as a website requesting information from a \
database. Robots, on the other hand, interact with software, \
hardware, and various electronics.\n\n\
\U00002666Working on a Team:\n\
Robotics is largely technical work, but certain \
soft skills are beneficial, Platt says. In particular, being a team player is essential. \
“You want to be someone with valuable skills,” \
such as the ability to write complex AI algorithms, \
“but you need to be someone who can also work on a team.\n \
Unless you work at a small startup, Platt adds, \
you can expect to be working with five or six other engineers, \
a project manager, product developers, and a user experience expert. \
You can also expect the team to follow an Agile project \
management style, with an iterative process for developing, \
testing, and getting feedback on a product.\n\
\U00002666Solving Complex Problems: \n\n\
Designing and building functioning technical \
systems is obviously a critical robotics skill, \
but it’s just as important to be able to figure out why \
a system isn’t functioning properly. If it’s a mechanical issue, \
you’ll need to know the best practices for making a repair. \n\n\
\U00002666Thinking Creatively :\n\
A little bit of creativity can go a \
long way for a robotics professional. \
It can be beneficial for solving problems, such as using an \
existing part in a new way or coming up with a brand-new design altogether. \
Creativity and teamwork go hand in hand, too—a willingness to work with others\
and accept their contributions can help the entire team \
come up with a new idea or different solution.\n\n\
\U00002666Active Learning:\n\
The field of robotics is always changing. \
There are new programming languages to learn, new AI concepts to test,\
and new and more durable materials to work with. \
A robotics engineer can demonstrate their value by \
constantly learning about these changes and applying them \
to new fields of robotics.\n\n\n\n\
Other things that you need to know before you pursue your career in robotics and hardware are:\
* Basic idea of how a basic breadboard functions and its fundamentals\n\
*For starting off with robotics Arduino is a very intelligent way to do so\n")
        elif game_development_on:
            await message.answer("Before you make up your mind to \
start you career in Game Developing you need to be firm in you mind that you \
want to take this as your career. Because this particular field \
demands one to have absolute enthusiasm and passion for Video games.\
Along with these things the Gaming Industry also demands a  a good \
knowledge of programming languages from basic to advanced \
and mastery of gaming specific programming languages.\n\n\
Here are some basic to advance requirements to become a game developer:\n\n\
\U00002666 A bachelors degree in Software Engineering or Computer \
sciences is to be attained by the individual after the completion of his college.\n\n\
\U00002666 Coding languages like C,C++,Java and C# for Unity (basics) ;     \
UnrealScript, Lua, JavaScript, SQL, Python, Rust, etc.\
From which C++ & C# being the most essential of them all \
as they are considered the foundation of any gaming developer and so \
any video game out there. Whereas Unreal engine and Unity being \
only gaming specific languages; more like platforms for \
designing of the game.\n\n\
\U00002666 The Designing of the game is something only creative \
people will be able to do and make it in a way \
that the target audience would want to buy it. \
Creativity deals with the design of each and every object, \
entity, human, etc in the game. \
But the part that is linked to creativity the post is the idea of the \
game and how the maker pictures it in the beginning of the \
developmental stages\n\n\
\U00002666 A passion for video games.\n\n\
\U00002666 Wide-ranging knowledge of gaming trends.\n\n\
\U00002666 Strong analytical frame of mind.\n\n\
Things you need to study to be a game developer:   \n\
*Bachelor of Science (B.Sc) in Graphics, Animation & Gaming.\n\
*Bachelor of Arts (BA) in Digital Filmmaking & Animation.\n\
*Bachelor of Technology (B. Tech) – Computer Science and Game Development.\n\
*Bachelor of Science in Animation Game Design and Development.\n\n")
        elif front_end_development_on:
            await message.answer("Some skills required to get into Front End Development are as follows:\n\n\n \
\U00002666 HTML \n\
Early Front End devs using HTML were limited by the language’s inability to handle design or style. HTML defines the \
structure of a website and basic elements of how a site should look. HTML can be used to make characters appear bold \
or italicized and which block of text should be a paragraph.\n\
HTML Tutorial: https://www.w3schools.com/html/\n\n\
\U00002666 CSS \n\
That’s nice if you want a text-based site, but what if you want to change the background color? That’s where CSS \
enters the picture. CSS is a language that determines how a page should look. Using CSS, Front End devs can code \
all the stylistic changes in one place without repeating that command every time you want a little style on your \
site. For example, it takes only a few lines of CSS to turn all our headlines blue.\n\
CSSS Tutorial: https://www.w3schools.com/css/\n\n\
\U00002666 JavaScript\n\
JavaScript is the final layer of cake and turns a static website into a dynamic experience. If you’ve had the pleasure \
of surfing the web in the mid-1990s — think AOL CDs and dial-up connections — you know all too well the frustration \
that comes with waiting for a page to load. If you wanted to do anything on a site, you’d have to wait for it to \
refresh. Luckily, we don’t have to wait anymore. Thank JavaScript for that.\n\
Js Tutorial: https://www.w3schools.com/js/\n\n\
\U00002666 JQuery and AJAX\n\
Now, Front End devs can manipulate web elements without having to wait for a site to load (Imagine waiting for Twitter \
to refresh every time you updated your feed.) Developers also use Front End frameworks to enhance or simplify \
JavaScript tasks. The AngularJS framework, for example, lets developers build single-page web apps efficiently. jQuery \
simplifies tasks and AJAX adds XML, a markup language, to JavaScript to enable sites to update without refreshing.\n\
JQuery Tutorial: https://www.w3schools.com/jquery/\n\
AJAX Tutorial: https://www.w3schools.com/js/js_ajax_intro.asp \n\n\
\U00002666 Bootstrap\n\
Bootstrap is a free and open-source CSS framework directed at responsive, mobile-first front-end web development. \
It contains CSS- and JavaScript-based design templates for typography, forms, buttons, navigation, and other interface \
components.\n\
Bootstrap Tutorial: https://www.w3schools.com/bootstrap/bootstrap_ver.asp\n\n")
        elif back_end_development_on:
            await message.answer("Some skills required to get into Front End Development are as follows:\n\n\n \
A Back End dev uses a set of Back End developer languages to bring the Front End language of a developer to life. \
While a Front End dev creates the user experience within a browser, the Back End dev is creating the logic that makes \
those requests a reality. In some ways, a Back End dev is creating the brains and logic of the website.\n\n\
\U00002666 PHP\n\
PHP is another server-side scripting language that can also be used to develop websites. It’s open source and free, \
which means it’s a versatile tool to create dynamic websites. A Front End needs a Back End otherwise it would be lines \
of inactive code. Front End languages communicate requests to Back End languages.  Every website has a server, \
database, and other applications that interact with the Front End through code created by a Back End dev.\n\
PHP Tutorial: https://www.w3schools.com/php/\n\n\
\U00002666 Python\n\
Python is another general purpose, object-oriented programming language. Python is used to code server-side logic and \
many popular websites, including Reddit and Instagram, are built upon Python. The language is easily scalable with \
frameworks like Django. Python has become increasingly popular due to its applications in machine learning and data \
science.\n\
Python Tutorial: https://www.w3schools.com/python/\n\n\
\U00002666 Ruby\n\
Ruby is a general-purpose, object-oriented programming language. That means it’s used widely and treats everything as \
an object. The philosophy behind Ruby, which emphasizes the human and favors expressiveness, has made it incredibly \
popular among developers and startups. Ruby on Rails is an incredibly popular framework used to help develop websites \
and applications by streamlining the development process.\n\
Ruby Tutorial: https://www.tutorialspoint.com/ruby/\n\n\
\U00002666 SQL\n\
SQL, or Structured Query Language, is used to manage data found on a database. MySQL is an open source data management \
system that’s widely used in Back End development. There are other Back End languages, such as Java or ASP.NET, that \
are used in different industries.\n\
SQL Tutorial: https://www.w3schools.com/sql/\n\n")
        elif android_development_on:
            await message.answer("Some skills required to get into Android Development are as follows:\n\n\n \
\U00002666 An Unprecedented Knowledge of Java and Kotlin\n \
One of the most must-have skills of all, proficiency in Java and Kotlin can be a game-changer for Android developers. \
Used to develop native Android apps, both Java and Kotlin are programming languages that Android developers should \
be comfortable working with.\n\
Java Course:\n\
https://www.w3schools.com/java/default.asp\n\
Kotlin Course:\n\
https://www.w3schools.com/kotlin/index.php\n\n\
\U00002666 Understanding of XML\n\
XML was created as a standard way to encode data for internet-based mobile applications. It is a structured \
markup language, sharing many features in common with HTML. In the Android world, developers use XML to create layouts \
that serve as the foundational UI definition for Android applications.\n\
XML Course:\n\
https://www.w3schools.com/xml/default.asp\n\n\
\U00002666 Vital Sense of the UX/UI\n\
Today, the majority of app users demand a highly engaging and responsive application that is easy to use. Hence, \
the demand for an intuitive UX and UI rises even more. o develop an Android app that stands out, one needs to have \
a good knowledge of the design requirements of Android apps and what type of designs users prefer.\n\
UI/UX Courses:\n\
1. https://www.udemy.com/course/ui-ux-web-design-using-adobe-xd/\n\n\
2. https://www.udemy.com/course/complete-web-designer-mobile-designer-zero-to-mastery/\n\n\
\U00002666 Required Skill in Cross-Platform Solutions\n\
Nowadays, cross-platform solutions are the need of the hour. Various frameworks like React Native and Flutter \
have come into play to let Android developers build applications that can operate on the iOS platform too. The \
tech giant Google has introduced Kotlin Multi-Platform, an extension of Kotlin language to enable mobile application \
development beyond the Android platform. This is a move that has been welcomed by Android users around the world, \
and any potential developer certainly needs to be mindful of it.\n\
React Native Course:\n\
https://www.udemy.com/course/the-complete-react-native-and-redux-course/\n\
Flutter Course:\n\
https://www.udemy.com/course/learn-flutter-dart-to-build-ios-android-apps/\n\n\
\U00002666 Android Studio\n\
The integrated development environment (IDE) of choice for Android developers is called Android Studio. Android \
Studio is built on top of the well-respected IntelliJ IDE, and it comes with great out-of-the-box support for many \
of the most common Android SDKs. Code completion helps make auto-complete suggestions as you type. Code debuggers \
let you step through your code to identify the source of errors.\n\n\
\U00002666 APIs\n\
As an Android app developer, you’ll likely want to interact with many other services. For example, you may want to \
allow your users to access a calendar from a third party service, or check the stock market. An Android app \
development company usually offers APIs, and will tell you exactly how to query them for data in a consistent, \
secure way. While you’re free to interact with any existing API, Google also makes it very easy to connect to \
their own APIs from your Android app.\n\
Java App Using REST API Course:\n\
https://www.youtube.com/watch?v=xPi-z3nOcn8\n\n\
\U00002666 Firebase on Android\n\
If you hate being a backend developer, Firebase on Android is the way for you. Firebase is a mobile platform that \
helps you quickly develop high-quality apps, grow your user base and earn more money. Firebase provides several \
utility features to make the life of an Android developer easy.\n\
Flutter and Firebase:\n\
https://www.udemy.com/course/flutter-firebase-build-a-complete-app-for-ios-android/\n\n\
\U00002666 Android security\n\
Android has built-in security features that significantly reduce the frequency and impact of application security \
issues. You can protect the user's privacy by using permissions. Share data securely by using signature-based \
permissions. Handle data security by using internal storage, external storage and ContentProviders very cautiously. \
By default, never export your Android component, such as ContentProvider, Service or BroadcastReceiver, unless \
you need to.")
        elif ios_development_on:
            await message.answer("Some skills required to get into IOS Development are as follows:\n\n\n \
\U00002666 The Swift 3.0 programming language\n \
Developed by Apple, Swift 3.0 is the global and most favored language that is used in iOS mobile app development. \
You should be proficient in Swift 3.0 like a cricketer is proficient is skilled in catching a ball.\n\n\
\U00002666 Objective-C programming language\n\
Objective-C is the primary programming language you use when writing software for OS X and iOS. It’s a superset of \
the C programming language and provides object-oriented capabilities and a dynamic runtime. Objective-C inherits \
the syntax, primitive types, and flow control statements of C and adds syntax for defining classes and methods. It \
also adds language-level support for object graph management and object literals while providing dynamic typing and \
binding, deferring many responsibilities until runtime.\n\n\
\U00002666 Apple’s Xcode IDE\n\
It is the primary object that you must add in your skill set. Xcode IDE is an excellent cause that delivers a \
unique app and offers majestic user experience. It is combined with Cocoa Touch frameworks and Cocoa and is the \
first environment to develop apps for several Apple devices like Apple, iPad, TV, iPhone, Mac, etc. It encourages \
a developer to allow several Apple service like Passbook, Game Changer. To become an iOS developer, you must \
know the Apple Xcode IDE.\n\n\
\U00002666 Design Guidelines\n\
The reason why Apple users are crazy about their devices is their uniqueness that lures them to purchase Apple \
products. To create iOS apps, there are defined guidelines to follow. While your training period in iOS app \
development company, you must discover how to develop such extraordinary apps while adhering to Apple’s design \
guidelines. Once you have inbuilt this art within yourself, you will be ready do wonders.\n\n\
\U00002666 UI and UX design experience\n\
Both UI and UX are the main features on which design of an app depends but functions vary slightly. UI form the \
appearances of the app and UX includes navigation etc. Effective performance of UI/UX design in the building a \
mobile app can perform an extreme change to its entire look which in turn engages more users. Thus, an iOS \
developer should have a fair idea of design concepts and should have the ability to create exciting UI/UX design \
for a mobile app they design and develop.\n\
UI/UX Course:\n\
https://www.udemy.com/course/app-design-uiux-plus-ios-development/\n\n\
\U00002666 Apple Human Interface Guidelines\n\
You must be aware of Apple Guidelines, as it will be the most important skill that help you best the best iOS app \
developer. It will make your learning journey smooth and straight. These guidelines support an app developer to \
develop apps that have maximum impact with superior visuals, and breathtaking user experience.\n\
Apple Guidelines:\n\
https://developer.apple.com/design/human-interface-guidelines/\n\n\
\U00002666 Networking\n\
You must be aware of JSON- JavaScript Object Notation to know how data is sent and accepted over networks. It is \
a conventional format for data exchange and to become an iOS developer, and you must have this skill set too.\n\
JSON course:\n\
https://www.w3schools.com/js/js_json_intro.asp\n\n\
\U00002666 Core Data\n\
Core Data is the most supportive thing that you can use to provide a smooth user experience, as Core Data \
eliminates this obstacle by storing data on Apple’s devices. It will reduce user frustration of starting from \
scratch every single time they use the app.\n\
Core Data Tutorials:\n\
https://www.youtube.com/playlist?list=PLMRqhzcHGw1aDYKmCuqXQ_IqpWpJlpoJ3\n\n\
\U00002666 Grand Central Dispatch\n\
Usually, an app does many tasks concurrently such as receiving data from the internet, following human inputs, \
presenting data and many more. Grand Central Dispatch plays a significant role in Apple devices to perform all \
these functions. It gives the user a smooth experience.\n\
Dispatch Documentation Apple:\n\
https://developer.apple.com/documentation/DISPATCH")

    elif message.text == "\U0001F4BB Courses":
        if ai_and_ml_on:
            await message.answer("List of some courses and programs for AI and ML:\n\n\n \
\U00002666 Artificial Intelligence Full Course | Artificial Intelligence Tutorial for Beginners | Edureka\n \
https://www.youtube.com/watch?v=JMUxmLyrhSk\n\n \
\U00002666 AI And Machine Learning Full Course | Artificial Intelligence & Machine Learning Course |Simplilearn\n \
https://www.youtube.com/watch?v=wnqkfpCpK1g\n\n \
\U00002666 Artificial Intelligence Course | Learn Machine Learning and Artificial Intelligence | Intellipaat\n \
https://www.youtube.com/watch?v=GhTREKMYp34\n\n \
\U00002666 Machine Learning Full Course in Hindi | Learn Machine Learning in 5 Hours | Great Learning\n \
https://www.youtube.com/watch?v=IoZGSQ07e8g\n\n \
\U00002666 Artificial Intelligence A-Z™: Learn How To Build An AI\n \
https://www.udemy.com/course/artificial-intelligence-az/\n\n \
\U00002666 Artificial Intelligence: Reinforcement Learning in Python\n \
https://www.udemy.com/course/artificial-intelligence-reinforcement-learning-in-python/\n\n \
\U00002666 Advanced AI: Deep Reinforcement Learning in Python\n \
https://www.udemy.com/course/deep-reinforcement-learning-in-python/\n\n \
\U00002666 Machine Learning A-Z™: Hands-On Python & R In Data Science\n \
https://www.udemy.com/course/machinelearning/\n\n \
\U00002666 List of AI and ML programs (EdX)\n \
https://www.edx.org/search?q=artificial%20intelligence&tab=program\n\n \
\U00002666 List of AI programs (Coursera)\n \
https://www.coursera.org/search?query=artificial%20intelligence\n\n \
\U00002666 List of ML programs (Coursera)\n \
https://www.coursera.org/search?query=machine%20learning\n\n \
\U00002666 Deep Learning Specialization\n \
https://www.coursera.org/specializations/deep-learning \n\n\
\U00002666 List of AI and ML programs (Udacity)\n \
https://www.udacity.com/courses/all?search=artificial%20intelligence")
        elif cyber_security_on:
            await message.answer("List of some courses for Cyber Security:\n\n\n \
\U00002666 Courses by Zaid Sabih\n \
https://www.udemy.com/user/zaidsabih/\n\n \
\U00002666 The Complete Cyber Security Course Bundle by Nathan House\n \
https://www.udemy.com/user/nathan-house/\n\n \
\U00002666 The Complete Ethical Hacking Course: Beginner to Advanced!\n \
https://www.udemy.com/course/penetration-testing/\n\n \
\U00002666 Learn Ethical Hacking: Beginner to Advanced!\n \
https://www.udemy.com/course/ethical-hacking-kali-linux/\n\n \
\U00002666 Cyber Security Training for Beginners | Edureka\n \
https://www.youtube.com/playlist?list=PL9ooVrP1hQOGPQVeapGsJCktzIO4DtI4_\n\n \
\U00002666 Full Ethical Hacking Course - Network Penetration Testing for Beginners\n \
https://www.youtube.com/watch?v=3Kq1MIfTWCE&t=1s\n\n \
\U00002666 Ethical Hacking & Penetration Testing - Complete Course\n \
https://www.youtube.com/playlist?list=PLBf0hzazHTGOEuhPQSnq-Ej8jRyXxfYvl\n\n \
\U00002666 MList of cyber security programs (edx)\n \
https://www.edx.org/search?q=cybersecurity&tab=program\n\n \
\U00002666 List of cyber security programs (coursera)\n \
https://www.coursera.org/search?query=cybersecurity\n\n \
\U00002666 List of cyber security programs (udacity)\n \
https://www.udacity.com/school-of-cybersecurity")
        elif blockchain_on:
            await message.answer("List of some courses and programs for Blockchain:\n\n\n \
\U00002666 Blockchain and Bitcoin Fundamentals\n\
https://www.udemy.com/course/blockchain-and-bitcoin-fundamentals/\n\n\
\U00002666 Bitcoin and Cryptocurrency Bootcamp\n\
https://www.udemy.com/course/bitcoin-and-cryptocurrency-bootcamp/\n\n\
\U00002666 Blockchain Specialization - University of California, Irvine(certified course)\n\
https://www.coursera.org/specializations/uci-blockchain\n\n\
\U00002666 Blockchain Tutorial For Beginners\n\
https://www.youtube.com/playlist?list=PLsyeobzWxl7oY6tZmnZ5S7yTDxyu4zDW-\n\n\
\U00002666 ETHEREUM DEVELOPMENT TUTORIALS\n\
https://ethereum.org/en/developers/tutorials/\n\n\
\U00002666 Ethereum Tutorial\n\
https://www.tutorialspoint.com/ethereum/index.htm \n\n")
        elif networking_on:
            await message.answer("List of some courses and programs for Networking:\n\n\n \
\U00002666 Networking Essentials \n\
https://www.netacad.com/courses/networking/networking-essentials\n\n\
\U00002666 CCNA: Introduction to Networks\n\
https://www.netacad.com/courses/networking/ccna-introduction-networks\n\n\
\U00002666 Introduction to networking for complete beginners\n\
https://www.udemy.com/course/introduction-to-networking-for-complete-beginners/\n\n\
\U00002666 The Complete Networking Fundamentals Course. Your CCNA start\n\
https://www.udemy.com/course/complete-networking-fundamentals-course-ccna-start/\n\n\
\U00002666 Computer Networks\n\
https://www.youtube.com/playlist?list=PLBlnK6fEyqRgMCUAG0XRw78UA8qnv6jEx \n\n")
        elif graphic_designing_on:
            await message.answer("List of some courses and programs for Graphics Design:\n\n\n \
\U00002666 Graphic Design Bootcamp: Photoshop, Illustrator, InDesign\n\
https://www.udemy.com/course/graphic-design-for-beginners/\n\n\
\U00002666 Graphic Design Masterclass: Learn Graphic Design in Projects\n\
https://www.udemy.com/course/graphic-design/\n\n\
\U00002666 Graphic Design Masterclass: Learn Graphic Design in Projects\n\
https://www.udemy.com/course/become-a-professional-logo-designer/ \n\n\
\U00002666 Beginners Guide to Graphic Design | 45 Episode FREE Series \n\
https://www.youtube.com/watch?v=WONZVnlam6U&list=PLYfCBK8IplO4E2sXtdKMVpKJZRBEoMvpn \n\n\
\U00002666 Graphics Design Skill Share\n\
https://www.skillshare.com/browse/graphic-design\n\n\
\U00002666 Graphic Design Specialization -  Certified Course by CalArts\n\
https://www.coursera.org/specializations/graphic-design \n\n")
        elif cloud_computing_on:
            await message.answer("List of some courses for Cloud Computing:\n\n\n \
\U00002666 Cloud Computing Full Course In 11 Hours | Cloud Computing Tutorial For Beginners | Edureka\n \
https://www.youtube.com/watch?v=2LaAJq1lB1Q\n\n \
\U00002666 Cloud Computing Full Course | Cloud Computing Tutorial For Beginners | Intellipaat\n \
https://www.youtube.com/watch?v=gIWel4gFZaY\n\n \
\U00002666 Introduction to Cloud Computing on Amazon AWS for Beginners\n \
https://www.udemy.com/course/introduction-to-cloud-computing-on-amazon-aws-for-beginners/\n\n \
\U00002666 AWS VPC and Networking in depth: Learn practically in 8 hrs\n \
https://www.udemy.com/course/networking-in-aws/\n\n \
\U00002666 List of cloud computing programmes (edx)\n \
https://www.edx.org/search?q=cloud%20computing&tab=program\n\n \
\U00002666 List of cloud computing programmes (coursera)\n \
https://www.coursera.org/search?query=cloud%20computing&\n\n \
\U00002666 Cloud computing courses on (udacity)\n \
https://www.udacity.com/school-of-cloud-computing")
        elif game_development_on:
            await message.answer("Here's some courses you can kick off your Game-development career with:\n\
\U00002666RUST Programming Tutorial #1- Hello World | Getting Started with Rust:\n\
https://www.youtube.com/watch?v=vOMJlQ5B-M0&list=PLVvjrrRCBy2JSHf9tGxGKJ-bYAN_uDCUL\n\n\
\U00002666Learn RUST by building real Applications:\n\
https://www.udemy.com/course/rust-fundamentals/\n\n\
\U00002666Unreal Engine 4 courses (Create multiplayer games with C++):\n\
https://www.udemy.com/course/unrealcourse/\n\n\
\U00002666Unreal Engine Blueprint Developer Tutorial  | Learn visual scripting:\n\
https://www.udemy.com/course/unrealblueprint/\n\n\
\U00002666Unreal engine C++ the ultimate Shooter Course:\n\
https://www.udemy.com/course/unreal-engine-the-ultimate-shooter-course/\n\n\
\U00002666Unreal Engine 5 Beginner tutorial- UE5 starter course:\n\
https://www.youtube.com/watch?v=gQmiqmxJMtA\n\n\
\U00002666Learn Unity- Beginner game-development tutorial:\n\
https://www.youtube.com/watch?v=gB1F9G0JXOo\n\n\
\U00002666Unity C# scripting | Complete C# for Unity Game development:\n\
https://www.udemy.com/course/unity-c-sharp-scripting/?src=sac&kw=C%23+for+unity\n\n\
\U00002666Lua Scripting | Master Lua scripting from Scratch:\n\
https://www.udemy.com/course/learn-lua-scripting-roblox/\n\n\
\U00002666Lua Programming and game development With LOVE:\n\
https://www.udemy.com/course/lua-love/\n\n\
\U00002666Here's some bonus courses if youve made it this far:\n\n\
\U00002666Complete Roblox Lua | Start making games with Roblox Studio:\n\
https://www.udemy.com/course/complete-roblox-lua-start-making-games-with-roblox-studio/\n\n\
\U00002666An Introduction to game development in Python:\n\
https://www.udemy.com/course/an-introduction-to-game-development-in-python/\n\n ")
        elif data_science_on:
            await message.answer("Here's some courses you can kick off your Data Science career with:\n\n\
\U00002666The complete SQL Bootcamp of Manipulation and Analysis of Data:\n\
https://www.udemy.com/course/the-complete-sql-bootcamp/\n\n\
\U00002666BI Analysis: MySQL for Data Analytics and Business Intelligence:\n\
https://www.udemy.com/course/sql-mysql-for-data-analytics-and-business-intelligence/\n\n\
\U000026662021 Python for Machine Learning and Data Science Mastercalss:\n\
https://www.udemy.com/course/python-for-machine-learning-data-science-masterclass/\n\n\
\U00002666Python for Data Science: Course for Beginners(Learn Python, Pandas, NumPy, Matplotlib):\n\
https://www.youtube.com/watch?v=LHBE6Q9XlzI\n\n\
\U00002666Learn Apache Spark3 with Scala-Hands on with big Data:\n\
https://www.udemy.com/course/apache-spark-with-scala-hands-on-with-big-data/\n\n\
\U00002666Apache Spark Full Course- Learn Complete Apache in 8 hours:\n\
https://www.youtube.com/watch?v=F8pyaR4uQ2g\n\n\
\U00002666R programming Tutorial - Learn the Basics of Statistical Computing:\n\
https://www.youtube.com/watch?v=_V8eKsto3Ug\n\n\
\U00002666R Programming A-Z: For Data Science(Courses and Exercises):\n\
https://www.udemy.com/course/r-programming/\n")
        elif robotics_and_hardware_on:
            await message.answer("Here's some courses you can kick off your Robotics \
and Hardware career with:\n\
\U00002666Here are some courses on arduino:\n\
\U00002666Basic electronics for Arduino Makers:\n\
https://www.udemy.com/course/basic-electronics/\n\n\
\U00002666Arduino step by step getting serious:\n\
https://www.udemy.com/course/arduino-sbs-getting-serious/\n\n\
\U00002666Arduino step by step: Getting started:\n\
https://www.udemy.com/course/arduino-sbs-17gs/\n\n\
\U00002666Arduino for Beginners with Grove:\n\
https://www.udemy.com/course/arduino-getting-started-with-grove/\n\n\
\n\n\
\U00002666Courses for beginners in Electronics:\n\
\U00002666Electronics Mastery- The beignners course in Electronics:\n\
https://www.udemy.com/course/electronics-mastery-understand-the-fundamentals-fast/\n\n\
\U00002666Complete UiPath RPA Develpoer Course: BUild 7 Robots:\n\
https://www.udemy.com/course/complete-uipath-rpa-developer-course/\n\n\
\n\n\
\U00002666Here's your guide in and around the Breadboard:\n\
\U00002666How to use the Breadboard:\n\
https://www.sciencebuddies.org/science-fair-projects/references/how-to-use-a-breadboard\n\n\
\U00002666How to use a Breadboard:\n\
https://youtu.be/6WReFkfrUIk\n\n")
        elif front_end_development_on:
            await message.answer("Here's some courses you can kick off your front end career:\n\n\n\
\U00002666The Complete Front-End Web Development Course!\n\
https://www.udemy.com/course/front-end-web-development/\n\n\
\U00002666Programming Foundations with JavaScript, HTML and CSS\n\
https://www.coursera.org/learn/duke-programming-web\n\n\
\U00002666The Web Developer Bootcamp 2022\n\
https://www.udemy.com/course/the-web-developer-bootcamp/\n\n\
\U00002666Front-End Web Development Quick Start With HTML5, CSS, and JavaScript\n\
https://www.pluralsight.com/courses/front-end-web-app-html5-javascript-css\n\n\
\U00002666Front-End Web Development with React\n\
https://www.coursera.org/learn/front-end-react\n\n")
        elif back_end_development_on:
            await message.answer("Here's some courses you can kick off your back end career:\n\n\n\
\U00002666Complete Backend Development 2022 Bundle - Python Roadmap\n\
https://www.udemy.com/course/software-developer-masterclass/\n\n\
\U00002666Django 3 - Python Backend Web Development For Beginner\n\
https://www.udemy.com/course/django-python-web-development-for-beginner/\n\n\
\U00002666Intro to Backend\n\
https://www.udacity.com/course/intro-to-backend--ud171\n\n\
\U00002666Building Web Applications in PHP\n\
https://www.coursera.org/learn/web-applications-php\n\n\
\U00002666The Complete Ruby on Rails Developer Course\n\
https://www.coursera.org/courses?query=php\n\n")
        elif android_development_on:
            await message.answer("List of some courses for Android Development:\n\n\n \
\U00002666 Android Development for Beginners - Full Course\n \
https://www.youtube.com/watch?v=fis26HvvDII\n\n \
\U00002666 Android Application Development Course\n \
https://www.youtube.com/playlist?list=PLknSwrodgQ72X4sKpzf5vT8kY80HKcUSe\n\n \
\U00002666 The Complete Android 12 & Kotlin Development Masterclass\n \
https://www.udemy.com/course/android-kotlin-developer/\n\n \
\U00002666 Android Java Masterclass - Become an App Developer\n \
https://www.udemy.com/course/master-android-7-nougat-java-app-development-step-by-step/\n\n \
\U00002666 List of android app development courses (Coursera)\n \
https://www.coursera.org/courses?query=android%20app%20development\n\n \
\U00002666 Android Basics in Kotlin\n \
https://developer.android.com/courses/android-basics-kotlin/course\n\n \
\U00002666 Build Your First Android App in Java\n \
https://developer.android.com/codelabs/build-your-first-android-app#0")
        elif ios_development_on:
            await message.answer("List of some courses for IOS Development:\n\n\n \
\U00002666 IOS Tutorial: How To Make Your First App\n\
https://www.youtube.com/watch?v=09TeUXjzpKs\n\n \
\U00002666 Get Started with IOS Development\n \
https://www.youtube.com/playlist?list=PLSzsOkUDsvdu5Mm67aBYs2YPu2OM4mFzt\n\n \
\U00002666 Learn IOS Development -  How to Build Apps\n \
https://www.youtube.com/playlist?list=PLpZBns8dFbgx0gr68lf-un9EjdmywTu4_\n\n \
\U00002666 IOS & Swift - The Complete iOS App Development Bootcamp\n \
https://www.udemy.com/course/ios-13-app-development-bootcamp/\n\n \
\U00002666 SwiftUI Masterclass 2022 - iOS 15 App Development & Swift 5\n \
https://www.udemy.com/course/swiftui-masterclass-course-ios-development-with-swift/\n\n \
\U00002666 List of IOS app development courses (Coursera)\n \
https://www.coursera.org/search?query=ios%20app%20development\n\n \
\U00002666 Mobile App Development with Swift\n \
https://www.edx.org/professional-certificate/curtinx-mobile-app-development-with-swift\n\n \
\U00002666 Become an iOS Developer\n \
https://www.udacity.com/course/ios-developer-nanodegree--nd003\n\n\
\U00002666 iOS Developer University Program\n\
https://developer.apple.com/programs/ios/university/")

    elif message.text == "\U0001F4D6 Books":
        if ai_and_ml_on:
            await message.answer("Some books to refer for AI and ML:\n\n\n \
\U00002666 Introduction to Machine Learning with Python\n \
https://www.amazon.in/Introduction-Machine-Learning-Python-Scientists/dp/9352134575/ref=sr_1_3\n\n \
\U00002666 Hands-On Machine Learning with Scikit-Learn, Keras and Tensor Flow\n \
https://www.amazon.in/Hands-Machine-Learning-Scikit-Learn-Tensor/dp/9352139054/ref=sr_1_1\n\n \
\U00002666 Deep Learning with Python\n \
https://www.amazon.in/Deep-Learning-Python-Francois-Chollet/dp/1617294438/ref=sr_1_3\n\n \
\U00002666 Artificial Intelligence | Third Edition | By Pearson: A Modern Approach\n \
https://www.amazon.in/Artificial-Intelligence-3e-Modern-Approach/dp/9332543518/ref=sr_1_2\n\n \
\U00002666 The Emotion Machine: Commonsense Thinking, Artificial Intelligence, and the Future of the Human Mind\n \
https://www.amazon.in/Emotion-Machine-Commonsense-Artificial-Intelligence/dp/0743276647/ref=sr_1_3\n\n \
\U00002666 Fluent Python: Clear, Concise, and Effective Programming\n \
https://www.amazon.in/Fluent-Python-Luciano-Ramalho/dp/935213205X/ref=sr_1_1\n\n \
\U00002666 Naked Statistics – Stripping the Dread from the Data\n \
https://www.amazon.in/Naked-Statistics-Stripping-Dread-Data/dp/039334777X/ref=sr_1_1\n\n \
\U00002666 Mathematics for Machine Learning\n \
https://www.amazon.in/Mathematics-Machine-Learning-Peter-Deisenroth/dp/110845514X/ref=sr_1_2\n\n \
\U00002666 Make Your Own Neural Network\n \
https://www.amazon.in/Make-Your-Own-Neural-Network/dp/1530826608/ref=sr_1_1\n\n \
\U00002666 Artificial Intelligence For Dummies\n \
https://www.amazon.in/Artificial-Intelligence-Dummies-John-Mueller/dp/8126576103/ref=sr_1_1_sspa\n\n \
\U00002666 Machine Learning For Absolute Beginners\n \
https://www.amazon.in/Machine-Learning-Absolute-Beginners-Introduction/dp/1549617214/ref=sr_1_1\n\n \
\U00002666 Deep Learning with R\n \
https://www.amazon.in/Deep-Learning-R_p1-Joseph-Allaire/dp/161729554X/ref=sr_1_1")
        elif cyber_security_on:
            await message.answer("Some books to refer for Cyber Security:\n\n\n \
\U00002666 Hacking: The Art Of Exploitation\n \
https://www.amazon.in/Hacking-Art-Exploitation-Jon-Erickson/dp/1593271441/ref=sr_1_1\n\n \
\U00002666 Metasploit: The Penetration Tester’s Guide\n \
https://www.amazon.in/Metasploit-Penetration-Tester%E2%80%B2s-David-Kennedy/dp/159327288X/ref=sr_1_1\n\n \
\U00002666 Penetration Testing: A Hands-On Introduction to Hacking\n \
https://www.amazon.in/Penetration-Testing-Hands-Introduction-Hacking/dp/1593275641/ref=sr_1_1\n\n \
\U00002666 The Hacker Playbook 3: Practical Guide To Penetration Testing\n \
https://www.amazon.in/Hacker-Playbook-Practical-Penetration-Testing/dp/1980901759/ref=sr_1_1\n\n \
\U00002666 Practical Malware Analysis: The Hands-On Guide to Dissecting Malicious Software\n \
https://www.amazon.in/Practical-Malware-Analysis-Hands-Dissecting/dp/1593272901/ref=sr_1_1\n\n \
\U00002666 Social Engineering: The Science of Human Hacking\n \
https://www.amazon.in/Social-Engineering-Science-Human-Hacking/dp/111943338X/ref=sr_1_1\n\n \
\U00002666 Applied Cryptography: Protocols, Algorithms, and Source Code in C\n \
https://www.amazon.in/Applied-Cryptography-Protocols-Algorithms-Source/dp/1119096723/ref=sr_1_1\n\n \
\U00002666 Black Hat Python: Python Programming for Hackers and Pen-testers\n \
https://www.amazon.in/Black-Hat-Python-Justin-Seitz/dp/1593275900/ref=sr_1_1\n\n \
\U00002666 The Web Application Hacker's Handbook: Finding and Exploiting Security Flaws\n \
https://www.amazon.in/Web-Application-Hackers-Handbook-Exploiting-ebook/dp/B005LVQA9S/ref=sr_1_1_sspa\n\n \
\U00002666 Kali Linux Revealed\n \
https://www.amazon.in/Kali-Linux-Revealed-Penetration-Distribution/dp/0997615605/ref=sr_1_1\n\n \
\U00002666 Linux Basics for Hackers\n \
https://www.amazon.in/Linux-Basics-Hackers-Networking-Scripting/dp/1593278551/ref=pd_sim_4/260-9296315-6994404")
        elif blockchain_on:
            await message.answer("Some books to refer for Blockchain:\n\n\n \
\U00002666 The Book of Satoshi:\n\
The Collected Writings of Bitcoin Creator Satoshi Nakamoto\n\
https://www.amazon.in/Book-Satoshi-Collected-Writings-Nakamoto-ebook/dp/B00M6KGJ2K\n\n\
\U00002666 Decentralized Applications:\n\
Harnessing Bitcoin’s Blockchain Technology\n\
https://www.amazon.in/Decentralized-Applications-Siraj-Raval/dp/1491924543\n\n\
\U00002666 Mastering Blockchain Programming with Solidity:\n\
Write Production-ready Smart Contracts for Ethereum Blockchain with Solidity\n\
https://www.amazon.in/Mastering-Blockchain-Programming-Solidity-production-ready-ebook/dp/B07W5F8S1L\n\n\
\U00002666 Mastering Bitcoin:\n\
Programming the Open Blockchain\n\
https://www.amazon.in/Mastering-Bitcoin-Programming-Open-Blockchain/dp/9352135741\n\n\
\U00002666 Hands-On Blockchain for Python Developers:\n\
Gain blockchain programming skills to build decentralized applications using Python\n\
https://www.amazon.in/Hands-Blockchain-Python-Developers-decentralized/dp/1788627857\n\n")
        elif networking_on:
            await message.answer("Some books to refer for Networking:\n\n\n \
\U00002666 CompTIA Network+ Certification All-in-One Exam Guide\n\
https://www.amazon.in/dp/1260122387\n\n\
\U00002666 Network Programmability and Automation\n\
https://www.amazon.in/dp/1491931256\n\n\
\U00002666 Computer Networking: A Top-Down Approach\n\
https://www.amazon.in/dp/0133594149\n\n\
\U00002666 Computer Networks\n\
https://www.amazon.in/Computer-Networks-5e-5th-Tanenbaum/dp/9332518742\n\n")
        elif graphic_designing_on:
            await message.answer("Some books to refer for Graphics Design:\n\n\n\
\U00002666 Logo Modernism\n\
https://www.amazon.in/dp/3836545306\n\n\
\U00002666 The Elements of Typographic Style (v4)\n\
https://www.amazon.in/dp/0881792128\n\n\
\U00002666 How to be a Graphic Designer Without Losing Your Soul\n\
https://www.amazon.in/dp/1856697096\n\n\
\U00002666 Graphic Design for Art, Fashion, Film, Architecture, Photography, Product Design and Everything in Between\n\
https://www.amazon.in/dp/3791383507 \n\n")
        elif cloud_computing_on:
            await message.answer("Some books to refer for Cloud Computing:\n\n\n \
\U00002666 Cloud Application Architectures: Building Applications and Infrastructure in the Cloud\n \
https://www.amazon.in/Cloud-Application-Architecture-Reese/dp/8184047142/ref=sr_1_1\n\n \
\U00002666 Cloud Computing: Principles and Paradigms: 81 (Wiley Series on Parallel and Distributed Computing)\n \
https://www.amazon.in/Cloud-Computing-Principles-Paradigms-Distributed/dp/0470887990/ref=sr_1_2\n\n \
\U00002666 Distributed Systems\n \
https://www.amazon.in/Distributed-Systems-Coulouris-George/dp/9332575223/ref=sr_1_1\n\n \
\U00002666 Explain the Cloud Like I'm 10\n \
https://www.amazon.in/Explain-Cloud-Like-Im-10/dp/0979707110/ref=sr_1_1\n\n \
\U00002666 Cloud Computing for Dummies, 2ed\n \
https://www.amazon.in/Cloud-Computing-Dummies-Judith-Hurwitz/dp/8126570555/ref=sr_1_2\n\n \
\U00002666 Architecting the Cloud: Design Decisions for Cloud Computing Service Models (SaaS, PaaS, and IaaS)\n \
https://www.amazon.in/Architecting-Cloud-Decisions-Computing-Service/dp/1118617614/ref=sr_1_1\n\n \
\U00002666 Ahead in the Cloud: Best Practices for Navigating the Future of Enterprise IT\n \
https://www.amazon.in/Ahead-Cloud-Practices-Navigating-Enterprise/dp/1981924310/ref=sr_1_1\n\n \
\U00002666 Cloud Computing: From Beginning to End\n \
https://www.amazon.in/Cloud-Computing-Beginning-Ray-Rafaels/dp/1511404582/ref=sr_1_1\n\n \
\U00002666 Infrastructure as Code: Managing Servers in the Cloud\n \
https://www.amazon.in/Infrastructure-As-Code-Managing-Servers/dp/9352133811/ref=sr_1_1\n\n \
\U00002666 Cloud Computing Concepts Technology and Architecture\n \
https://www.amazon.in/Cloud-Computing-Concepts-Technology-Architecture/dp/B099KSQYJP/ref=sr_1_2\n\n \
\U00002666 Cloud Computing: A Hands-On Approach\n \
https://www.amazon.in/Cloud-Computing-Hands-Arshdeep-Bahga/dp/8173719233/ref=sr_1_1")
        elif game_development_on:
            await message.answer("Here's some books for you to refer for Game-development:\n\
\U00002666Hands-On Unity 2020 Game Development: Build, customize, \
and optimize professional games using Unity 2020 and C# 1st Edition\n\
https://www.amazon.in/Hands-Unity-2020-Game-Development-ebook/dp/B087BXKD89/ref=sr_1_2   \n \n\
\U00002666Game Development Projects with Unreal Engine: Learn to \
build your first games and bring your ideas to life using UE4 and C++ \n\
https://www.amazon.in/Game-Development-Projects-Unreal-Engine/dp/1800209223/ref=sr_1_4\n\n\
\U00002666Unity Game Development Blueprint:\n\
https://www.amazon.in/Unity-Game-Development-Blueprints-Doran/dp/1783553650/ref=sr_1_6?\n\n\
\U00002666Game Feel: A Game Designer's Guide to Virtual Sensation \
(Morgan Kaufmann Game Design Books)\n\
https://www.amazon.in/Game-Feel-Designers-Sensation-Kaufmann/dp/0123743281/ref=sr_1_1\n\n\
\U00002666The Art of Game Design: A Book of Lenses, Third Edition \n\
https://www.amazon.in/Art-Game-Design-Lenses-Third/dp/1138632058/ref=sr_1_1 \n\n\
\U00002666Practical Game Design: Learn the art of game design through \
applicable skills and cutting-edge insights\n\
https://www.amazon.in/Practical-Game-Design-applicable-cutting-edge/dp/1787121798/ref=sr_1_1\n\n\
\U00002666Game Engine Architecture, Third Edition \n\
https://www.amazon.in/Engine-Architecture-Third-Jason-Gregory/dp/1138035459/ref=sr_1_1\n\n\
\U00002666Unity from Zero to Proficiency (Intermediate): \
A step-by-step guide to coding your first FPS in C# with Unity. [Third Edition]\n\
https://www.amazon.in/Unity-Proficiency-Intermediate-step-step/dp/1696564298/ref=sr_1_1\n\n")
        elif data_science_on:
            await message.answer("Here's some books for you to refer for Data Science:\n\
\U00002666Data Science from scratch:\n\
https://www.amazon.in/Data-Science-Scratch-Joel-Grus/dp/149190142X/ref=sr_1_2\n\n\
\U00002666Hands-On Machine Learning with Scikit-Learn, Keras and Tensor Flow: \
Concepts, Tools and Techniques to Build Intelligent Systems:\n\
https://www.amazon.in/Hands-Machine-Learning-Scikit-Learn-Tensor/dp/9352139054/ref=sr_1_1\n\n\
\U00002666Build a carerr in Data Science:\n\
https://www.amazon.in/Build-Career-Science-Emily-Robinson/dp/1617296244/ref=sr_1_1\n\n\
\U00002666R for Data Science: Import, Tidy, Transform, Visualize, and Model Data:\n\
https://www.amazon.in/Data-Science-Transform-Visualize-Model/dp/9352134974/ref=sr_1_3\n\n\
\U00002666Python Data Science Handbook: Essential Tools for Working with Data:\n\
https://www.amazon.in/Python-Data-Science-Handbook-Essential/dp/9352134915/ref=sr_1_1\n\n\
\U00002666Practical Statistics for Data Scientists: \
50+ Essential Concepts Using R and Python, Second Edition Paperback:\n\
https://www.amazon.in/Practical-Statistics-Data-Scientists-Essential/dp/8194435005/ref=sr_1_1\n\n\
\U00002666Deep learning with python:\n\
https://www.amazon.in/Deep-Learning-Python-Francois-Chollet/dp/1617294438/ref=sr_1_3\n\n\
\U00002666Introduction to Machine Learning with Python: \
A Guide for Data Scientists (Greyscale Indian Edition):\n\
https://www.amazon.in/Introduction-Machine-Learning-Python-Scientists/dp/9352134575/ref=sr_1_3\n\n")
        elif robotics_and_hardware_on:
            await message.answer("Here's some books for you to refer to for \
Robotics and hardware:\n\
\U00002666Springer Handbook of Robotics :\n\
https://www.amazon.in/Springer-Handbook-Robotics-Handbooks/dp/3319325507/ref=sr_1_1\n\n\
\U00002666Robotics, Vision and Control: Fundamental Algorithms \
In MATLAB® Second, Completely Revised, Extended And Updated Edition:\n\
https://www.amazon.in/Robotics-Vision-Control-Fundamental-Algorithms/dp/3319544128/ref=sr_1_2\n\n\
\U00002666Probabilistic Robotics (Intelligent Robotics and Autonomous Agents series):\n\
https://www.amazon.in/Probabilistic-Robotics/dp/0262201623/ref=sr_1_1\n\n\
\U00002666Introduction to Robotics: Mechanics and Control:\n\
https://www.amazon.in/Introduction-Robotics-Mechanics-Control-3e/dp/8131718360/ref=sr_1_3\n\n\
\U00002666Modern Robotics: Mechanics, Planning, and Control:\n\
https://www.amazon.in/Modern-Robotics-Mechanics-Planning-Control/dp/1107156300/ref=sr_1_1\n\n\
\U00002666Planning Algorithims:\n\
https://www.amazon.in/Planning-Algorithms-Steven-M-LaValle/dp/0521862051/ref=sr_1_1\n\n\
\U00002666Principles of Robot Motion: \
Theory, Algorithms, and Implementations \
(Intelligent Robotics and Autonomous Agents series):\n\
https://www.amazon.in/Principles-Robot-Motion-Algorithms-Implementation/dp/0262033275/ref=sr_1_1\n\n\
\U00002666Mechanics of Robotic Manipulation (Intelligent Robotics and Autonomous Agents series):\n\
https://www.amazon.in/Mechanics-Manipulation-Intelligent-Robotics-Autonomous/dp/0262133962/ref=sr_1_2\n\n\
\U00002666The Art of electronics:\n\
https://www.amazon.in/Art-Electronics-Paul-Horowitz/dp/0521809266/ref=sr_1_2\n\n\
\U00002666Practical Electronics for Inventors, Fourth Edition:\n\
https://www.amazon.in/Practical-Electronics-Inventors-Fourth-Scherz/dp/1259587541/ref=sr_1_2\n\n\
\U00002666Getting Started With Electronics:\n\
https://www.amazon.in/Getting-Started-Electronics-Forrest-Mims/dp/0945053282/ref=sr_1_2\n\n\
\U00002666Understanding Basic Electronics:\n\
https://www.amazon.in/Understanding-Basic-Electronics-ARRL-Inc-ebook/dp/B0112HMEUI/ref=sr_1_7\n\n\
\U00002666Beginner's Guide to Reading Schematics, Fourth Edition:\n\
https://www.amazon.in/Beginners-Guide-Reading-Schematics-Gibilisco/dp/1260031101/ref=sr_1_1\n\n")
        elif front_end_development_on:
            await message.answer("Here's some books for you to refer for Front End Development:\n\n\n\
\U00002666 HTML and CSS: Design and build websites, by Jon Duckett\n\
https://amzn.to/2LrksaL\n\n\
\U00002666 JavaScript and JQuery: Interactive Front-End Web Development, by Jon Duckett\n\
https://amzn.to/2HICgNJ\n\n\
\U00002666 Learning Web Design: A beginner’s guide to HTML, CSS, Javascript, and Web Graphics, By Jennifer Niederst \
Robbins\n\
https://amzn.to/2Lvf1aK\n\n\
\U00002666 Eloquent Javascript: by Marijn Haverbake\n\
https://amzn.to/2NNC7MI\n\n\
\U00002666 Designing with Web Standards (Voices That Matter)\n\
https://amzn.to/2PGV2eJ\n\n")
        elif back_end_development_on:
            await message.answer("Here's some books for you to refer for Back End Development:\n\n\n\
\U00002666 Head First Java: By Kathy Sierra, Bert Bates\n\
https://www.amazon.in/gp/product/0596009208/\n\n\
\U00002666 Programming: Principles and Practice Using C++: By Bjarne Stroustrup\n\
https://www.amazon.in/gp/product/B00KPTEH8C/\n\n\
\U00002666 Learn Python The Hard Way: By Zed A. Shaw\n\
https://www.amazon.in/gp/product/9332582106/\n\n\
\U00002666 The Joy of PHP Programming: By Alan Forbes\n\
https://www.amazon.in/gp/product/1522792147/\n\n\
\U00002666 Beginning Node.js: By Basarat Ali Syed\n\
https://www.amazon.in/gp/product/1484201884/\n\n\
\U00002666 PHP & MySQL: The Missing Manual\n\
https://www.amazon.in/gp/product/144934190X/\n\n")
        elif android_development_on:
            await message.answer("Some books to refer for Android Development:\n\n\n \
\U00002666 Android Programming with Kotlin for Beginners\n \
https://www.amazon.in/gp/product/B07RLJNJHS/\n\n \
\U00002666 Android App Development for Dummies\n \
https://www.amazon.in/Android-App-Development-Dummies-3ed/dp/8126557869/\n\n \
\U00002666 Android Programming for Beginners\n \
https://www.amazon.in/Android-Programming-Beginners-depth-full-featured/dp/1789538505/\n\n \
\U00002666 Android Programming: The Big Nerd Ranch Guide\n \
https://www.amazon.in/Android-Programming-Ranch-Guide-Guides/dp/0135245125/\n\n \
\U00002666 Android Studio 3.0 Development Essentials\n \
https://www.amazon.in/Android-Studio-3-0-Development-Essentials/dp/1977540090/\n\n \
\U00002666 Android Cookbook: Problems and Solutions for Android\n \
https://www.amazon.in/Android-Cookbook-Problems-Solutions-Developers/dp/9352135555/\n\n \
\U00002666 Head First Android Development 2e\n \
https://www.amazon.in/dp/1491974052?tag=hackr0df-21&geniuslink=true\n\n \
\U00002666 Android App Development for Dummies\n \
https://www.amazon.in/Android-App-Development-Dummies-3ed/dp/8126557869/ref=sr_1_1_sspa\n\n \
\U00002666 GUI Design for Android Apps\n \
https://www.amazon.in/dp/B0781Y3PQG?tag=hackr0df-21&geniuslink=true\n\n \
\U00002666 The Busy Coder's Guide to Advanced Android Development\n \
https://www.amazon.in/dp/098167805X?tag=hackr0df-21&geniuslink=true\n\n \
\U00002666 Professional Android\n \
https://www.amazon.in/dp/1118949528?tag=hackr0df-21&geniuslink=true")
        elif ios_development_on:
            await message.answer("Some books to refer for IOS Development:\n\n\n \
\U00002666 iOS Programming: The Big Nerd Ranch Guide\n \
https://www.amazon.in/iOS-Programming-Nerd-Ranch-Guide/dp/0135264022/ref=sr_1_1\n\n \
\U00002666 iOS 15 Programming Fundamentals with Swift: Swift, Xcode, and Cocoa Basics\n \
https://www.amazon.in/iOS-Programming-Fundamentals-Swift-Grayscale/dp/9355421303/ref=sr_1_3\n\n \
\U00002666  iOS 15 Programming for Beginners\n \
https://www.amazon.in/iOS-Programming-Beginners-Kickstart-development-ebook/dp/B09CHHWVK3/ref=sr_1_1\n\n \
\U00002666 Beginning iOS 14 & Swift App Development\n \
https://www.amazon.in/Beginning-iOS-Swift-App-Development/dp/9811486042/ref=sr_1_1\n\n \
\U00002666 iOS 14 Programming for Beginners 5th Edition\n \
https://www.amazon.in/iOS-14-Programming-Beginners-building/dp/1800209746/ref=sr_1_3\n\n \
\U00002666 Mastering Swift 5.3\n \
https://www.amazon.in/Mastering-Swift-5-3-knowledge-programming/dp/1800562152/ref=sr_1_2\n\n \
\U00002666  iOS 14 Programming Fundamentals with Swift\n \
https://www.amazon.in/iOS-Programming-Fundamentals-Swift-Grayscale/dp/9385889419/ref=sr_1_1\n\n \
\U00002666 Programming iOS 14\n \
https://www.amazon.in/Programming-iOS-14-Controllers-Frameworks-ebook/dp/B08KWQ34WF/ref=sr_1_5\n\n \
\U00002666 SwiftUI Cookbook\n \
https://www.amazon.in/SwiftUI-Cookbook-Discover-solutions-practices-ebook/dp/B08C5JW4DX/ref=sr_1_1\n\n \
\U00002666 iOS Navigation 101\n \
https://www.amazon.in/iOS-Navigation-101-Development-Efficiently-ebook/dp/B07MDQS8ZV/ref=sr_1_1")

    elif message.text == "\U0001F3C5 Certifications":
        if cyber_security_on:
            await message.answer("Certifications that can help boost your career:\n\n\n \
\U00002666 Certified Information Systems Security Professional (CISSP)\n \
https://www.isc2.org/Certifications/CISSP\n\n \
\U00002666 Certified Ethical Hacker (CEH)\n \
https://www.eccouncil.org/programs/certified-ethical-hacker-ceh/\n\n \
\U00002666 Offensive Security Certified Professional (OSCP)\n \
https://www.offensive-security.com/pwk-oscp/\n\n \
\U00002666 CompTIA Security+\n \
https://www.comptia.org/certifications/security\n\n \
\U00002666 CompTIA Pentest+\n \
https://www.comptia.org/certifications/pentest\n\n \
\U00002666 Certified Information Systems Auditor (CISA)\n \
https://www.isaca.org/credentialing/cisa\n\n \
\U00002666 Certified Information Security Manager (CISM)\n \
https://www.isaca.org/credentialing/cism\n\n \
\U00002666 Systems Security Certified Practitioner (SSCP)\n \
https://www.isc2.org/Certifications/SSCP\n\n \
\U00002666 GIAC Security Essentials Certification (GSEC)\n \
https://www.giac.org/certifications/security-essentials-gsec/\n\n \
\U00002666 CompTIA Advanced Security Practitioner (CASP+)\n \
https://www.comptia.org/certifications/comptia-advanced-security-practitioner\n\n \
\U00002666 GIAC Certified Incident Handler (GCIH)\n \
https://www.giac.org/certifications/certified-incident-handler-gcih/")
        elif blockchain_on:
            await message.answer("Certifications that will help boost your career:\n\n\n\
\U00002666 Certified Blockchain Expert -  Blockchain Council\n\
https://www.blockchain-council.org/certifications/certified-blockchain-professional-expert/\n\n\
\U00002666 Certified Ethereum Expert - Blockchain Council\n\
https://www.blockchain-council.org/certifications/certified-ethereum-expert-cee/\n\n\
\U00002666 Certified Blockchain Professional - EC Council\n\
https://www.eccouncil.org/programs/certified-blockchain-professional-cbp/\n\n\
\U00002666 Certified Enterprise Blockchain Architect (CEBA) - 101 Blockchains\n\
https://academy.101blockchains.com/courses/certified-enterprise-blockchain-architect\n\n\
\U00002666 Blockchain Technology — EdX\n\
https://www.edx.org/professional-certificate/uc-berkeleyx-blockchain-fundamentals\n\n\
\U00002666 Certified Blockchain Developer — Educative\n\
https://www.educative.io/courses/hands-on-blockchain-hyperledger-fabric\n\n")
        elif networking_on:
            await message.answer("Certifications that will help boost your career:\n\n\n\
\U00002666 CompTIA IT Fundamentals (ITF+)\n\
https://www.comptia.org/certifications/network\n\n\
\U00002666 Cisco Certified Network Associate (CCNA)\n\
https://www.cisco.com/c/en/us/training-events/training-certifications/certifications/associate/ccna.html\n\n\
\U00002666 Cisco Certified Network Professional (CCNP) Enterprise:\n\
https://www.cisco.com/c/en/us/training-events/training-certifications/certifications/professional/ccnp-enterprise.\
html\n\n\
\U00002666 Cisco Certified Internetwork Expert (CCIE) Enterprise Infrastructure\n\
https://www.cisco.com/c/en/us/training-events/training-certifications/certifications/expert/ccie-enterprise-\
infrastructure.html\n\n\
\U00002666 VMWare Certified Technical Associate - Network Virtualization (VCTA-NV)\n\
https://www.vmware.com/education-services/certification/vcta-nv.html\n\n\
\U00002666 Juniper Networks Certified Associate - Junos (JNCIA-Junos)\n\
https://www.juniper.net/us/en/training/certification.html \n\n")
        elif graphic_designing_on:
            await message.answer("Certifications that will help boost your career:\n\n\n\
\U00002666 Adobe Certified Associate in Graphic Design and Illustration\n\
https://edex.adobe.com/teaching-resources/v770dfc88\n\n\
\U00002666 Visual Design Using Adobe Photoshop\n\
https://edex.adobe.com/teaching-resources/v97ccf4fe\n\n\
\U00002666 Print and Digital Media Publication Using Adobe InDesign\n\
https://edex.adobe.com/teaching-resources/v042df592 \n\n")
        elif cloud_computing_on:
            await message.answer("Certifications that can help boost your career:\n\n\n \
\U00002666 Microsoft Certified: Microsoft Azure Fundamentals\n \
https://docs.microsoft.com/en-us/learn/certifications/azure-fundamentals/\n\n \
\U00002666 Microsoft Certified: Azure Solutions Architect Expert\n \
https://docs.microsoft.com/en-us/learn/certifications/azure-solutions-architect/\n\n \
\U00002666 Microsoft Certified: Azure Administrator Associate\n \
https://docs.microsoft.com/en-us/learn/certifications/azure-administrator/\n\n \
\U00002666 AWS Certified SysOps Administrator\n \
https://aws.amazon.com/certification/certified-sysops-admin-associate/\n\n \
\U00002666 AWS Certified Solutions Architect – Associate\n \
https://aws.amazon.com/certification/certified-solutions-architect-associate/\n\n \
\U00002666 AWS Certified Developer – Associate\n \
https://aws.amazon.com/certification/certified-developer-associate/\n\n \
\U00002666 Google Certified Professional Cloud Architect\n \
https://cloud.google.com/certification/cloud-architect\n\n \
\U00002666 Google Certified Professional Data Engineer\n \
https://cloud.google.com/certification/data-engineer\n\n \
\U00002666 CompTIA Cloud+\n \
https://www.comptia.org/certifications/cloud\n\n \
\U00002666 Certified Cloud Security Professional (CCSP)\n \
https://www.isc2.org/Certifications/CCSP")
        elif game_development_on:
            await message.answer("Certifications that can help boost your career:\n\n\n \
\U00002666Professional Certificate in Computer Science for Game Development (Harvard University)\n \
https://www.edx.org/professional-certificate/harvardx-computer-science-for-game-development\n\n \
\U00002666Unity certified associate-game-developer\n \
https://unity.com/products/unity-certifications/associate-game-developer\n\n  ")
        elif robotics_and_hardware_on:
            await message.answer("Certifications that can help boost your career:\n\n\n \
\U00002666A3 CERTIFIED ROBOT INTEGRATOR PROGRAM\n \
https://www.automate.org/a3-content/robotic-integrator-certification-program\n\n \
\U00002666FANUC National Certifications for Robotics and Advanced Automation Manufacturing\n \
https://www.fanucamerica.com/education/nocti-certifications-robotics\n\n ")
        elif data_science_on:
            await message.answer("Certifications that can help boost your career:\n\n\n \
\U00002666IBM Data Science Professional Certificate\n \
https://www.ibm.com/training/badge/fb3af6d8-2402-4acb-b852-7a0c5034c976\n\n \
\U00002666HarvardX’s Data Science Professional Certificate\n \
https://www.edx.org/professional-certificate/harvardx-data-science\n\n \
\U00002666Amazon AWS Big Data Certification\n \
https://aws.amazon.com/certification/certified-big-data-specialty/\n\n \
\U00002666Microsoft Certified Azure Data Scientist Associate\n \
https://docs.microsoft.com/en-us/learn/certifications/azure-data-scientist/\n\n ")
        elif front_end_development_on:
            await message.answer("Certifications that can help boost your career:\n\n\n \
\U00002666W3C Front-End Web Developer Professional Certificate\n \
https://www.edx.org/professional-certificate/w3cx-front-end-web-developer\n\n \
\U00002666Certified Web Professional - Web Developer\n \
https://iwanet.org/profdevel/certification-levels/\n\n \
\U00002666Web Foundations Associate\n \
https://www.ciwcertified.com/\n\n \
\U00002666HTML5 Application Development Fundamentals\n \
https://docs.microsoft.com/en-us/learn/certifications/exams/98-375\n\n ")
        elif back_end_development_on:
            await message.answer("Certifications that can help boost your career:\n\n\n \
\U00002666CWP Web Developer Certificate\n \
https://iwanet.org/profdevel/certification-levels/\n\n \
\U00002666Oracle Certified Professional (OCP) MySQL 5.6 Developer\n \
https://education.oracle.com/oracle-certification-path/pfamily_406\n\n \
\U00002666Amazon Web Services (AWS Certified Developer – Associate Level)\n \
https://aws.amazon.com/certification/certified-developer-associate/\n\n \
\U00002666IBM Full Stack Cloud Developer Professional Certificate\n \
https://www.coursera.org/professional-certificates/ibm-full-stack-cloud-developer\n\n")

    elif message.text == "\U0001F393 Degrees":
        if cyber_security_on:
            await message.answer("Cyber Security Degrees which you can acquire:\n\n\n \
\U00002666 Colleges providing Bachelors Degree in Cyber Security\n \
https://www.bachelorstudies.com/Bachelor/Cyber-Security/\n\n \
\U00002666 Colleges providing Masters Degree in Cyber Security\n \
https://www.masterstudies.com/Masters-Degree/Cyber-Security/\n\n \
\U00002666 Caltech CTME Cybersecurity Certificate Program\n \
https://www.upgrad.com/cybersecurity-certificate-program-caltech\n\n \
\U00002666 Advanced Certificate Programme in Cyber Security\n \
https://www.upgrad.com/cyber-security-certification-pgc-iiitb\n\n \
\U00002666 Executive PG Programme in Software Development - Specialisation in Cyber Security\n \
https://www.upgrad.com/cyber-security-pgd-iiitb")
        elif blockchain_on:
            await message.answer("Possible Blockchain based degrees:\n\n\n\
\U00002666 Top 5 Universities for Blockchain Degrees(international)\n\
https://www.stoodnt.com/blog/top-5-universities-for-blockchain-degrees/\n\n\
\U00002666 Masters Programs in Blockchain in Europe 2022\n\
https://www.masterstudies.com/Masters-Degree/Blockchain/Europe/\n\n\
\U00002666 Advanced Certification in Software Engineering for Cloud, Blockchain & IoT - IIT: B\n\
https://www.greatlearning.in/iit-madras-acse \n\n")
        elif networking_on:
            await message.answer("Possible Networking based degrees:\n\n\n\
\U00002666 Bachelor Programs in Computer Networking(international)\n\
https://www.bachelorstudies.com/Bachelor/Computer-Networking/\n\n\
\U00002666 Bachelor Network Courses(India)\n\
https://collegedunia.com/courses/network#6\n\n\
M.E. (Computer Networking) Colleges in India\n\
https://targetstudy.com/colleges/me-computer-networking-degree-colleges-in-india.html\n\n\
Networking Colleges in India - 2022\n\
https://www.shiksha.com/it-software/networking-hardware-security/colleges/colleges-india \n\n")
        elif graphic_designing_on:
            await message.answer("Possible Graphic Design based degrees:\n\n\n\
\U00002666 Bachelor Programs in Graphic Design(international)\n\
https://www.bachelorstudies.com/Bachelor/Graphic-Design/\n\n\
\U00002666 BA in Graphics Design(India)\n\
https://www.collegedekho.com/courses/ba-graphic-design/\n\n\
\U00002666 Masters Programs in Graphic Design(international)\n\
https://www.masterstudies.com/Masters-Degree/Graphic-Design/\n\n\
\U00002666 Master of Arts [M.A.] in Graphic Design\n\
https://collegedunia.com/courses/master-of-arts-ma-graphic-design \n\n")
        elif cloud_computing_on:
            await message.answer("Cloud Computing Degrees which you can acquire:\n\n\n \
\U00002666 Colleges providing Bachelors Degree in Cloud Computing\n \
https://www.bachelorstudies.com/Bachelor/Cloud-Computing/\n\n \
https://www.securitydegreehub.com/best-cloud-computing-degree-programs/\n\n \
\U00002666 Colleges providing Masters Degree in Cloud Computing\n \
https://www.securitydegreehub.com/best-cloud-computing-masters-degree/\n\n \
https://www.masterstudies.com/Masters-Degree/Cloud-Computing/\n\n\
\U00002666 Executive PG Programme in Software Development - Specialisation in Cloud Computing\n \
https://www.upgrad.com/cloud-computing-pgd-iiitb\n\n \
\U00002666 Advanced Certificate Programme in Cloud Computing\n \
https://www.upgrad.com/cloud-computing-certification-pgc-iiitb")
        elif game_development_on:
            await message.answer("\U00002666 Your collective platform where you can get your Degrees\
for Game Development:\n\
https://web.ue-germany.com/en/bachelor/game-design\n\n\
\U00002666Bachelors in game development :\n\
https://www.bachelorstudies.com/Game-Design/\n\n\
\U00002666Masters in Game development programs:\n\
https://www.masterstudies.com/Masters-Degree/Game-Design/\n\n\
\U00002666Theory:\n\
https://www.bachelorstudies.com/Game-Theory/\n\n")
        elif data_science_on:
            await message.answer("Your Collective platforms where you can get \
your degrees in Data Science from:\n\n\
Keystone Bachelorstudies.com:\n\n\
\U00002666Bachelors in Data Science:\n\
https://www.bachelorstudies.com/Data-Science/\n\n\
\U00002666Masters in Data Science:\n\
https://www.masterstudies.com/Masters-Degree/Data-Science/\n\n")
        elif robotics_and_hardware_on:
            await message.answer("Your collective platform where you can \
get your degrees in Robotics and Hardware:\n\
\U00002666Bachelor Programs in robotics:\n\
https://www.bachelorstudies.com/Bachelor/Robotics/#:~\n\n\
\U00002666Masters Programs in Robotics:\n\
https://www.masterstudies.com/Masters-Degree/Robotics/\n\n")
        elif front_end_development_on:
            await message.answer("Web Development Degrees which you can acquire:\n\n\n \
\U00002666Bachelor’s in Web Development\n\
https://www.collegerank.net/web-development-bachelors/\n\n\
\U00002666Masters Programs in Web Development\n\
https://www.masterstudies.com/Masters-Degree/Web-Development/\n\n")
        elif back_end_development_on:
            await message.answer("Web Development Degrees which you can acquire:\n\n\n \
\U00002666Bachelor’s in Web Development\n\
https://www.collegerank.net/web-development-bachelors/\n\n\
\U00002666Masters Programs in Web Development\n\
https://www.masterstudies.com/Masters-Degree/Web-Development/\n\n")

    elif message.text == "\U0001F935 Jobs":
        if ai_and_ml_on:
            await message.answer("Job Roles differ from company to company. Here is a list of some common job \
roles for ai and ml:\n\n\n \
\U00002666 Business Intelligence Developer\n \
The primary responsibility of a Business Intelligence Developer is to consider the business acumen along with AI. \
They recognize different business trends by assessing complicated data sets. They help in swelling the profits of a \
company by preparing, developing and nourishing business intelligence solutions.\n\n \
\U00002666 Machine Learning Engineer\n \
Machine learning engineers are involved in building and maintaining self-running software that facilitates machine \
learning initiatives. They are in continuous demand by the companies and their position rarely remains vacant. \
They work with huge chunks of data and possess extraordinary data management traits.\n\n \
\U00002666 Research Scientist\n \
Research scientists undertake efforts in performing extensive research dealing with applications of machine learning \
and machine intelligence. A research scientist is one who has gained expertise in the field of applied mathematics, \
statistics, deep learning, and machine learning.\n\n \
\U00002666 AI Data Analyst\n \
The major function of an AI data analyst is to perform data mining, data cleaning, and data interpretation. By \
cleaning data, requisite data is collected to carry out data interpretation. Any sort of useless data is discarded \
by them so that it does not hamper the data interpretation process.\n\n \
\U00002666 Product Manager\n \
In the field of AI, the duty of a product manager is to resolve challenging problems by strategically collecting \
data. You should possess the skill of identifying relevant problems that obstructs the business proceedings. \
The next step is to get hold of related data sets to facilitate data interpretation.\n\n \
\U00002666 AI Engineer\n \
AI engineers are problem-solvers who develop, test and apply different models of Artificial Intelligence. \
They effectively handle AI infrastructure. They make use of machine learning algorithms and understanding of \
the neural network to develop useful AI models.\n\n \
\U00002666 Robotics Scientist\n \
A reduction in jobs will indeed take place due to the emergence of robotics in the field of AI. Conversely, \
jobs will also rise as robotics scientists are in incessant demands by major industries for programming their \
machines. The robots will help in carrying out certain tasks efficiently.")
        elif cyber_security_on:
            await message.answer("Job Roles differ from company to company. Here is a list of some common job \
roles for cyber security:\n\n\n \
\U00002666 Security Architect\n \
The Security Architect takes care of planning, implementing, and testing security systems. They are responsible for \
protecting the data from hackers, malware, and DDoS attacks. Since this is a senior-level position, adequate \
training with certification will be expected. The job of the security architect is to protect the network using \
proper firewalls.\n\n \
\U00002666 Security Consultant\n \
The Security Consultant is a flexible and tech-savvy person who protects the organization’s data and capital. \
They understand and analyze various security systems in all fields. The Security Consultant determines the \
different tests, like vulnerability, to protect the computer, network, and data. They are also capable of providing \
technical guidance when required.\n\n \
\U00002666 Penetration Tester\n \
A Penetration Tester finds the weaknesses and loopholes in the system that hackers can use. They are also \
called Ethical Hackers. They have a range of tools to test the network, web application, or product. They also \
document the research and findings to be helpful in the future.\n\n \
\U00002666 Chief Information Security Officer (CISO)\n \
This is an advanced-level job for which you will be required to handle a Security Officers team. You have the power \
to create your own security measure. You will also be required to collaborate with other stakeholders in determining \
the security of the system since this is an advanced role. There is an absolute necessity for proper training \
and certification.\n\n \
\U00002666 Cryptographer\n \
Cryptographers are security system professionals who are responsible for writing a code that hackers can’t crack. \
It is a mid-senior-level job that you will enjoy if you love coding.\n\n \
\U00002666 Security Analyst\n \
As a Security Analyst, you will be required to plan and execute various security measures. You analyze and document \
the security of the system and find the areas that are prone to attacks. This is an entry-level job if you aspire to \
become a cyber security professional.\n\n \
\U00002666 Security Engineer \n \
A Security Engineer is responsible for rebuilding the security system for the organization. They build the \
necessary arrangements to safeguard the system. This is an entry-level job if you aspire to become a cyber \
security professional.\n\n\
Some other roles may include:\n\
\U00002666 Security Auditor\n\
\U00002666 Security Director\n\
\U00002666 System Administrator\n\
\U00002666 Incident Responder\n\
\U00002666 Security Specialist\n\
\U00002666 Source Code Auditor")
        elif blockchain_on:
            await message.answer("Job Roles differ from company to company. Here is a list of some common job \
roles for blockchain:\n\n\n \
\U00002666 Blockchain Developer\n\
Blockchain developers with the expertise to help companies explore Blockchain platforms are in high demand. Blockchain \
development might be the most marketable career path today because people are eager to realize all the benefits of \
Blockchain. These individuals require absolute attention to detail as theirs is a high ranking position. Blockchain \
developers are programmers who create applications for blockchain. They typically have a lot of experience working \
with C++, Python, and Javascript before becoming Blockchain developers.\n\n\
\U00002666 Blockchain Solution Architect\n\
The Blockchain Solution Architect has the responsibility of designing, assigning, and connecting Blockchain solution \
components with the team experts such as developers, network administrators, UX designers, and IT Operations whose to \
develop to complete the Blockchain solutions.\n\n\
\U00002666 Blockchain Project Manager\n\
This individual is entrusted with the responsibility of connecting Blockchain projects to experts whose duty it is to \
develop Blockchain solutions. Blockchain project managers need to be equipped with the skills of a traditional (cloud) \
project manager. They also need to master the technical bit to understand the technology thoroughly. Another important \
ability is excellent communication skills; this is essential when addressing non-technical workers, when providing \
useful updates or when trying to get resources from higher authorities.\n\n\
\U00002666 Blockchain UX Designer\n\
With the incorporation of Blockchain into so many industries, its design as well as user interface, is becoming \
critical. The role of a Blockchain designer is shaping a user interface that creates trust and is alluring to a \
regular user. These individuals need to be able to pay attention to detail, have an artistic touch, but most \
importantly they need to be hardworking as their line of work requires them to spend countless hours behind their \
computers.\n\n\
\U00002666 Blockchain Quality Engineer\n\
In any development environment, we have a quality assurance engineer who tests and ensures that all areas of the \
project are of the required quality. In the Blockchain world, a Blockchain engineer plays a similar role by \
guaranteeing that all operations are of excellence in the Blockchain development environment. In other words, they \
conduct the testing and automation of frameworks for Blockchain. These individuals need to have a third eye as far as \
payment to detail is concerned because a small mistake on their part affects everyone using their technology. \
Excellent communication skills would also go a long way in maintaining good work relationships.\n\n\
\U00002666 Blockchain Legal Consultant\n\
Of course, as organizations try to comprehend the adoption of Blockchain into their systems legal issues always arise. \
As companies launch this new technology, they are also looking for legal expertise on what considerations to make \
while investing. They are curious about the implications of their actions, about how to handle their finances, and \
lastly how to manage their identity. Of course, for such an individual, proper communication skills are mandatory. You \
also need to have a good grasp of your international law as Blockchain is tech without borders for the same reason it \
is advisable that such people master as many universal languages as they can.\n\n")
        elif networking_on:
            await message.answer("Job Roles differ from company to company. Here is a list of some common job \
roles for networking:\n\n\n \
\U00002666 Network Engineer\n\
A network engineer designs and manages the groups of computers networked together. The network engineer performs tasks \
such as installing and configuring communication hardware, setting up of the network communication link, installing \
and configuring application software, troubleshooting operations to ensure continuous network availability, and \
offering technical support and assistance.\n\n\
\U00002666 Network Analyst\n\
Network analysts support the computer network and the overall computer infrastructure. Job duties might involve \
installing network software and training the user in new applications. The analyst might be responsible for \
coordinating system enhancements between the software and hardware, documenting procedures, and producing policies and \
procedures.\n\n\
\U00002666 Information Systems Administrator\n\
Information systems administrators assist with the design, delivery, and maintenance of an information technology \
infrastructure within the organization. The person assists in strategic planning and in evaluating and recommending \
services, products, and projects. The job involves assisting in the planning, development, implementation, and \
maintenance of the information platform. The information platform might include Web servers and services, \
technological applications, and interactive applications. Administrators also supply instruction, user aids, and \
assistance in problem solving for library IT applications.\n\n\
\U00002666 Network Technician\n\
The network technician generally services network computers and troubleshoots for potential problems. Network \
technicians often work the help-desk services to repair or upgrade computers. Technicians need to be familiar with the \
different operating systems such as Microsoft, Novell, and Unix, as well as the basics of computer networking. \n\n\
\U00002666 Computer Networking Instructor\n\
The increasing use of computer networks has created a need for more instructors who have a solid networking background \
and can teach those skills to students. Unlike in some other academic fields, one need not have a doctoral degree in \
computer networking to be a computer networking instructor. Although community colleges and four-year schools might \
prefer instructors to have a master’s degree, for-profit and certification schools usually only require substantial \
experience in the profession. It is also a way to remain a working professional while supplementing an income and \
contributing to the growth of the profession. \n\n")
        elif graphic_designing_on:
            await message.answer("Job Roles differ from company to company. Here is a list of some common job \
roles for graphic designing:\n\n\n \
\U00002666 Graphic designer\n\
Graphic designers develop graphics and layouts for product illustrations, company logos, websites and more. This job \
title can cover a huge range of duties in a huge range of industries.\n\n\
\U00002666 Creative director\n\
Creative directors determine the creative vision of a project. They make sure the overall aesthetic and cohesive look \
stays on track by leading their team through the steps to create something, whether that is a tangible product like a \
video game, film, magazine or something more abstract like an advertising campaign or brand identity.\n\n\
\U00002666 User experience (UX) designer\n\
UX designers work to make products, processes and services seamless, enjoyable and intuitive for users. They think \
about how the product feels, how users will use it. They ensure the product flows from one step to the next. UX \
designers might run user tests, refining any bumps or confusions in the process. This career involves tons of \
out-of-the-box thinking, creative intuition and a natural appreciation for smooth design.\n\n\
\U00002666 User interface (UI) designer\n\
UI design is often considered a subset of UX design and has similar overall goals. User interface designers focus on \
how the product is laid out. They design each screen and each page, ensuring that the layout visually works with the \
overall path a UX designer has charted.\n\n\
\U00002666 Production artist\n\
Production artists take over the hands-on steps of production—whether that’s in graphics, film, art or other formats. \
They upload and ensure the accuracy of design files throughout the last stages of development. The job is equal parts \
design and computer applications skill.\n\n\
\U00002666 Product developer\n\
Product developers ideate, lead and manage the creation of products. They can work on so many different things that \
their job duties will vary widely, but general tasks include performing industry research, creating illustrations, \
presenting the product to employers or stakeholders and contributing to the development process.\n\n\
\U00002666 Art director\n\
Art directors take charge of the visual style and content in magazines, newspapers, product packaging and movie and \
television productions. They create design and direct other artists to develop each contributing piece. They work \
closely with their employers or clients to cast an artistic vision that meets objectives, the available budget and \
desired impact.\n\n\
\U00002666 Marketing specialist\n\
Marketing specialists collect and analyze data on target customers, initiate marketing campaigns, measure \
effectiveness of marketing attempts and create strategies to promote their company and its goods or services.\n\n\
\U00002666 Multimedia artist or animator\n\
Multimedia artists and animators design complex graphics and animation using computer animation or modeling programs. \
They think about story development, visual impact and platforms to create media content that will meet their \
employer’s objectives. More brands and organizations are looking to increase their online video presence—and that’s \
been a boon for graphic designers with animation and motion graphics skills.\n\n\
\U00002666 Freelancer\n\
While it’s not a unique design job in its own right, but most of the job titles mentioned above can be performed as a \
freelancer. Designers who have some experience on their resume, a stunning portfolio of work or expertise in niche \
areas of design, marketing and graphics could build a career finding freelance projects.\n\n")
        elif cloud_computing_on:
            await message.answer("Job Roles differ from company to company. Here is a list of some common job \
roles for cloud computing:\n\n\n \
\U00002666 Cloud Engineer\n \
In an organization, from designing cloud software and systems to implementing and maintaining them, cloud engineers \
are accountable for all technical duties related to Cloud Computing. They possess talents that span in several \
domains including IT architecture, operations and software development.\n\n \
\U00002666 Cloud Architect\n \
A cloud architect is a professional who focuses on the bigger picture of designing the infrastructure and \
configuration, rather than designing and configuring the individual server. Innovations in technology could \
affect the company’s cloud infrastructure. A cloud engineer must have the ability to foresee how those changes \
and emerging technologies will affect their existing systems. To achieve success, the aspirant should carry eight \
to ten years of experience and must be able to build a roadmap for the company’s existing and future cloud \
assets.\n\n \
\U00002666 Cloud Developer\n \
As it is clear from the title, these professionals are the one who is responsible for coding and developing cloud \
applications. An effective cloud developer has to be expert in most – if not all – the major coding languages, with \
a minimum of 5 years of experience. Professionals in this role will work towards building, testing, debugging and \
deploying of applications in an organization’s cloud server, often using DevOps practices.\n\n \
\U00002666 Cloud System Operations Administrator\n \
Once the application has been designed and developed, Cloud System Operations Administrators are the one who takes \
over the project. These professionals are responsible for managing and monitoring most of the activities that \
follow the development of the applications. The aspirant should possess a deep understanding of system management, \
visualization and troubleshooting. They should have proficient command over Linux, along with a few configuration \
management tools, monitoring tools and coding languages.\n\n \
\U00002666 Cloud Product Manager\n \
A cloud product manager is responsible for the efficient performance and product planning for the cloud-based \
applications – product concepts and strategy documents. Their responsibilities also revolve around identifying \
product positioning and allowing the sales process. Along with experience in working with a software development \
company, they must have a Bachelor’s degree in business administration or computer science.\n\n \
\U00002666 Cloud Automation Engineer\n \
It is one of the most critical and influential roles that affect an organization’s success in the cloud industry. \
A cloud automation engineer possesses experience in software development or IT operations and applies it on cloud \
automation, orchestration and integration. This role often requires a wider understanding and knowledge of \
hardware and software, along with data centre and cloud infrastructure. A cloud automation engineer is responsible \
for implementing, optimizing and supporting cloud infrastructure.")
        elif data_science_on:
            await message.answer("Data science combines several disciplines, including statistics, \
data analysis, machine learning, and computer science. It can be daunting if you’re new \
to the field, but keep in mind that different roles and companies will \
prefer some skills over others. This means that you don’t have to be an expert at everything. \
There are potential data science jobs for lots of different experience levels.\n\
One important piece of advice for your job search is to read data science job \
descriptions carefullyThis will enable you to apply to jobs you’re already qualified\
for, or develop specific data skill sets to match the roles you want to pursue. \
“Data scientist” is often used as a blanket title to describe jobs that are \
drastically different. Let’s look at four kinds of data science jobs.\n\n\
Four Types of Data Science Jobs:\n\n\
\U00002666 The Data Analyst:\n\
There are some companies where being a data scientist is synonymous with being \
a data analyst. Your job might consist of tasks like pulling data out of \
SQL databases, becoming an Excel or Tableau master, and producing basic data visualizations \
and reporting dashboards. You may on occasion analyze the results of \
an A/B test or take the lead on your company’s Google Analytics account.\n\
A company like this is a great place for an aspiring data scientist to learn the ropes.\n\
Once you have a handle on your day-to-day responsibilities, a company like this \
can be a great environment to try new things and expand your skill set.\n\
\n\n\n\
\U00002666 The Data Engineer:\n\
Some companies get to the point where they have a lot of traffic (and an \
increasingly large amount of data), and they start looking for \
someone to set up a lot of the data infrastructure that the company will need \
moving forward. They’re also looking for someone to provide analysis. You’ll \
see job postings listed under both data scientist and data engineer for this type \
of position. Since you’d be (one of) the first data hires, heavy statistics \
and machine learning expertise is less important than strong software engineering skills.\n\
Mentorship opportunities for junior data scientists can be less plentiful at \
a company looking to leverage rapidly increasing amounts of data.\n\
As a result, you’ll have great opportunities to shine and grow via trial by fire, \
but there will be less guidance and you may face a greater risk of flopping or stagnating.\n\
\n\n\
\U00002666 The Machine Learning Engineer:\n\
There are a number of companies for whom their data \
(or their data analysis platform) is their product. In this case, \
the data analysis or machine learning going on can be pretty intense. \
This is probably the ideal situation for someone who has a formal mathematics, \
statistics, or physics background and is hoping to continue down a more academic path.\n\
Machine learning engineers often focus more on producing great \
data-driven products than they do answering operational questions for a company.\n\
Companies that fall into this group could be consumer-facing \
companies with massive amounts of data or companies that are offering a data-based service.\n\
\n\n\n\
\U00002666 The Data Science Generalist:\n\
A lot of companies are looking for a generalist to join an established \
team of other data scientists. The company you’re interviewing for cares \
about data but probably isn’t a data company. It’s equally important \
that you can perform analysis, touch production code, visualize data, etc.\n\
Some of the most important data generalist skills are familiarity with tools \
designed for big data, and experience with messy, real-life datasets.\n\
Generally, these companies are either looking for generalists or they’re looking \
to fill a specific niche where they feel their team is lacking, such as \
data visualization or machine learning.\n")
        elif game_development_on:
            await message.answer("The video game industry is booming and there are many \
types of jobs in the game industry for you to choose from! Click on each role for detailed \
job descriptions, salary expectations and other key information \
about working in game dev.\n\n\
the following are the Possible jobs for you in the Gaming Industry:\n\n\
\U00002666 Game Designer:\n\
Game designers create the concepts and worlds of video games. They are \
involved with the design of the genre, environment, story, characters, gameplay \
system, objectives and user experience of video games.\n\
A Game Designer is the creative force behind the development of a video game. \
They are the originator of the game concept and will develop it through to its \
final release. Game Designers author the storyline, writing the plot points, character \
development, and game objectives that drive the game. The designer will work within \
the rules of the genre of the game, with real innovation occurring when the \
genre is pushed to its limits or reinvented.\n\n\
\U00002666 System Designer:\n\
A System Designer is the creator of the software systems that will power a video game. \
They are brought in early in the development process to analyse the scope \
and design of the game to set up the platforms that will bring the game to life.\n\n\
\U00002666 Level Designer:\n\
A Level Designer is the creator of the levels within a game, mapping out the layout \
so that it functions within the rules of the game and executes \
gameplay as created by the Game Designer.\n\
The first stage of the level design process is to sketch out the layout of the \
level in two dimensions, this is based on the concept art and storyboards that \
are provided by the Game Designer. Once they have been signed off they are then rendered \
to their 3D iterations and the level is then populated with characters, objects, \
events, environments and circles of action.\n\n\
\U00002666 Game Programmer:\n\
Game programmer is a general term applied to the computer engineers \
that work on computer games. Usually trained in the basic languages of \
computer programming, programmers make a game come to life. They may \
specialize in areas of coding such as graphics, AI, sound, scripting, \
user interface, network, tools, porting, etc.\n\n\
\U00002666 AI Programmer:\n\
Artificial Intelligence (AI) Programmers can be said to give a game its brain. They \
create algorithms that set the behavior of characters and elements based on the gameplay \
of the individual player. This is done by customising the reactions of gameplay to the \
actions of the player. Elements such as pathfinding, group movement and camera control \
are all embedded into the gameplay strategy.\n\n\
\U00002666 Gameplay Engineer:\n\
Gameplay Engineers are code writers who adapt software to the requirements of a \
video game. They may also be required to create custom software for \
functions specific to a game.\n\n\
\U00002666 Video Game Artist:\n\
A Game Artist is often a generalist animator and/or 3D \
modeler who creates both 2D and 3D art for video games. \
Working from design briefs and concept art, Game Artists give \
expression to the script from the storyboard \
to populate the world of the game.\n\n\
\U00002666 Character Artist:\n\
3D Character Artists create 3D models of characters for films and video \
games. Models are often based on original concept art.\n\
Character Artists for computer games draw up the visual elements of as \
briefed by the Art Director and Lead Character Artist. They create illustrations \
of characters, vehicles, environment, weapons, props, etc from \
the original concept artist’s sketches.\n\n\
\U00002666 Environment Artist:\n\
3D Environment Artists are 3D Modelers who specialize in creating indoor and \
outdoor settings for films or video games.\n\n")
        elif robotics_and_hardware_on:
            await message.answer("Some of the Jobs availabe if you want to pursue your career in\
Robotics and hardware.\n\
\U00002666 Design Engineer:\n\
Design engineers create the visual look of a robot. They often start by sketching \
blueprints, schematics, or figures of a robot’s intended design, then work \
with a mechanical engineering team to ensure those plans are followed \
correctly during development.\n\
Though their work is concerned with the physical appearance, proportions, and \
functions of a robot, it is also important that design engineers have advanced \
computer science knowledge and that they understand how the various components \
of their design work together to bring a machine to life.\n\
\n\n\
\U00002666 Software Engineer:\n\
Software engineers in robotics are in charge of developing the software that \
allows each machine to function. They work closely with software designers \
and programmers to integrate new software with existing systems and typically \
remain involved throughout the robot’s construction to ensure full functionality is achieved.\n\
In robotics, software engineers are also tasked with staying up-to-date with \
changing technologies and trends, and must apply updates or reconfigure \
existing robotics software as needed.\n\
\n\n\
\U00002666 Hardware Engineer:\n\
A hardware engineer is responsible for the computer hardware that robots \
utilize to function. They can have a hand in everything from prototyping to development,\
and are often tasked with overseeing the execution of a hardware build.\n\
Once a robot has been constructed, a hardware engineer may also partake in\
testing and analysis of the designed systems, and lead a team in making any\
necessary changes for improvement.\n\
\n\n\
\U00002666 User Experience (UX) Designer:\n\
The work of a UX designer is one aspect of robotics Padir considers integral \
but often underrepresented in the larger robotics field. When building a robot, \
“sometimes engineers can overlook what the user needs,” he explains, identifying \
that it is up to the UX designer to represent this perspective in the development \
process.\n\
These professionals are typically tasked with evaluating how consumers will interact \
with a robot, and making decisions about how to build a system \
that’s best equipped to meet those needs. \n\
\n\n\
\U00002666 Data Scientist:\n\
As most robots run on data, the work of a data scientist is critical within the \
robotics field. These professionals are responsible for designing data modeling \
processes and creating the algorithms and predictive models on which the data is \
gathered and interpreted. They also analyze data sets on which existing robots function, \
make adjustments to collection processes or storage systems, and measure effectiveness in \
order to improve functionality.\n\
\n\n\
\U00002666 Machine Learning Engineer:\n\
Machine learning engineers are responsible for the automation aspect of robotics. \
These professionals rely heavily on data and predictive analytics in their work. In many \
cases, they use advanced software to automate predictive models as a way of advancing the \
machine’s function and helping it “learn” from its experiences.\n\
Machine learning engineers are often highly skilled in data science, deep \
learning, natural language processing, programming, and more.\n\
\n\n\
\U00002666 Algorithm Engineers:\n\
In the scope of robotics, an algorithm engineer’s main role is to research, develop, \
and then test the algorithms on which a robot runs. These professionals work \
closely with the rest of the development team to understand the desired functionality \
of the robot, then identify and integrate the data needed to reach that goal.\n\
This role straddles the line between data science, software, and computer science, \
requiring professionals to be well versed in all three disciplines.\n")
        elif front_end_development_on:
            await message.answer("Some of the Jobs availabe if you want to pursue your career in\
Front End Development\n\n\n\
\U00002666 Front-End Developer\n\
The generic job title that describes a developer who is skilled to some degree at HTML, CSS, DOM, and JavaScript and \
implementing these technologies on the web platform.\n\n\
\U00002666 Front-End Engineer (aka JavaScript Developer or Full-stack JavaScript Developer)\n\
The job title given to a developer who comes from a computer science, engineering, background and is using these \
skills to work with front-end technologies. This role typically requires a computer science degree and years of \
software development experience. When the word JavaScript Application is included in the job title, this will \
denote that the developer should be an advanced JavaScript developer possessing advanced programming, software \
development, and application development skills (i.e has years of experience building front-end applications).\n\n\
\U00002666 CSS/HTML Developer\n\
The front-end job title that describes a developer who is skilled at HTML and CSS, excluding JavaScript and \
Application know how.\n\n\
\U00002666 Front-End Web Designer\n\
When the word Designer is included in the job title, this will denote that the designer will posses front-end \
skills (i.e., HTML & CSS) but also professional design (Visual Design and Interaction Design) skills.\n\n\
\U00002666 Front-End SEO Expert\n\
When the word SEO is included in the job title, this will denote that the developer has extensive experience \
crafting front-end technologies towards an SEO strategy.\n\n\
\U00002666 Front-End Accessibility Expert\n\
When the word Accessibility is included in the job title, this will denote that the developer has extensive \
experience crafting front-end technologies that support accessibility requirements and standards.\n\n\
\U00002666 Front-End Dev. Ops\n\
When the word DevOps is included in the job title, this will denote that the developer has extensive experience \
with software development practices pertaining to collaboration, integration, deployment, automation, and measurement.\
\n\n\
\U00002666 Front-End Testing/QA\n\
When the word Testing or QA is included in the job title, this will denote that the developer has extensive \
experience testing and managing software that involves unit testing, functional testing, user testing, \
and A/B testing.")
        elif back_end_development_on:
            await message.answer("Areas of Work for Backend Engineers and Developers\n\n\
\U00002666Backend developers can find career opportunities in a variety of industries and locations. Some backend \
developers work exclusively with one company, while others work for agencies that specialize in web development for \
their clients. Beginning a career in this field requires learning the various aspects of server-side language and \
gaining an understanding of the other tools used daily. It’s also recommended that you seek an entry-level position \
to gain practical, hands-on experience. \n\n\
\U00002666Employers who hire backend developers tend to value a mixture of relevant education, updated skills \
training, and practical experience in the industry. A passion for learning new technologies is a significant \
plus in the web development industry. Those who move up the ranks toward senior backend developer positions often \
possess a strong knowledge of frontend development. If you’re interested in a fruitful career in this field, starting \
with backend development training is the first step. Moving on to frontend, or full-stack development certification is \
an important future step for optimizing your career opportunities.\n\n\n\
\U00002666Salaries and Career Prospects for Backend Developers\n\n\
\U00002666According to the Bureau of Labor Statistics, the career outlook for web development is favorable, as the \
industry expected to grow much faster than average. As with most web development careers, location can make a big \
difference in terms of average salary.\n\n\
\U00002666According to Glassdoor, the average salary for a web developer in the United States is $75,487 per year, with\
specializations leading to a higher average salary. Top cities where web developers earn more than the national \
average include San Francisco, Seattle, New York City, Los Angeles, and Chicago. Those who pursue additional training \
and education to become full-stack developers are typically able to command higher salaries. \n\n\
\U00002666To give you a sense of how fast the field of web development—including backend developers—is growing, \
consider the fact that there were approximately 148,500 positions for developers five years ago. Looking ahead five \
years into the future, that number is expected to grow to an estimated 188,000. This is substantial growth, which \
indicates a promising future for those who are just now getting their foot in the door of web development.\n\n")
        elif android_development_on:
            await message.answer("Job Roles differ from company to company. Here is a list of some common job \
roles for Android Development:\n\n\
\U00002666 Mobile software system Engineer\n\
\U00002666 Mobile Application Developer\n\
\U00002666 Android Application Developer\n\
\U00002666 Senior Android Developer\n\
\U00002666 Senior Mobile Developer")
        elif ios_development_on:
            await message.answer("Job Roles differ from company to company. Here is a list of some common job \
roles for IOS Development:\n\n\
\U00002666 Senior iOS Developer \n\
\U00002666 iOS Developer \n\
\U00002666 iOS Engineer \n\
\U00002666 Senior iOS Engineer \n\
\U00002666 iOS Mobile Core Engineer")

    elif message.text == "\U0001F393 Certifications/Degrees":
        if ai_and_ml_on:
            await message.answer("Here is a list of degrees which you can apply for AI and ML:\n\n\n \
\U00002666 Bachelors degree provided by colleges in AI and ML\n \
https://www.bachelorstudies.com/Bachelor/Artificial-Intelligence/\n\n \
\U00002666 Masters degree provided by colleges in AI and ML\n \
https://www.masterstudies.com/MSc/Artificial-Intelligence/\n\n\
\U00002666 List of degree programs (Upgrad)\n \
https://www.upgrad.com/machine-learning-course/\n\n\n\
Here are some certifications which you can acquire for AI and ML\n\n\
\U00002666 List of Learnbay certifications\n \
https://www.learnbay.co/data-science-course/data-science-certification-courses/\n\n \
https://www.learnbay.co/data-science-course/artificial-intelligence-certification-course/\n\n \
https://www.learnbay.co/data-science-course/data-science-ai-for-managers/\n\n \
\U00002666 Artificial Intelligence Engineer by Simplilearn\n \
https://www.simplilearn.com/artificial-intelligence-masters-program-training-course\n\n \
\U00002666 List of 15 Artificial Intelligence Courses and Certifications\n \
https://digitaldefynd.com/best-artificial-intelligence-courses-training-certifications/\n\n")
        elif android_development_on:
            await message.answer("Here is a list of degrees which you can apply for Android Development:\n\n\n \
\U00002666 Colleges providing masters degree in mobile application development\n \
https://www.findamasters.com/masters-degrees/?Keywords=mobile+application+development\n\n \
\U00002666 Android Basics by Google (Udacity Nanodegree)\n\
https://www.udacity.com/course/android-basics-nanodegree-by-google--nd803\n\n \
\U00002666 Become an Android Kotlin Developer (Udacity Nanodegree)\n \
https://www.udacity.com/course/android-kotlin-developer-nanodegree--nd940\n\n\n\
Here are some certifications which you can acquire for Android Development\n\n\
\U00002666 Associate Android Developer Certification\n \
https://grow.google/certificates/android-developer/\n\n\
\U00002666 Associate Android Developer\n \
https://developers.google.com/certification/associate-android-developer")

    elif message.text == "\U0001F519 Back":
        if ai_and_ml_on:
            ai_and_ml_on = False
            await message.answer("\U0001F519 Back", reply_markup=guides_menu_keyboard)
        elif cyber_security_on:
            cyber_security_on = False
            await message.answer("\U0001F519 Back", reply_markup=guides_menu_keyboard)
        elif blockchain_on:
            blockchain_on = False
            await message.answer("\U0001F519 Back", reply_markup=guides_menu_keyboard)
        elif networking_on:
            networking_on = False
            await message.answer("\U0001F519 Back", reply_markup=guides_menu_keyboard)
        elif graphic_designing_on:
            graphic_designing_on = False
            await message.answer("\U0001F519 Back", reply_markup=guides_menu_keyboard)
        elif cloud_computing_on:
            cloud_computing_on = False
            await message.answer("\U0001F519 Back", reply_markup=guides_menu_keyboard)
        elif front_end_development_on and web_development_on and software_development_on:
            front_end_development_on = False
            await message.answer("\U0001F519 Back", reply_markup=web_development_keyboard)
        elif back_end_development_on and web_development_on and software_development_on:
            back_end_development_on = False
            await message.answer("\U0001F519 Back", reply_markup=web_development_keyboard)
        elif web_development_on and software_development_on:
            web_development_on = False
            await message.answer("\U0001F519 Back", reply_markup=software_development_keyboard)
        elif android_development_on and application_development_on and software_development_on:
            android_development_on = False
            await message.answer("\U0001F519 Back", reply_markup=application_development_keyboard)
        elif ios_development_on and application_development_on and software_development_on:
            ios_development_on = False
            await message.answer("\U0001F519 Back", reply_markup=application_development_keyboard)
        elif application_development_on and software_development_on:
            application_development_on = False
            await message.answer("\U0001F519 Back", reply_markup=software_development_keyboard)
        elif software_development_on:
            software_development_on = False
            await message.answer("\U0001F519 Back", reply_markup=guides_menu_keyboard)
        elif data_science_on:
            data_science_on = False
            await message.answer("\U0001F519 Back", reply_markup=guides_menu_keyboard)
        elif game_development_on:
            game_development_on = False
            await message.answer("\U0001F519 Back", reply_markup=guides_menu_keyboard)
        elif robotics_and_hardware_on:
            robotics_and_hardware_on = False
            await message.answer("\U0001F519 Back", reply_markup=guides_menu_keyboard)
        else:
            await message.answer("\U0001F519 Back", reply_markup=top_menu_keyboard)

    elif message.text == "\U0001F51D Main Menu":
        await message.answer("\U0001F51D Main Menu", reply_markup=top_menu_keyboard)
    else:
        await message.reply("\U0000274C Not a recognized command\n\nSelect one of the buttons or enter \
/start to reload the bot")


# Starts polling/checking whether any changes are made in Telegram Bot i.e. whether any command is pressed or
# text is entered.
executor.start_polling(dp)
