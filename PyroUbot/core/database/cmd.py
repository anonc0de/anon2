from PyroUbot.core.database import mongodb
from pymongo.errors import PyMongoError

module_usage_collection = mongodb.module

def update_module(module_name):
    try:
        module_doc = module_usage_collection.find_one({"module_name": module_name})
        if module_doc:
            module_usage_collection.update_one(
                {"module_name": module_name},
                {"$inc": {"usage_count": 1}}
            )
        else:
            module_usage_collection.insert_one({"module_name": module_name, "usage_count": 1})
    except PyMongoError as e:
        print(f"Error in updating module usage: {str(e)}")

def usage_module():
    result_list = []
    try:
        for module_doc in module_usage_collection.find():
            module_name = module_doc["module_name"]
            usage_count = module_doc["usage_count"]
            result_list.append({"module_name": module_name, "usage_count": usage_count})
    except PyMongoError as e:
        print(f"Error in getting module usage results: {str(e)}")
    return result_list
