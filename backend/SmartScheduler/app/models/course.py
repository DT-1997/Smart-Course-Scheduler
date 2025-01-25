from app.extensions import db

class Course(db.Model):
    __tablename__ = 'course'

    # 课程 ID (自增主键)
    course_id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    # 课程编号
    course_code = db.Column(db.String(255), unique=True)

    # 课程名称
    course_name = db.Column(db.String(255), nullable=False)

    # 课程类别
    course_category = db.Column(db.String(255))

    # 课程属性
    course_property = db.Column(db.String(255))

    # 课程类型
    course_type = db.Column(db.String(255))

    # 课程性质
    course_nature = db.Column(db.String(255))

    # 课程英文名
    course_english_name = db.Column(db.String(255))

    # 开课院系
    teaching_department = db.Column(db.String(255))

    # 是否启用
    is_enabled = db.Column(db.Boolean)

    # 总学时
    total_hours = db.Column(db.Integer)

    # 理论学时
    theory_hours = db.Column(db.Integer)

    # 实验学时
    experiment_hours = db.Column(db.Integer)

    # 上机学时
    computer_hours = db.Column(db.Integer)

    # 实践学时
    practical_hours = db.Column(db.Integer)

    # 其他学时
    other_hours = db.Column(db.Integer)

    # 学分
    credit = db.Column(db.Float)

    # 周学时
    weekly_hours = db.Column(db.Float)

    # 是否纯实践环节
    is_pure_practice = db.Column(db.Boolean)