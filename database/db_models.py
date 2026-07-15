from database.database import Base
from sqlalchemy.sql.sqltypes import Integer, String, Boolean
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship

class DbUser(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index= True)
    username = Column(String)
    email = Column (String)

    