from MyApp import db

Base = db.Model # 这句话你是否还记的?
# from sqlalchemy.ext.declarative import declarative_base
# Base = declarative_base()
# 每一次我们在创建数据表的时候都要做这样一件事
# 然而Flask-SQLAlchemy已经为我们把 Base 封装好了

# 建立User数据表
class Users(Base): # Base实际上就是 db.Model
    __tablename__ = "users"
    __table_args__ = {"useexisting": True}
    # 在SQLAlchemy 中我们是导入了Column和数据类型 Integer 在这里
    # 就和db.Model一样,已经封装好了
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(32))
    password = db.Column(db.String(32))


if __name__ == '__main__':
    from MyApp import create_app
    app = create_app()
    # 这里你要回顾一下Flask应该上下文管理了
    # 离线脚本:
    with app.app_context():
        db.drop_all()
        db.create_all()