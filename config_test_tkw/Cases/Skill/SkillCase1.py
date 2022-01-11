#coding=utf-8
from Core.BaseCase import BaseCase

class SkillCase1(BaseCase):
    """
    验证主动技能是否配置AI
    """
    def run(self):
        self.title = "验证主动技能是否配置AI"
        # self.desc = "描述描述"
        self.add_depends("TeamBase")
        self.add_depends("SkillAiConfig")
        self.add_depends("Translate")
        for record in self._TeamBase.get_records():
            if 1 == record.ifVisible:
                skill = "Skill" + record.tag
                skillAi = self._SkillAiConfig.get_record(skill)
                name = self._Translate.get_record(record.name).text
                self.do_assert(skillAi, "主动技能{}  AI没有配置".format(skill),
                               record, name)
