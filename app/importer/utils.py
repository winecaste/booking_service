import datetime
import json

from app.bookings.dao import BookingDAO
from app.hotels.dao import HotelDAO
from app.hotels.rooms.dao import RoomDAO
from app.logger import logger

TABLE_MODEL_MAP = {
    "hotels": HotelDAO,
    "rooms": RoomDAO,
    "bookings": BookingDAO,
}


def convert_csv_to_postgres(csv_data):
    try:
        data = []
        for row in csv_data:
            for k, v in row.items():
                if v.isdigit():
                    row[k] = int(v)
                elif k == "services":
                    row[k] = json.loads(v.replace("'", '"'))
                elif "date" in k:
                    row[k] = datetime.strptime(v, "%Y-%m-%d")
            data.append(row)
        return data
    except Exception:
        logger.error("Cannot convert CSV into DB format", exc_info=True)
