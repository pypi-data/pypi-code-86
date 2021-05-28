# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.3078
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class CdsFlowConventions(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
      required_map (dict): The key is attribute name
                           and the value is whether it is 'required' or 'optional'.
    """
    openapi_types = {
        'roll_frequency': 'str',
        'currency': 'str',
        'payment_frequency': 'str',
        'day_count_convention': 'str',
        'roll_convention': 'str',
        'payment_calendars': 'list[str]',
        'reset_calendars': 'list[str]',
        'settle_days': 'int',
        'reset_days': 'int',
        'scope': 'str',
        'code': 'str'
    }

    attribute_map = {
        'roll_frequency': 'rollFrequency',
        'currency': 'currency',
        'payment_frequency': 'paymentFrequency',
        'day_count_convention': 'dayCountConvention',
        'roll_convention': 'rollConvention',
        'payment_calendars': 'paymentCalendars',
        'reset_calendars': 'resetCalendars',
        'settle_days': 'settleDays',
        'reset_days': 'resetDays',
        'scope': 'scope',
        'code': 'code'
    }

    required_map = {
        'roll_frequency': 'optional',
        'currency': 'required',
        'payment_frequency': 'required',
        'day_count_convention': 'required',
        'roll_convention': 'required',
        'payment_calendars': 'required',
        'reset_calendars': 'required',
        'settle_days': 'required',
        'reset_days': 'required',
        'scope': 'optional',
        'code': 'optional'
    }

    def __init__(self, roll_frequency=None, currency=None, payment_frequency=None, day_count_convention=None, roll_convention=None, payment_calendars=None, reset_calendars=None, settle_days=None, reset_days=None, scope=None, code=None):  # noqa: E501
        """
        CdsFlowConventions - a model defined in OpenAPI

        :param roll_frequency:  The frequency at which the reference bonds are updated, this defaults to 6M, but can be 3M, exp for historically issued products
        :type roll_frequency: str
        :param currency:  Currency of the flow convention. (required)
        :type currency: str
        :param payment_frequency:  When generating a multiperiod flow, or when the maturity of the flow is not given but the start date is,  the tenor is the time-step from the anchor-date to the nominal maturity of the flow prior to any adjustment. (required)
        :type payment_frequency: str
        :param day_count_convention:  when calculating the fraction of a year between two dates, what convention is used to represent the number of days in a year  and difference between them.  Supported string (enumeration) values are: [Actual360, Act360, MoneyMarket, Actual365, Act365, Thirty360, ThirtyU360, Bond, ThirtyE360, EuroBond, ActAct, ActualActual, ActActIsda, ActActIsma, ActActIcma, Invalid]. (required)
        :type day_count_convention: str
        :param roll_convention:  When generating a set of dates, what convention should be used for adjusting dates that coincide with a non-business day.  Supported string (enumeration) values are: [NoAdjustment, None, Previous, P, Following, F, ModifiedPrevious, MP, ModifiedFollowing, MF, EndOfMonth, EOM, EndOfMonthPrevious, EOMP, EndOfMonthFollowing, EOMF, Invalid]. (required)
        :type roll_convention: str
        :param payment_calendars:  An array of strings denoting holiday calendars that apply to generation of payment schedules. (required)
        :type payment_calendars: list[str]
        :param reset_calendars:  An array of strings denoting holiday calendars that apply to generation of reset schedules. (required)
        :type reset_calendars: list[str]
        :param settle_days:  Number of Good Business Days between the trade date and the effective or settlement date of the instrument. (required)
        :type settle_days: int
        :param reset_days:  The number of Good Business Days between determination and payment of reset. (required)
        :type reset_days: int
        :param scope:  The scope used when updating or inserting the convention.
        :type scope: str
        :param code:  The code of the convention.
        :type code: str

        """  # noqa: E501

        self._roll_frequency = None
        self._currency = None
        self._payment_frequency = None
        self._day_count_convention = None
        self._roll_convention = None
        self._payment_calendars = None
        self._reset_calendars = None
        self._settle_days = None
        self._reset_days = None
        self._scope = None
        self._code = None
        self.discriminator = None

        self.roll_frequency = roll_frequency
        self.currency = currency
        self.payment_frequency = payment_frequency
        self.day_count_convention = day_count_convention
        self.roll_convention = roll_convention
        self.payment_calendars = payment_calendars
        self.reset_calendars = reset_calendars
        self.settle_days = settle_days
        self.reset_days = reset_days
        self.scope = scope
        self.code = code

    @property
    def roll_frequency(self):
        """Gets the roll_frequency of this CdsFlowConventions.  # noqa: E501

        The frequency at which the reference bonds are updated, this defaults to 6M, but can be 3M, exp for historically issued products  # noqa: E501

        :return: The roll_frequency of this CdsFlowConventions.  # noqa: E501
        :rtype: str
        """
        return self._roll_frequency

    @roll_frequency.setter
    def roll_frequency(self, roll_frequency):
        """Sets the roll_frequency of this CdsFlowConventions.

        The frequency at which the reference bonds are updated, this defaults to 6M, but can be 3M, exp for historically issued products  # noqa: E501

        :param roll_frequency: The roll_frequency of this CdsFlowConventions.  # noqa: E501
        :type: str
        """

        self._roll_frequency = roll_frequency

    @property
    def currency(self):
        """Gets the currency of this CdsFlowConventions.  # noqa: E501

        Currency of the flow convention.  # noqa: E501

        :return: The currency of this CdsFlowConventions.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this CdsFlowConventions.

        Currency of the flow convention.  # noqa: E501

        :param currency: The currency of this CdsFlowConventions.  # noqa: E501
        :type: str
        """
        if currency is None:
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501

        self._currency = currency

    @property
    def payment_frequency(self):
        """Gets the payment_frequency of this CdsFlowConventions.  # noqa: E501

        When generating a multiperiod flow, or when the maturity of the flow is not given but the start date is,  the tenor is the time-step from the anchor-date to the nominal maturity of the flow prior to any adjustment.  # noqa: E501

        :return: The payment_frequency of this CdsFlowConventions.  # noqa: E501
        :rtype: str
        """
        return self._payment_frequency

    @payment_frequency.setter
    def payment_frequency(self, payment_frequency):
        """Sets the payment_frequency of this CdsFlowConventions.

        When generating a multiperiod flow, or when the maturity of the flow is not given but the start date is,  the tenor is the time-step from the anchor-date to the nominal maturity of the flow prior to any adjustment.  # noqa: E501

        :param payment_frequency: The payment_frequency of this CdsFlowConventions.  # noqa: E501
        :type: str
        """
        if payment_frequency is None:
            raise ValueError("Invalid value for `payment_frequency`, must not be `None`")  # noqa: E501

        self._payment_frequency = payment_frequency

    @property
    def day_count_convention(self):
        """Gets the day_count_convention of this CdsFlowConventions.  # noqa: E501

        when calculating the fraction of a year between two dates, what convention is used to represent the number of days in a year  and difference between them.  Supported string (enumeration) values are: [Actual360, Act360, MoneyMarket, Actual365, Act365, Thirty360, ThirtyU360, Bond, ThirtyE360, EuroBond, ActAct, ActualActual, ActActIsda, ActActIsma, ActActIcma, Invalid].  # noqa: E501

        :return: The day_count_convention of this CdsFlowConventions.  # noqa: E501
        :rtype: str
        """
        return self._day_count_convention

    @day_count_convention.setter
    def day_count_convention(self, day_count_convention):
        """Sets the day_count_convention of this CdsFlowConventions.

        when calculating the fraction of a year between two dates, what convention is used to represent the number of days in a year  and difference between them.  Supported string (enumeration) values are: [Actual360, Act360, MoneyMarket, Actual365, Act365, Thirty360, ThirtyU360, Bond, ThirtyE360, EuroBond, ActAct, ActualActual, ActActIsda, ActActIsma, ActActIcma, Invalid].  # noqa: E501

        :param day_count_convention: The day_count_convention of this CdsFlowConventions.  # noqa: E501
        :type: str
        """
        if day_count_convention is None:
            raise ValueError("Invalid value for `day_count_convention`, must not be `None`")  # noqa: E501

        self._day_count_convention = day_count_convention

    @property
    def roll_convention(self):
        """Gets the roll_convention of this CdsFlowConventions.  # noqa: E501

        When generating a set of dates, what convention should be used for adjusting dates that coincide with a non-business day.  Supported string (enumeration) values are: [NoAdjustment, None, Previous, P, Following, F, ModifiedPrevious, MP, ModifiedFollowing, MF, EndOfMonth, EOM, EndOfMonthPrevious, EOMP, EndOfMonthFollowing, EOMF, Invalid].  # noqa: E501

        :return: The roll_convention of this CdsFlowConventions.  # noqa: E501
        :rtype: str
        """
        return self._roll_convention

    @roll_convention.setter
    def roll_convention(self, roll_convention):
        """Sets the roll_convention of this CdsFlowConventions.

        When generating a set of dates, what convention should be used for adjusting dates that coincide with a non-business day.  Supported string (enumeration) values are: [NoAdjustment, None, Previous, P, Following, F, ModifiedPrevious, MP, ModifiedFollowing, MF, EndOfMonth, EOM, EndOfMonthPrevious, EOMP, EndOfMonthFollowing, EOMF, Invalid].  # noqa: E501

        :param roll_convention: The roll_convention of this CdsFlowConventions.  # noqa: E501
        :type: str
        """
        if roll_convention is None:
            raise ValueError("Invalid value for `roll_convention`, must not be `None`")  # noqa: E501

        self._roll_convention = roll_convention

    @property
    def payment_calendars(self):
        """Gets the payment_calendars of this CdsFlowConventions.  # noqa: E501

        An array of strings denoting holiday calendars that apply to generation of payment schedules.  # noqa: E501

        :return: The payment_calendars of this CdsFlowConventions.  # noqa: E501
        :rtype: list[str]
        """
        return self._payment_calendars

    @payment_calendars.setter
    def payment_calendars(self, payment_calendars):
        """Sets the payment_calendars of this CdsFlowConventions.

        An array of strings denoting holiday calendars that apply to generation of payment schedules.  # noqa: E501

        :param payment_calendars: The payment_calendars of this CdsFlowConventions.  # noqa: E501
        :type: list[str]
        """
        if payment_calendars is None:
            raise ValueError("Invalid value for `payment_calendars`, must not be `None`")  # noqa: E501

        self._payment_calendars = payment_calendars

    @property
    def reset_calendars(self):
        """Gets the reset_calendars of this CdsFlowConventions.  # noqa: E501

        An array of strings denoting holiday calendars that apply to generation of reset schedules.  # noqa: E501

        :return: The reset_calendars of this CdsFlowConventions.  # noqa: E501
        :rtype: list[str]
        """
        return self._reset_calendars

    @reset_calendars.setter
    def reset_calendars(self, reset_calendars):
        """Sets the reset_calendars of this CdsFlowConventions.

        An array of strings denoting holiday calendars that apply to generation of reset schedules.  # noqa: E501

        :param reset_calendars: The reset_calendars of this CdsFlowConventions.  # noqa: E501
        :type: list[str]
        """
        if reset_calendars is None:
            raise ValueError("Invalid value for `reset_calendars`, must not be `None`")  # noqa: E501

        self._reset_calendars = reset_calendars

    @property
    def settle_days(self):
        """Gets the settle_days of this CdsFlowConventions.  # noqa: E501

        Number of Good Business Days between the trade date and the effective or settlement date of the instrument.  # noqa: E501

        :return: The settle_days of this CdsFlowConventions.  # noqa: E501
        :rtype: int
        """
        return self._settle_days

    @settle_days.setter
    def settle_days(self, settle_days):
        """Sets the settle_days of this CdsFlowConventions.

        Number of Good Business Days between the trade date and the effective or settlement date of the instrument.  # noqa: E501

        :param settle_days: The settle_days of this CdsFlowConventions.  # noqa: E501
        :type: int
        """
        if settle_days is None:
            raise ValueError("Invalid value for `settle_days`, must not be `None`")  # noqa: E501

        self._settle_days = settle_days

    @property
    def reset_days(self):
        """Gets the reset_days of this CdsFlowConventions.  # noqa: E501

        The number of Good Business Days between determination and payment of reset.  # noqa: E501

        :return: The reset_days of this CdsFlowConventions.  # noqa: E501
        :rtype: int
        """
        return self._reset_days

    @reset_days.setter
    def reset_days(self, reset_days):
        """Sets the reset_days of this CdsFlowConventions.

        The number of Good Business Days between determination and payment of reset.  # noqa: E501

        :param reset_days: The reset_days of this CdsFlowConventions.  # noqa: E501
        :type: int
        """
        if reset_days is None:
            raise ValueError("Invalid value for `reset_days`, must not be `None`")  # noqa: E501

        self._reset_days = reset_days

    @property
    def scope(self):
        """Gets the scope of this CdsFlowConventions.  # noqa: E501

        The scope used when updating or inserting the convention.  # noqa: E501

        :return: The scope of this CdsFlowConventions.  # noqa: E501
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this CdsFlowConventions.

        The scope used when updating or inserting the convention.  # noqa: E501

        :param scope: The scope of this CdsFlowConventions.  # noqa: E501
        :type: str
        """

        self._scope = scope

    @property
    def code(self):
        """Gets the code of this CdsFlowConventions.  # noqa: E501

        The code of the convention.  # noqa: E501

        :return: The code of this CdsFlowConventions.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this CdsFlowConventions.

        The code of the convention.  # noqa: E501

        :param code: The code of this CdsFlowConventions.  # noqa: E501
        :type: str
        """

        self._code = code

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CdsFlowConventions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
