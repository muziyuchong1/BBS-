from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import resolve,reverse

from ..models import Board,Topics,Post
from ..views import topic_posts

# 为topic_posts视图创建一个新的测试文件
#测试设置开始变得更加复杂。可以创建混合类或抽象类来根据需要重用代码。
# 还可以使用第三方库来设置一些测试数据，以减少样板代码
class TopicPostsTests(TestCase):
    def setUp(self):
        board = Board.objects.create(name='Django',description='Djnago board.')
        user = User.objects.create_user(username='jann',email='muziyuchong@163.com',password='qiangli')
        topic = Topics.objects.create(subject='ok',board=board,starter = user)
        Post.objects.create(message= 'are you ok ',topic =topic,created_by = user)
        url = reverse('topic_posts',kwargs={'pk':board_pk,'topic_pk':topic.pk})
        self.reponse=self.client.get(url)


    def test_status_code(self):
        self.assertEquals(self.reponse.status_code,200)

    def test_view_function(self):
        view = resolve('/boards/1/topics/1/')
        self.assertEquals(view.func,topic_posts)

