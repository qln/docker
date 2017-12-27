from django.conf.urls import *
from . import testdb
 
urlpatterns = [
    url(r'^testdb$', testdb.testdb),
]
