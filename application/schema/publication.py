from marshmallow import Schema, fields, post_load, validates, validates_schema
from marshmallow.exceptions import ValidationError
from marshmallow_enum import EnumField
from pycpfcnpj import cpfcnpj

from domain.model.publication import PublicationType
from .publication_type import publication_types


class PublicationSchema(Schema):
    ordinance_type = EnumField(PublicationType, error='Invalid type {input}')
    ordinance_number = fields.String(required=True)
    process = fields.String(missing=None)
    publish_date = fields.DateTime(format='%Y-%m-%d', required=True)
    issuer = fields.Integer(required=True)
    issuer_name = fields.String(required=True)
    owner_doc = fields.String(data_key='owner_id', required=True)
    term = fields.String(missing=None)
    link = fields.String(missing=None)
    notes = fields.String(missing=None)
    details = fields.Dict(missing=None)

    @validates('owner_doc')
    def validate_owner_doc(self, owner_doc: str, **_):
        if not cpfcnpj.validate(owner_doc):
            raise ValidationError(f'{owner_doc} is not a valid CPF/CNPJ')

    @validates_schema
    def validate_details(self, data: dict, **_):
        schema = publication_types[data['ordinance_type']]
        details = data.get('details') or {}
        errors = schema.validate(details)

        if errors:
            raise ValidationError({'details': errors})

    @post_load
    def transform(self, data: dict, **_) -> dict:
        data['owner_doc'] = cpfcnpj.clear_punctuation(data['owner_doc'])
        data['issuer'] = str(data['issuer'])

        return data


class PublicationQuery(Schema):
    ordinance_type = EnumField(
        PublicationType,
        missing=None,
        error='Invalid type {input}'
    )
    publish_start = fields.DateTime(missing=None)
    publish_end = fields.DateTime(missing=None)
    owner_doc = fields.String(missing=None)

    @post_load
    def transform(self, data: dict, **_):
        return {key: value for key, value in data.items() if value is not None}
