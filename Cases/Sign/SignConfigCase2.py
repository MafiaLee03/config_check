#coding=utf-8
from Core.BaseCase import BaseCase

class SignConfigCase2(BaseCase):
    """
    月签
   根据SignConfig。rewardId检查是否存在对应奖励配置RewardConfig.tag
    """

    def run(self):
        self.title = "签到配置奖励测试"
        self.desc = "根据SignConfig。rewardId检查是否存在对应奖励配置RewardConfig.tag"
        self.add_depends("SignConfig")
        self.add_depends("RewardConfig")
        for record in self._SignConfig.get_records():
            rewardId = record.rewardId
            if rewardId:
                Rc = self._RewardConfig.get_record(rewardId)
                if Rc == None:
                    self.do_assert(0, "奖励配置表到RewardConfig"+"没有找到对应的SignConfig.rewardId:"+rewardId+"，请检查配置文件", record, self._error_cnt)