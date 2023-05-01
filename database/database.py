#(©)CodeXBotz




import pymongo, os
from config import DB_URI, DB_NAME


dbclient = pymongo.MongoClient(DB_URI)
database = dbclient[DB_NAME]


user_data = database['users']



async def present_user(user_id : int):
    found = user_data.find_one({'_id': user_id})
    if found:
        return True
    else:
        return False

# collect the user shortner site details
async def get_short(user_id :int) 
    user_id = int(user_id)
    user = await user_data.find_one({"user_id": user_id})
    if not user:
        res = {
            "user_id": user_id,
            "shortener_api": None,
            "header_text": "",
            "footer_text": "",
            "base_site": None,
            "is_header_text": True,
            "is_footer_text": True,
        }
        await user_data.insert_one(res)
        user = await user_data.find_one({"user_id": user_id})

    return user
    
    
async def add_user(user_id: int):
    user_data.insert_one({'_id': user_id})
    return

async def full_userbase():
    user_docs = user_data.find()
    user_ids = []
    for doc in user_docs:
        user_ids.append(doc['_id'])
        
    return user_ids

async def del_user(user_id: int):
    user_data.delete_one({'_id': user_id})
    return
