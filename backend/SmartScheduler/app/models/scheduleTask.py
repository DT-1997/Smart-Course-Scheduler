from app.extensions import db

class ScheduleTask(db.Model):
    __tablename__ = 'schedule_task'

    # 排课任务 ID (自增主键)
    task_id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    # 学年学期
    academic_year_term = db.Column(db.String(255))

    # 课程编号
    course_code = db.Column(db.String(255), nullable=False)

    # 课程名称
    course_name = db.Column(db.String(255), nullable=False)

    # 教师工号
    teacher_id = db.Column(db.String(255))

    # 任课教师
    teacher_name = db.Column(db.String(255))

    # 教学班组成
    class_composition = db.Column(db.String(255))

    # 教学班编号
    class_id = db.Column(db.String(255))

    # 课程归属
    course_belonging = db.Column(db.String(255))

    # 课程学分
    course_credit = db.Column(db.Float)

    # 教学班名称
    class_name = db.Column(db.String(255))

    # 学时类型
    hour_type = db.Column(db.String(255))

    # 开课学时
    open_hours = db.Column(db.Integer)

    # 排课学时
    schedule_hours = db.Column(db.Integer)

    # 总学时
    total_hours = db.Column(db.Integer)

    # 排课优先级
    priority = db.Column(db.Integer)

    # 教学班人数
    class_size = db.Column(db.Integer)

    # 课程性质
    course_nature = db.Column(db.String(255))

    # 开课校区
    campus = db.Column(db.String(255))

    # 是否外聘
    is_external = db.Column(db.Boolean)

    # 开课院系
    teaching_department = db.Column(db.String(255))

    # 开课周次学时
    week_hours = db.Column(db.String(255))

    # 连排节次
    consecutive_periods = db.Column(db.String(255))

    # 指定教室类型
    assigned_room_type = db.Column(db.String(255))

    # 指定教室
    assigned_room = db.Column(db.String(255))

    # 指定教学楼
    assigned_building = db.Column(db.String(255))

    # 指定时间
    assigned_time = db.Column(db.String(255))
