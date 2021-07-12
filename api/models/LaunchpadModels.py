from django.db import models
from datetime import datetime


class Launchpads(models.Model):
    id = models.AutoField(primary_key=True)
    dapp_version = models.FloatField()
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=5000, blank=True)
    website_link = models.CharField(max_length=5000, blank=True)
    creator_wallet_address = models.CharField(max_length=50)
    pool_address = models.CharField(max_length=50, blank=True, default="")
    reward_vault_address = models.CharField(max_length=50, blank=True, default="")
    hash = models.CharField(
        max_length=100, blank=False, unique=True)
    start_time = models.FloatField(blank=True, default=0)
    start_delay = models.FloatField()
    running_period = models.FloatField()
    run_time = models.FloatField(blank=True, default=0)
    total_staked = models.FloatField(default=0)
    total_reward_amount = models.FloatField()
    reward_token_address = models.CharField(max_length=50)
    reward_token_symbol = models.CharField(max_length=10)
    reward_token_symbol_link = models.CharField(max_length=300)
    reward_token_decimal = models.IntegerField()
    network_id = models.IntegerField()
    status = models.CharField(max_length=20, default="PENDING")
    identifier = models.CharField(max_length=25)
    created_time = models.DateTimeField(default=datetime.now)
    last_updated = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.pool_address

