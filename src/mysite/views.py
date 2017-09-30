# coding: utf-8
import logging

from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from rest_framework import viewsets, decorators
from rest_framework.response import Response

from mysite.exceptions import MySiteException
from mysite.serializers import UserSerializer
from users.models import User

log = logging.getLogger(__name__)


class UserViewSet(viewsets.ReadOnlyModelViewSet, viewsets.mixins.UpdateModelMixin):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

    def get_queryset(self):
        try:
            username = self.request.user.username if self.request and self.request.user else None
            q = Q(username=username) | Q(username=None)
            return self.queryset.filter(q)
        except (AttributeError, ObjectDoesNotExist):
            return self.queryset.none()

    @decorators.list_route(methods=['POST'])
    def get_user(self, request):
        """
        获取用户信息
        :param request:
        :return:
        """
        username = request.data.get('username')

        if not username:
            log.warning('username 缺参')
            return MySiteException(code='-1', detail='username 是必填项')

        # strip
        username = username.strip()

        """查看用户是否存在"""
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            log.warning('用户不存在')
            raise MySiteException(code='-1001', detail='用户不存在')
        except User.MultipleObjectsReturned:
            log.warning('用户不止一个')
            raise MySiteException(code='-1002', detail='用户有多个')

        return Response({'code': 0, 'msg': '获取用户信息成功',
                         'data': {'user': UserSerializer(user).data, 'user_id': user.id}})
