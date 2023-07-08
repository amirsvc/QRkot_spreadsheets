from datetime import datetime
from typing import Union

from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.charity_project import charity_project_crud
from app.crud.donation import donation_crud
from app.models import CharityProject, Donation


def close_invest(db_obj: Union[Donation, CharityProject]) -> None:
    db_obj.fully_invested = True
    db_obj.invested_amount = db_obj.full_amount
    db_obj.close_date = datetime.now()


async def make_invest(session: AsyncSession) -> None:
    all_charity_projects = await charity_project_crud.get_for_invest(session)
    all_donations = await donation_crud.get_for_invest(session)
    if not all([all_charity_projects, all_donations]):
        return
    for charity_project in all_charity_projects:
        for donation in all_donations:
            need_invest = (
                charity_project.full_amount - charity_project.invested_amount
            )
            available_money = donation.full_amount - donation.invested_amount
            money_left = need_invest - available_money

            if money_left == 0:
                close_invest(charity_project)
                close_invest(donation)

            if money_left < 0:
                donation.invested_amount += abs(money_left)
                close_invest(charity_project)

            if money_left > 0:
                charity_project.invested_amount += available_money
                close_invest(donation)