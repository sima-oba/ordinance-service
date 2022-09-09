from marshmallow import Schema, fields


class DegradedAreaRecoveryPlanSchema(Schema):
    prad = fields.String(required=True)
