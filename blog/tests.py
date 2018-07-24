from django.db.models import Max
from django.test import Client, TestCase

from django.contrib.auth.models import User
from .models import Post, Category, Contact

class BlogTestCase(TestCase):

    def setUp(self):
        
        self.user = User.objects.create_user(username='testuser', password='12345')
        login = self.client.login(username='testuser', password='12345')

        cateogory1 = Category.objects.create(title="TestCategory1")
        cateogory2 = Category.objects.create(title="TestCategory2")

        blogpost1 = Post.objects.create(title='Title', author=User.objects.get(id=1), 
                                        body='Body',category=Category.objects.get(id=1),image=None)
        blogpost2 = Post.objects.create(title='Title2', author=User.objects.get(id=1),
                                        body='Body',category=Category.objects.get(id=2),image=None)

    def test_categories_created(self):
        categories = Category.objects.all()
        self.assertEqual(categories.count(), 2)

    def test_user_created(self):
        test_users = User.objects.all()
        self.assertEqual(test_users.count(), 1)

    def test_post_created(self):
        posts = Post.objects.all()
        self.assertEqual(posts.count(), 2)

    def test_post_category_foreignkey_match(self):
        post = Post.objects.get(id=1)
        self.assertEqual(post.category, Category.objects.get(id=1))







