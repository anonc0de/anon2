from PyroUbot.core.database import mongo_client

module_usage_collection = mongo_client["PyroUbot"]["module_usage"]

def update_module(module_name):
    module_doc = module_usage_collection.find_one({"module_name": module_name})
    if module_doc:
        module_usage_collection.update_one(
            {"module_name": module_name},
            {"$inc": {"usage_count": 1}}
        )
    else:
        module_usage_collection.insert_one({"module_name": module_name, "usage_count": 1})
