from app.models.user_session import UserSession
from app.repository.base import BaseRepository


class SessionRepository(BaseRepository):

    def __init__(self, db):
        super().__init__(db, UserSession)

    def deactivate_old_sessions(self, user_id: int):
        sessions = self.db.query(UserSession).filter(UserSession.user_id == user_id,
                                                     UserSession.is_active == True).all()

        for s in sessions:
            s.is_active = False

        self.db.commit()

    def get_active_session(self, token: str):
        return self.db.query(UserSession).filter(UserSession.token == token, UserSession.is_active == True).first()
