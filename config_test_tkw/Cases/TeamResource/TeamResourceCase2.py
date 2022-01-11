#coding=utf-8
from Core.BaseCase import BaseCase
from Core.Container import Container
import os

class TeamResourceCase2(BaseCase):
    """
    验证剧情展示武将timeline高低配本地资源是否存在
    """
    def run(self):
        self.title = "验证剧情展示武将timeline高低配本地资源是否存在"
        self.add_depends("TeamRoleModel")
        self.add_depends("Translate")
        path = Container.get_config('res_root')
        for record in self._TeamRoleModel.get_records():
            showPlotModel = record.showPlotModel
            showPlotModelLow = record.showPlotModelLow
            name = self._Translate.get_record(record.skinName).text
            if showPlotModel == showPlotModelLow:
                self.do_assert(False, "TeamRoleModel剧情展示武将timeline高低配配置相同，请检查配置",
                               record, name)
            else:
                self.do_assert(os.path.exists(path + "\\Resources_moved\\" + showPlotModel.replace("/", "\\")),
                               "找不到剧情展示武将{}高模资源，请检查".format(name),
                               record, name)
                self.do_assert(os.path.exists(path + "\\Resources_moved\\" + showPlotModelLow.replace("/", "\\")),
                               "找不到剧情展示武将{}低模资源，请检查".format(name),
                               record, name)