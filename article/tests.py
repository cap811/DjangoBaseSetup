from django.test import TestCase

# Test the article index view.
def test_index(self):
    response = self.client.get('/')
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'articles/index.html')
    
# Test the article detail view.
def test_detail(self):
    response = self.client.get('/article/1/')
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'articles/detail.html')
