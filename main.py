from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

API_KEY = "2142160935:AAEGjTuZrHdNmLrGwVimS_OLs-qSfV-fd6c"

bot = Bot(token=API_KEY)
dp = Dispatcher(bot)

what_is_bot_button = KeyboardButton("\U0001F937 What is CSGuider Bot? \U0001F937")
why_we_created_bot_button = KeyboardButton("\U0001F914 Why we created this bot? \U0001F914")
important_note_button = KeyboardButton("\U00002757\U00002757Important Note\U00002757\U00002757")
go_to_guides_button = KeyboardButton("\U0001F4DA\U0001F4DA Go to Guides \U0001F4DA\U0001F4DA")

top_menu_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(what_is_bot_button)
top_menu_keyboard.add(why_we_created_bot_button)
top_menu_keyboard.add(important_note_button)
top_menu_keyboard.add(go_to_guides_button)

ai_and_ml_button = KeyboardButton("\U00002699 AI and ML Guide \U00002699")
cyber_security_button = KeyboardButton("\U0001F3AD Cyber Security Guide \U0001F3AD")
game_development_button = KeyboardButton("\U0001F3AE Game Development Guide \U0001F3AE")
software_development_keyboard = KeyboardButton("\U0001F5A5 Software Development Guide \U0001F5A5")
blockchain_button = KeyboardButton("\U0001F517 Blockchain Guide \U0001F517")
cloud_computing_button = KeyboardButton("\U00002601 Cloud Computing Guide \U00002601")
networking_button = KeyboardButton("\U0001F4F6 Networking Guide \U0001F4F6")
graphic_designing_button = KeyboardButton("\U0001F5BC Graphic Designing Guide \U0001F5BC")
data_science_button = KeyboardButton("\U0001F4CA Data Science Guide \U0001F4CA")
robotics_and_hardware_button = KeyboardButton("\U0001F916 Robotics and Hardware Guide \U0001F916")
web_development_button = KeyboardButton("\U0001F310 Web Development Guide \U0001F310")
front_end_development_button = KeyboardButton("\U00002B06 Front-End Web Development Guide \U00002B06")
back_end_development_button = KeyboardButton("\U00002B07 Back-End Web Development Guide \U00002B07")
full_stack_development_button = KeyboardButton("\U00002195 Full Stack Web Development Guide \U00002195")
application_development_button = KeyboardButton("\U0001F4BB Application Development Guide \U0001F4BB")
android_development_button = KeyboardButton("\U0001F4F1 Android App Development Guide \U0001F4F1")
ios_development_button = KeyboardButton("\U0001F4F2 IOS App Development Guide \U0001F4F2")
desktop_development_button = KeyboardButton("\U0001F5A5 Desktop App Development Guide \U0001F5A5")
back_button = KeyboardButton("\U0001F519 Back")
back_to_top_menu_button = KeyboardButton("\U0001F51D Main Menu")

guides_menu_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(ai_and_ml_button, cyber_security_button)
guides_menu_keyboard.add(game_development_button, software_development_keyboard)
guides_menu_keyboard.add(blockchain_button, cloud_computing_button)
guides_menu_keyboard.add(networking_button, graphic_designing_button)
guides_menu_keyboard.add(data_science_button, robotics_and_hardware_button)
guides_menu_keyboard.add(back_button, back_to_top_menu_button)

skills_required_button = KeyboardButton("\U0001F530 Skills Required")
courses_button = KeyboardButton("\U0001F4BB Courses")
books_button = KeyboardButton("\U0001F4D6 Books")
certifications_button = KeyboardButton("\U0001F3C5 Certifications")
degrees_button = KeyboardButton("\U0001F393 Degrees")
jobs_button = KeyboardButton("\U0001F935 Jobs")
certifications_degrees_button = KeyboardButton("\U0001F393 Certifications/Degrees")

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

graphic_designing_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(skills_required_button, courses_button)
graphic_designing_keyboard.add(books_button, certifications_button)
graphic_designing_keyboard.add(degrees_button, jobs_button)
graphic_designing_keyboard.add(back_button, back_to_top_menu_button)

cloud_computing_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(skills_required_button, courses_button)
cloud_computing_keyboard.add(books_button, certifications_button)
cloud_computing_keyboard.add(degrees_button, jobs_button)
cloud_computing_keyboard.add(back_button, back_to_top_menu_button)

software_development_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(web_development_button)
software_development_keyboard.add(application_development_button)
software_development_keyboard.add(back_button, back_to_top_menu_button)

web_development_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(front_end_development_button)
web_development_keyboard.add(back_end_development_button)
web_development_keyboard.add(full_stack_development_button)
web_development_keyboard.add(back_button, back_to_top_menu_button)

application_development_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(android_development_button)
application_development_keyboard.add(ios_development_button)
application_development_keyboard.add(desktop_development_button)
application_development_keyboard.add(back_button, back_to_top_menu_button)

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


@dp.message_handler(commands=['start', 'help'])
async def welcome(message: types.Message):
    if message.is_command():
        await message.reply("Hello, Welcome to CSGuider Bot", reply_markup=top_menu_keyboard)
    else:
        await message.reply(message.text + " is not a recognized command, please enter /start")


@dp.message_handler()
async def main_keyboard_answer(message: types.Message):

    global ai_and_ml_on, cyber_security_on, game_development_on, software_development_on, blockchain_on, \
        cloud_computing_on, networking_on, graphic_designing_on, data_science_on, robotics_and_hardware_on, \
        web_development_on, front_end_development_on, back_end_development_on, full_stack_development_on, \
        application_development_on, android_development_on, ios_development_on, desktop_development_on

    if message.text == "\U0001F937 What is CSGuider Bot? \U0001F937":
        await message.answer("\U0001F4BB CSGuiderBot\n\n\n\
\U0001F4BB What is CSGuider Bot?\n\n\
CSGuider is a comprehensive guide to specialization within the Computer Science field.\n\n\
It is aimed at providing students with a list of possible opportunities within the Computer Science field along with \
providing them with resources related to these specialization fields with the help of a responsive UI.\n\n\
\U0001F4BB The following resources are included in the CSGuider Bot:\n\
\U0001F537Skills Required \n\
\U0001F537Courses\n\
\U0001F537Books\n\
\U0001F537Degrees\n\
\U0001F537Certifications\n\
\U0001F537Job Opportunities\n\n\
All these features are conveniently packed into an easy to use and interactive Telegram Bot ")

    elif message.text == "\U0001F914 Why we created this bot? \U0001F914":
        pass

    elif message.text == "\U00002757\U00002757Important Note\U00002757\U00002757":
        pass

    elif message.text == "\U0001F4DA\U0001F4DA Go to Guides \U0001F4DA\U0001F4DA":
        await message.answer("Guides", reply_markup=guides_menu_keyboard)

    elif message.text == "\U00002699 AI and ML Guide \U00002699":
        ai_and_ml_on = True
        await message.answer("\U00002699 AI and ML Guide \U00002699", reply_markup=ai_and_ml_keyboard)

    elif message.text == "\U0001F3AD Cyber Security Guide \U0001F3AD":
        cyber_security_on = True
        await message.answer("\U0001F3AD Cyber Security Guide \U0001F3AD", reply_markup=cyber_security_keyboard)

    elif message.text == "\U0001F3AE Game Development Guide \U0001F3AE":
        game_development_on = True
        pass

    elif message.text == "\U0001F5A5 Software Development Guide \U0001F5A5":
        software_development_on = True
        await message.answer("\U0001F5A5 Software Development Guide \U0001F5A5",
                             reply_markup=software_development_keyboard)
    elif message.text == "\U0001F310 Web Development Guide \U0001F310":
        web_development_on = True
        await message.answer("\U0001F310 Web Development Guide \U0001F310", reply_markup=web_development_keyboard)
    elif message.text == "\U00002B06 Front-End Web Development Guide \U00002B06":
        front_end_development_on = True
        # await message.answer("\U00002B06 Front-End Web Development Guide \U00002B06", reply_markup=front_end_development_keyboard)
        pass
    elif message.text == "\U00002B07 Back-End Web Development Guide \U00002B07":
        back_end_development_on = True
        # await message.answer("\U00002B07 Back-End Web Development Guide \U00002B07", reply_markup=back_end_development_keyboard)
        pass
    elif message.text == "\U00002195 Full Stack Web Development Guide \U00002195":
        full_stack_development_on = True
        # await message.answer("\U00002195 Full Stack Web Development Guide \U00002195", reply_markup=full_stack_development_keyboard)
        pass
    elif message.text == "\U0001F4BB Application Development Guide \U0001F4BB":
        application_development_on = True
        await message.answer("\U0001F4BB Application Development Guide \U0001F4BB",
                             reply_markup=application_development_keyboard)
    elif message.text == "\U0001F4F1 Android App Development Guide \U0001F4F1":
        android_development_on = True
        # await message.answer("\U0001F4F1 Android App Development Guide \U0001F4F1", reply_markup=android_development_keyboard)
        pass
    elif message.text == "\U0001F4F2 IOS App Development Guide \U0001F4F2":
        ios_development_on = True
        # await message.answer("\U0001F4F2 IOS App Development Guide \U0001F4F2", reply_markup=ios_development_keyboard)
        pass
    elif message.text == "\U0001F5A5 Desktop App Development Guide \U0001F5A5":
        desktop_development_on = True
        # await message.answer("\U0001F5A5 Desktop App Development Guide \U0001F5A5", reply_markup=desktop_development_keyboard)
        pass

    elif message.text == "\U0001F517 Blockchain Guide \U0001F517":
        blockchain_on = True
        await message.answer("\U0001F517 Blockchain Guide \U0001F517", reply_markup=blockchain_keyboard)

    elif message.text == "\U00002601 Cloud Computing Guide \U00002601":
        cloud_computing_on = True
        await message.answer("\U00002601 Cloud Computing Guide \U00002601", reply_markup=cloud_computing_keyboard)

    elif message.text == "\U0001F4F6 Networking Guide \U0001F4F6":
        networking_on = True
        await message.answer("\U0001F4F6 Networking Guide \U0001F4F6", reply_markup=networking_keyboard)

    elif message.text == "\U0001F5BC Graphic Designing Guide \U0001F5BC":
        graphic_designing_on = True
        await message.answer("Graphic Designing", reply_markup=graphic_designing_keyboard)

    elif message.text == "\U0001F4CA Data Science Guide \U0001F4CA":
        data_science_on = True
        pass

    elif message.text == "\U0001F916 Robotics and Hardware Guide \U0001F916":
        robotics_and_hardware_on = True
        pass

    elif message.text == "\U0001F530 Skills Required":
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
hackers and spyware.\n\n\
\U00002666 Cryptography Skills\n\
Cryptography is the study and application of techniques for reliable communication in the presence of third parties \
called adversaries. Cryptography deals with converting a normal text/message known as plain text to a non-readable \
form known as ciphertext during the transmission to make it incomprehensible to hackers.\n\n\
\U00002666 Database Skills\n\
DBMS is the crux of creating and managing all databases. Accessing a database where all the information is stored \
can put the company in a tremendous threat, so ensuring that this software is hack-proof is important.\n\n\
\U00002666 Problem-solving Skills\n\
Apart from the technical skills pointed above, an ethical hacker also must be a critical thinker and dynamic \
problem solver. They must be wanting to learn new ways and ensure all security breaches are thoroughly checked.")
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
\U0001F5A7 Internet\n\
Internet is a worldwide virtual networking medium that connects computers all across the world. Net is short for the \
internet and has millions of smaller networks that carry a huge array of information.\n\n\
\U0001F5A7 Linux\n\
Linux is a Unix-like operating system. Just like Windows, Mac OS, and IOS, Linux is an operating system used by \
millions across the globe. Android itself is powered by the Linux operating system. \n\n\
\U0001F5A7 Ethernet\n\
Ethernet refers to a system that connects a series of computers in a local area network (LAN). This is often done \
through ethernet cables, which plug into a router or other port in the modem in addition to the computer port.\n\n\
\U0001F5A7 Network Security\n\
Here's how network security is used on computer network engineer resumes:\n\
Create and enforce network security policy.\n\
Analyzed data network documentation and assisted in communicating to management regarding the current operational \
status of networks.\n\
Appointed to Boundary Protection Technician, providing network security and monitoring firewall; opened firewall ports \
on case-by-case basis.\n\n\
\U0001F5A7 Assurance\n\
Here's how assurance is used on computer network engineer resumes:\n\
Performed information assurance vulnerability assessments on more than 12 ships.\n\
Implemented Information Assurance controls to ensure all resident information systems were safe and secure.\n\n\
\U0001F5A7 Hardware\n\
Hardware is the physical part attached to a computer or other similar devices. Components are the internal parts of \
hardware which include RAM, hard drives, motherboard, and so on. External hardware devices which include, keyboard, \
mouse, printer, and so on are known as peripherals. All of these together are called computer hardware.\n\n")
        elif graphic_designing_on:
            await message.answer("Some skills required to get into GRaphics Design are as follows:\n\n\n \
\U0001F58C 3D Design\n\
3D design is the process of using software to create a mathematical representation of a 3-dimensional object or shape. \
The created object is called a 3D model and these 3-dimensional models are used for computer-generated (CG) design. 3D \
design is used in a variety of industries to help artists shape, communicate, document, analyse and share their \
ideas.\n\n\
\U0001F58C Digital Illustration (Adobe Illustrator)\n\
Illustrator is widely used by graphic designers, web designers, visual artists, and professional illustrators \
throughout the world to create high quality artwork. Illustrator includes many sophisticated drawing tools that \
can reduce the time need to create illustrations.\n\n\
\U0001F58C Adobe Photoshop \n\
Learning Photoshop for graphic design is an essential skill for anyone working or wanting to work in graphic design. \
Photoshop is the standard digital tool used a wide variety of graphic design roles, including print, web and \
interactive design, as well as video. Those looking to start a career in graphic design will need to learn Photoshop, \
but this is simply one step in the process of becoming a graphic designer. Learning Photoshop alone is not enough to \
become a graphic designer.\n\n\
\U0001F58C Logo Design \n\
Designers know the importance of a great first impression, which is why graphic designer logos are some of the most \
creative and compelling logos out there. At a glance, the right logo builds trust in your design skills and sets you \
apart from the competition. \n\n\
\U0001F58C Typography \n\
Graphic designers use typography to adjust the text within the design. This helps in creating content with a purpose. \
The planned use of typefaces allows the designers to make a design look aesthetic and pleasing. The designers have \
been using typefaces strategically to make a text readable and also to make an impression on viewers. Because of such \
designs with unique typography ideas, a brand can communicate with its audience in an effective way.\n\n\
\U0001F58C Vector Graphics\n\
Vector graphics are computer images created using a sequence of commands or mathematical statements that place lines \
and shapes in a two-dimensional or three-dimensional space. In vector graphics, a graphic artist's work, or file, is \
created and saved as a sequence of vector statements. A vector graphic file describes a series of points to be \
connected. \n\n")
        elif cloud_computing_on:
            await message.answer("Some skills required to get into Cloud Computing are as follows:\n\n\n \
\U00002666 Understanding the Linux OS\n \
The first and foremost thing is to get good hands-on on a Linux operating system. Practicing Linux would help you \
as a cloud engineer, or as a cloud architect, you should have this fundamental understanding of your operating \
system. This can be as simple as installing a virtual machine using VirtualBox or to create a VM in a cloud \
environment. Some more complex commands can include installing various software, carrying out load analysis, \
installing packages, or even modifying them. \n\n\
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
cloud. Therefore learning Docker or Kubernetes will give a good push towards being a good cloud engineer.\n\n\
\U00002666 Understanding Virtualization\n\
This means not depending upon personal individual hardware that faces problems when scaling but rather running \
application software on virtual machines. This reduces the hardware dependency and also aids in fault tolerance, \
making it one of the most desirable skills of a cloud engineer. Examples include AWS EC2 (Elastic Compute) and \
AWS Lambda.\n\n\
\U00002666 Cloud Service Providers\n\
There are many cloud service vendors that offer storage, database, compute machine learning, and migration services \
but AWS is the leader being closely followed by Microsoft’s Azure. Knowing how different cloud providers work and \
ship resources to their clients will help you understand cloud computing in detail and familiarize you with the \
best practices to follow. Other cloud providers include Google’s GCP, IBM, and OpenStack.\n\n\
\U00002666 Security and Recovery\n\
Cloud security is one of the most difficult subdomains in the cloud since it involves critical measures to be taken \
when there is a data breach or disaster recovery. It demands advanced skills in cybersecurity and cloud combined \
since any time the cloud resources are down, it can result in huge losses and unavailability of services to the \
client thereby affecting their business in turn.\n\n\
\U00002666 Web Services and API\n\
Cloud infrastructure is heavily based upon APIs and web services for the integration of applications on the \
internet. Some examples are XML, SOAP, WSDL, and other open standards are used to transfer and describe data \
and list services available. Gaining an understanding of these fundamentals can help you in your journey in \
the cloud.")

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
\U000026A1 Blockchain and Bitcoin Fundamentals\n\
https://www.udemy.com/course/blockchain-and-bitcoin-fundamentals/\n\n\
\U000026A1 Bitcoin and Cryptocurrency Bootcamp\n\
https://www.udemy.com/course/bitcoin-and-cryptocurrency-bootcamp/\n\n\
\U000026A1 Blockchain Specialization - University of California, Irvine(certified course)\n\
https://www.coursera.org/specializations/uci-blockchain\n\n\
\U000026A1 Blockchain Tutorial For Beginners\n\
https://www.youtube.com/playlist?list=PLsyeobzWxl7oY6tZmnZ5S7yTDxyu4zDW-\n\n\
\U000026A1 ETHEREUM DEVELOPMENT TUTORIALS\n\
https://ethereum.org/en/developers/tutorials/\n\n\
\U000026A1 Ethereum Tutorial\n\
https://www.tutorialspoint.com/ethereum/index.htm \n\n")
        elif networking_on:
            await message.answer("List of some courses and programs for Networking:\n\n\n \
\U0001F5A7 Networking Essentials \n\
https://www.netacad.com/courses/networking/networking-essentials\n\n\
\U0001F5A7 CCNA: Introduction to Networks\n\
https://www.netacad.com/courses/networking/ccna-introduction-networks\n\n\
\U0001F5A7 Introduction to networking for complete beginners\n\
https://www.udemy.com/course/introduction-to-networking-for-complete-beginners/\n\n\
\U0001F5A7 The Complete Networking Fundamentals Course. Your CCNA start\n\
https://www.udemy.com/course/complete-networking-fundamentals-course-ccna-start/\n\n\
\U0001F5A7 Computer Networks\n\
https://www.youtube.com/playlist?list=PLBlnK6fEyqRgMCUAG0XRw78UA8qnv6jEx \n\n")
        elif graphic_designing_on:
            await message.answer("List of some courses and programs for Graphics Design:\n\n\n \
\U0001F58C Graphic Design Bootcamp: Photoshop, Illustrator, InDesign\n\
https://www.udemy.com/course/graphic-design-for-beginners/\n\n\
\U0001F58C Graphic Design Masterclass: Learn Graphic Design in Projects\n\
https://www.udemy.com/course/graphic-design/\n\n\
\U0001F58C Graphic Design Masterclass: Learn Graphic Design in Projects\n\
https://www.udemy.com/course/become-a-professional-logo-designer/ \n\n\
\U0001F58C Beginners Guide to Graphic Design | 45 Episode FREE Series \n\
https://www.youtube.com/watch?v=WONZVnlam6U&list=PLYfCBK8IplO4E2sXtdKMVpKJZRBEoMvpn \n\n\
\U0001F58C Graphics Design Skill Share\n\
https://www.skillshare.com/browse/graphic-design\n\n\
\U0001F58C Graphic Design Specialization -  Certified Course by CalArts\n\
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
\U000026A1 The Book of Satoshi:\n\
The Collected Writings of Bitcoin Creator Satoshi Nakamoto\n\
https://www.amazon.in/Book-Satoshi-Collected-Writings-Nakamoto-ebook/dp/B00M6KGJ2K\n\n\
\U000026A1 Decentralized Applications:\n\
Harnessing Bitcoin’s Blockchain Technology\n\
https://www.amazon.in/Decentralized-Applications-Siraj-Raval/dp/1491924543\n\n\
\U000026A1 Mastering Blockchain Programming with Solidity:\n\
Write Production-ready Smart Contracts for Ethereum Blockchain with Solidity\n\
https://www.amazon.in/Mastering-Blockchain-Programming-Solidity-production-ready-ebook/dp/B07W5F8S1L\n\n\
\U000026A1 Mastering Bitcoin:\n\
Programming the Open Blockchain\n\
https://www.amazon.in/Mastering-Bitcoin-Programming-Open-Blockchain/dp/9352135741\n\n\
\U000026A1 Hands-On Blockchain for Python Developers:\n\
Gain blockchain programming skills to build decentralized applications using Python\n\
https://www.amazon.in/Hands-Blockchain-Python-Developers-decentralized/dp/1788627857\n\n")
        elif networking_on:
            await message.answer("Some books to refer for Networking:\n\n\n \
\U0001F5A7 CompTIA Network+ Certification All-in-One Exam Guide\n\
https://www.amazon.in/dp/1260122387\n\n\
\U0001F5A7 Network Programmability and Automation\n\
https://www.amazon.in/dp/1491931256\n\n\
\U0001F5A7 Computer Networking: A Top-Down Approach\n\
https://www.amazon.in/dp/0133594149\n\n\
\U0001F5A7 Computer Networks\n\
https://www.amazon.in/Computer-Networks-5e-5th-Tanenbaum/dp/9332518742\n\n")
        elif graphic_designing_on:
            await message.answer("Some books to refer for Graphics Design:\n\n\n\
\U0001F58C Logo Modernism\n\
https://www.amazon.in/dp/3836545306\n\n\
\U0001F58C The Elements of Typographic Style (v4)\n\
https://www.amazon.in/dp/0881792128\n\n\
\U0001F58C How to be a Graphic Designer Without Losing Your Soul\n\
https://www.amazon.in/dp/1856697096\n\n\
\U0001F58C Graphic Design for Art, Fashion, Film, Architecture, Photography, Product Design and Everything in Between \n\
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
\U000026A1 Certified Blockchain Expert -  Blockchain Council\n\
https://www.blockchain-council.org/certifications/certified-blockchain-professional-expert/\n\n\
\U000026A1 Certified Ethereum Expert - Blockchain Council\n\
https://www.blockchain-council.org/certifications/certified-ethereum-expert-cee/\n\n\
\U000026A1 Certified Blockchain Professional - EC Council\n\
https://www.eccouncil.org/programs/certified-blockchain-professional-cbp/\n\n\
\U000026A1 Certified Enterprise Blockchain Architect (CEBA) - 101 Blockchains\n\
https://academy.101blockchains.com/courses/certified-enterprise-blockchain-architect\n\n\
\U000026A1 Blockchain Technology — EdX\n\
https://www.edx.org/professional-certificate/uc-berkeleyx-blockchain-fundamentals\n\n\
\U000026A1 Certified Blockchain Developer — Educative\n\
https://www.educative.io/courses/hands-on-blockchain-hyperledger-fabric\n\n")
        elif networking_on:
            await message.answer("Certifications that will help boost your career:\n\n\n\
\U0001F5A7 CompTIA IT Fundamentals (ITF+)\n\
https://www.comptia.org/certifications/network\n\n\
\U0001F5A7 Cisco Certified Network Associate (CCNA)\n\
https://www.cisco.com/c/en/us/training-events/training-certifications/certifications/associate/ccna.html\n\n\
\U0001F5A7 Cisco Certified Network Professional (CCNP) Enterprise:\n\
https://www.cisco.com/c/en/us/training-events/training-certifications/certifications/professional/ccnp-enterprise.\
html\n\n\
\U0001F5A7 Cisco Certified Internetwork Expert (CCIE) Enterprise Infrastructure\n\
https://www.cisco.com/c/en/us/training-events/training-certifications/certifications/expert/ccie-enterprise-\
infrastructure.html\n\n\
\U0001F5A7 VMWare Certified Technical Associate - Network Virtualization (VCTA-NV)\n\
https://www.vmware.com/education-services/certification/vcta-nv.html\n\n\
\U0001F5A7 Juniper Networks Certified Associate - Junos (JNCIA-Junos)\n\
https://www.juniper.net/us/en/training/certification.html \n\n")
        elif graphic_designing_on:
            await message.answer("Certifications that will help boost your career:\n\n\n\
\U0001F58C Adobe Certified Associate in Graphic Design and Illustration\n\
https://edex.adobe.com/teaching-resources/v770dfc88\n\n\
\U0001F58C Visual Design Using Adobe Photoshop\n\
https://edex.adobe.com/teaching-resources/v97ccf4fe\n\n\
\U0001F58C Print and Digital Media Publication Using Adobe InDesign\n\
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
\U000026A1 Top 5 Universities for Blockchain Degrees(international)\n\
https://www.stoodnt.com/blog/top-5-universities-for-blockchain-degrees/\n\n\
\U000026A1 Masters Programs in Blockchain in Europe 2022\n\
https://www.masterstudies.com/Masters-Degree/Blockchain/Europe/\n\n\
\U000026A1 Advanced Certification in Software Engineering for Cloud, Blockchain & IoT - IIT: B\n\
https://www.greatlearning.in/iit-madras-acse \n\n")
        elif networking_on:
            await message.answer("Possible Networking based degrees:\n\n\n\
\U0001F5A7 Bachelor Programs in Computer Networking(international)\n\
https://www.bachelorstudies.com/Bachelor/Computer-Networking/\n\n\
\U0001F5A7 Bachelor Network Courses(India)\n\
https://collegedunia.com/courses/network#6\n\n\
M.E. (Computer Networking) Colleges in India\n\
https://targetstudy.com/colleges/me-computer-networking-degree-colleges-in-india.html\n\n\
Networking Colleges in India - 2022\n\
https://www.shiksha.com/it-software/networking-hardware-security/colleges/colleges-india \n\n")
        elif graphic_designing_on:
            await message.answer("Possible Graphic Design based degrees:\n\n\n\
\U0001F58C Bachelor Programs in Graphic Design(international)\n\
https://www.bachelorstudies.com/Bachelor/Graphic-Design/\n\n\
\U0001F58C BA in Graphics Design(India)\n\
https://www.collegedekho.com/courses/ba-graphic-design/\n\n\
\U0001F58C Masters Programs in Graphic Design(international)\n\
https://www.masterstudies.com/Masters-Degree/Graphic-Design/\n\n\
\U0001F58C Master of Arts [M.A.] in Graphic Design\n\
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
\U000026A1 Blockchain Developer\n\
Blockchain developers with the expertise to help companies explore Blockchain platforms are in high demand. Blockchain \
development might be the most marketable career path today because people are eager to realize all the benefits of \
Blockchain. These individuals require absolute attention to detail as theirs is a high ranking position. Blockchain \
developers are programmers who create applications for blockchain. They typically have a lot of experience working \
with C++, Python, and Javascript before becoming Blockchain developers.\n\n\
\U000026A1 Blockchain Solution Architect\n\
The Blockchain Solution Architect has the responsibility of designing, assigning, and connecting Blockchain solution \
components with the team experts such as developers, network administrators, UX designers, and IT Operations whose to \
develop to complete the Blockchain solutions.\n\n\
\U000026A1 Blockchain Project Manager\n\
This individual is entrusted with the responsibility of connecting Blockchain projects to experts whose duty it is to \
develop Blockchain solutions. Blockchain project managers need to be equipped with the skills of a traditional (cloud) \
project manager. They also need to master the technical bit to understand the technology thoroughly. Another important \
ability is excellent communication skills; this is essential when addressing non-technical workers, when providing \
useful updates or when trying to get resources from higher authorities.\n\n\
\U000026A1 Blockchain UX Designer\n\
With the incorporation of Blockchain into so many industries, its design as well as user interface, is becoming \
critical. The role of a Blockchain designer is shaping a user interface that creates trust and is alluring to a \
regular user. These individuals need to be able to pay attention to detail, have an artistic touch, but most \
importantly they need to be hardworking as their line of work requires them to spend countless hours behind their \
computers.\n\n\
\U000026A1 Blockchain Quality Engineer\n\
In any development environment, we have a quality assurance engineer who tests and ensures that all areas of the \
project are of the required quality. In the Blockchain world, a Blockchain engineer plays a similar role by \
guaranteeing that all operations are of excellence in the Blockchain development environment. In other words, they \
conduct the testing and automation of frameworks for Blockchain. These individuals need to have a third eye as far as \
payment to detail is concerned because a small mistake on their part affects everyone using their technology. \
Excellent communication skills would also go a long way in maintaining good work relationships.\n\n\
\U000026A1 Blockchain Legal Consultant\n\
Of course, as organizations try to comprehend the adoption of Blockchain into their systems legal issues always arise. \
As companies launch this new technology, they are also looking for legal expertise on what considerations to make \
while investing. They are curious about the implications of their actions, about how to handle their finances, and \
lastly how to manage their identity. Of course, for such an individual, proper communication skills are mandatory. You \
also need to have a good grasp of your international law as Blockchain is tech without borders for the same reason it \
is advisable that such people master as many universal languages as they can.\n\n")
        elif networking_on:
            await message.answer("Job Roles differ from company to company. Here is a list of some common job \
roles for networking:\n\n\n \
\U0001F5A7 Network Engineer\n\
A network engineer designs and manages the groups of computers networked together. The network engineer performs tasks \
such as installing and configuring communication hardware, setting up of the network communication link, installing \
and configuring application software, troubleshooting operations to ensure continuous network availability, and \
offering technical support and assistance.\n\n\
\U0001F5A7 Network Analyst\n\
Network analysts support the computer network and the overall computer infrastructure. Job duties might involve \
installing network software and training the user in new applications. The analyst might be responsible for \
coordinating system enhancements between the software and hardware, documenting procedures, and producing policies and \
procedures.\n\n\
\U0001F5A7 Information Systems Administrator\n\
Information systems administrators assist with the design, delivery, and maintenance of an information technology \
infrastructure within the organization. The person assists in strategic planning and in evaluating and recommending \
services, products, and projects. The job involves assisting in the planning, development, implementation, and \
maintenance of the information platform. The information platform might include Web servers and services, \
technological applications, and interactive applications. Administrators also supply instruction, user aids, and \
assistance in problem solving for library IT applications.\n\n\
\U0001F5A7 Network Technician\n\
The network technician generally services network computers and troubleshoots for potential problems. Network \
technicians often work the help-desk services to repair or upgrade computers. Technicians need to be familiar with the \
different operating systems such as Microsoft, Novell, and Unix, as well as the basics of computer networking. \n\n\
\U0001F5A7 Computer Networking Instructor\n\
The increasing use of computer networks has created a need for more instructors who have a solid networking background \
and can teach those skills to students. Unlike in some other academic fields, one need not have a doctoral degree in \
computer networking to be a computer networking instructor. Although community colleges and four-year schools might \
prefer instructors to have a master’s degree, for-profit and certification schools usually only require substantial \
experience in the profession. It is also a way to remain a working professional while supplementing an income and \
contributing to the growth of the profession. \n\n")
        elif graphic_designing_on:
            await message.answer("Job Roles differ from company to company. Here is a list of some common job \
roles for graphic designing:\n\n\n \
\U0001F58C Graphic designer\n\
Graphic designers develop graphics and layouts for product illustrations, company logos, websites and more. This job \
title can cover a huge range of duties in a huge range of industries.\n\n\
\U0001F58C Creative director\n\
Creative directors determine the creative vision of a project. They make sure the overall aesthetic and cohesive look \
stays on track by leading their team through the steps to create something, whether that is a tangible product like a \
video game, film, magazine or something more abstract like an advertising campaign or brand identity.\n\n\
\U0001F58C User experience (UX) designer\n\
UX designers work to make products, processes and services seamless, enjoyable and intuitive for users. They think \
about how the product feels, how users will use it. They ensure the product flows from one step to the next. UX \
designers might run user tests, refining any bumps or confusions in the process. This career involves tons of \
out-of-the-box thinking, creative intuition and a natural appreciation for smooth design.\n\n\
\U0001F58C User interface (UI) designer\n\
UI design is often considered a subset of UX design and has similar overall goals. User interface designers focus on \
how the product is laid out. They design each screen and each page, ensuring that the layout visually works with the \
overall path a UX designer has charted.\n\n\
\U0001F58C Production artist\n\
Production artists take over the hands-on steps of production—whether that’s in graphics, film, art or other formats. \
They upload and ensure the accuracy of design files throughout the last stages of development. The job is equal parts \
design and computer applications skill.\n\n\
\U0001F58C Product developer\n\
Product developers ideate, lead and manage the creation of products. They can work on so many different things that \
their job duties will vary widely, but general tasks include performing industry research, creating illustrations, \
presenting the product to employers or stakeholders and contributing to the development process.\n\n\
\U0001F58C Art director\n\
Art directors take charge of the visual style and content in magazines, newspapers, product packaging and movie and \
television productions. They create design and direct other artists to develop each contributing piece. They work \
closely with their employers or clients to cast an artistic vision that meets objectives, the available budget and \
desired impact.\n\n\
\U0001F58C Marketing specialist\n\
Marketing specialists collect and analyze data on target customers, initiate marketing campaigns, measure \
effectiveness of marketing attempts and create strategies to promote their company and its goods or services.\n\n\
\U0001F58C Multimedia artist or animator\n\
Multimedia artists and animators design complex graphics and animation using computer animation or modeling programs. \
They think about story development, visual impact and platforms to create media content that will meet their \
employer’s objectives. More brands and organizations are looking to increase their online video presence—and that’s \
been a boon for graphic designers with animation and motion graphics skills.\n\n\
\U0001F58C Freelancer\n\
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

    elif message.text == "\U0001F393 Certifications/Degrees":
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
        elif full_stack_development_on and web_development_on and software_development_on:
            full_stack_development_on = False
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
        elif desktop_development_on and application_development_on and software_development_on:
            desktop_development_on = False
            await message.answer("\U0001F519 Back", reply_markup=application_development_keyboard)
        elif application_development_on and software_development_on:
            application_development_on = False
            await message.answer("\U0001F519 Back", reply_markup=software_development_keyboard)
        elif software_development_on:
            software_development_on = False
            await message.answer("\U0001F519 Back", reply_markup=guides_menu_keyboard)
        else:
            await message.answer("\U0001F519 Back", reply_markup=top_menu_keyboard)
           
    elif message.text == "\U0001F51D Main Menu":
        await message.answer("\U0001F51D Main Menu", reply_markup=top_menu_keyboard)
    else:
        await message.reply("\U0000274C Not a recognized command\n\nSelect one of the buttons or enter \
/start to reload the bot")


executor.start_polling(dp)
