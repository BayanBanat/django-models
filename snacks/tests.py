from django.test import TestCase
from django.urls import reverse

class TestSnacks(TestCase):
    def test_status_code(self):
        url = reverse('snacks_list')  
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_snack_list_templates(self):
        url = reverse('snacks_list')  
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snacks_list.html')



    def test_snack_detail_templates(self):
        url = reverse('snack_detail')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_detail.html')

    
