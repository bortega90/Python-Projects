from django.db import models

# Create class called UniversityCampus with attributes.
class UniversityCampus(models.Model):
    campus_name = models.CharField(max_length=60, default="", blank=True, null=False)
    state = models.CharField(max_length=2, default="", blank=True, null=False)
    campus_ID = models.IntegerField(default="", blank=True, null=False)
    # creates model manager
    object = models.Manager()
    # displays input values in the form of a string.
    def __str__(self):
        # returns the input value of the campus name, state, and campus id
        # field as a tuple to display in the browser instead of the default times
        display_location = "{0.campus_name}: {0.state}: {0.campus_ID}"
        return display_location.format(self)

    # displays University Campus
    class Meta:
        verbose_name = 'University Campus'

