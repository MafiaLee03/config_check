#coding=utf-8
from Core.BaseCase import BaseCase

class ArenaTimesRewardCase(BaseCase):
    """
    ArenaTimesReward表检查
    """
    def run(self):
        self.title = "ArenaTimesReward表检查"
        self.desc = "检查内容：奖励是否存在"
        self.add_depends("RewardConfig")
        listreward = []
        for i in self._RewardConfig.get_records():
            RewardTag = i.tag
            listreward.append(RewardTag)
        self.add_depends("ArenaTimesReward")

        for record in self._ArenaTimesReward.get_records():
            dailyRankReward = record.arenaTimesReward
            self.do_assert(dailyRankReward in listreward, "不存在的奖励",record,dailyRankReward + "在rewardconfig中没有")
            