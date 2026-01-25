from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from app.core.config import get_settings
from sqlalchemy.orm import sessionmaker

settings = get_settings()

engine = create_async_engine(settings.DATABASE_URL, echo=True, future=True)

AsyncSessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False) # async session factory that will prevent objects from
											  # expiring after commits

async def get_db():	# dependency for FastAPI routes
	async with AsyncSessionLocal() as session:
		yield session
