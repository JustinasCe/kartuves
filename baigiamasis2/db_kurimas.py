from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from bs4 import BeautifulSoup
import requests


# db kurimas
engine = create_engine('sqlite:///zodynas.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

source = requests.get("https://lt.wikipedia.org/wiki/Telefonas").text
soup = BeautifulSoup(source, "html.parser")
blokas = soup.find_all("div", class_="mw-body")


class Zodynas(Base):
    __tablename__ = 'Zodynas'
    id = Column(Integer, primary_key=True)
    zodis = Column('Zodis', String)

    def __init__(self, zodis):
        self.zodis = zodis

    def __repr__(self):
        return f'{self.id} {self.zodis}'


def kurti_db():
    for tekstas in blokas:
        try:
            visas_tekstas = tekstas.find("div", class_="mw-parser-output").text.strip()
            tekstas_be_nbsp = ' '.join(visas_tekstas.split())
            svarus_tekstas_v1 = tekstas_be_nbsp.lower()
            svarus_tekstas_v2 = svarus_tekstas_v1.replace("#", " ")
            svarus_tekstas_v3 = svarus_tekstas_v2.replace(",", " ")
            svarus_tekstas_v4 = svarus_tekstas_v3.replace(".", " ")
            svarus_tekstas_v5 = svarus_tekstas_v4.replace("(", " ")
            svarus_tekstas_v6 = svarus_tekstas_v5.replace(")", " ")
            svarus_tekstas_v7 = svarus_tekstas_v6.replace("]", " ")
            svarus_tekstas_v8 = svarus_tekstas_v7.replace("[", " ")
            svarus_tekstas_v9 = svarus_tekstas_v8.replace("-", " ")
            zodziai = svarus_tekstas_v9.split()

            for zodis in zodziai:
                if 5 <= len(zodis) < 8 and zodis.isalpha():
                    irasas = Zodynas(zodis)
                    session.add(irasas)
                    session.commit()
                else:
                    pass
        except AttributeError:
            pass


def trinti_db():
    Base.metadata.drop_all(engine)
    session.commit()


Base.metadata.create_all(engine)
