from django.conf.urls import include, re_path
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'StockMarketPrediction.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    re_path(r'^$', 'Predictions.views.index', name='index'),
    re_path(r'^companies/$', 'Predictions.views.companies', name='companies'),
    re_path(r'^selected_company/$', 'Predictions.views.selected_company', name='selected_company'),
    re_path(r'^fundamental_analysis/(?P<company>[A-Z]+$)', 'Predictions.views.fundamental', name='fundamental'),
    re_path(r'^technical_analysis/(?P<company>[A-Z]+$)', 'Predictions.views.technical', name='technical'),
    re_path(r'^recommendation/$', 'Predictions.views.recommendation', name='recommendation'),
    re_path(r'^update/$', 'Predictions.views.update', name='update'),
    re_path(r'^accuracies/$', 'Predictions.views.accuracies', name='accuracies'),


]
