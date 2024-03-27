import codecs
import csv
from typing import Literal

from fastapi import APIRouter, Depends, UploadFile

from app.exceptions import CannotAddDataToDatabase, CannotProcessCSV
from app.importer.utils import TABLE_MODEL_MAP, convert_csv_to_postgres
from app.users.dependencies import get_current_user

router = APIRouter(prefix="/import", tags=["Import CSV"])


@router.post("/{table_name}", status_code=201, dependencies=[Depends(get_current_user)])
async def import_csv(
    table_name: Literal["hotels", "rooms", "bookings"],
    file: UploadFile,
):
    ModelDAO = TABLE_MODEL_MAP[table_name]
    csvReader = csv.DictReader(codecs.iterdecode(file.file, "utf-8"), delimiter=";")
    csvConvert = convert_csv_to_postgres(csvReader)
    file.file.close()
    if not csvConvert:
        raise CannotProcessCSV
    add_data = await ModelDAO.add_bulk(csvConvert)
    if not add_data:
        raise CannotAddDataToDatabase
