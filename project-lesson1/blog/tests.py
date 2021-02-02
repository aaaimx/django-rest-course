from django.test import TestCase
from .models import Post

# Create your tests here.
class PostTest(TestCase):

    def setUp(self):

        instance = Post.objects.create(title='Curso de Django', description='....')
        instance.save()

        instance = Post.objects.create(title='Angular vs React')
        instance.save()

    def test_for_post(self):
        # 
        print(Post.objects.all())
        print(Post.objects.filter(title='Curso de Django'))
        print(Post.objects.filter(title__icontains='Curso'))
        # print(Post.objects.filter(created_at__range=['2021-01-01', '2021-02-01']))
        instance = Post.objects.get(pk=1)
        instance.title = 'Django REST'
        instance.save()

        print(Post.objects.all())
        instance.delete()
        print(Post.objects.all())



