from app.extensions import db

class Department(db.Model):
    __tablename__ = 'department'

    # 部门ID (自增主键)
    department_id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    # 部门代码
    department_code = db.Column(db.String(255), nullable=True, unique=True)

    # 部门名称
    department_name = db.Column(db.String(255), nullable=False)

    # 部门序号
    department_number = db.Column(db.Integer)

    # 部门英文名称
    department_english_name = db.Column(db.String(255))

    # 部门简称
    department_short_name = db.Column(db.String(255))

    # 部门地址
    department_address = db.Column(db.String(255))

    # 是否实体
    is_entity = db.Column(db.Boolean)

    # 行政负责人
    administrative_leader = db.Column(db.String(255))

    # 党委负责人
    party_committee_leader = db.Column(db.String(255))

    # 建立年月
    establishment_date = db.Column(db.String(100))

    # 失效日期
    expiration_date = db.Column(db.String(100))

    # 所属单位类别
    unit_type = db.Column(db.String(255))

    # 所属单位办别
    unit_office_type = db.Column(db.String(255))

    # 上级部门
    superior_department = db.Column(db.String(255))

    # 固定教学楼
    fixed_building = db.Column(db.String(255))

    # 开课院系
    teaching_department = db.Column(db.String(255))

    # 上课院系
    class_department = db.Column(db.String(255))

    # 固定电话
    landline_phone = db.Column(db.String(50))

    # 备注说明
    remarks = db.Column(db.String(255))

    # 是否启用
    is_enabled = db.Column(db.Boolean)

    # 是否开课教研室
    is_class_research_room = db.Column(db.Boolean)