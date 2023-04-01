# defined_jobs = [
#     {
#         "id":1,
#         "title":"Data Science",
#         "location": "Hyderabad",
#         "Salary": 1000.00,
#         "Work Type": "Remote"
#     },
#     {
#             "id":2,
#             "title":"Data Analyst",
#             "location": "Bengaluru",
#             "Salary": 900.00
#     },
#     {
#             "id":3,
#             "title":"Frontend Developer",
#             "location": "Bhubaneswar",
#             "Salary": 1100.00,
#             "Work Type": "Hybrid"
#     },
#     {
#             "id":4,
#             "title":"Data Engineer",
#             "location": "Hyderabad",
#             "Salary": 1500.00,
#             "Work Type": "Office"
#     }]
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

username = 'Rinku'
password = 'Rinku25112021'
host = 'rinku.cqhvo2hszsw7.us-east-1.rds.amazonaws.com'
port = 3306
DB_NAME = 'rinku'

engine = create_engine(f"mysql+pymysql://{username}:{password}@{host}/{DB_NAME}")

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

# job1 = Job(title="Frontend Developer",location= "Bhubaneswar",Salary= 1100.00,work_Type= "Hybrid")
#
#
# session.add(job1)
# session.commit()