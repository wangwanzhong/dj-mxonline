from datetime import datetime
from django.db import models


class CityDict(models.Model):
    name = models.CharField(max_length=50, verbose_name='城市名称')
    desc = models.CharField(max_length=200, verbose_name='城市描述')
    add_time = models.DateTimeField('添加时间', default=datetime.now)

    class Meta:
        verbose_name = '城市'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseOrg(models.Model):
    name = models.CharField(max_length=50, verbose_name='机构名称')
    desc = models.TextField('机构描述')
    categroy = models.CharField(default='pxjg', max_length=20, choices=(('pxjg', '培训机构'),('gr', '个人'),('gx', '高校'),))
    click_nums = models.IntegerField('点击数', default=0)
    fav_nums = models.IntegerField('收藏数', default=0)
    image = models.ImageField('封面', upload_to='org/%Y%m', max_length=100)
    address = models.CharField(max_length=150, verbose_name='机构地址')
    city = models.ForeignKey(CityDict, verbose_name='城市')
    add_time = models.DateTimeField('添加时间', default=datetime.now)

    class Meta:
        verbose_name = '课程机构'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Teacher(models.Model):
    org = models.ForeignKey(CourseOrg, verbose_name='所属机构')
    name = models.CharField(max_length=50, verbose_name='教师名称')
    work_years = models.IntegerField('工作年限', default=0)
    work_company = models.CharField(max_length=50, verbose_name='公司名称')
    work_position = models.CharField(max_length=50, verbose_name='工作职位')
    points = models.CharField(max_length=50, verbose_name='教学特点')
    click_nums = models.IntegerField('点击数', default=0)
    fav_nums = models.IntegerField('收藏数', default=0)
    add_time = models.DateTimeField('添加时间', default=datetime.now)

    class Meta:
        verbose_name = '教师'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
