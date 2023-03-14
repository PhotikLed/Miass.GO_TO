import sqlalchemy
from data.db_session import SqlAlchemyBase


class Rating(SqlAlchemyBase):
    __tablename__ = 'rating'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True)
    sum_of_rating = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    count_of_marks = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
