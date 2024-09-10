from users.schemas import CreateUser


def create_user(user_in: CreateUser) -> dict:
    # to return dict
    user = user_in.model_dump()
    return {"status": "success", "user": user}
