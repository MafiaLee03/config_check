#coding=utf-8
from Core.BaseCase import BaseCase

class ArenaRobotCase(BaseCase):
    """
    ArenaRobot表检查
    """
    def run(self):
        self.title = "ArenaRobot表检查"
        self.desc = "检查内容：机器人配置是否正确、排名区间配置规范"
        self.add_depends("Skill_Base")
        listrobot = []
        for i in self._Skill_Base.get_records():
            robotid = i.id
            listrobot.append(robotid)
        self.add_depends("Skill_Base")
        rank = 0
        for record in self._Skill_Base.get_records():
            i = record.timeline
            # dailyRankReward = record.robotBattleId
            # self.do_assert(int(record.tag) > rank,"配置错误的排名",record,"配置值" + record.tag + "应大于上一配置排名%d"%(rank))
            # rank = int(record.tag)
            # for i in dailyRankReward:
            self.do_assert(record in listrobot,"机器人配置错误",record,"配置值：")
            print(i)