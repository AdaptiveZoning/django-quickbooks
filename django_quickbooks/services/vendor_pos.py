from django_quickbooks import QUICKBOOKS_ENUMS
from django_quickbooks.services.base import Service


class VendorPOSService(Service):
    qb_type = None

    def add(self, object):
        return self._add(QUICKBOOKS_ENUMS.RESOURCE_VENDOR_POS, object)

    def update(self, object):
        return self._update(QUICKBOOKS_ENUMS.RESOURCE_VENDOR_POS, object)

    def all(self):
        return self._all(QUICKBOOKS_ENUMS.RESOURCE_VENDOR_POS)

    def find_by_id(self, id):
        return self._find_by_id(QUICKBOOKS_ENUMS.RESOURCE_VENDOR_POS, id)
