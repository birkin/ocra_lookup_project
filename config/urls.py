from django.contrib import admin
from django.urls import path
from ocra_lookup_app import views


urlpatterns = [
    ## main ---------------------------------------------------------
    path( 'info/', views.info, name='info_url' ),
    path( 'find/', views.find, name='find_url' ),
    path( 'results/', views.results, name='results_url' ),

    path( 'htmx_example/', views.htmx_example, name='htmx_example_url' ),

    ## other --------------------------------------------------------
    path( '', views.root, name='root_url' ),
    path( 'admin/', admin.site.urls ),
    path( 'error_check/', views.error_check, name='error_check_url' ),
    path( 'version/', views.version, name='version_url' ),
]
