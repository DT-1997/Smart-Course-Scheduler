from app.blueprints.upload import upload_bp

import pandas as pd
from flask import request, jsonify
from app.extensions import db, create_logger
from app.models import Class, Department, Teacher, Classroom, TeachingBuilding, Course, ScheduleTask, MajorDirection, Major



# Create a logger for the load module
logger = create_logger('upload', 'logs/upload.log')

def convert_to_boolean(value):
    """将自定义值（如 '未毕业', '已毕业'）转换为布尔值"""
    if isinstance(value, str):
        value = value.strip()  # 去掉前后空格
        if value in ['是', '已毕业', '启用', '固定', '可用']:
            return True
        elif value in ['否', '未毕业', '禁用', '非固定', '不可用']:
            return False
    return None  # 如果无法识别，则返回 None

def convert_nan_to_none(value):
    """将 NaN 转换为 None"""
    if pd.isna(value):  # 判断是否是 NaN
        return None
    return value


@upload_bp.route('/upload-class', methods=['POST'])
def upload_excel():
    # 获取上传的文件
    file = request.files['file']

    if file.filename.endswith('.xls') or file.filename.endswith('.xlsx'):
        # 读取 Excel 文件，将第二行作为列名
        df = pd.read_excel(file, engine='openpyxl', header=1)

        # 遍历每一行数据并插入到数据库
        for index, row in df.iterrows():
            try:
                # 逐列转换数据，确保 NaN 转换为 None，布尔值转换正确
                fixed_classroom_number = convert_nan_to_none(row.iloc[21])  # 第 22 列
                is_fixed_classroom = convert_to_boolean(row.iloc[22])  # 第 23 列
                is_graduated = convert_to_boolean(row.get('是否毕业'))
                is_expanded = convert_to_boolean(row.get('是否扩招'))

                # 创建 Class 实例
                new_class = Class(
                    class_number=convert_nan_to_none(row.get('班级编号')),
                    class_name=convert_nan_to_none(row.get('班级名称')),
                    class_short_name=convert_nan_to_none(row.get('班级简称')),
                    duration=convert_nan_to_none(row.get('学制')),
                    education_level=convert_nan_to_none(row.get('培养层次')),
                    class_type=convert_nan_to_none(row.get('班级类别')),
                    counselor=convert_nan_to_none(row.get('辅导员')),
                    head_teacher=convert_nan_to_none(row.get('班主任')),
                    monitor=convert_nan_to_none(row.get('班长')),
                    class_assistant=convert_nan_to_none(row.get('班助')),
                    expected_graduation_year=convert_nan_to_none(row.get('预计毕业年度')),
                    is_graduated=is_graduated,
                    class_size=convert_nan_to_none(row.get('班级人数')),
                    gender_distribution=convert_nan_to_none(row.get('性别分布(男/女)')),
                    max_class_size=convert_nan_to_none(row.get('班级最大人数')),
                    enrollment_year=convert_nan_to_none(row.get('入学年份')),
                    department=convert_nan_to_none(row.get('所属院系')),
                    major_id=convert_nan_to_none(row.get('专业编号')),
                    major_name=convert_nan_to_none(row.get('专业')),
                    major_direction=convert_nan_to_none(row.get('专业方向')),
                    campus=convert_nan_to_none(row.get('校区')),
                    fixed_classroom_number=fixed_classroom_number,
                    is_fixed_classroom=is_fixed_classroom,
                    remarks=convert_nan_to_none(row.get('备注')),
                    head_teacher_phone=convert_nan_to_none(row.get('班主任联系电话')),
                    head_teacher_id=convert_nan_to_none(row.get('班主任工号')),
                    graduation_year_semester=convert_nan_to_none(row.get('毕业学年学期')),
                    is_expanded=is_expanded,
                    academic_advisor=convert_nan_to_none(row.get('学业导师'))
                )

                # 插入到数据库
                db.session.add(new_class)

            except Exception as e:
                # 捕获错误并打印，继续处理下一行
                print(f"Error processing row {index}: {e}")
                continue

        # 提交事务
        db.session.commit()
        return jsonify({"message": "Data uploaded successfully!"}), 200
    else:
        return jsonify({"message": "Invalid file format!"}), 400

@upload_bp.route('/upload-department', methods=['POST'])
def upload_department_excel():
    # 获取上传的文件
    file = request.files['file']

    if file.filename.endswith('.xls') or file.filename.endswith('.xlsx'):
        # 读取 Excel 文件，从第一行开始作为列名
        df = pd.read_excel(file, engine='openpyxl', header=0)

        # 遍历每一行数据并插入到数据库
        for index, row in df.iterrows():
            try:
                # 转换布尔值和空值
                is_entity = convert_to_boolean(row.get('是否实体'))
                is_enabled = convert_to_boolean(row.get('是否启用'))
                is_open = convert_to_boolean(row.get('是否开课教研室'))

                # 创建 Department 实例
                new_department = Department(
                    department_code=convert_nan_to_none(row.get('部门代码')),
                    department_name=convert_nan_to_none(row.get('部门名称')),
                    department_number=convert_nan_to_none(row.get('部门序号')),
                    department_english_name=convert_nan_to_none(row.get('部门英文名称')),
                    department_short_name=convert_nan_to_none(row.get('部门简称')),
                    department_address=convert_nan_to_none(row.get('部门地址')),
                    is_entity=is_entity,
                    administrative_leader=convert_nan_to_none(row.get('行政负责人')),
                    party_committee_leader=convert_nan_to_none(row.get('党委负责人')),
                    establishment_date=convert_nan_to_none(row.get('建立年月')),
                    expiration_date=convert_nan_to_none(row.get('失效日期')),
                    unit_type=convert_nan_to_none(row.get('所属单位类别')),
                    unit_office_type=convert_nan_to_none(row.get('所属单位办别')),
                    superior_department=convert_nan_to_none(row.get('上级部门')),
                    fixed_building=convert_nan_to_none(row.get('固定教学楼')),
                    teaching_department=convert_nan_to_none(row.get('开课院系')),
                    class_department=convert_nan_to_none(row.get('上课院系')),
                    landline_phone=convert_nan_to_none(row.get('固定电话')),
                    remarks=convert_nan_to_none(row.get('备注说明')),
                    is_enabled=is_enabled,
                    is_class_research_room=is_open
                )

                # 插入到数据库
                db.session.add(new_department)

            except Exception as e:
                # 捕获错误并打印日志，继续处理下一行
                logger.error(f"Error processing row {index}: {e}")
                continue

        # 提交事务
        try:
            db.session.commit()
            logger.info("Department data uploaded successfully.")
            return jsonify({"message": "Department data uploaded successfully!"}), 200
        except Exception as e:
            logger.error(f"Error committing to database: {e}")
            db.session.rollback()
            return jsonify({"message": "Failed to upload department data."}), 500
    else:
        logger.error("Invalid file format.")
        return jsonify({"message": "Invalid file format!"}), 400

@upload_bp.route('/upload-teacher', methods=['POST'])
def upload_teacher_excel():
    # 获取上传的文件
    file = request.files['file']

    if file.filename.endswith('.xls') or file.filename.endswith('.xlsx'):
        # 读取 Excel 文件，从第一行开始作为列名
        df = pd.read_excel(file, engine='openpyxl', header=1)

        # 遍历每一行数据并插入到数据库
        for index, row in df.iterrows():
            try:
                # 转换布尔值和空值
                is_external = convert_to_boolean(row.get('是否外聘'))


                # 创建 Teacher 实例
                new_teacher = Teacher(
                    employee_id=convert_nan_to_none(row.get('工号')),
                    name=convert_nan_to_none(row.get('姓名')),
                    gender=convert_nan_to_none(row.get('性别')),
                    english_name=convert_nan_to_none(row.get('英文姓名')),
                    ethnicity=convert_nan_to_none(row.get('民族')),
                    title=convert_nan_to_none(row.get('职称')),
                    unit=convert_nan_to_none(row.get('单位')),
                    is_external=is_external,
                    staff_type=convert_nan_to_none(row.get('教职工类别'))
                )

                # 插入到数据库
                db.session.add(new_teacher)

            except Exception as e:
                # 捕获错误并打印日志，继续处理下一行
                logger.error(f"Error processing row {index}: {e}")
                continue

        # 提交事务
        try:
            db.session.commit()
            logger.info("Teacher data uploaded successfully.")
            return jsonify({"message": "Teacher data uploaded successfully!"}), 200
        except Exception as e:
            logger.error(f"Error committing to database: {e}")
            db.session.rollback()
            return jsonify({"message": "Failed to upload teacher data."}), 500
    else:
        logger.error("Invalid file format.")
        return jsonify({"message": "Invalid file format!"}), 400

@upload_bp.route('/upload-classroom', methods=['POST'])
def upload_classroom_excel():
    # 获取上传的文件
    file = request.files['file']

    if file.filename.endswith('.xls') or file.filename.endswith('.xlsx'):
        # 读取 Excel 文件，从第一行开始作为列名
        df = pd.read_excel(file, engine='openpyxl', header=1)

        # 遍历每一行数据并插入到数据库
        for index, row in df.iterrows():
            try:
                # 转换布尔值和空值
                has_air_conditioning = convert_to_boolean(row.get('是否有空调'))
                is_enabled = convert_to_boolean(row.get('是否启用'))

                # 创建 Classroom 实例
                new_classroom = Classroom(
                    classroom_code=convert_nan_to_none(row.get('教室编号')),
                    classroom_name=convert_nan_to_none(row.get('教室名称')),
                    campus=convert_nan_to_none(row.get('校区')),
                    teaching_building=convert_nan_to_none(row.get('教学楼')),
                    floor=convert_nan_to_none(row.get('所在楼层')),
                    classroom_tag=convert_nan_to_none(row.get('教室标签')),
                    classroom_type=convert_nan_to_none(row.get('教室类型')),
                    exam_capacity=convert_nan_to_none(row.get('考场容纳')),
                    max_class_capacity=convert_nan_to_none(row.get('最大上课容纳人数')),
                    has_air_conditioning=has_air_conditioning,
                    is_enabled=is_enabled,
                    classroom_description=convert_nan_to_none(row.get('教室描述')),
                    management_department=convert_nan_to_none(row.get('管理部门')),
                    weekly_schedule_hours=convert_nan_to_none(row.get('周安排学时')),
                    classroom_area=convert_nan_to_none(row.get('教室面积')),
                    desk_chair_type=convert_nan_to_none(row.get('桌椅类型'))
                )

                # 插入到数据库
                db.session.add(new_classroom)

            except Exception as e:
                # 捕获错误并打印日志，继续处理下一行
                logger.error(f"Error processing row {index}: {e}")
                continue

        # 提交事务
        try:
            db.session.commit()
            logger.info("Classroom data uploaded successfully.")
            return jsonify({"message": "Classroom data uploaded successfully!"}), 200
        except Exception as e:
            logger.error(f"Error committing to database: {e}")
            db.session.rollback()
            return jsonify({"message": "Failed to upload classroom data."}), 500
    else:
        logger.error("Invalid file format.")
        return jsonify({"message": "Invalid file format!"}), 400

@upload_bp.route('/upload-teaching-building', methods=['POST'])
def upload_teaching_building_excel():
    # 获取上传的文件
    file = request.files['file']

    if file.filename.endswith('.xls') or file.filename.endswith('.xlsx'):
        # 读取 Excel 文件，从第二行开始作为列名
        df = pd.read_excel(file, engine='openpyxl', header=1)

        # 遍历每一行数据并插入到数据库
        for index, row in df.iterrows():
            try:
                # 转换布尔值和空值
                is_available = convert_to_boolean(row.get('可用状态'))

                # 创建 TeachingBuilding 实例
                new_teaching_building = TeachingBuilding(
                    building_code=convert_nan_to_none(row.get('教学楼编号')),
                    building_name=convert_nan_to_none(row.get('教学楼名称')),
                    campus_name=convert_nan_to_none(row.get('校区名称')),
                    is_available=is_available
                )

                # 插入到数据库
                db.session.add(new_teaching_building)

            except Exception as e:
                # 捕获错误并打印日志，继续处理下一行
                logger.error(f"Error processing row {index}: {e}")
                continue

        # 提交事务
        try:
            db.session.commit()
            logger.info("Teaching building data uploaded successfully.")
            return jsonify({"message": "Teaching building data uploaded successfully!"}), 200
        except Exception as e:
            logger.error(f"Error committing to database: {e}")
            db.session.rollback()
            return jsonify({"message": "Failed to upload teaching building data."}), 500
    else:
        logger.error("Invalid file format.")
        return jsonify({"message": "Invalid file format!"}), 400

@upload_bp.route('/upload-course', methods=['POST'])
def upload_course_excel():
    # 获取上传的文件
    file = request.files['file']

    if file.filename.endswith('.xls') or file.filename.endswith('.xlsx'):
        # 读取 Excel 文件，从第一行开始作为列名
        df = pd.read_excel(file, engine='openpyxl', header=0)

        # 遍历每一行数据并插入到数据库
        for index, row in df.iterrows():
            try:
                # 转换布尔值和空值
                is_enabled = convert_to_boolean(row.get('是否启用'))
                is_pure_practice = convert_to_boolean(row.get('是否纯实践环节'))

                # 创建 Course 实例
                new_course = Course(
                    course_code=convert_nan_to_none(row.get('课程编号')),
                    course_name=convert_nan_to_none(row.get('课程名称')),
                    course_category=convert_nan_to_none(row.get('课程类别')),
                    course_property=convert_nan_to_none(row.get('课程属性')),
                    course_type=convert_nan_to_none(row.get('课程类型')),
                    course_nature=convert_nan_to_none(row.get('课程性质')),
                    course_english_name=convert_nan_to_none(row.get('课程英文名')),
                    teaching_department=convert_nan_to_none(row.get('开课院系')),
                    is_enabled=is_enabled,
                    total_hours=convert_nan_to_none(row.get('总学时')),
                    theory_hours=convert_nan_to_none(row.get('理论学时')),
                    experiment_hours=convert_nan_to_none(row.get('实验学时')),
                    computer_hours=convert_nan_to_none(row.get('上机学时')),
                    practical_hours=convert_nan_to_none(row.get('实践学时')),
                    other_hours=convert_nan_to_none(row.get('其他学时')),
                    credit=convert_nan_to_none(row.get('学分')),
                    weekly_hours=convert_nan_to_none(row.get('周学时')),
                    is_pure_practice=is_pure_practice
                )

                # 插入到数据库
                db.session.add(new_course)

            except Exception as e:
                # 捕获错误并打印日志，继续处理下一行
                logger.error(f"Error processing row {index}: {e}")
                continue

        # 提交事务
        try:
            db.session.commit()
            logger.info("Course library data uploaded successfully.")
            return jsonify({"message": "Course library data uploaded successfully!"}), 200
        except Exception as e:
            logger.error(f"Error committing to database: {e}")
            db.session.rollback()
            return jsonify({"message": "Failed to upload course library data."}), 500
    else:
        logger.error("Invalid file format.")
        return jsonify({"message": "Invalid file format!"}), 400


@upload_bp.route('/upload-schedule-task', methods=['POST'])
def upload_schedule_task_excel():
    # 获取上传的文件
    file = request.files['file']

    if file.filename.endswith('.xls') or file.filename.endswith('.xlsx'):
        # 读取 Excel 文件，从第一行开始作为列名
        df = pd.read_excel(file, engine='openpyxl', header=0)

        # 遍历每一行数据并插入到数据库
        for index, row in df.iterrows():
            try:
                # 转换布尔值和空值
                is_external = convert_to_boolean(row.get('是否外聘'))

                # 创建 Course 实例
                new_schedule_task = ScheduleTask(
                    academic_year_term=convert_nan_to_none(row.get('学年学期')),
                    course_code=convert_nan_to_none(row.get('课程编号')),
                    course_name=convert_nan_to_none(row.get('课程名称')),
                    teacher_id=convert_nan_to_none(row.get('教师工号')),
                    teacher_name=convert_nan_to_none(row.get('任课教师')),
                    class_composition=convert_nan_to_none(row.get('教学班组成')),
                    class_id=convert_nan_to_none(row.get('教学班编号')),
                    course_belonging=convert_nan_to_none(row.get('课程归属')),
                    course_credit=convert_nan_to_none(row.get('课程学分')),
                    class_name=convert_nan_to_none(row.get('教学班名称')),
                    hour_type=convert_nan_to_none(row.get('学时类型')),
                    open_hours=convert_nan_to_none(row.get('开课学时')),
                    schedule_hours=convert_nan_to_none(row.get('排课学时')),
                    total_hours=convert_nan_to_none(row.get('总学时')),
                    priority=convert_nan_to_none(row.get('排课优先级')),
                    class_size=convert_nan_to_none(row.get('教学班人数')),
                    course_nature=convert_nan_to_none(row.get('课程性质')),
                    campus=convert_nan_to_none(row.get('开课校区')),
                    is_external=is_external,
                    teaching_department=convert_nan_to_none(row.get('开课院系')),
                    week_hours=convert_nan_to_none(row.get('开课周次学时')),
                    consecutive_periods=convert_nan_to_none(row.get('连排节次')),
                    assigned_room_type=convert_nan_to_none(row.get('指定教室类型')),
                    assigned_room=convert_nan_to_none(row.get('指定教室')),
                    assigned_building=convert_nan_to_none(row.get('指定教学楼')),
                    assigned_time=convert_nan_to_none(row.get('指定时间'))
                )

                # 插入到数据库
                db.session.add(new_schedule_task)

            except Exception as e:
                # 捕获错误并打印日志，继续处理下一行
                logger.error(f"Error processing row {index}: {e}")
                continue

        # 提交事务
        try:
            db.session.commit()
            logger.info("Schedule Task data uploaded successfully.")
            return jsonify({"message": "Schedule Task data uploaded successfully!"}), 200
        except Exception as e:
            logger.error(f"Error committing to database: {e}")
            db.session.rollback()
            return jsonify({"message": "Failed to upload Schedule Task data."}), 500
    else:
        logger.error("Invalid file format.")
        return jsonify({"message": "Invalid file format!"}), 400

@upload_bp.route('/upload-major-direction', methods=['POST'])
def upload_major_direction_excel():
    # 获取上传的文件
    file = request.files['file']

    if file.filename.endswith('.xls') or file.filename.endswith('.xlsx'):
        # 读取 Excel 文件，从第十六行开始作为列名
        df = pd.read_excel(file, engine='openpyxl', header=15)

        # 遍历每一行数据并插入到数据库
        for index, row in df.iterrows():
            try:
                # 创建 MajorDirection 实例
                new_major_direction = MajorDirection(
                    direction_code=convert_nan_to_none(row.get('专业方向编号*')),
                    direction_name=convert_nan_to_none(row.get('专业方向名称*')),
                    grade=convert_nan_to_none(row.get('年级*')),
                    department=convert_nan_to_none(row.get('院系*')),
                    major_code=convert_nan_to_none(row.get('专业编号*')),
                    major_name=convert_nan_to_none(row.get('专业名称'))  # Changed column name
                )

                # 插入到数据库
                db.session.add(new_major_direction)

            except Exception as e:
                # 捕获错误并打印日志，继续处理下一行
                logger.error(f"Error processing row {index}: {e}")
                continue

        # 提交事务
        try:
            db.session.commit()
            logger.info("Major direction data uploaded successfully.")
            return jsonify({"message": "Major direction data uploaded successfully!"}), 200
        except Exception as e:
            logger.error(f"Error committing to database: {e}")
            db.session.rollback()
            return jsonify({"message": "Failed to upload major direction data."}), 500
    else:
        logger.error("Invalid file format.")
        return jsonify({"message": "Invalid file format!"}), 400

@upload_bp.route('/upload-major', methods=['POST'])
def upload_major_excel():
    # 获取上传的文件
    file = request.files['file']

    if file.filename.endswith('.xls') or file.filename.endswith('.xlsx'):
        # 读取 Excel 文件，从第二行开始作为列名
        df = pd.read_excel(file, engine='openpyxl', header=1)  # 设置header=1从第二行开始读取



        # 遍历每一行数据并插入到数据库
        for index, row in df.iterrows():
            try:
                is_established = convert_to_boolean(row.get('开办状态'))

                # 创建 MajorData 实例
                new_major = Major(
                    major_short_name=convert_nan_to_none(row.get('专业简称')),
                    duration=convert_nan_to_none(row.get('学制')),
                    english_name=convert_nan_to_none(row.get('英文名称')),
                    is_established=is_established,
                    department=convert_nan_to_none(row.get('所属院系')),
                    major_name=convert_nan_to_none(row.get('专业名称')),
                    major_code=convert_nan_to_none(row.get('专业编号')),
                    education_level=convert_nan_to_none(row.get('培养层次'))
                )

                # 插入到数据库
                db.session.add(new_major)

            except Exception as e:
                # 捕获错误并打印日志，继续处理下一行
                logger.error(f"Error processing row {index}: {e}")
                continue

        # 提交事务
        try:
            db.session.commit()
            logger.info("Major data uploaded successfully.")
            return jsonify({"message": "Major data uploaded successfully!"}), 200
        except Exception as e:
            logger.error(f"Error committing to database: {e}")
            db.session.rollback()
            return jsonify({"message": "Failed to upload major data."}), 500
    else:
        logger.error("Invalid file format.")
        return jsonify({"message": "Invalid file format!"}), 400

