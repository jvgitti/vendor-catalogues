from sqlalchemy import Column, String, BigInteger
from server import db
from server import ma


class Vendor(db.Model):
    __tablename__ = "tb_vendor"

    Id = Column(BigInteger, primary_key=True, autoincrement=True)
    Name = Column(String, nullable=False)
    CNPJ = Column(String, nullable=False, unique=True)
    City = Column(String)


class VendorSchema(ma.ModelSchema):
    class Meta:
        fields = (
            "Id",
            "Name",
            "CNPJ",
            "City"
        )
