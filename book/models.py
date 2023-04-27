from django.db import models

# Create your models here.
"""
1 模型类 需要继承自models.Model
2 定义属性 
    id 系统默认会生成
    2.1 属性名=models.类型（选项）
        不要使用python mysql 关键字
        不要使用连续的下划线 __ 
    2.2 类型 MySql的类型 
    2.3 选项 是否有默认值，是否唯一，是否为null
        CharField 必须设置 max_length
        verbose_name 主要是 admin站点使用
3. 改变表的名称
    默认表的名称都是：
"""
class BookInfo(models.Model):

    name=models.CharField(max_length=20, unique=True)
    pub_date=models.DateField(null=True)
    readcount=models.IntegerField(default=0)
    commentcount=models.IntegerField(default=0)
    is_delete=models.BooleanField(default=False)

    class Meta:
        db_table='bookinfo'
        verbose_name='书籍管理'

    def __str__(self):
        return self.name

class PeopleInfo(models.Model):

    GENDER_CHOICE = (
        (1, 'male'),
        (2, 'female')
    )

    name=models.CharField(max_length=10, unique=True)
    gender=models.SmallIntegerField(choices=GENDER_CHOICE, default=1)
    description=models.CharField(max_length=100, null=True)
    is_delete=models.BooleanField(default=False)

    #外键
    #系统会自动在外键名后面加_id

    #外键的级联操作
    #主表的一条数据 如果删除了
    #从表有关的数据应该怎么办呢？
    #1 SET_NULL
    #2 抛出异常 不让删除
    #3 级联删除

    book=models.ForeignKey(BookInfo, on_delete=models.CASCADE)

    class Meta:
        db_table='peopleinfo'

    def __str__(self):
        return self.name

