from unicodedata import category

from chatbot_financas.models import *
from sqlalchemy import Column, ForeignKey, String,Integer,Float, Table, DateTime,Enum
from sqlalchemy.orm import Relationship, properties, registry, relationship


mapper_registry = registry()

TimeAndIdMixin = [
    Column("id",Integer,primary_key=True,autoincrement=True),
    Column("created_at",DateTime),
    Column("updated_at",DateTime)
]



user_table = Table("users",mapper_registry.metadata,
    *TimeAndIdMixin,
    Column("chat_id",Integer,primary_key=True),
    Column("name",String(30),nullable=False),
    Column("balance",Float,default=0.00)
)

mapper_registry.map_imperatively(User,user_table,properties={
    'debts':relationship("debts",back_populates="debts"),
    'transactions':relationship("transactions",back_populates="transactions"),
    "fixed-incomes":relationship("fixed-incomes",back_populates="fixed-incomes")
})



debt_table = Table("debts",mapper_registry.metadata,
        *TimeAndIdMixin,
        Column("name",String(30),nullable=False),
        Column("value",Float,default=0.00),
        Column("user_id",ForeignKey("users.id"))
)
    
mapper_registry.map_imperatively(Debt,debt_table)

category_table = Table("categories",mapper_registry.metadata,
    *TimeAndIdMixin,
    Column("name",String(30))
)

mapper_registry.map_imperatively(Category,category_table,properties={'categories',relationship("categories",back_populates='categories')})

transaction_table = Table("transactions",mapper_registry.metadata,
    *TimeAndIdMixin,
    Column("amount",Float),
    Column("description",String(100)),
    Column("category_id",ForeignKey("categories.id")),
    Column("user_id",ForeignKey("users.id")),
    Column("type",Enum(TransactionType, name="transactiontype"),nullable=False)
)

mapper_registry.map_imperatively(Transaction,transaction_table)

fixed_income_table = Table("fixed-incomes",mapper_registry.metadata,
    *TimeAndIdMixin,
    Column("user_id",ForeignKey("users.id")),
    Column("profitability",Float),
    Column("ir",Float),
    Column("iof",Float),
    Column("b3",Float)
)

    
