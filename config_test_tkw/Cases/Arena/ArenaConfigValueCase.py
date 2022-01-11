#coding=utf-8
from Core.BaseCase import BaseCase

class ArenaConfigValueCase(BaseCase):
    """
    ConfigValue表竞技场部分检查
    """
    def run(self):
        self.title = "ConfigValue表竞技场部分检查"
        self.desc = "检查内容：初始名次配置合理性、扫荡和喊话配置是否正确"
        self.add_depends("Translate")
        listreward = []
        for i in self._Translate.get_records():
            RewardTag = i.tag
            listreward.append(RewardTag)
        self.add_depends("ConfigValue")

        for record in self._ConfigValue.get_records():
            if record.tag == "Arena_PlayerInitRank":
                content = record.content
                # print(type(content))
                content = eval(content)
                print(type(content))
                min1 = content['min']
                max1 = content['max']
                # print(min1 > max1)
                self.do_assert(min1 <= max1, "初始排名错误",record,"左区间:%d"%(min1) + "应小于右区间:%d"%(max1))
            elif record.tag == "Arena_SignatureInitAll" or record.tag == 'Arena_SweepingTalk':
                cont = record.content
                cont = list(filter(None,cont.split(';')))
                for i in cont :
                    self.do_assert(i in listreward, "不存在的宣言",record,i + "在translate中没有")