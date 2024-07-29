from django.urls import path
from django.views.generic.base import RedirectView, TemplateView

from . import views

urlpatterns = [
    path(
        r"authors/",
        TemplateView.as_view(template_name="opal/instructions_authors.html"),
        name="opal-authors",
    ),
    path(
        r"rules/",
        TemplateView.as_view(template_name="opal/instructions_solvers.html"),
        name="opal-rules",
    ),
    path(r"list/", views.HuntList.as_view(), name="opal-hunt-list"),
    path(r"puzzles/<str:slug>/", views.PuzzleList.as_view(), name="opal-puzzle-list"),
    path(
        r"puzzle/<str:hunt>/<str:slug>/",
        views.show_puzzle,
        name="opal-show-puzzle",
    ),
    path(r"", RedirectView.as_view(pattern_name="opal-hunt-list"), name="opal-index"),
]
