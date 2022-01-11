#coding=utf-8
from Core.BaseCase import BaseCase
from Core.Container import Container
import os

class TeamResourceCase1(BaseCase):
    """
    验证武将timeline高低配本地资源是否存在
    """
    def run(self):
        self.title = "验证武将timeline高低配本地资源是否存在"
        self.add_depends("TeamBase")
        self.add_depends("TeamRoleModel")
        self.add_depends("Translate")
        path = Container.get_config('res_root')
        for record in self._TeamBase.get_records():
            if 1 == record.ifVisible:
                name = self._Translate.get_record(record.name).text
                showModel = self._TeamRoleModel.get_record(record.roleModel).showModel
                showModelLow = self._TeamRoleModel.get_record(record.roleModel).showModelLow
                if showModel == showModelLow:
                    self.do_assert(False, "TeamRoleModel高低模型配置相同，请检查配置",
                                   record, name)
                else:
                    self.do_assert(os.path.exists(path + "\\Resources_moved\\" + showModel.replace("/", "\\")), "找不到武将{}高模资源，请检查".format(name),
                                   record, name)
                    self.do_assert(os.path.exists(path + "\\Resources_moved\\" + showModelLow.replace("/", "\\")),
                           "找不到武将{}低模资源，请检查".format(name),
                           record, name)