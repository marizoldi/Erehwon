from django.db import models

# Create your models here.
from django.views.generic import TemplateView

# from http://m-x.io/blog/how-to-use-django-postman-with-django-notifications/

"""Handle notification signals from django-postman and pass
them to django-notifications. Postman does not """

# In the app's models.py:

from django.contrib.auth.models import User

from notifications.signals import notify

#User = profiles.ErehwonUser
from django.contrib.auth import get_user_model
def send(users=[], label='', extra_context={}):
    print("send fired")

    if label == 'postman_message':
        print("send in pm fired")
        msg = extra_context['pm_message']
        User = get_user_model()
        user = User.objects.get(pk=msg.sender_id)
        notify.send(user, recipient=users[0], verb='New message', description=msg.subject)

#due to bug in django postman management.py, include the schema for unrelated package here:
from django.utils.translation import ugettext_lazy as _
class NoticeType(models.Model):

    label = models.CharField(_("label"), max_length=40)
    display = models.CharField(_("display"), max_length=50)
    description = models.CharField(_("description"), max_length=100)

    # by default only on for media with sensitivity less than or equal to this number
    default = models.IntegerField(_("default"))

    def __str__(self):
        return self.label

    class Meta:
        verbose_name = _("notice type")
        verbose_name_plural = _("notice types")

    @classmethod
    def create(cls, label, display, description, default=2, verbosity=1):
        """
        Creates a new NoticeType.
        This is intended to be used by other apps as a post_syncdb manangement step.
        """
        try:
            notice_type = cls._default_manager.get(label=label)
            updated = False
            if display != notice_type.display:
                notice_type.display = display
                updated = True
            if description != notice_type.description:
                notice_type.description = description
                updated = True
            if default != notice_type.default:
                notice_type.default = default
                updated = True
            if updated:
                notice_type.save()
                if verbosity > 1:
                    print("Updated %s NoticeType" % label)
        except cls.DoesNotExist:
            cls(label=label, display=display, description=description, default=default).save()
            if verbosity > 1:
                print("Created %s NoticeType" % label)
