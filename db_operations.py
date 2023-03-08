from data import db_session
from data.users import User


def add_user_if_not_in_base(user_id, first_name, last_name):
    db_sess = db_session.create_session()
    if db_sess.query(User).filter_by(id=user_id).first() is None:
        user = User(id=user_id, username=first_name + ' ' + last_name)
        db_sess.add(user)
        db_sess.commit()
