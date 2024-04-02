

# СЕРВЕРНАЯ ЧАСТЬ




from fastapi import APIRouter, Request
from schemas import TaskCreateSchema, TaskUpdateSchema
from models import TaskModel
from sqlalchemy.orm import Session
from database import engine
from sqlalchemy import select, insert

tasks_router = APIRouter(prefix='/api/v1/tasks') # префикс для разработчика чисто, чтобы понимали что тут находится какой-то интерфейс 

"""@tasks_router.post(path='/create/')# full path = /api/v1/tasks/create/
def create_task_point(request: Request, task: TaskCreateSchema):
    new_task = TaskModel(
        title=task.title,
        description=task.description,
    )
    session = Session(engine) # <- создаю сессию с БД
    session.add(new_task) # <- записывает обьект в БД
    session.commit() # <- делает сохрание
    session.close() # <- закрывает сессию
    return {"task": task}

@tasks_router.get('/list/')
def list_tasks_point(request:Request):
    session = Session(engine)
    stmt = select(TaskModel)
    print(stmt)

    SELECT tasks_table.id, tasks_table.title, tasks_table.description, tasks_table.status     
    FROM tasks_table

    tasks:list = session.scalars(stmt).all()
    return tasks
"""

@tasks_router.get('/list')
def get_list_task(request: Request): #Этот реквест нужно обязательно прописывать, в некоторых гайдах его нет
    session = Session(engine)# экземпляр класса, отвечающий за соединение с базой данных
    stmt = select(TaskModel) # (sql запрос по форме запросить таблицу таск модел)
    object_db = session.execute(stmt) #формируется скл объект, получаем объект с базы данных (всю табличку дёрнет, получим объект но работать с ним не сможем, надо преобразовать)
    tasks:list = object_db.scalars().all() # скалларс преобразует всё это в понятный нам тип список, по-другому бы не получилось работать с ним
    session.close()
    return tasks # закрыли сессию и возвращаем список

@tasks_router.post('/create')
def create_task(request: Request, task: TaskCreateSchema):
    session = Session(engine) # экземпляр класса, который позволяет подключиться к БД
    stmt = insert(TaskModel).values(title=task.title,  # insert импортируется из sqlalchemy,
                                    description=task.description) # нельзя чтобы в строке не было больше 80 символов ПРАВИЛО ХОРОШЕГО ТОНА, можно включить в настройках)
    session.execute(stmt)
    session.commit() #сделалит сохранение, без КОММИТА не сохранится! как dump в джсоне
    session.close()
    return task

@tasks_router.put('/list/') # можно на один адрес разные методы накидывать
def update_task(request: Request, task_id: int, task_change: TaskUpdateSchema): # task_id:int получаем айди к изменению у пользователя, 
    session = Session(engine)
    stmt = select(TaskModel).where(TaskModel.id==task_id) # формируем запрос: мы хотим получить из таблички таск модел запись по айдишнику
    object_db = session.execute(stmt)
    print(object_db)
    task = object_db.scalars().first()
    task.title = task_change.title
    task.description = task_change.description
    task.status = task_change.status
    session.merge(task) # обновит существующий через мердж
    session.commit()
    session.close()
    return task_change

@tasks_router.delete('/list/')
def delete_task(request: Request, task_id: int):
    session = Session(engine)
    stmt = select(TaskModel).where(TaskModel.id==task_id) # формируем запрос: мы хотим получить из таблички таск модел запись по айдишнику
    object_db = session.execute(stmt)
    task = object_db.scalar() # .one() один объект из списка извлекает
    session.delete(task)
    session.commit()
    session.close()
    return {'message': f'task id: {task_id} delete'}