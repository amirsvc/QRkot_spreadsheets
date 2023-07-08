from sqlalchemy import Column, ForeignKey, Integer, Text

from app.models.base import BaseAbstract


class Donation(BaseAbstract):
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    comment = Column(Text)

    def __repr__(self):
        return (
            f'ID Юзера- {self.user_id}'
            f'Комментарий - {self.comment}'
            f'{super().__repr__()}'
        )
