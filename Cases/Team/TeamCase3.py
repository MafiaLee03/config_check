#coding=utf-8
from Core.BaseCase import BaseCase

class TeamCase3(BaseCase):
    """
    验证NpcTeamValue英雄的攻击范围
    """
    def run(self):
        self.title = "验证NpcTeamValue英雄的攻击范围"
        # self.desc = "aaaa1"
        self.add_depends("NpcTeamValue")
        self.add_depends("TeamBase")
        self.add_depends("Translate")
        # 去掉开场武将
        bsTeam = ['bs_player_t01', 'bs_player_t02', 'bs_player_t03', 'bs_enemy_t01', 'ShangDang_b01_t03', 'Boss_zhouyu', 'Boss_sunce']
        for record in self._NpcTeamValue.get_records():
            teamId = record.roleModel
            npcName = self._Translate.get_record(record.name).text
            if record.tag in bsTeam:
                continue
            teamBase = self._TeamBase.get_record(teamId)
            self.do_assert(teamBase.atkDistance == record.atkDistance,
                           "攻击范围 teamBase atkDistance:{}, NpcTeamValue atkDistance:{} ".format(teamBase.atkDistance,
                                                                                          record.atkDistance),
                           record, npcName)