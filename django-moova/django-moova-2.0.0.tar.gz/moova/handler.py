# -*- coding: utf-8 -*-
import logging

from moova.connector import Connector, ConnectorException
from moova.settings import api_settings

logger = logging.getLogger(__name__)


class MoovaHandler(object):
    """
        Handler to send shipping payload to Moova
    """
    def __init__(self, base_url=api_settings.MOOVA['BASE_URL'],
                 secret=api_settings.MOOVA['SECRET'],
                 key=api_settings.MOOVA['KEY'],
                 verify=True):

        self.base_url = base_url
        self.secret = secret
        self.key = key
        self.verify = verify
        self.connector = Connector(self._headers(), verify_ssl=self.verify)

    def _headers(self):
        """
            Here define the headers for all connections with Moova.
        """
        return {
            'Authorization': self.secret,
            'Content-Type': 'application/json'
        }

    def get_shipping_label(self, shipping_id):
        """
            This method helps us to obtain the url of the label for
            our shipping created.
        """
        url = f'{self.base_url}shippings/{shipping_id}/label/?appId={self.key}'

        try:
            response = self.connector.get(url)
            return response['label']
        except ConnectorException as error:
            logger.error(error)
            raise ConnectorException(error.message, error.description, error.code) from error

    def get_default_payload(self, instance):
        """
            This method generates by default all the necessary data with
            an appropriate structure for Moova courier.
        """
        try:
            payload = {
                'currency': api_settings.MOOVA['CURRENCY'],
                'type': api_settings.MOOVA['TYPE'],
                'flow': api_settings.MOOVA['FLOW'],
                'from': {
                    'street': api_settings.REMITENTE['STREET'],
                    'number': api_settings.REMITENTE['NUMBER'],
                    'floor': api_settings.REMITENTE['FLOOR'],
                    'apartment': api_settings.REMITENTE['APARTMENT'],
                    'city': api_settings.REMITENTE['CITY'],
                    'state': api_settings.REMITENTE['STATE'],
                    'postalCode': api_settings.REMITENTE['POSTALCODE'],
                    'country': api_settings.REMITENTE['COUNTRY'],
                    'instructions': api_settings.REMITENTE['INSTRUCTIONS'],
                    'contact': {
                        'firstName': api_settings.REMITENTE['FIRST_NAME'],
                        'lastName': api_settings.REMITENTE['LAST_NAME'],
                        'email': api_settings.REMITENTE['EMAIL'],
                        'phone': api_settings.REMITENTE['PHONE']
                    }
                },
                'to': {
                    'street': instance.address.street,
                    'number': instance.address.number,
                    'floor': '',
                    'apartment': instance.address.unit,
                    'city': instance.address.commune.name,
                    'state': instance.address.commune.region.name,
                    'postalCode': instance.address.commune.code,
                    'country': api_settings.REMITENTE['COUNTRY'],
                    'instructions': instance.order.comment,
                    'contact': {
                        'firstName': instance.address.customer.first_name,
                        'lastName': instance.address.customer.last_name,
                        'email': instance.address.customer.email,
                        'phone': instance.address.customer.phone
                    },
                    'message': ''
                },
                'internalCode': api_settings.MOOVA['INTERNALCODE'],
                'extra': api_settings.MOOVA['EXTRA'],
                'conf': {
                    'assurance': api_settings.MOOVA['ASSURANCE'],
                    'items': [
                        {
                            'item': {
                                'description': '',
                                'price': '',
                            }
                        }
                    ]
                }
            }

            if hasattr(instance, 'order_details'):
                payload['config']['items'] = [
                    {
                        'item': {
                            'description': detail.product.name,
                            'price': int(detail.unit_price),
                            'weight': 20,
                            'length': 20,
                            'width': 20,
                            'height': 20
                        }
                    } for detail in instance.order_details.all()
                ]

            logger.debug(payload)
            return payload
        except Exception as error:
            logger.error(error)
            raise Exception(error) from error

    def create_shipping(self, data):
        """
            This method generate a Moova shipping.
            If the get_default_payload method returns data, send it here,
            otherwise, generate your own payload.

            Additionally data was added to the response:
                tracking_number -> number to track the shipment.
                label -> url for view label.
        """
        url = f'{self.base_url}shippings?appId={self.key}'
        logger.debug(data)

        try:
            response = self.connector.post(url, data)
            tracking_number = response.get('id')
            label = self.get_shipping_label(tracking_number)

            logger.debug(tracking_number, label, response)
            return {**response, 'label': label, 'tracking_number': tracking_number}

        except ConnectorException as error:
            logger.error(error)
            raise ConnectorException(error.message, error.description, error.code) from error

    def get_tracking(self, identifier):
        """
            This method obtain a detail a shipping of Enviame.
        """
        url = f'{self.base_url}shippings/{identifier}?appId={self.key}'

        try:
            response = self.connector.get(url)
            logger.debug(response)
            return response
        except ConnectorException as error:
            logger.error(error)
            raise ConnectorException(error.message, error.description, error.code) from error
