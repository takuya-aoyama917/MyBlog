from .models import Category

def common(request):
  Category_data = Category.objects.all()
  context = {
    'category_data': Category_data
  }
  return context