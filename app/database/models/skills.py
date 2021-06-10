from sqlalchemy import Column, Integer, String


from database import Base

class Skill(Base):
    '''
    Database model Skill
    '''
    __tablename__ = "skill"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)