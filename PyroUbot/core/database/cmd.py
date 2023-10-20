from PyroUbot.core.database import mongodb
from pymongo.errors import PyMongoError

modules = mongodb.module

async def get_module_usage(module_name):
    module = await modules.find_one({"module_name": module_name})
    if not module:
        return 0
    return module.get("usage_count", 0)

async def record_module_usage(module_name):
    try:
        module = await modules.find_one({"module_name": module_name})
        if module:
            usage_count = module.get("usage_count", {})
            if module_name in usage_count:
                usage_count[module_name] += 1
            else:
                usage_count[module_name] = 1
            await modules.update_one({"module_name": module_name}, {"$set": {"usage_count": usage_count}})
        else:
            await modules.insert_one({"module_name": module_name, "usage_count": {module_name: 1}})
        return True
    except PyMongoError as e:
        print(f"Error in recording module usage: {str(e)}")
        return False

async def remove_module_usage(module_name):
    try:
        module = await modules.find_one({"module_name": module_name})
        if module:
            usage_count = module.get("usage_count", 0)
            if usage_count > 0:
                await modules.update_one({"module_name": module_name}, {"$set": {"usage_count": usage_count - 1}})
        return True
    except PyMongoError as e:
        print(f"Error in removing module usage: {str(e)}")
        return False
