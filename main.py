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

blockchain_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(skills_required_button, courses_button)
blockchain_keyboard.add(books_button, certifications_button)
blockchain_keyboard.add(degrees_button, jobs_button)
blockchain_keyboard.add(back_button, back_to_top_menu_button)

networking_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(skills_required_button, courses_button)
networking_keyboard.add(books_button, certifications_button)
networking_keyboard.add(degrees_button, jobs_button)
networking_keyboard.add(back_button, back_to_top_menu_button)

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
        await message.answer("Blockchain Guide", reply_markup=blockchain_keyboard)
    elif message.text == "Cloud Computing Guide":
        cloud_computing_on = True
        pass
    elif message.text == "Networking Guide":
        networking_on = True
        await message.answer("Networking Guide", reply_markup=networking_keyboard)
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
        elif blockchain_on:
            await message.answer("Some skills required to get into Blockchain are as follows:\n\n\n \
\U000026A1 Blockchain architecture. \n \
Blockchain developers should fully understand how blockchain works and the architecture on which it's based. They \
should be well versed in concepts such as cryptography, consensus, hash functions, distributed ledgers, smart \
contracts and any other concepts integral to understanding blockchain's inner workings. Developers should also be \
familiar with the four types of blockchain architecture: consortium, private, public and hybrid.\n\n\
\U000026A1 Cryptography. \n \
Effective cryptography is essential to providing a secure blockchain environment, and developers should have a strong \
foundation in cryptographic concepts and practices, including wallets, keys and digital signatures. \n\n\
\U000026A1 Data structures. \n\
The entire blockchain network consists of data structures. Each block can be considered a type of data structure that \
clusters transactions for the public ledger. Blockchain developers must routinely work with data structures and should \
understand how the blockchain network uses them. \n\n\
\U000026A1 Smart contracts. \n\
Smart contracts are self-executing contracts that enable two parties to exchange goods and services without an \
intermediary. Smart contracts have become a staple of blockchain implementations, and developers should have a \
thorough understanding of what they are and how they enforce business logic. \n\n\
\U000026A1 Web development. \n\
Blockchain and web development go hand in hand, especially with blockchain's emphasis on decentralized applications. \
Blockchain developers should be experienced in all aspects of web development.\n\n\
\U000026A1 Programming languages. \n\
Blockchain technologies often use different programming languages, depending on the platforms used to implement the \
blockchain environments. Although developers can't be experts in every language, they still need to be proficient in \
any number of them. Some of the more common languages used for blockchain include Java, C++, Python and JavaScript. \n")
        elif networking_on:
            await message.answer("In order to build a career in networking, one needs to develop skill and knowledge \
pertaining to the following topics: \n\n\n \
\U0001F5A71. Internet\n\
Internet is a worldwide virtual networking medium that connects computers all across the world. Net is short for the \
internet and has millions of smaller networks that carry a huge array of information.\n\n\
\U0001F5A72. Linux\n\
Linux is a Unix-like operating system. Just like Windows, Mac OS, and IOS, Linux is an operating system used by \
millions across the globe. Android itself is powered by the Linux operating system. \n\n\
\U0001F5A73. Ethernet\n\
Ethernet refers to a system that connects a series of computers in a local area network (LAN). This is often done \
through ethernet cables, which plug into a router or other port in the modem in addition to the computer port.\n\n\
\U0001F5A74. Network Security\n\
Here's how network security is used on computer network engineer resumes:\n\
Create and enforce network security policy.\n\
Analyzed data network documentation and assisted in communicating to management regarding the current operational \
status of networks.\n\
Appointed to Boundary Protection Technician, providing network security and monitoring firewall; opened firewall ports \
on case-by-case basis.\n\n\
\U0001F5A75. Assurance\n\
Here's how assurance is used on computer network engineer resumes:\n\
Performed information assurance vulnerability assessments on more than 12 ships.\n\
Implemented Information Assurance controls to ensure all resident information systems were safe and secure.\n\n\
\U0001F5A76. Hardware\n\
Hardware is the physical part attached to a computer or other similar devices. Components are the internal parts of \
hardware which include RAM, hard drives, motherboard, and so on. External hardware devices which include, keyboard, \
mouse, printer, and so on are known as peripherals. All of these together are called computer hardware.\n\n\
")
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
        elif blockchain_on:
            await message.answer("List of some courses and programs for Blockchain:\n\n\n \
\U000026A1Blockchain and Bitcoin Fundamentals\n\
https://www.udemy.com/course/blockchain-and-bitcoin-fundamentals/\n\n\
\U000026A1Bitcoin and Cryptocurrency Bootcamp\n\
https://www.udemy.com/course/bitcoin-and-cryptocurrency-bootcamp/\n\n\
\U000026A1Blockchain Specialization - University of California, Irvine(certified course)\n\
https://www.coursera.org/specializations/uci-blockchain\n\n\
\U000026A1Blockchain Tutorial For Beginners\n\
https://www.youtube.com/playlist?list=PLsyeobzWxl7oY6tZmnZ5S7yTDxyu4zDW-\n\n\
\U000026A1ETHEREUM DEVELOPMENT TUTORIALS\n\
https://ethereum.org/en/developers/tutorials/\n\n\
\U000026A1Ethereum Tutorial\n\
https://www.tutorialspoint.com/ethereum/index.htm \n\n")
        elif networking_on:
            await message.answer("List of some courses and programs for Networking:\n\n\n \
\U0001F5A7Networking Essentials \n\
https://www.netacad.com/courses/networking/networking-essentials\n\n\
\U0001F5A7CCNA: Introduction to Networks\n\
https://www.netacad.com/courses/networking/ccna-introduction-networks\n\n\
\U0001F5A7Introduction to networking for complete beginners\n\
https://www.udemy.com/course/introduction-to-networking-for-complete-beginners/\n\n\
\U0001F5A7The Complete Networking Fundamentals Course. Your CCNA start\n\
https://www.udemy.com/course/complete-networking-fundamentals-course-ccna-start/\n\n\
\U0001F5A7Computer Networks\n\
https://www.youtube.com/playlist?list=PLBlnK6fEyqRgMCUAG0XRw78UA8qnv6jEx \n\n\
")
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
        elif blockchain_on:
            await message.answer("Some books to refer for Blockchain:\n\n\n \
\U000026A1The Book of Satoshi:\n\
The Collected Writings of Bitcoin Creator Satoshi Nakamoto\n\
https://www.amazon.in/Book-Satoshi-Collected-Writings-Nakamoto-ebook/dp/B00M6KGJ2K\n\n\
\U000026A1Decentralized Applications:\n\
Harnessing Bitcoin’s Blockchain Technology\n\
https://www.amazon.in/Decentralized-Applications-Siraj-Raval/dp/1491924543\n\n\
\U000026A1Mastering Blockchain Programming with Solidity:\n\
Write Production-ready Smart Contracts for Ethereum Blockchain with Solidity\n\
https://www.amazon.in/Mastering-Blockchain-Programming-Solidity-production-ready-ebook/dp/B07W5F8S1L\n\n\
\U000026A1Mastering Bitcoin:\n\
Programming the Open Blockchain\n\
https://www.amazon.in/Mastering-Bitcoin-Programming-Open-Blockchain/dp/9352135741\n\n\
\U000026A1Hands-On Blockchain for Python Developers:\n\
Gain blockchain programming skills to build decentralized applications using Python\n\
https://www.amazon.in/Hands-Blockchain-Python-Developers-decentralized/dp/1788627857\n\n\
            ")
        
        elif networking_on:
            await message.answer("Some books to refer for Networking:\n\n\n \
\U0001F5A7CompTIA Network+ Certification All-in-One Exam Guide\n\
https://www.amazon.in/dp/1260122387\n\n\
\U0001F5A7Network Programmability and Automation\n\
https://www.amazon.in/dp/1491931256\n\n\
\U0001F5A7Computer Networking: A Top-Down Approach\n\
https://www.amazon.in/dp/0133594149\n\n\
\U0001F5A7Computer Networks\n\
https://www.amazon.in/Computer-Networks-5e-5th-Tanenbaum/dp/9332518742\n\n")

    elif message.text == "Certifications":
        if cyber_security_on:
            pass
        elif blockchain_on:
            await message.answer("Certifications that will help boost your career:\n\n\n\
\U000026A1Certified Blockchain Expert -  Blockchain Council\n\
https://www.blockchain-council.org/certifications/certified-blockchain-professional-expert/\n\n\
\U000026A1Certified Ethereum Expert - Blockchain Council\n\
https://www.blockchain-council.org/certifications/certified-ethereum-expert-cee/\n\n\
\U000026A1Certified Blockchain Professional - EC Council\n\
https://www.eccouncil.org/programs/certified-blockchain-professional-cbp/\n\n\
\U000026A1Certified Enterprise Blockchain Architect (CEBA) - 101 Blockchains\n\
https://academy.101blockchains.com/courses/certified-enterprise-blockchain-architect\n\n\
\U000026A1Blockchain Technology — EdX\n\
https://www.edx.org/professional-certificate/uc-berkeleyx-blockchain-fundamentals\n\n\
\U000026A1Certified Blockchain Developer — Educative\n\
https://www.educative.io/courses/hands-on-blockchain-hyperledger-fabric\n\n")
        elif networking_on:
            await message.answer("Certifications that will help boost your career:\n\n\n\
\U0001F5A7CompTIA IT Fundamentals (ITF+)\n\
https://www.comptia.org/certifications/network\n\n\
\U0001F5A7Cisco Certified Network Associate (CCNA)\n\
https://www.cisco.com/c/en/us/training-events/training-certifications/certifications/associate/ccna.html\n\n\
\U0001F5A7Cisco Certified Network Professional (CCNP) Enterprise:\n\
https://www.cisco.com/c/en/us/training-events/training-certifications/certifications/professional/ccnp-enterprise.\
html\n\n\
\U0001F5A7Cisco Certified Internetwork Expert (CCIE) Enterprise Infrastructure\n\
https://www.cisco.com/c/en/us/training-events/training-certifications/certifications/expert/ccie-enterprise-\
infrastructure.html\n\n\
\U0001F5A7VMWare Certified Technical Associate - Network Virtualization (VCTA-NV)\n\
https://www.vmware.com/education-services/certification/vcta-nv.html\n\n\
\U0001F5A7Juniper Networks Certified Associate - Junos (JNCIA-Junos)\n\
https://www.juniper.net/us/en/training/certification.html \n\n")
    elif message.text == "Degrees":
        if cyber_security_on:
            pass
        elif blockchain_on:
            await message.answer("Possible Blockchain based degrees:\n\n\n\
\U000026A1Top 5 Universities for Blockchain Degrees(international)\n\
https://www.stoodnt.com/blog/top-5-universities-for-blockchain-degrees/\n\n\
\U000026A1Masters Programs in Blockchain in Europe 2022\n\
https://www.masterstudies.com/Masters-Degree/Blockchain/Europe/\n\n\
\U000026A1Advanced Certification in Software Engineering for Cloud, Blockchain & IoT - IIT: B\n\
https://www.greatlearning.in/iit-madras-acse \n\n")
        elif networking_on:
            await message.answer("Possible NEtworking based degrees:\n\n\n\
\U0001F5A7Bachelor Programs in Computer Networking(international)\n\
https://www.bachelorstudies.com/Bachelor/Computer-Networking/\n\n\
\U0001F5A7Bachelor Network Courses(India)\n\
https://collegedunia.com/courses/network#6\n\n\
M.E. (Computer Networking) Colleges in India\n\
https://targetstudy.com/colleges/me-computer-networking-degree-colleges-in-india.html\n\n\
Networking Colleges in India - 2022\n\
https://www.shiksha.com/it-software/networking-hardware-security/colleges/colleges-india \n\n")
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
        elif blockchain_on:
            await message.answer("Job Roles differ from company to company. Here is a list of some common job \
roles:\n\n\n \
\U000026A1Blockchain Developer\n\
Blockchain developers with the expertise to help companies explore Blockchain platforms are in high demand. Blockchain \
development might be the most marketable career path today because people are eager to realize all the benefits of \
Blockchain. These individuals require absolute attention to detail as theirs is a high ranking position. Blockchain \
developers are programmers who create applications for blockchain. They typically have a lot of experience working \
with C++, Python, and Javascript before becoming Blockchain developers.\n\n\
\U000026A1Blockchain Solution Architect\n\
The Blockchain Solution Architect has the responsibility of designing, assigning, and connecting Blockchain solution \
components with the team experts such as developers, network administrators, UX designers, and IT Operations whose to \
develop to complete the Blockchain solutions.\n\n\
\U000026A1Blockchain Project Manager\n\
This individual is entrusted with the responsibility of connecting Blockchain projects to experts whose duty it is to \
develop Blockchain solutions. Blockchain project managers need to be equipped with the skills of a traditional (cloud) \
project manager. They also need to master the technical bit to understand the technology thoroughly. Another important \
ability is excellent communication skills; this is essential when addressing non-technical workers, when providing \
useful updates or when trying to get resources from higher authorities.\n\n\
\U000026A1Blockchain UX Designer\n\
With the incorporation of Blockchain into so many industries, its design as well as user interface, is becoming \
critical. The role of a Blockchain designer is shaping a user interface that creates trust and is alluring to a \
regular user. These individuals need to be able to pay attention to detail, have an artistic touch, but most \
importantly they need to be hardworking as their line of work requires them to spend countless hours behind their \
computers.\n\n\
\U000026A1Blockchain Quality Engineer\n\
In any development environment, we have a quality assurance engineer who tests and ensures that all areas of the \
project are of the required quality. In the Blockchain world, a Blockchain engineer plays a similar role by \
guaranteeing that all operations are of excellence in the Blockchain development environment. In other words, they \
conduct the testing and automation of frameworks for Blockchain. These individuals need to have a third eye as far as \
payment to detail is concerned because a small mistake on their part affects everyone using their technology. \
Excellent communication skills would also go a long way in maintaining good work relationships.\n\n\
\U000026A1Blockchain Legal Consultant\n\
Of course, as organizations try to comprehend the adoption of Blockchain into their systems legal issues always arise. \
As companies launch this new technology, they are also looking for legal expertise on what considerations to make \
while investing. They are curious about the implications of their actions, about how to handle their finances, and \
lastly how to manage their identity. Of course, for such an individual, proper communication skills are mandatory. You \
also need to have a good grasp of your international law as Blockchain is tech without borders for the same reason it \
is advisable that such people master as many universal languages as they can.\n\n")
        elif networking_on:
            await message.answer("Job Roles differ from company to company. Here is a list of some common job \
roles:\n\n\n \
\U0001F5A7Network Engineer\n\
A network engineer designs and manages the groups of computers networked together. The network engineer performs tasks \
such as installing and configuring communication hardware, setting up of the network communication link, installing \
and configuring application software, troubleshooting operations to ensure continuous network availability, and \
offering technical support and assistance.\n\n\
\U0001F5A7Network Analyst\n\
Network analysts support the computer network and the overall computer infrastructure. Job duties might involve \
installing network software and training the user in new applications. The analyst might be responsible for \
coordinating system enhancements between the software and hardware, documenting procedures, and producing policies and \
procedures.\n\n\
\U0001F5A7Information Systems Administrator\n\
Information systems administrators assist with the design, delivery, and maintenance of an information technology \
infrastructure within the organization. The person assists in strategic planning and in evaluating and recommending \
services, products, and projects. The job involves assisting in the planning, development, implementation, and \
maintenance of the information platform. The information platform might include Web servers and services, \
technological applications, and interactive applications. Administrators also supply instruction, user aids, and \
assistance in problem solving for library IT applications.\n\n\
\U0001F5A7Network Technician\n\
The network technician generally services network computers and troubleshoots for potential problems. Network \
technicians often work the help-desk services to repair or upgrade computers. Technicians need to be familiar with the \
different operating systems such as Microsoft, Novell, and Unix, as well as the basics of computer networking. \n\n\
\U0001F5A7Computer Networking Instructor\n\
The increasing use of computer networks has created a need for more instructors who have a solid networking background \
and can teach those skills to students. Unlike in some other academic fields, one need not have a doctoral degree in \
computer networking to be a computer networking instructor. Although community colleges and four-year schools might \
prefer instructors to have a master’s degree, for-profit and certification schools usually only require substantial \
experience in the profession. It is also a way to remain a working professional while supplementing an income and \
contributing to the growth of the profession. \n\n")

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
        elif blockchain_on:
            blockchain_on = False
            await message.answer("Back", reply_markup=guides_menu_keyboard)
        elif networking_on:
            networking_on = False
            await message.answer("Back", reply_markup=guides_menu_keyboard)    
        else:
            await message.answer("Back", reply_markup=top_menu_keyboard)
    elif message.text == "Main Menu":
        await message.answer("Main Menu", reply_markup=top_menu_keyboard)
    else:
        await message.reply("Not a recognized command, select one of the buttons")


executor.start_polling(dp)
