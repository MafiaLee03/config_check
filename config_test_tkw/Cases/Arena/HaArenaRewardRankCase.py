from Core.BaseCase import BaseCase

class HaArenaRewardRankCase(BaseCase):
    def run(self):
        self.title = "HA竞技场排行奖励表检查"
        self.desc = "只是尝试一下"
        self.add_depends("ArenaRewardRank")
        for i in self._ArenaRewardRank.get_records():
            print(i.id)