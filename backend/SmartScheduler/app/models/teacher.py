from app.extensions import db

class Teacher(db.Model):
    __tablename__ = 'teacher'

    # 教师ID (自增主键)
    teacher_id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    # 工号
    employee_id = db.Column(db.String(255), nullable=False)

    # 姓名
    name = db.Column(db.String(255), nullable=False)

    # 性别
    gender = db.Column(db.String(50))

    # 英文姓名
    english_name = db.Column(db.String(255))

    # 民族
    ethnicity = db.Column(db.String(100))

    # 职称
    title = db.Column(db.String(255))

    # 单位
    unit = db.Column(db.String(255), nullable=False)

    # 是否外聘
    is_external = db.Column(db.Boolean)

    # 教职工类别
    staff_type = db.Column(db.String(255))