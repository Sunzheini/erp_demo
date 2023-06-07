from django.conf import settings
from django.conf.urls.static import static

from django.urls import path, include

from erp_demo.interaction_mng.forms import InteractionForm, InteractionViewForm, InteractionEditForm, InteractionDeleteForm
from erp_demo.interaction_mng.models import Interaction
from erp_demo.interaction_mng.views import InteractionMngViews

# Set-up
# ----------------------------------------------------------------------------------

template_list = [
    'interaction_mng/interaction_mng_index.html',
    'interaction_mng/interaction_list.html',
    'interaction_mng/add_interaction.html',
    'interaction_mng/show_interaction.html',
    'interaction_mng/edit_interaction.html',
    'interaction_mng/delete_interaction.html',
]

redirect_url = 'interaction list'

form_list = [
    # Create, View, Edit, Delete
    InteractionForm, InteractionViewForm, InteractionEditForm, InteractionDeleteForm,
]

files_are_used = False

# ----------------------------------------------------------------------------------

urlpatterns = [
    path('', InteractionMngViews(
        template_list, redirect_url, form_list, Interaction, files_are_used
    ).index_view, name='interaction mng index'),

    path('interaction-list/', InteractionMngViews(
        template_list, redirect_url, form_list, Interaction, files_are_used
    ).list_view, name='interaction list'),

    path('add-interaction/', InteractionMngViews(
        template_list, redirect_url, form_list, Interaction, files_are_used
    ).create_view, name='add interaction'),

    path('show-interaction/<int:pk>/<slug:slug>/', InteractionMngViews(
        template_list, redirect_url, form_list, Interaction, files_are_used
    ).show_view, name='show interaction'),

    path('edit-interaction/<int:pk>/<slug:slug>/', InteractionMngViews(
        template_list, redirect_url, form_list, Interaction, files_are_used
    ).edit_view, name='edit interaction'),

    path('delete-interaction/<int:pk>/<slug:slug>/', InteractionMngViews(
        template_list, redirect_url, form_list, Interaction, files_are_used
    ).delete_view, name='delete interaction'),
]
