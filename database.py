from sqlalchemy import Column, Integer, Float, String, Date, Time, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
from sqlalchemy import create_engine
from sqlalchemy import and_, or_
from dotenv import load_dotenv
from os import getenv
from datetime import date, time
import datetime


#importaciones locales

from functions import *

load_dotenv()

user = getenv('USERDB')
password = getenv('PASSDB')
hostname = getenv('HOSTNAME')
port = getenv('PORTDB')
db=getenv('DATABASE')

print(user, password, hostname, port, db)

engine = create_engine(f'postgresql://{user}:{password}@{hostname}:{port}/{db}?sslmode=require')

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class User:
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    names = Column(String(120), nullable=False)
    lastnames = Column(String(150), nullable=False)
    documentType = Column(String(40), nullable=False)
    numDocument = Column(String(18), nullable=False)
    phone = Column(String(16), nullable=False)
    area = Column(String(100), nullable=False)
    email = Column(String(150),nullable=False)
    username = Column(String(20), nullable=False)
    password = Column(String(25), nullable=False)
    rol = Column(String(120), nullable=False)



    def __init__(self, names, lastnames, documentType, numDocument, phone, area, email, username, password, rol):
        self.names = names
        self.lastnames = lastnames
        self.documentType = documentType
        self.numDocument = numDocument
        self.phone = phone
        self.area = area
        self.email = email
        self.username =username
        self.password = passwordHash(password)
        self.rol = rol

class Equipment:
    __tablename__ = 'equipments'
    id = Column(Integer, primary_key=True)
    name = Column(String(100),nullable=False)
    equipmentCode = Column(String(120), nullable=False)
    equipmentSerial = Column(String(120), nullable=False)
    monitorCode = Column(String(120), nullable=True)
    monitorBrand = Column(String(120), nullable=True)
    monitorModel = Column(String(120), nullable=True)
    monitorSerial = Column(String(120), nullable=True)
    management = Column(String(120), nullable=True)
    user = Column(String(120), nullable=True)
    functionalities = Column(String(300), nullable=True)
    garantia = Column(String(120), nullable=True)



    def __init__(self, name, equipmentCode, equipmentSerial, monitorCode, monitorBrand, monitorModel, monitorSerial, management, user, functionalities, garantia):
        self.name = name
        self.equipmentCode = equipmentCode
        self.equipmentSerial = equipmentSerial
        self.monitorCode = monitorCode
        self. monitorBrand = monitorBrand
        self.monitorModel = monitorModel
        self.monitorSerial = monitorSerial
        self.management = management
        self.user = user
        self.functionalities = functionalities
        self.garantia = garantia


class DamageReport:
    __tablename__ = 'damageReports'
    id = Column(Integer, primary_key=True)
    reportName = Column(String(150), nullable=False)
    area = Column(String(120), nullable=False)
    equipmentCode = Column(String(120), nullable=False)
    components = Column(String(300), nullable=False)
    faultDescription = Column(String(350), nullable=False)
    typeMaintenance = Column(String(120), nullable=False)
    dateReport = Column(Date, nullable=False)
    functionalities = Column(String(300), nullable=True)

    def __init__(self, reportName, area, equipmentCode, components, faultDescription, typeMaintenance, functionalities):
        self.reportName = reportName
        self.area = area
        self.equipmentCode = equipmentCode
        self.components = components
        self.faultDescription = faultDescription
        self.typeMaintenance = typeMaintenance
        self.dateReport = date.today()
        self.functionalities = functionalities

class MaintenanceReport:
    __tablename__ = 'maintenanceReports'
    id = Column(Integer, primary_key=True)
    reportName = Column(String(150), nullable=False)
    area = Column(String(120), nullable=False)
    equipmentCode = Column(String(120), nullable=False)
    components = Column(String(300), nullable=False)
    faultDescription = Column(String(350), nullable=False)
    typeMaintenance = Column(String(120), nullable=False)
    dateReport = Column(Date, nullable=False)
    functionalities = Column(String(300), nullable=True)

    def __init__(self, reportName, area, equipmentCode, components, faultDescription, typeMaintenance, functionalities):
        self.reportName = reportName
        self.area = area
        self.equipmentCode = equipmentCode
        self.components = components
        self.faultDescription = faultDescription
        self.typeMaintenance = typeMaintenance
        self.dateReport = date.today()
        self.functionalities = functionalities