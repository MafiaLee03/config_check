#coding=utf-8
from Core.Container import Container
import os
from Core.Util import *
class BaseCase:
    def __init__(self, name, category):
        self.title = "" # 用于测试报告展示
        self.desc = "" # 用于测试报告展示
        self._error_detail = []
        self._correct_cnt = 0
        self._error_cnt = 0
        self._success = True
        self._level = 1 #TODO 这里做枚举，用于区分用例的级别
        self._name = name
        self._category = category

    def add_depends(self, table_name):
        table_obj = Container.find_table(table_name)
        alias_name = table_name.replace(".", "_")
        setattr(self, "_" + alias_name, table_obj)

    def run(self):
        pass

    def do_assert(self, is_correct, msg, record, comment=None):
        if is_correct:
            self._correct_cnt = self._correct_cnt + 1
        else:
            self._error_cnt = self._error_cnt + 1
            self._success = False
            tag = ""
            if type(record) == str:
                tag = record
            else:
                tag = record.tag
            self._error_detail.append([tag, msg, comment])
    
    def is_success(self):
        return self._success
    
    def convert_list_to_html(self, value_list):
        if len(value_list) <= 0:
            return ""
        html = []
        html.append("<html><meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\"/><body>")
        html.append("<h1>")
        html.append("{}/{}".format(self._category,self._name))
        html.append("</h1>")
        html.append("<h3>")
        html.append(self.title)
        html.append("</h3>")
        html.append("<p>")
        html.append(self.desc)
        html.append("</p>")
        head_list = ["Tag", "错误描述", "备注"]
        table_html = convert_list_to_table(head_list, value_list)
        html.extend(table_html)
        html.append("</html>")
        return "".join(html)

    def dump_detail_report(self, report_root):
        report_path = os.path.join(report_root, self._category,"{}.html".format(self._name))
        report_dir = os.path.dirname(report_path)
        if not os.path.exists(report_dir):
            os.makedirs(report_dir)
        with open(report_path, 'w', encoding="utf-8") as f:
            f.write(self.convert_list_to_html(self._error_detail))

    def get_summary(self):
        return [self._name, self.title, self.desc, self._correct_cnt, self._error_cnt]

        
