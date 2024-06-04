import asyncio
from admin.superadmin import superadmin_auto_create
    

async def db_tasks():
    try:
        await superadmin_auto_create()
        return "Super admin has been successfully created"
    except Exception as e:
        #добавить лог
        return e
    

if __name__ == "__main__":
    asyncio.run(db_tasks())