from app.extensions import db

class Class(db.Model):
    __tablename__ = 'class'

    # 部门ID (主键)
    class_id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    # 班级编号
    class_number = db.Column(db.String(255), nullable=False)

    # 班级名称
    class_name = db.Column(db.String(255), nullable=False)

    # 班级简称
    class_short_name = db.Column(db.String(255))

    # 学制
    duration = db.Column(db.String(255), nullable=False)

    # 培养层次
    education_level = db.Column(db.String(255), nullable=False)

    # 班级类别
    class_type = db.Column(db.String(255), nullable=False)

    # 辅导员
    counselor = db.Column(db.String(255))

    # 班主任
    head_teacher = db.Column(db.String(255))

    # 班长
    monitor = db.Column(db.String(255))

    # 班助
    class_assistant = db.Column(db.String(255))

    # 预计毕业年度
    expected_graduation_year = db.Column(db.String(255))

    # 是否毕业
    is_graduated = db.Column(db.Boolean, nullable=False)

    # 班级人数
    class_size = db.Column(db.Integer, nullable=False)

    # 性别分布
    gender_distribution = db.Column(db.String(255))

    # 班级最大人数
    max_class_size = db.Column(db.Integer, nullable=False)

    # 入学年份
    enrollment_year = db.Column(db.String(255), nullable=False)

    # 所属院系
    department = db.Column(db.String(255), nullable=False)

    # 专业编号
    major_id = db.Column(db.String(255), nullable=False)

    # 专业名称
    major_name = db.Column(db.String(255), nullable=False)

    # 专业方向
    major_direction = db.Column(db.String(255))

    # 校区
    campus = db.Column(db.String(255), nullable=False)

    # 固定教室编号
    fixed_classroom_number = db.Column(db.String(255))

    # 是否是固定教室
    is_fixed_classroom = db.Column(db.Boolean, nullable=False)

    # 备注
    remarks = db.Column(db.String(255))

    # 班主任联系电话
    head_teacher_phone = db.Column(db.String(255))

    # 班主任工号
    head_teacher_id = db.Column(db.String(255))

    # 毕业学年学期
    graduation_year_semester = db.Column(db.String(255))

    # 是否扩招
    is_expanded = db.Column(db.Boolean)

    # 学业导师
    academic_advisor = db.Column(db.String(255))