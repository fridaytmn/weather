import asyncio
import winsdk.windows.devices.geolocation as wdg
from typing import NamedTuple
from exception import CantGetCoordinates


class Coordinates(NamedTuple):
    longitude: float
    latitude: float

async def getCoords():
    locator = wdg.Geolocator()
    pos = await locator.get_geoposition_async()
    return (pos.coordinate.latitude, pos.coordinate.longitude)


def get_gps_coordinates() -> Coordinates:
    try:
        return Coordinates(asyncio.run(getCoords())[1], asyncio.run(getCoords())[0])
    except CantGetCoordinates:
        pass
