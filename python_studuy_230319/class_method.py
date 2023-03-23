"""
类方法学习
"""

class Human:
    nums = 0

    def __init__(self, nums):
        self.nums = nums

    # 普通的方法
    def count_people(self):
        print('这是普通方法')
        self.nums += 1
        print(self.nums)

    # 类方法
    @classmethod
    def count_people_new(cls):
        print('这是静态方法')
        result = lambda x: x+2
        print(result(Human.nums))

    

if __name__ == '__main__':
    print(Human.nums)
    Human(5).count_people()
    Human.count_people_new()