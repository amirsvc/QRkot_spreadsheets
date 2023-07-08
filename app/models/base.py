from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, Integer

from app.core.db import Base


class BaseAbstract(Base):
    __abstract__ = True

    full_amount = Column(Integer, nullable=False)
    invested_amount = Column(Integer, default=0, nullable=False)
    fully_invested = Column(Boolean, default=False, nullable=False)
    create_date = Column(DateTime, default=datetime.now, nullable=False)
    close_date = Column(DateTime, default=None)

    def __repr__(self):
        return (
            f'Требуемая сумма - {self.full_amount}.'
            f'Внесённая сумма - {self.invested_amount}.'
            f'Проект закрыт - {self.fully_invested}.'
            f'Дата создания - {self.create_date}.'
            f'Дата закрытия - {self.close_date}.'
        )
