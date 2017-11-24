from datetime import datetime

from django.db import models


class Course(models.Model):
    name = models.CharField('课程名称', max_length=10)
    desc = models.CharField('课程描述', max_length=300)
    detail = models.TextField('课程详情')
    degree = models.CharField('难度', choices=(('cj', '初级'), ('zj', '中级'), ('gj', '高级'),), max_length=2)
    learn_times = models.IntegerField('学习时长', default=0, help_text='单位分钟')
    students = models.IntegerField('学习人数', default=0)
    fav_nums = models.IntegerField('收藏人数', default=0)
    image = models.ImageField('封面', upload_to='courses/%Y%m', max_length=100)
    click_nums = models.IntegerField('点击数', default=0)
    add_time = models.DateTimeField('添加时间', default=datetime.now)

    class Meta:
        verbose_name = '课程'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Lesson(models.Model):
    course = models.ForeignKey(Course, '课程')
    name = models.CharField('章节名称', max_length=100)
    add_time = models.DateTimeField('添加时间', default=datetime.now)

    class Meta:
        verbose_name = '章节'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Video(models.Model):
    lesson = models.ForeignKey(Lesson, '章节')
    name = models.CharField('视频名称', max_length=100)
    add_time = models.DateTimeField('添加时间', default=datetime.now)

    class Meta:
        verbose_name = '视频'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseResource(models.Model):
    course = models.ForeignKey(Course, '课程')
    name = models.CharField('资源名称', max_length=100)
    download_url = models.FileField('资源文件', upload_to='courses/%Y%m', max_length=100)
    add_time = models.DateTimeField('添加时间', default=datetime.now)

    class Meta:
        verbose_name = '课程资源'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
