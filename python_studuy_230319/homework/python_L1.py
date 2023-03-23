"""
python L1课后练习
编写学员实体类，对应属性包含：学号、姓名、性别。
编写学员名单管理类，实现删除学员方法、查询学员方法。
"""
class Student:
    """
    学员实体类
    """
    def __init__(self, student_id, name, sex):
        self.student_id = student_id
        self.name = name
        self.sex = sex

class StudentList:
    def __init__(self, student_list):
        self.s_list = student_list

    def get(self, student_id):
        """
        根据 student_id 查询信息
        """
        if not student_id:
            print('请输入学员id')
            return False

        for student_list in self.s_list:
            if student_list.student_id == student_id:
                print(f'student_id:{student_id}的数据为：[{student_list.name, student_list.sex}]\n')
                return [{student_list.student_id, student_list.name, student_list.sex}]

    def delete(self, student_id):
        """
        根据 student_id 删除信息
        """
        if not student_id:
            print('请输入学员id')
            return False

        for student_list in self.s_list:
            if student_list.student_id == student_id:
                self.s_list.remove(student_list)

        # 验证下结果
        print(f'验证下删除student_id{student_id}后，剩余的学员数据：')
        for stu_list in self.s_list:
            print([stu_list.student_id, stu_list.name, stu_list.sex])

if __name__ == '__main__':
    # 入参自己定义
    s1 = Student(1,'zhangsan','man')
    s2 = Student(2,'lisi','woman')
    s3 = Student(3,'wangwu','man')
    # 初始化一个成员名单
    s_list = StudentList([s1, s2, s3])
    # 实现get()方法
    s_list.get(1)
    # 实现delete
    s_list.delete(1)