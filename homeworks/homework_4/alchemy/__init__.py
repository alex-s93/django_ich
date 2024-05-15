from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

engine = create_engine('mysql+pymysql://root:Great123@localhost:3306/test_sqlalchemy')
Base = declarative_base()
