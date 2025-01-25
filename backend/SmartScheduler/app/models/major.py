from app.extensions import db

class Major(db.Model):
    __tablename__ = 'major'

    # 专业ID (自增主键)
    major_id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    # 专业简称
    major_short_name = db.Column(db.String(255))

    # 学制
    duration = db.Column(db.String(255))

    # 英文名称
    english_name = db.Column(db.String(255))

    # 开办状态
    is_established = db.Column(db.String(255))

    # 所属院系
    department = db.Column(db.String(255))

    # 专业名称
    major_name = db.Column(db.String(255), nullable=False)

    # 专业编号
    major_code = db.Column(db.String(255))

    # 培养层次
    education_level = db.Column(db.String(255))
