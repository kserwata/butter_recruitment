from django.db import models


STATUSES = (
    ('S', 'S'),
    ('A', 'A'),
    ('R', 'R')
)


class Activity(models.Model):
    id = models.CharField(max_length=128, unique=True, primary_key=True)
    activity_date = models.DateTimeField()
    track_id = models.CharField(max_length=128)
    status = models.CharField(max_length=1, choices=STATUSES)
    billing_amount = models.DecimalField(decimal_places=2, max_digits=12)

    def __str__(self):
        return 'Transaction ID: {}, date: {}, track_id: {} with status: {} for {}'.format(
            self.id,
            self.activity_date.isoformat(),
            self.track_id,
            self.status,
            self.billing_amount
        )
