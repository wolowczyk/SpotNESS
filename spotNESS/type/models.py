from django.db import models


class SpotType(models.Model):
    name = models.CharField(max_length=27)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


# SPOT_TYPES = [
#     (1, 'View'),
#     (2, 'Food'),
#     (3, 'Restaurant'),
#     (4, 'Urban exploration'),
#     (5, 'City attraction'),
#     (6, 'Cafe'),
#     (7, 'Experience/story'),
#     (8, 'Wild sleeping'),
#     (9, 'Activity'),
#     (10, 'Party'),
#     (11, 'Nature')
# ]