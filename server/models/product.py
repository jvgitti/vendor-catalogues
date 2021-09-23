from sqlalchemy import Column, String, BigInteger, Numeric, ForeignKey, Integer
from server import db
from server import ma


class Product(db.Model):
    __tablename__ = "tb_product"

    Id = Column(BigInteger, primary_key=True, autoincrement=True)
    Name = Column(String, nullable=False)
    Code = Column(String, nullable=False, unique=True)
    Price = Column(Numeric(scale=2))
    Vendor_Id = Column(Integer, ForeignKey("tb_vendor.Id"), index=True, nullable=False)


class ProductSchema(ma.ModelSchema):
    class Meta:
        fields = (
            "Id",
            "Name",
            "Code",
            "Price",
            "Vendor_Id"
        )
