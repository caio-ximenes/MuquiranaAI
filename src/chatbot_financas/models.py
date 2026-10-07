from datetime import date,datetime
from enum import Enum



class TimeAndIdMixin:
    id:int
    created_at:datetime
    updated_at:datetime


class TransactionType(Enum):
    EARN = "earn"
    SPENT = "spent"

class User(TimeAndIdMixin):
    chat_id:int
    name:str
    balance:float

class Debt(TimeAndIdMixin):
    name:str
    value:float
    user:User


class Category(TimeAndIdMixin):
    name:str


class Transaction(TimeAndIdMixin):
    amount:float
    description:str
    category:Category
    type:TransactionType
    

class FixedIncome(TimeAndIdMixin):
    user:User
    profitability:float
    ir:float
    iof:float
    b3:float


    
    