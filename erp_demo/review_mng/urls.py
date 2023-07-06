from django.urls import path, include

from erp_demo.review_mng.forms import ManagementReviewForm, ManagementReviewViewForm, ManagementReviewEditForm, ManagementReviewDeleteForm
from erp_demo.review_mng.models import ManagementReview
from erp_demo.review_mng.views import ReviewMngViews

# Set-up
# ----------------------------------------------------------------------------------

template_list = [
    'review_mng/review_mng_index.html',
    'review_mng/review_list.html',
    'review_mng/add_review.html',
    'review_mng/show_review.html',
    'review_mng/edit_review.html',
    'review_mng/delete_review.html',
]

redirect_url = 'review list'

form_list = [
    # Create, View, Edit, Delete
    ManagementReviewForm, ManagementReviewViewForm, ManagementReviewEditForm, ManagementReviewDeleteForm,
]

files_are_used = False

# ----------------------------------------------------------------------------------

urlpatterns = [
    path('', ReviewMngViews(
        template_list, redirect_url, form_list, ManagementReview, files_are_used
    ).index_view, name='review mng index'),

    path('review-list/', ReviewMngViews(
        template_list, redirect_url, form_list, ManagementReview, files_are_used
    ).list_view, name='review list'),

    path('add-review/', ReviewMngViews(
        template_list, redirect_url, form_list, ManagementReview, files_are_used
    ).create_view, name='add review'),

    path('show-review/<int:pk>/<slug:slug>/', ReviewMngViews(
        template_list, redirect_url, form_list, ManagementReview, files_are_used
    ).show_view, name='show review'),

    path('edit-review/<int:pk>/<slug:slug>/', ReviewMngViews(
        template_list, redirect_url, form_list, ManagementReview, files_are_used
    ).edit_view, name='edit review'),

    path('delete-review/<int:pk>/<slug:slug>/', ReviewMngViews(
        template_list, redirect_url, form_list, ManagementReview, files_are_used
    ).delete_view, name='delete review'),
]
