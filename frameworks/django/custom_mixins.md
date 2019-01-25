Custom Mixins
=============

Example of defining a method in a mixin that overrides or extends a method 
outside the mixin's own inheritance chain:

- _**In articles/views.py**_

```python
class ArticleCreate(LoginRequiredMixin, mixins.SuccessMessageMixin, generic.CreateView):
    fields = ('title', 'body', 'author', 'published')
    model = models.Article
    
    success_message = "Article Created!"


class ArticleUpdate(LoginRequiredMixin, mixins.SuccessMessageMixin, generic.UpdateView):
    fields = ('title', 'body', 'author', 'published')
    model = models.Article
    
    def get_success_message(self):
        obj = self.get_object()
        return "{} updated!".format(obj.title)
```

- _**In articles/mixins.py**_

```python
from django.contrib import messages

class SuccessMessageMixin:
    success_message = ""
    
    def get_success_message(self):
        return self.success_message

    # we can extend or override methods that are defined in (or inherited by) the Mixin user.
    # So, here we are extending a method that X has, but isn't in SuccessMessageMixin's own inheritance
    # tree.
    def form_valid(self, form):
		req = self.request
        msg = self.get_success_message()
        messages.success(req, msg)
        return super().form_valid(form)
```
