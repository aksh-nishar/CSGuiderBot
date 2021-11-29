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
certifications_degrees_button = KeyboardButton("Certifications/Degrees")

ai_and_ml_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(skills_required_button, courses_button)
ai_and_ml_keyboard.add(books_button, jobs_button)
ai_and_ml_keyboard.add(certifications_degrees_button)
ai_and_ml_keyboard.add(back_button, back_to_top_menu_button)

cyber_security_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(skills_required_button, courses_button)
cyber_security_keyboard.add(books_button, certifications_button)
cyber_security_keyboard.add(degrees_button, jobs_button)
cyber_security_keyboard.add(back_button, back_to_top_menu_button)

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


@dp.message_handler(commands=['start', 'help'])
async def welcome(message: types.Message):
    if message.is_command():
        await message.reply("Hello, Welcome to CSGuider Bot", reply_markup=top_menu_keyboard)
    else:
        await message.reply(message.text + " is not a recognized command, please enter /start")


@dp.message_handler()
async def main_keyboard_answer(message: types.Message):

    global ai_and_ml_on, cyber_security_on, game_development_on, software_development_on, blockchain_on, \
        cloud_computing_on, networking_on, graphic_designing_on, data_science_on, robotics_and_hardware_on

    if message.text == "What is CSGuider Bot?":
        pass
    elif message.text == "Why we created this bot?":
        pass
    elif message.text == "\U00002757\U00002757Important Note\U00002757\U00002757":
        pass
    elif message.text == "Go to Guides":
        await message.answer("Guides", reply_markup=guides_menu_keyboard)
    elif message.text == "AI and ML Guide":
        ai_and_ml_on = True
        await message.answer("AI and ML Guide", reply_markup=ai_and_ml_keyboard)
    elif message.text == "Cyber Security Guide":
        cyber_security_on = True
        await message.answer("Cyber Security Guide", reply_markup=cyber_security_keyboard)
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
    elif message.text == "Skills Required":
        if ai_and_ml_on:
            await message.answer("Some skills required to get into AI and ML are as follows:\n\n\n \
\U00002666 Applied Mathematics which include\n \
Linear algebra, probability, statistics, multivariate calculus, distributions like Poisson, normal, binomial, etc\
and some knowledge of Physics concepts.\n\n \
\U00002666 Computer Science Fundamentals and Programming\n \
CS concepts like data structures and algorithms, space and time complexity, programming languages like Python and R\
for ML and statistics, Spark and Hadoop for distributed computing, SQL for database management, Apache Kafka for\
data pre-processing, etc. Python libraries like NumPy, Pandas, Matplotlib, Scikit-Learn, Tensor-Flow, etc.\n\n \
\U00002666 Machine Learning algorithms\n \
Some common ones include Naïve Bayes Classifier, K Means Clustering, Support Vector Machine, Apriori Algorithm, \
Linear Regression, Logistic Regression, Decision Trees, Random Forests, etc.\n\n \
\U00002666 Neural Networks\n \
Different types of neural networks like Feedforward Neural Network, Recurrent Neural Network, \
Convolutional Neural Network, Modular Neural Network, Radial basis function Neural Network, etc.\n\n \
\U00002666 Natural Language Processing\n \
This is so that machines can understand and interpret the human language to eventually understand human \
communication in a better way. Natural Language Toolkit which is the most popular platform for creating \
applications relating to NLP.\n\n \
\U00002666 Data Modeling and Evaluation\n \
Data modeling involves understanding the underlying structure of the data and then finding patterns that are \
not obvious to the naked eye. You also need to evaluate the data using an algorithm that is suitable for the data.\n\n\
\U00002666 Communication Skills\n \
That’s because while you understand the data and the insights obtained using machine learning better than anyone \
else, it is equally important that you can convey these insights to a non-technical team, your shareholders, \
or clients.")
        elif cyber_security_on:
            pass
    elif message.text == "Courses":
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
\U00002666 List of AI and ML programs (Udacity)\n \
https://www.udacity.com/courses/all?search=artificial%20intelligence")
        elif cyber_security_on:
            pass
    elif message.text == "Books":
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
            pass
    elif message.text == "Certifications":
        if cyber_security_on:
            pass
    elif message.text == "Degrees":
        if cyber_security_on:
            pass
    elif message.text == "Jobs":
        if ai_and_ml_on:
            await message.answer("Job Roles differ from company to company. Here is a list of some common job \
roles:\n\n\n \
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
            pass
    elif message.text == "Certifications/Degrees":
        if ai_and_ml_on:
            await message.answer("Here is a list of certifications and degrees which you can apply for \
AI and ML:\n\n\n \
\U00002666 List of degree programs (Upgrad)\n \
https://www.upgrad.com/machine-learning-course/\n\n \
\U00002666 List of Learnbay certifications\n \
https://www.learnbay.co/data-science-course/data-science-certification-courses/\n\n \
https://www.learnbay.co/data-science-course/artificial-intelligence-certification-course/\n\n \
https://www.learnbay.co/data-science-course/data-science-ai-for-managers/\n\n \
\U00002666 Artificial Intelligence Engineer by Simplilearn\n \
https://www.simplilearn.com/artificial-intelligence-masters-program-training-course\n\n \
\U00002666 List of 15 Artificial Intelligence Courses and Certifications\n \
https://digitaldefynd.com/best-artificial-intelligence-courses-training-certifications/\n\n \
\U00002666 Bachelors degree provided by colleges in AI and ML\n \
https://www.bachelorstudies.com/Bachelor/Artificial-Intelligence/\n\n \
\U00002666 Masters degree provided by colleges in AI and ML\n \
https://www.masterstudies.com/MSc/Artificial-Intelligence/")
    elif message.text == "Back":
        if ai_and_ml_on:
            ai_and_ml_on = False
            await message.answer("Back", reply_markup=guides_menu_keyboard)
        elif cyber_security_on:
            cyber_security_on = False
            await message.answer("Back", reply_markup=guides_menu_keyboard)
        else:
            await message.answer("Back", reply_markup=top_menu_keyboard)
    elif message.text == "Main Menu":
        await message.answer("Main Menu", reply_markup=top_menu_keyboard)
    else:
        await message.reply("Not a recognized command, select one of the buttons")


executor.start_polling(dp)
