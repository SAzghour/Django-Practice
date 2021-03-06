"""Training URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from .views import (
    product_list_views,
    product_details_views,
    product_create_views,
    render_initial_data,
    dynamic_views,
    procuct_delete_views
)

app_name = 'products'

urlpatterns = [
    path('product_list/', product_list_views, name="list"),
    path('product/', product_details_views, name='details'),
    path('dynamic/<int:my_id>/', dynamic_views, name="dynamic"),
    path('product/<int:obj_id>/delete/', procuct_delete_views, name="delete"),
    path('create/', product_create_views, name="create"),
    path('initial/', render_initial_data, name="initial")
]