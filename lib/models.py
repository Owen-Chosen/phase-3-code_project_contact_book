from main import Base
from sqlalchemy import Column, DateTime, String, Integer, func



class Contact(Base):
    __tablename__ = 'contacts'
    id = Column(Integer(), primary_key=True)
    firstname = Column(String())
    lastname = Column(String())
    phone = Column(Integer())
    email = Column(Integer())
    created_at = Column(DateTime(), server_default=func.now())

    def __repr__(self):
        return f"{self.id}, firstname: {self.firstname},
          lastname: {self.lastname}, phone: {self.phone}, email: {self.email}"