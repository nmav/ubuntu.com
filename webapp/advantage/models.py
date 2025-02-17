from typing import List


class Entitlement:
    def __init__(
        self,
        type: str,
        enabled_by_default: bool,
        support_level: str = None,
    ):
        self.type = type
        self.support_level = support_level
        self.enabled_by_default = enabled_by_default


class Product:
    def __init__(
        self,
        id: str,
        name: str,
    ):
        self.id = id
        self.name = name


class Listing:
    def __init__(
        self,
        id: str,
        name: str,
        marketplace: str,
        price: int,
        currency: str,
        status: str,
        product: Product = None,
        trial_days: int = None,
        period: str = None,
    ):
        self.id = id
        self.name = name
        self.marketplace = marketplace
        self.product = product
        self.price = price
        self.currency = currency
        self.status = status
        self.trial_days = trial_days
        self.period = period


class UserSubscription:
    def __init__(
        self,
        account_id: str,
        product_name: str,
        type: str,
        start_date: str,
        number_of_machines: int,
        machine_type: str,
        marketplace: str,
        price: int,
        currency: str,
        entitlements: List[Entitlement],
        statuses: dict,
        contract_id: str,
        subscription_id: str = None,
        end_date: str = None,
        period: str = None,
        listing_id: str = None,
        renewal_id: str = None,
    ):
        self.account_id = account_id
        self.product_name = product_name
        self.type = type
        self.start_date = start_date
        self.end_date = end_date
        self.number_of_machines = number_of_machines
        self.machine_type = machine_type
        self.marketplace = marketplace
        self.price = price
        self.currency = currency
        self.entitlements = entitlements
        self.statuses = statuses
        self.period = period
        self.subscription_id = subscription_id
        self.contract_id = contract_id
        self.listing_id = listing_id
        self.renewal_id = renewal_id
