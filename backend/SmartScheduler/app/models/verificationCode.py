from app.extensions import db
from datetime import datetime, timezone, timedelta


class VerificationCode(db.Model):
    __tablename__ = 'verification_codes'  # Table name in the database

    # Primary key for the verification code table
    id = db.Column(db.Integer, primary_key=True)

    # Email address associated with the verification code
    # Bound email address
    email = db.Column(db.String(255), nullable=False, unique=True)

    # The 6-character verification code
    code = db.Column(db.String(6), nullable=False)  # Verification code

    # Expiration time for the verification code,
    # default is 15 minutes from creation
    expires_at = db.Column(
        db.DateTime,
        default=lambda: datetime.now(timezone.utc) + timedelta(minutes=15)
    )

    def is_expired(self):
        """
        Checks if the verification code has expired.
        If the 'expires_at' field is timezone-naive,
        it adds UTC timezone information.
        Returns True if the current time exceeds the expiration time.
        """
        if self.expires_at.tzinfo is None:
            self.expires_at = self.expires_at.replace(tzinfo=timezone.utc)
        return datetime.now(timezone.utc) > self.expires_at
