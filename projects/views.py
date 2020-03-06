import logging
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .models import Projects
from .serializers import ProjectModelSerializer
from .serializers import ProjectNamesModelSerializer
from rest_framework import mixins, permissions
from rest_framework import generics
from rest_framework import viewsets
from .serializers import InterfacesByProjectIdSerializer

logger = logging.getLogger('test')


class ProjectViewSet(viewsets.ModelViewSet):
	"""
	list:
	获取项目列表数据

	create:
	创建项目

	destroy:
	删除项目

	update:
	完整更新项目

	partial_update:
	部分更新项目

	retrieve:
	获取项目详情数据

	names:
	获取所有项目ID和项目名

	interfaces:
	获取某个项目下的所有接口信息

	"""
	queryset = Projects.objects.all()
	serializer_class = ProjectModelSerializer
	# 需要分页过滤排序可以加上下面的三行
	filter_backends = [DjangoFilterBackend, OrderingFilter]
	filterset_fields = ['name', 'leader', 'tester']
	ordering_fields = ['id', 'name', 'leader']

	# AllowAny 允许任何人访问接口
	# IsAuthenticated 只有登录之后可以请求
	# IsAdminUser 管理员才可以请求
	# IsAuthenticatedOrReadOnly 登录才可以请求，不登录只能访问获取信息的接口
	
	# 类视图指定优先级最高，类视图指定了，全局配置指定的就不生效了，如果类不指定权限，全局的则生效
	permission_classes = [permissions.IsAuthenticated] # 只有登录之后才可以请求


	@action(methods=['get'], detail=False)
	def names(self, request, *args, **kwargs):
		queryset = self.get_queryset() # 经过过滤分页排序引擎之后的查询集
		serializer = self.get_serializer(instance=queryset, many=True)
		# logger.error('这里有一个严重的错误')
		return Response(serializer.data)

	# 获取某个项目的接口列表
	@action(detail=True)
	def interfaces(self, request, *args, **kwargs):
		instance = self.get_object()
		serializer = self.get_serializer(instance=instance)
		return Response(serializer.data)


	def get_serializer_class(self):
		if self.action == "names":
			return ProjectNamesModelSerializer
		elif self.action == "interfaces":
			return InterfacesByProjectIdSerializer
		return self.serializer_class

