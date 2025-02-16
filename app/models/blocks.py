import uuid

from django.db import models


class Currency(models.Model):
    name = models.CharField(max_length=10, unique=True, db_index=True)

    def __str__(self):
        return self.name


class Provider(models.Model):
    name = models.CharField(max_length=50, unique=True, db_index=True)
    api_key = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class Block(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name="blocks")
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, related_name="blocks")
    block_number = models.BigIntegerField(db_index=True)
    stored_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('currency', 'block_number')
        ordering = ['-stored_at']
        indexes = [
            models.Index(fields=["currency", "provider"]),
            models.Index(fields=["currency", "block_number"]),
        ]

    def __str__(self):
        return f"{self.currency.name} - Block {self.block_number}"
