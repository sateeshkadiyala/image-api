from marshmallow import Schema, fields, validates_schema, ValidationError


class ImageSchema(Schema):
    """
    DynamoDB Image Item Schema which validates the data on get, put or post items to table
    """
    id = fields.UUID(required=False)
    dimensions = fields.List(fields.Integer, required=True)
    type = fields.Str(require=True)
    uploaded_at = fields.Datetime(required=True)
    url = fields.Str(required=True)

    @validates_schema
    def validate_dimensions(self, data):
        dimensions = data['dimensions']

        if len(dimensions) != 2:
            raise ValidationError("Invalid dimensions")


