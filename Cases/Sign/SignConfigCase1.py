#coding=utf-8
from Core.BaseCase import BaseCase
class SignConfigCase1(BaseCase):
    """
    月签
    检测SignConfig.tag和SignConfig.rewardId命名等
    """
    def run(self):
        self.title = "签到配置表SignConfig测试"
        self.desc = "月签配置表"
        self.add_depends("SignConfig")
        s="sign_"
        for record in self._SignConfig.get_records():
            rewardId=record.rewardId.split(s)[1]
            self.do_assert(int(record.tag)==int(rewardId), "SignConfig.tag:"+record.tag+" 和 "+"SignConfig.rewardId:"+record.rewardId+"命名序号不相等，请检查配置",record,self._error_cnt)

