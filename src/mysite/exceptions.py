# -*- coding: utf-8 -*-
from rest_framework import status
from rest_framework.exceptions import APIException


class MySiteException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = '服务异常'
    default_code = '-1'

    def __init__(self, detail=None, code=None, data=None):
        if detail is None:
            detail = self.default_detail
        if code is None:
            code = self.default_code
        self.detail = detail
        self.code = code
        self.data = data

    def get_full_details(self):
        return {'code': self.code, 'msg': self.detail, 'data': self.data}
