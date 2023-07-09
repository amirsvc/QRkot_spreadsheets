import copy
from datetime import datetime

from aiogoogle import Aiogoogle

from app.core.config import settings

FORMAT = "%Y/%m/%d %H:%M:%S"
ROW_COUNT = 100
COLUMN_COUNT = 11
SHEET_SIZE_ERROR = (
    'В таблицу добавляется {rows} строк и {columns} столбцов.'
    f'Тогда как в таблице всего {ROW_COUNT} строк и {COLUMN_COUNT} столбцов.'
)
BODY = {
    'properties': {
        'title': '',
        'locale': 'ru_RU',
    },
    'sheets': [{'properties': {
        'sheetType': 'GRID',
        'sheetId': 0,
        'title': 'Лист1',
        'gridProperties': {
            'rowCount': ROW_COUNT,
            'columnCount': COLUMN_COUNT,
        }
    }}]
}
SPREADSHEET_TITLE = 'Отчет от {now_date_time}'
TABLE_HEADER = [
    ['Отчет от', ''],
    ['Топ проектов по скорости закрытия'],
    ['Название проекта', 'Время сбора', 'Описание'],
]


async def spreadsheets_create(
    wrapper_services: Aiogoogle,
    input_body: dict = BODY,
) -> str:
    now_date_time = datetime.now().strftime(FORMAT)
    spreadsheet_body = copy.deepcopy(input_body)
    spreadsheet_body['properties']['title'] = SPREADSHEET_TITLE.format(
        date_time_now=now_date_time,
    )
    service = await wrapper_services.discover('sheets', 'v4')
    response = await wrapper_services.as_service_account(
        service.spreadsheets.create(json=spreadsheet_body)
    )
    return response['spreadsheetId']


async def set_user_permissions(
        spreadsheet_id: str,
        wrapper_services: Aiogoogle
) -> None:
    permissions_body = {
        'type': 'user',
        'role': 'writer',
        'emailAddress': settings.email,
    }
    service = await wrapper_services.discover('drive', 'v3')
    await wrapper_services.as_service_account(
        service.permissions.create(
            fileId=spreadsheet_id,
            json=permissions_body,
            fields="id",
        ))


async def spreadsheets_update_value(
        spreadsheet_id: str,
        charity_projects: list,
        wrapper_services: Aiogoogle,
) -> None:
    now_date_time = datetime.now().strftime(FORMAT)
    service = await wrapper_services.discover('sheets', 'v4')
    table_head = copy.deepcopy(TABLE_HEADER)
    table_head[0][1] = now_date_time
    table_values = [
        *table_head,
        *[list(map(str, [
            project.name,
            str(project.close_date - project.create_date),
            project.description,
        ])) for project in charity_projects]
    ]
    update_body = {
        'majorDimension': 'ROWS',
        'values': table_values,
    }
    rows_count = len(table_values)
    columns_count = max(map(len, table_values))
    if rows_count > ROW_COUNT or columns_count > COLUMN_COUNT:
        raise ValueError(SHEET_SIZE_ERROR.format(
            rows=rows_count,
            columns=columns_count,
        ))
    await wrapper_services.as_service_account(
        service.spreadsheets.values.update(
            spreadsheetId=spreadsheet_id,
            range=f'R1C1:R{rows_count}C{columns_count}',
            valueInputOption='USER_ENTERED',
            json=update_body,
        )
    )
