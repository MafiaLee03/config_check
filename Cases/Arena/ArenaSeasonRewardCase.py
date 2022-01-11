#coding=utf-8
from Core.BaseCase import BaseCase

class ArenaSeasonRewardCase(BaseCase):
    """
    ArenaSeasonReward表检查
    """
    def run(self):
        self.title = "ArenaSeasonReward表检查"
        self.desc = "检查内容：奖励是否存在、排名区间配置规范"
        self.add_depends("RewardConfig")
        listreward = []
        for i in self._RewardConfig.get_records():
            RewardTag = i.tag
            listreward.append(RewardTag)
        self.add_depends("ArenaSeasonReward")
        rank = 0
        for record in self._ArenaSeasonReward.get_records():
            dailyRankReward = record.seasonRewards
            self.do_assert(dailyRankReward in listreward, "不存在的奖励",record,dailyRankReward + "在rewardconfig中没有")
            self.do_assert(int(record.tag) > rank,"配置错误的排名",record,"配置值" + record.tag + "应大于上一配置排名%d"%(rank))
            rank = int(record.tag)