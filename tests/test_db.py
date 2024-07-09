from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    user = User(
        username="Claudio",
        email="claudio@lucas.com",
        password="plataforma93/4",
    )

    session.add(user)
    session.commit()

    result = session.scalar(
        select(User).where(User.email == "claudio@lucas.com")
    )

    assert result.username == 'Claudio'
