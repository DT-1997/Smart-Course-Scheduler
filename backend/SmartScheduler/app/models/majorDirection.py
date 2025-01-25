from app.extensions import db

class MajorDirection(db.Model):
    __tablename__ = 'major_direction'

    # 专业方向 ID (自增主键)
    direction_id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    # 专业方向编号
    direction_code = db.Column(db.String(255), nullable=False, unique=True)

    # 专业方向名称
    direction_name = db.Column(db.String(255), nullable=False)

    # 年级
    grade = db.Column(db.String(255), nullable=False)

    # 院系
    department = db.Column(db.String(255), nullable=False)

    # 专业编号
    major_code = db.Column(db.String(255), nullable=False)

    # 专业名称
    major_name = db.Column(db.String(255))