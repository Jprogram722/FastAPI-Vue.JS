
# import modules
from sqlalchemy import create_engine, Integer, String, Column, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

# create connection
engine = create_engine('mysql+pymysql://root:SoPro!234@localhost/ecomweb')

# create the base for the tables
Base = declarative_base()

class Author(Base):
    __tablename__ = 'author'

    id = Column(Integer, primary_key=True)
    fname = Column(String(255))
    lname = Column(String(255))

    books = relationship('Book', back_populates='author')

class Book(Base):
    __tablename__ = 'book'

    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    author_id = Column(Integer, ForeignKey('author.id'))

    author = relationship('Author', back_populates='books')


# create the tables
Base.metadata.create_all(bind=engine)

# create session
SessionLocal = sessionmaker(bind=engine)

db = SessionLocal()

author1 = Author(fname='Andy', lname='Pye')
book1 = Book(title='SUS MONKEY', author=author1)
book2 = Book(title='RE4 BAD', author=author1)

db.add(author1)
db.commit()



