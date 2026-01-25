from sqlalchemy import Column, Integer, String, Boolean, Text
from app.db.base import Base

class User(Base):

	__tablename__ = "user_data"
	
	user_id = Column(Integer, primary_key=True, index=True)	# no need to 'autoincrement="auto"' since 'primary_key' handles that 
	education = Column(String(100), nullable=False)		# automatically
	gender = Column(String(10), nullable=False)
	marital_status = Column(String(15), nullable=False)
	last_bill = Column(Integer, nullable=False)
	last_payment = Column(Integer, nullable=False)
