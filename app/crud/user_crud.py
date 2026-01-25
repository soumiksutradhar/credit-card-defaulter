from sqlalchemy.ext.asyncio import AsyncSession
from app.models.user import User
from app.schemas.user_schemas import UserCreate

async def create_user(db: AsyncSession, user: UserCreate): # creates new user record in DB

	new_user = User(education=user.education, gender=user.gender, marital_status=usr.marital_status, last_bill=user.last_bill, last_payment=user.last_payment)
	
	db.add(new_user)	# stages new record insert
	await db.commit() 		# writes record to postgres DB
	await db.refresh(new_user) 	# fetch new record from DB and update new_user in memory
