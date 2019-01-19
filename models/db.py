from datetime import datetime
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SESSION_ENGINE = create_engine('sqlite:///chatdb.sqlite')
Base = declarative_base()


class User(Base):
    """Users of the system"""

    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    password = Column(String)
    created = Column(DateTime, default=datetime.now)
    phone_number = Column(String)
    image_url = Column(String)


class Chats(Base):
    """Database for chats"""

    __tablename__ = 'chats'
    id = Column(Integer, primary_key=True)
    question = Column(String, unique=True)
    answer = Column(String)
    created = Column(DateTime, default=datetime.now)


Base.metadata.create_all(SESSION_ENGINE)
Session = sessionmaker(bind=SESSION_ENGINE)
db_session = Session()

if __name__ == '__main__':
    chat_ex_1 = Chats(question='What is you name?', answer='swaggernauts')
    chat_ex_w = Chats(question='Blue or Red', answer='def blue, although red is cool too!')
    db_session.add_all([chat_ex_1, chat_ex_w])
    db_session.commit()
    