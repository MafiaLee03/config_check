#coding=utf-8
from Core.BaseCase import BaseCase
class MallCase1(BaseCase):
    """
    基金配置表奖励的奖励配置是否存在，依赖之类的是否存在
    """
    def run(self):
        self.title = "基金配置表Mill测试"
        self.desc = "基金配置表"
        self.add_depends("Mall")
        self.add_depends("Charge")
        self.add_depends("RewardConfig")

        for record in self._Mall.get_records():
            charge=record.chargeTag
            fixedGift = record.fixedGift
            if charge:
                c=self._Charge.get_record(charge)
                if c==None:
                    self.do_assert(0, "配置表Charge" + "没有找到到对应的Mall.chargeTag:" + charge + "，请检查配置文件", record, self._error_cnt)
            if fixedGift:
                Gift=self._RewardConfig.get_record(fixedGift)
                if Gift == None:
                    self.do_assert(0, "奖励配置表RewardConfig" + "没有找到对应的Mall.fixedGift:" + fixedGift + "，请检查配置文件",record, self._error_cnt)