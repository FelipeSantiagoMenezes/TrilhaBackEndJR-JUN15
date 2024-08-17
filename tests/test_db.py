from sqlalchemy import select

from src.models.models import User


def test_create_user(session):
    new_user = User(
        username='username', email='teste@email.com', password='password'
    )
    session.add(new_user)
    session.commit()

    user = session.scalar(select(User).where(User.username == 'username'))
    assert new_user.username == user.username
