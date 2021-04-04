from django.db import models
from django.utils.timezone import localtime


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return "{user} entered at {entered} {leaved}".format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved="leaved at " + str(self.leaved_at) if self.leaved_at else "not leaved"
        )

    def get_duration(self):
        local_entered_at = localtime(self.entered_at)
        local_leaved_at = localtime(self.leaved_at) if self.leaved_at \
            else localtime()

        return int((local_leaved_at - local_entered_at).total_seconds())

    def is_visit_long(self, minutes=60):
        return self.get_duration() // 60 > minutes

    def format_duration(self, duration):
        hours = str(duration // 3600)
        minutes = str((duration % 3600) // 60)

        if len(hours) == 1:
            hours = f"0{hours}"

        if len(minutes) == 1:
            minutes = f"0{minutes}"

        return f"{hours}:{minutes}"
