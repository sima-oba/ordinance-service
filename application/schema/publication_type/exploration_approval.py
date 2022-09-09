from marshmallow import Schema, fields


class ExplorationApprovalSchema(Schema):
    area = fields.String(required=True)
