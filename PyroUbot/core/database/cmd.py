from PyroUbot.core.database import mongo_client

module_usage_collection = mongodb.module

def update_module(module_name):
    module_doc = module_usage_collection.find_one({"module_name": module_name})
    if module_doc:
        module_usage_collection.update_one(
            {"module_name": module_name},
            {"$inc": {"usage_count": 1}}
        )
    else:
        module_usage_collection.insert_one({"module_name": module_name, "usage_count": 1})


def usage_module():
    result_list = []
    for module_doc in module_usage_collection.find():
        module_name = module_doc["module_name"]
        usage_count = module_doc["usage_count"]
        result_list.append({"module_name": module_name, "usage_count": usage_count})
    return result_list
