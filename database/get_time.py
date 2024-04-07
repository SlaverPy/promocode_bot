from .model import DistributionTime
from tortoise.exceptions import DoesNotExist


async def get_time_object():
    try:
        records = await DistributionTime.all().order_by('-id').first()
        if records:
            return records
    except DoesNotExist:
        records = await DistributionTime.create()
        return records


