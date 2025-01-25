from  app.extensions import db

class TeachingBuilding(db.Model):
    __tablename__ = 'teaching_building'

    # 教学楼ID (自增主键)
    building_id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    # 教学楼编号
    building_code = db.Column(db.String(255), nullable=False, unique=True)

    # 教学楼名称
    building_name = db.Column(db.String(255), nullable=False)

    # 校区名称
    campus_name = db.Column(db.String(255), nullable=False)

    # 可用状态
    is_available = db.Column(db.Boolean, nullable=False)
