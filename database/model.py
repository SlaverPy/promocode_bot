from tortoise.models import Model
from tortoise import fields
from tortoise.fields.relational import OnDelete


class BotUser(Model):
    id = fields.IntField(pk=True)
    user_id = fields.IntField()
    username = fields.CharField(max_length=255)
    is_active = fields.BooleanField(default=True)
    can_get_code = fields.BooleanField(default=True)
    create_at = fields.DatetimeField(auto_now_add=True)


class Promocods(Model):
    id = fields.IntField(pk=True)
    promocode = fields.CharField(max_length=255)
    is_active = fields.BooleanField(default=True)
    user = fields.ForeignKeyField('models.BotUser', on_delete=OnDelete.SET_NULL, null=True)
    create_at = fields.DatetimeField(auto_now_add=True)


class DistributionTime(Model):
    time_start = fields.DatetimeField(null=True)
    time_end = fields.DatetimeField(null=True)
    create_at = fields.DatetimeField(auto_now_add=True)
