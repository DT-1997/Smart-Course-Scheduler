from app.extensions import db


class Classroom(db.Model):
    __tablename__ = 'classroom'

    # 教室 ID (自增主键)
    classroom_id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    # 教室编号
    classroom_code = db.Column(db.String(255), nullable=False, unique=True)

    # 教室名称
    classroom_name = db.Column(db.String(255), nullable=False)

    # 校区
    campus = db.Column(db.String(255), nullable=False)

    # 教学楼
    teaching_building = db.Column(db.String(255), nullable=False)

    # 所在楼层
    floor = db.Column(db.String(100), nullable=False)

    # 教室标签
    classroom_tag = db.Column(db.String(255))

    # 教室类型
    classroom_type = db.Column(db.String(255), nullable=False)

    # 考场容纳人数
    exam_capacity = db.Column(db.Integer)

    # 最大上课容纳人数
    max_class_capacity = db.Column(db.Integer, nullable=False)

    # 是否有空调
    has_air_conditioning = db.Column(db.Boolean, nullable=False)

    # 是否启用
    is_enabled = db.Column(db.Boolean, nullable=False)

    # 教室描述
    classroom_description = db.Column(db.String(255))

    # 管理部门
    management_department = db.Column(db.String(255))

    # 周安排学时
    weekly_schedule_hours = db.Column(db.Integer)

    # 教室面积
    classroom_area = db.Column(db.Float)

    # 桌椅类型
    desk_chair_type = db.Column(db.String(255))