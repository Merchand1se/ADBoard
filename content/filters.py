from django_filters import FilterSet, ChoiceFilter
from .models import *

class PostsFilter(FilterSet):
    category = ChoiceFilter(
        field_name='category_choice',
        queryset=Post.CATEGORY_CHOICES,
        label='Category'
    )
    class Meta:
        models = Post,
        fields = (
            'author',
            'creationdate',
            'price',
        )

class ReplyFilter(FilterSet):
    def __init__(self, *args, **kwargs):
        super(ReplyFilter, self).__init__(*args, **kwargs)
        self.filters['post_replied'].queryset = Post.objects.filter(author=kwargs['request'])

    class Meta:
        models = Reply,
        fields = (
            'post_replied'
        )


