#coding=utf-8
from Core.BaseCase import BaseCase
class FundConfigCase1(BaseCase):
    """
    检查基金配置奖励是否存在奖励配置表RewardConfig中
    """
    def run(self):
        self.title = "基金配置表FundConfig和RewardConfig奖励配置是否一致测试"
        self.desc = "基金配置表"
        self.add_depends("FundConfig")
        self.add_depends("RewardConfig")

        for record in self._FundConfig.get_records():
            freeReward=record.freeReward
            specialReward = record.specialReward
            if freeReward:
                free=self._RewardConfig.get_record(freeReward)
                if free==None:
                    self.do_assert(0, "奖励配置表RewardConfig" + "没有找到对应的FundCongfig.freeReward:" + freeReward + "，请检查配置文件", record, self._error_cnt)
            if specialReward:
                special=self._RewardConfig.get_record(specialReward)
                if special == None:
                    self.do_assert(0, "奖励配置表RewardConfig" + "没有找到对应的FundCongfig.specialReward:" + specialReward + "，请检查配置文件",record, self._error_cnt)



