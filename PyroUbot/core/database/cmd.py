from PyroUbot.core.database import mongodb
from pymongo.errors import PyMongoError

modules = mongodb.module


async def get_module():
    module = await modules.find_one({"module": module_name, {"usage_count": "usage_count"})
    if not module:
        return []
    return module["modulers"]


async def add_module(module_name):
    moduler = await get_module()
    moduler.append(module_name)
    await resell.update_one(
        {"module": module_name}, {"$inc": {"usage_count": 1}}, upsert=True
    )
    return True

