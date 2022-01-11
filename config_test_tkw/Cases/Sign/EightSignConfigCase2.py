#coding=utf-8
from Core.BaseCase import BaseCase
class EightSignConfigCase2(BaseCase):
    """
    遍历签到配置命名的tag不能重复命名,或者tag为空的检查、
    这个判断为空的使用，得重构TopjoyExcel的方法_init_record 这个方法默认使用get_records获取表的时候会过滤掉tag=null的行数据
    """
    def run(self):
        self.title = "签到配置表EightSignConfig测试"
        self.desc = "EightSignConfig.tag不能重复命名 或者为空"
        self.add_depends("EightSignConfig")
        nun_List = []
        nun_recrd=[]
        for record in self._EightSignConfig.get_records():
            tag=record.tag
            nun_List.append(tag)
            nun_recrd.append(record)
        for record1 in nun_recrd:
            if record1.tag == None:
                self.do_assert(0, "EightSignConfig.tag填写为空,请检查配置文件", record1, self._error_cnt)
            else:
                if nun_List.count(record1.tag)>1:
                    self.do_assert(0,"EightSignConfig.tag 有重复的tag命名,请检查配置文件",record1,self._error_cnt)



