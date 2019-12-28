# TODO: ここにSQLAlchemyのモデルを書く
# TODO:  ここにSQLAlchemyのモデルを書く
#from flask import g
#from flaskr.db import get_db

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#db = get_db()

class Post(db.Model):
    """
    postテーブル

    id          : 主キー
    author_id   : 投稿者id
    created : 投稿日
    title   : タイトル
    body    : 本文
    """
    __tablename__ = 'post'

    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.String(255), nullable=False)
    created = db.Column(DateTime, default=datetime.now(),nullable=False)
    title = db.Column(db.String(255), nullable=False)
    body = db.Column(db.String(255), nullable=False)

    pass
