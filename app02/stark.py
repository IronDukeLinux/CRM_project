# '2018/8/28 17:19'
# coding=utf-8


from stark.service.sites import site, ModelStark
from app02 import models

# print(models.Food._meta.app_label)
# print(models.Food._meta.model_name)
site.register(models.Food)
