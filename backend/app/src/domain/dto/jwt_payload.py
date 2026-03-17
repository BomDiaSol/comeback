import datetime


class JwtPayload:
    def __init__(self, user_id: int):
        self.user_id = user_id
        self.created_at = datetime.datetime.now(datetime.timezone.utc)
        self.expiration = self.created_at + datetime.timedelta(hours=1)

    def to_dict(self):
        return {
            "sub": str(self.user_id),
            "iat": int(self.created_at.timestamp()),
            "exp": int(self.expiration.timestamp()),
        }
