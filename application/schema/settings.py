from marshmallow import Schema, fields, validate


class SettingsSchema(Schema):
    alert_message = fields.String()
    alert_days_before = fields.Integer(validates=validate.Range(0, 365))
    template_id = fields.UUID(required=True)
    subject = fields.String(required=True)
