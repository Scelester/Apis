from django.db import models

# Create your models here.
class Occation(models.Model):

    name = models.CharField(_(""), max_length=50)

    class Meta:
        verbose_name = _("occation")
        verbose_name_plural = _("occations")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("occation_detail", kwargs={"pk": self.pk})



class All_cakes(models.Model):
    name = models.CharField(_(""), max_length=50)
    occation = models.ForeignKey("Occation", verbose_name=_(""), on_delete=models.CASCADE)
