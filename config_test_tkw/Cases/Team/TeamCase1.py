#coding=utf-8
from Core.BaseCase import BaseCase

class TeamCase1(BaseCase):
    """
    验证当前已开放的武将，布阵模型处-职业图标
    """
    def run(self):
        self.title = "验证当前已开放的武将，布阵模型处-职业图标"
        # self.desc = "aaaa1"
        self.add_depends("TeamRoleModel")
        self.add_depends("TeamBase")
        # 根据配置当前
        dic = {"embattle_icon_general_type_01": 1, "embattle_icon_general_type_03": 2,
               "embattle_icon_general_type_04": 3}
        for record in self._TeamBase.get_records():
            # 判断当前武将是否开放可见
            if 1 == record.ifVisible:
                # 获取TeamBase表中job职业
                job = record.job
                # 获取TeamRoleModel表中
                teamIcon = self._TeamRoleModel.get_record(record.tag).generalTypeIcon
                self.do_assert(job == dic[teamIcon], "teamBase job:{}, TeamRoleModel job:{} ".format(job, teamIcon),
                               record)
