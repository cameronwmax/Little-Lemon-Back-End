from django.test import TestCase
from restaurant.models import Menu
from rest_framework.test import APIClient
from restaurant.serializers import MenuItemSerializer

class MenuViewTest(TestCase):
  def setup(self):
    Menu.objects.create(title='IceCream', price=80, inventory=1)

  def test_getall(self):
    client = APIClient()
    response = client.get("http://127.0.0.1:8000/restaurant/menu/")

    menu_items = Menu.objects.all()
    serializer = MenuItemSerializer(menu_items, many=True)

    self.assertEqual(response.data, serializer.data)