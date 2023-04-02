from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os


####### to be deleted before each deplaoymnet
# from os.path import join, dirname
# from dotenv import load_dotenv
# if os.environ.get("dev_area")=="dev":
#
#
# dotenv_path = join(dirname(__file__), '.env')
# load_dotenv(dotenv_path)
####### to be deleted before each deplaoymnet

host=os.environ.get("host")
username=os.environ.get("username")
password=os.environ.get("password")
DB_NAME=os.environ.get("DB_NAME")
port = os.environ.get("port")
dev_area = os.environ.get("dev_area")

db_string = f"mysql+pymysql://{username}:{password}@{host}/{DB_NAME}"
engine = create_engine(db_string, connect_args={
    "ssl":{
        "ssl_ca": "/etc/ssl/cert.pem"
    }
})

Session = sessionmaker(bind=engine)

session = Session()

Base = declarative_base()

class Job(Base):
    __tablename__="job"
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    location = Column(String(50), nullable=True)
    Salary = Column(Float, nullable=False)
    work_Type = Column(String(50), nullable=True)


Base.metadata.create_all(engine)

if dev_area=="dev":
    job1 = Job(title="ML Engineer",location= "Bengaluru",Salary= 2000.00,work_Type= "Hybrid")
    session.add(job1)
else:
    job1 = Job(title="Frontend Developer", location="Bhubaneswar", Salary=1100.00, work_Type="Office")
    job2 = Job(title="Backend Developer", location="Chicago", Salary=1200.00, work_Type="Work from Home")
    job3 = Job(title="DBA", location="Hyderabad", Salary=1300.00, work_Type="Hybrid")

session.commit()