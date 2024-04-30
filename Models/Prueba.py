from sqlalchemy.sql.functions import current_timestamp
from Database.Conn import Base
from sqlalchemy import String, Column, DateTime, Integer


class PruebaModel(Base):

    __tablename__ = 'prueba'

    prueba_id = Column(Integer, primary_key=True)
    name = Column(String)
    active = Column(Integer, server_default=str(1))
    created_at = Column(DateTime, default=current_timestamp())
    updated_at = Column(
        DateTime, default=current_timestamp(), onupdate=current_timestamp()
    )

    def __init__(self, **kwargs):

        self.prueba_id = kwargs['prueba_id']
        self.name = kwargs['name']
        self.active = kwargs['active']
