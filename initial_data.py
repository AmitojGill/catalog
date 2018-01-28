# This Python file uses the following encoding: utf-8
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Categories, Items

engine = create_engine('sqlite:///catalog.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()


category1 = Categories(name="Business")

session.add(category1)
session.commit()

item1 = Items(name="Crushing It!",
				description="In his 2009 international bestseller Crush It, Gary insisted that a vibrant personal brand was crucial to entrepreneurial success, In Crushing It!, Gary explains why that\’s even more true today, offering his unique perspective on what has changed and what principles remain timeless.",
				img= "https://goo.gl/4HkuKC",
				buy="https://goo.gl/92b2gx",
				category=category1)
session.add(item1)
session.commit()

item2 = Items(name="Tribe of Mentors",
				description="Tim Ferriss, the #1 New York Times best-selling author of The 4-Hour Workweek, shares the ultimate choose-your-own-adventure book—a compilation of tools, tactics, and habits from 130+ of the world's top performers. From iconic entrepreneurs to elite athletes, from artists to billionaire investors, their short profiles can help you answer life\'s most challenging questions, achieve extraordinary results, and transform your life.",
				img= "https://goo.gl/chXm4v",
				buy="https://goo.gl/E4NceU",
				category=category1)
session.add(item2)
session.commit()

item3 = Items(name="Outliers",
				description="In this stunning new book, Malcolm Gladwell takes us on an intellectual journey through the world of \'outliers\'--the best and the brightest, the most famous and the most successful. He asks the question: what makes high-achievers different?",
				img= "https://goo.gl/5JNYdE",
				buy="https://goo.gl/9uYgHD",
				category=category1)
session.add(item3)
session.commit()

item4 = Items(name="The Compound Effect",
				description="No gimmicks. No Hyperbole. No Magic Bullet. The Compound Effect is based on the principle that decisions shape your destiny. Little, everyday decisions will either take you to the life you desire or to disaster by default. Darren Hardy, publisher of Success Magazine, presents The Compound Effect, a distillation of the fundamental principles that have guided the most phenomenal achievements in business, relationships, and beyond. This easy-to-use, step-by-step operating system allows you to multiply your success, chart your progress, and achieve any desire. If you\'re serious about living an extraordinary life, use the power of The Compound Effect to create the success you want.",
				img= "https://goo.gl/t7GhMP",
				buy="https://goo.gl/Zb4MsV",
				category=category1)
session.add(item4)
session.commit()

item5 = Items(name="Alibaba",
				description="In just a decade and half Jack Ma, a man who rose from humble beginnings and started his career as an English teacher, founded and built Alibaba into the second largest Internet company in the world. The company\'s $25 billion IPO in 2014 was the world’s largest, valuing the company more than Facebook or Coca Cola. Alibaba today runs the e-commerce services that hundreds of millions of Chinese consumers depend on every day, providing employment and income for tens of millions more. A Rockefeller of his age, Jack has become an icon for the country’s booming private sector, and as the face of the new, consumerist China is courted by heads of state and CEOs from around the world.",
				img= "https://goo.gl/5RE2Lp",
				buy="https://goo.gl/4obh5N",
				category=category1)
session.add(item5)
session.commit()

item6 = Items(name="Elon Musk",
				description="In Elon Musk: Tesla, SpaceX, and the Quest for a Fantastic Future, veteran technology journalist Ashlee Vance provides the first inside look into the extraordinary life and times of Silicon Valley\'s most audacious entrepreneur. Written with exclusive access to Musk, his family and friends, the book traces the entrepreneur\'s journey from a rough upbringing in South Africa to the pinnacle of the global business world. Vance spent over 40 hours in conversation with Musk and interviewed close to 300 people to tell the tumultuous stories of Musk\'s world-changing companies: PayPal, Tesla Motors, SpaceX and SolarCity, and to characterize a man who has renewed American industry and sparked new levels of innovation while making plenty of enemies along the way.",
				img= "https://goo.gl/F6WX4a",
				buy="https://goo.gl/oDX8Eq",
				category=category1)
session.add(item6)
session.commit()

category2 = Categories(name="Parenting & Relationships")

session.add(category2)
session.commit()

item7 = Items(name="How to Talk So Kids Will Listen & Listen So Kids Will Talk", 
				description="The ultimate \'parenting bible\' (The Boston Globe) with a new foreword—and available as an ebook for the first time—a timeless, beloved book on how to effectively communicate with your child from the #1 New York Times bestselling authors.", 
				img = "https://goo.gl/eb1w6j",
				buy = "https://goo.gl/rpzs53",
				category=category2)
session.add(item7)
session.commit()

item8 = Items(name="Mind in the Making: The Seven Essential Life Skills Every Child Needs",
				description="Families and Work Institute President Ellen Galinsky (Ask the Children, The Six Stages of Parenthood) presents a book of groundbreaking advice based on the latest research on child development.",
				img = "https://goo.gl/W5waLz",
				buy = "https://goo.gl/J4nGyg",
				category=category2)
session.add(item8)
session.commit()

item9 = Items(name="Einstein Never Used Flash Cards",
				description="In Einstein Never Used Flashcards highly credentialed child psychologists, Kathy Hirsh-Pasek, Ph.D., and Roberta Michnick Golinkoff, Ph.D., with Diane Eyer, Ph.D., offer a compelling indictment of the growing trend toward accelerated learning. It\'s a message that stressed-out parents are craving to hear: Letting tots learn through play is not only okay-it\'s better than drilling academics!",
				img = "https://goo.gl/r3E5xg",
				buy = "https://goo.gl/SSnjVz",
				category=category2)
session.add(item9)
session.commit()

item10 = Items(name="Simplicity Parenting",
				description="Today\'s busier, faster society is waging an undeclared war on childhood. With too much stuff, too many choices, and too little time, children can become anxious, have trouble with friends and school, or even be diagnosed with behavioral problems. Now internationally renowned family consultant Kim John Payne helps parents reclaim for their children the space and freedom that all kids need for their attention to deepen and their individuality to flourish.",
				img = "https://goo.gl/DoZ1mQ",
				buy = "https://goo.gl/NLWByq",
				category=category2)
session.add(item10)
session.commit()

item11 = Items(name="The 5 Love Languages",
				description="n the #1 New York Times bestseller The 5 Love Languages, you\'ll discover the secret that has transformed millions of relationships worldwide. Whether your relationship is flourishing or failing, Dr. Gary Chapman\'s proven approach to showing and receiving love will help you experience deeper and richer levels of intimacy with your partner—starting today.",
				img = "https://goo.gl/kPjUmD",
				buy = "https://goo.gl/QJfuom",
				category=category2)
session.add(item11)
session.commit()

item12 = Items(name="The Whole-Brain Child", 
				description="In this pioneering, practical book, Daniel J. Siegel, neuropsychiatrist and author of the bestselling Mindsight, and parenting expert Tina Payne Bryson offer a revolutionary approach to child rearing with twelve key strategies that foster healthy brain development, leading to calmer, happier children. The authors explain—and make accessible—the new science of how a child\'s brain is wired and how it matures. The “upstairs brain,” which makes decisions and balances emotions, is under construction until the mid-twenties. And especially in young children, the right brain and its emotions tend to rule over the logic of the left brain. No wonder kids throw tantrums, fight, or sulk in silence. By applying these discoveries to everyday parenting, you can turn any outburst, argument, or fear into a chance to integrate your child\'s brain and foster vital growth.",
				img = "https://goo.gl/XhJaC6",
				buy = "https://goo.gl/vqZaYU",
				category=category2)
session.add(item12)
session.commit()

item17 = Items(name="How Children Succeed", 
				description="Why do some children succeed while others fail? The story we usually tell about childhood and success is the one about intelligence: success comes to those who score highest on tests, from preschool admissions to SATs. But in How Children Succeed, Paul Tough argues that the qualities that matter more have to do with character: skills like perseverance, curiosity, optimism, and self-control.",
				img = "https://goo.gl/g9XP5s",
				buy = "https://goo.gl/rPehGG",
				category=category2)
session.add(item17)
session.commit()


category3 = Categories(name="History")

session.add(category3)
session.commit()

item13 = Items(name="Sapiens", 
				description="Dr. Harari also compels us to look ahead, because over the last few decades humans have begun to bend laws of natural selection that have governed life for the past four billion years. We are acquiring the ability to design not only the world around us, but also ourselves. Where is this leading us, and what do we want to become?",
				img = "https://goo.gl/wXoZgK",
				buy = "https://goo.gl/GrqWYx",
				category=category3)
session.add(item13)
session.commit()

item14 = Items(name="Homo Deus", 
				description="Over the past century humankind has managed to do the impossible and rein in famine, plague, and war. This may seem hard to accept, but, as Harari explains in his trademark style—thorough, yet riveting—famine, plague and war have been transformed from incomprehensible and uncontrollable forces of nature into manageable challenges. For the first time ever, more people die from eating too much than from eating too little; more people die from old age than from infectious diseases; and more people commit suicide than are killed by soldiers, terrorists and criminals put together. The average American is a thousand times more likely to die from binging at McDonalds than from being blown up by Al Qaeda.",
				img = "https://goo.gl/yjG2kj",
				buy = "https://goo.gl/zW1HeB",
				category=category3)
session.add(item14)
session.commit()

category4 = Categories(name="Science")

session.add(category4)
session.commit()

item15 = Items(name="Astrophysics for People in a Hurry", 
				description="What is the nature of space and time? How do we fit within the universe? How does the universe fit within us? There\'s no better guide through these mind-expanding questions than acclaimed astrophysicist and best-selling author Neil deGrasse Tyson.",
				img = "https://goo.gl/qwk8yf",
				buy = "https://goo.gl/TsH9dR",
				category=category4)
session.add(item15)
session.commit()

category5 = Categories(name="Health & Fitness")

session.add(category5)
session.commit()

item16 = Items(name="The Power of Habit", 
				description="In The Power of Habit, Pulitzer Prize–winning business reporter Charles Duhigg takes us to the thrilling edge of scientific discoveries that explain why habits exist and how they can be changed. Distilling vast amounts of information into engrossing narratives that take us from the boardrooms of Procter & Gamble to sidelines of the NFL to the front lines of the civil rights movement, Duhigg presents a whole new understanding of human nature and its potential. At its core, The Power of Habit contains an exhilarating argument: The key to exercising regularly, losing weight, being more productive, and achieving success is understanding how habits work. As Duhigg shows, by harnessing this new science, we can transform our businesses, our communities, and our lives.",
				img = "https://goo.gl/Wv8UaF",
				buy = "https://goo.gl/HzCc9b",
				category=category5)
session.add(item16)
session.commit()

item18 = Items(name="You Are a Badass", 
				description="In this refreshingly entertaining how-to guide, bestselling author and world-traveling success coach, Jen Sincero, serves up 27 bitesized chapters full of hilariously inspiring stories, sage advice, easy exercises, and the occasional swear word, helping you to: Identify and change the self-sabotaging beliefs and behaviors that stop you from getting what you want, Create a life you totally love. And create it NOW, Make some damn money already. The kind you've never made before.",
				img = "https://goo.gl/4v39Ui",
				buy = "https://goo.gl/Jd2jfN",
				category=category5)
session.add(item18)
session.commit()
