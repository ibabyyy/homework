from unicodedata import name
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker


# # # ###########################################
# # Do not touch!
# # Database Connection stuff!
# Erzeugen einer neuen Datenbank Engine
database = create_engine("sqlite:///friendbook.db")
# Basisklasse für Klassen
Base = declarative_base()

# Öffne Verbindung zur Datenbank
Session = sessionmaker(bind=database)
# Offene Verbindung zur Datenbank
session = Session()
# # # ###########################################

#Haupt
class Freunde(Base):
    __tablename__ = "Freunde"

    id = Column(Integer, primary_key=True)
    vorname = Column(String)
    name = Column(String)


#Geburtstag
class Geburtstagtag(Base):
    __tablename__ = "Geburtstagtag"

    id = Column(Integer, primary_key=True)
    day = Column(String)

    # Foreignkeys
    geburtstagtag_id = Column(Integer, ForeignKey("Freunde.id"))

class Geburtstagmonat(Base):
    __tablename__ = "Geburtstagmonat"

    id = Column(Integer, primary_key=True)
    monat = Column(String)

    # Foreignkeys
    geburtstagmonat_id = Column(Integer, ForeignKey("Geburtstagtag.id"))

class Geburtstagjahr(Base):
    __tablename__ = "Geburtstagjahr"

    id = Column(Integer, primary_key=True)
    jahr = Column(String)

    # Foreignkeys
    geburtstagjahr_id = Column(Integer, ForeignKey("Geburtstagmonat.id"))



#Adresse
class Adresseort(Base):
    __tablename__ = "Adresseort"

    id = Column(Integer, primary_key=True)
    ort = Column(String)

    # Foreignkeys
    adresseort_id = Column(Integer, ForeignKey("Freunde.id"))

class Adressestrasse(Base):
    __tablename__ = "Adressestrasse"

    id = Column(Integer, primary_key=True)
    ort = Column(String)

    # Foreignkeys
    adressestrasse_id = Column(Integer, ForeignKey("Adresseort.id"))

class Adressenummer(Base):
    __tablename__ = "Adressenummer"

    id = Column(Integer, primary_key=True)
    nummer = Column(Integer)
    
    # Foreignkeys
    adressenummer_id = Column(Integer, ForeignKey("Adressestrasse.id"))




def initialize_database():
    """
    Initializes the database and creates all tables.
    See more here: https://docs.sqlalchemy.org/en/14/orm/tutorial.html
    """
    Base.metadata.create_all(database)


def database_add_friend(friend: Freunde):
    """
    Database command to add a new friend.
    """
    session.add(friend)
    session.commit()
##########################################################
def database_add_geburtstagtag(tag: Geburtstagtag):
    """
    Database commadn to add new Tag.
    """
    session.add(tag)
    session.commit()

def database_add_geburtstagmonat(monat: Geburtstagmonat):
    """
    Database commadn to add new Monat.
    """
    session.add(monat)
    session.commit()

def database_add_geburtstagjahr(jahr: Geburtstagjahr):
    """
    Database commadn to add new Jahr.
    """
    session.add(jahr)
    session.commit()
#######################################################

def database_get_all_friends():
    """
    Database command to get all friends.
    """
    all_friends = session.query(Freunde).all()
    print(all_friends)


# # # ###########################################
# # # Main
# # # ###########################################
if __name__ == "__main__":
    initialize_database()

    # Example to add a new friend
    vorname2 = input("vorname: ")
    name2 = input("name: ")
    new_friend = Freunde(vorname = vorname2, name = name2)
    print(vorname2)
    print(name2)
    database_add_friend(new_friend)

    new_tag = Geburtstagtag(day = input("enter tag as number: "))
    database_add_geburtstagtag(new_tag)

    new_monat = Geburtstagmonat(monat = input("enter monat as number: "))
    database_add_geburtstagmonat(new_monat)

    new_jahr = Geburtstagjahr(jahr = input("enter jahr as number: "))
    database_add_geburtstagjahr(new_jahr)

    # Example to list all friends
    database_get_all_friends()