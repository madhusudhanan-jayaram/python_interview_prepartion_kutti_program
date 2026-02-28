from dataclasses import dataclass, field

@dataclass()
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class Customer:
    customer_id: str
    first_name: str
    last_name: str
    email: str
    phone: Optional[str]
    date_of_birth: str
    created_at: datetime = field(default_factory=datetime.utcnow)

    def __post_init__(self):
        # Rule: customer_id cannot be empty
        if not self.customer_id.strip():
            raise ValueError("customer_id cannot be empty")

        # Rule: email must contain '@'
        if "@" not in self.email:
            raise ValueError("Invalid email address")

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

c = Customer(
    customer_id="BARC12345",
    first_name="Madhu",
    last_name="Sudhanan",
    email="madhu@example.com",
    phone="1234567890",
    date_of_birth="1995-01-01"
)







