#coding=utf-8
from Core.BaseCase import BaseCase

class DemoCase1(BaseCase):
    """
    这里简单描述一下这个测试用例的场景
    """
    def run(self):
        self.title = "Demo"
        self.desc = "Demo"
        self.add_depends("Army")
        for record in self._Army.get_records():
            print(record.tag, record.job, record.formation, record.initNum, record.armyGenius)
