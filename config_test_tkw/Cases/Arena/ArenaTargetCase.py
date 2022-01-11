#coding=utf-8
from Core.BaseCase import BaseCase
import re

class ArenaTargetCase(BaseCase):
    """
    ArenaTarget表检查
    """
    def run(self):
        self.title = "ArenaTarget表检查"
        self.desc = "检查内容：随机对手逻辑规范、排名区间配置规范"
        self.add_depends("ArenaTarget")
        rank = 0
        for record in self._ArenaTarget.get_records():
            # print("********")
            # print(record.firstTarget)
            # print(record.firstTarget['type'])
            firstTarget = record.firstTarget
            type1 = firstTarget['type']
            min1 = firstTarget['min']
            max1 = firstTarget['max']
            self.do_assert(type1 in ['fixed','relative'],"随机类型错误",record,"配置值：" + record.firstTarget['type'])
            if type1 == "relative":
                self.do_assert(min1 < max1,"随机区间错误",record,"左区间:%d"%(min1) + "应小于右区间:%d"%(max1))
            else :
                self.do_assert(min1 <= max1,"随机区间错误",record,"左区间:%d"%(min1) + "应小于右等于区间:%d"%(max1))
            self.do_assert(int(record.tag) > rank,"配置错误的排名",record,"配置值" + record.tag + "应大于上一配置排名%d"%(rank))
            rank = int(record.tag)