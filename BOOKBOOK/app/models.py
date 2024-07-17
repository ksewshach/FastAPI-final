from database import Model
from sqlalchemy.orm import Mapped, mapped_column

class ChapterModel(Model):

    __tablename__ = 'chapter_table'

    id: Mapped[int] = mapped_column(primary_key=True) # праймари ки - генерируется сам
    title: Mapped[str]
    description: Mapped[str]
    status: Mapped[bool] = mapped_column(default=False)


class Users(Model):

    __tablename__ = 'users_list'

    id: Mapped[int] = mapped_column(primary_key=True) # праймари ки - генерируется сам
    username: Mapped[str]
    email: Mapped[str]
    password: Mapped[str]