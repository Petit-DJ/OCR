from app.database.database import Base
from sqlalchemy.sql.sqltypes import Integer, String, Boolean
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship

class DbUser(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index= True)
    username = Column(String)
    email = Column (String)
    ocr_txt = relationship('DbOcr', back_populates='user')

class DbOcr(Base):
    __tablename__ = "ocr"
    ocr_id = Column(Integer, primary_key=True, index=True)
    file_name = Column (String)
    ocr_text = Column (String)
    unique_id = Column(Integer, ForeignKey("user.id"))
    user = relationship('DbUser', back_populates='ocr_txt')
