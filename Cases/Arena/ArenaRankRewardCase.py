#coding=utf-8
from Core.BaseCase import BaseCase

class ArenaRankRewardCase(BaseCase):
    """
    ArenaRankReward表检查
    """
    def run(self):
        self.title = "ArenaRankReward表检查"
        self.desc = "检查内容：奖励是否存在"
        self.add_depends("RewardConfig")
        listreward = []
        for i in self._RewardConfig.get_records():
            RewardTag = i.tag
            listreward.append(RewardTag)
        self.add_depends("ArenaRankReward")

        for record in self._ArenaRankReward.get_records():
            dailyRankReward = record.dailyRankReward
            self.do_assert(dailyRankReward in listreward, "不存在的奖励",record,dailyRankReward + "在rewardconfig中没有")
            