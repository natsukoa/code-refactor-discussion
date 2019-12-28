# TODO:  ここにSQLAlchemyのモデルを書く
#from flask import g
#from flaskr.db import get_db

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#db = get_db()

class User(db.Model):
    """
    userテーブル

    id       : 主キー
    username : ユーザ名
    password : パスワード
    """
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
