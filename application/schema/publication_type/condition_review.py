from marshmallow import Schema, fields


class ConditionReviewSchema(Schema):
    origin_ordinance = fields.String(required=True)
