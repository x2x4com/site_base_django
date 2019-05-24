#!/usr/bin/env python
# encoding: utf-8
# ===============================================================================
#
#         FILE:
#
#        USAGE:
#
#  DESCRIPTION:
#
#      OPTIONS:  ---
# REQUIREMENTS:  ---
#         BUGS:  ---
#        NOTES:  ---
#       AUTHOR:  YOUR NAME (),
#      COMPANY:
#      VERSION:  1.0
#      CREATED:
#     REVISION:  ---
# ===============================================================================

from rest_framework import serializers
import control.models

# details of models
# https://segmentfault.com/a/1190000010024982
#
# 1 StringRelatedField
# 使用 StringRelatedField 将返回一个对应关系 model 的 __unicode__() 方法的字符串。
#
# 这个字段是只读的。
#
# 参数：
#
# many 如果应用于多对多关系，则应将此参数设置为 True
#
#
# 2 PrimaryKeyRelatedField
# 使用 PrimaryKeyRelatedField 将返回一个对应关系 model 的主键。
#
# 参数：
#
# queryset 用于在验证字段输入时模型实例查找。 关系必须明确设置 queryset，或设置 read_only = True
#
# many 如果是对应多个的关系，就设置为 True
#
# allow_null 如果设置为 True，则该字段将接受 None 的值或为空的关系的空字符串。默认为 False
#
# pk_field 设置为一个字段以控制主键值的序列化/反序列化。例如，pk_field = UUIDField（format ='hex'） 将UUID主键序列化为紧凑的十六进制表示。
#
#
# 3 PrimaryKeyRelatedField
# 使用 PrimaryKeyRelatedField 将返回一个对应关系 model 的主键。
#
# 参数：
#
# queryset 用于在验证字段输入时模型实例查找。 关系必须明确设置 queryset，或设置 read_only = True
#
# many 如果是对应多个的关系，就设置为 True
#
# allow_null 如果设置为 True，则该字段将接受 None 的值或为空的关系的空字符串。默认为 False
#
# pk_field 设置为一个字段以控制主键值的序列化/反序列化。例如，pk_field = UUIDField（format ='hex'） 将UUID主键序列化为紧凑的十六进制表示。
#
#
# 4 SlugRelatedField
# 使用 SlugRelatedField 将返回一个指定对应关系 model 中的字段，需要擦参数 slug_field 中指定字段名称。
#
# 参数：
#
# slug_field 应该用于表示目标的字段。这应该是唯一标识任何给定实例的字段。例如 username 。这是必选参数
#
# queryset 验证字段输入时用于模型实例查询的查询器。 关系必须明确设置 queryset，或设置 read_only = True
#
# many 如果应用于多对多关系，则应将此参数设置为 True
#
# allow_null 如果设置为 True，则该字段将接受 None 的值或为空的关系的空字符串。默认为 False
#
#
# 5 HyperlinkedIdentityField
# 使用 HyperlinkedIdentityField 将返回指定 view-name 的超链接的字段。
#
# 参数：
#
# view_name 应该用作关系目标的视图名称。如果您使用的是标准路由器类，则它将是格式为 <model_name>-detail 的字符串。必选参数
#
# lookup_field 应该用于查找的目标上的字段。应该对应于引用视图上的 URL 关键字参数。默认值为 pk
#
# lookup_url_kwarg 与查找字段对应的 URL conf 中定义的关键字参数的名称。默认使用与 lookup_field 相同的值
#
# format 如果使用 format 后缀，超链接字段将对目标使用相同的 format 后缀，除非使用 format 参数进行覆盖
#
#
# 6 嵌套序列化关系模型(既直接嵌套一个序列化的类)
# 在序列化模型中指定嵌套序列化关系模型将返回一个该嵌套序列化关系模型对应的数据模型中序列化的数据。
# 读起来有些拗口，看例子吧。
#
# 参数：
#
# many 如果应用于多对多关系，则应将此参数设置为 True


class ControlSomeControlSerializer(serializers.ModelSerializer):
    tags = serializers.StringRelatedField(many=True)
    owner = serializers.StringRelatedField()

    class Meta:
        model = control.models.SomeControl
        fields = ('id', 'title', 'body', 'type', 'owner', 'tags')
        read_only_fields = ('id', 'owner')

