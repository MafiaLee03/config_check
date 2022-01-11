#coding=utf-8
from Core.BaseCase import BaseCase
import os
class EightSignConfigCase1(BaseCase):
    """
    八日登陆
    检测EightSignConfig的资源是否存在
    """

    def run(self):
        self.title = "八日配置表对应工程资源测试"
        self.desc = "检测资源存不存在"
        self.add_depends("EightSignConfig")
        #资源工程根目录
        path="C:/tkw_git/tkwclient/unity_project/Assets/Resources_moved/"

        for record in self._EightSignConfig.get_records():
            rewar_paths=path+record.reward_pic

            general_paths=path+record.general_img

            title_paths=path+record.reward_title_pic

            bg_paths=path+record.bg_img

            if(os.path.exists(rewar_paths)==False):
                self.do_assert(0,"资源在工程目录中找不到"+"EightSignConfig.reward_pic："+ record.reward_pic ,record,self._error_cnt)

            if (os.path.exists(bg_paths) == False):
                self.do_assert(0, "资源在工程目录中找不到" "EightSignConfig.bg_img："+ record.bg_img, record,self._error_cnt)

            if (os.path.exists(general_paths) == False):
                self.do_assert(0, "资源在工程目录中找不到" "EightSignConfig.general_img："+ record.general_img, record, self._error_cnt)

            if (os.path.exists(title_paths) == False):
                self.do_assert(0, "资源在工程目录中找不到" +"EightSignConfig.reward_title_pic："+ record.reward_title_pic, record,self._error_cnt)










