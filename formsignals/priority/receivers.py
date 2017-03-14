from django.dispatch import receiver
from django.forms import signals as form_signals
from ..blog.models import BlogEntry
from ..blog.forms import BlogEntryForm
from .models import BlogEntryPriority
from .forms import BlogEntryPriorityForm


def add_fields_from_form(source_form, destination_form):
    """Adds all the fields from the source form to the destination form.
    """
    for field_name, field in source_form.fields.items():
        destination_form.fields[field_name] = field


@receiver(form_signals.post_init, sender=BlogEntryForm)
def add_priority_field_to_blog_entry_form(sender, form, **kwargs):
    # Add the priority field to the BlogEntry form
    priority_form = BlogEntryPriorityForm(data=kwargs.get('data'))
    add_fields_from_form(source_form=priority_form, destination_form=form)


@receiver(form_signals.post_clean, sender=BlogEntryForm)
def check_priority_is_in_title(sender, form, cleaned_data, **kwargs):
    # Only allow priority to be set if 'Priority' is also in the title
    if cleaned_data.get('priority') and 'Priority' not in cleaned_data.get('title', ''):
        form.add_error('priority', "Blog entry may not be marked with priority unless 'Priority' is in the title.")


@receiver(form_signals.post_save, sender=BlogEntryForm)
def save_blog_entry_priority_on_form_save(sender, form, **kwargs):
    # Save the BlogEntryPriority
    BlogEntryPriority.objects.create(blog_entry=form.instance, priority=form.cleaned_data['priority'])
