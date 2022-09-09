from marshmallow import Schema, fields, validates, post_load, EXCLUDE
from marshmallow.exceptions import ValidationError
from pycpfcnpj import cpfcnpj


class OwnerSchema(Schema):
    class Meta:
        unknown = EXCLUDE
    _id = fields.String(required=True)
    doc = fields.String(required=True)
    name = fields.String(required=True)
    email = fields.Email(required=True)

    @validates('doc')
    def validate_doc(self, doc: str, **_):
        if not cpfcnpj.validate(doc):
            raise ValidationError(f'Invalid CPF/CNPJ {doc}')

    @post_load
    def transform(self, data: dict, **_) -> dict:
        data['doc'] = cpfcnpj.clear_punctuation(data['doc'])
        return data
