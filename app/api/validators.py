from http import HTTPStatus

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.charity_project import charity_project_crud
from app.models import CharityProject


async def check_name_duplicate(
        charity_project_name: str,
        session: AsyncSession,
) -> None:
    charity_project_id = await charity_project_crud.get_id_by_name(charity_project_name, session)
    if charity_project_id is not None:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Проект с таким именем уже существует!',
        )


async def check_charity_project_exists(
        charity_project_id: int,
        session: AsyncSession,
) -> CharityProject:
    charity_project = await charity_project_crud.get(
        charity_project_id, session
    )
    if charity_project is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Благотворительный проект не найден!',
        )
    return charity_project


async def check_charity_project_invested_amount(
        charity_project_id: int,
        session: AsyncSession,
) -> CharityProject:
    charity_project = await charity_project_crud.get(
        charity_project_id, session
    )
    if charity_project.invested_amount > 0:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='В проект были внесены средства, не подлежит удалению!',
        )
    return charity_project


async def check_charity_project_for_update(
    charity_project_id: int,
    obj_in: int,
    session: AsyncSession,
) -> CharityProject:
    charity_project = await charity_project_crud.get(
        charity_project_id, session,
    )
    if charity_project.fully_invested:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail=('Закрытый проект нельзя редактировать!'),
        )
    if obj_in.full_amount and charity_project.invested_amount > obj_in.full_amount:
        raise HTTPException(
            status_code=HTTPStatus.UNPROCESSABLE_ENTITY,
            detail=('Нельзя указывать требуемую сумму меньше внесённой!'),
        )
    return charity_project
