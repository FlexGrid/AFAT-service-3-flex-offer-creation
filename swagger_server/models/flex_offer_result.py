# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.flex_offer_result_aggr_flex_offer import FlexOfferResultAggrFlexOffer  # noqa: F401,E501
from swagger_server.models.flex_offer_result_expected_result import FlexOfferResultExpectedResult  # noqa: F401,E501
from swagger_server import util


class FlexOfferResult(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, aggr_flex_offer: FlexOfferResultAggrFlexOffer=None, expected_result: List[FlexOfferResultExpectedResult]=None):  # noqa: E501
        """FlexOfferResult - a model defined in Swagger

        :param aggr_flex_offer: The aggr_flex_offer of this FlexOfferResult.  # noqa: E501
        :type aggr_flex_offer: FlexOfferResultAggrFlexOffer
        :param expected_result: The expected_result of this FlexOfferResult.  # noqa: E501
        :type expected_result: List[FlexOfferResultExpectedResult]
        """
        self.swagger_types = {
            'aggr_flex_offer': FlexOfferResultAggrFlexOffer,
            'expected_result': List[FlexOfferResultExpectedResult]
        }

        self.attribute_map = {
            'aggr_flex_offer': 'aggr_flex_offer',
            'expected_result': 'expected_result'
        }
        self._aggr_flex_offer = aggr_flex_offer
        self._expected_result = expected_result

    @classmethod
    def from_dict(cls, dikt) -> 'FlexOfferResult':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The FlexOfferResult of this FlexOfferResult.  # noqa: E501
        :rtype: FlexOfferResult
        """
        return util.deserialize_model(dikt, cls)

    @property
    def aggr_flex_offer(self) -> FlexOfferResultAggrFlexOffer:
        """Gets the aggr_flex_offer of this FlexOfferResult.


        :return: The aggr_flex_offer of this FlexOfferResult.
        :rtype: FlexOfferResultAggrFlexOffer
        """
        return self._aggr_flex_offer

    @aggr_flex_offer.setter
    def aggr_flex_offer(self, aggr_flex_offer: FlexOfferResultAggrFlexOffer):
        """Sets the aggr_flex_offer of this FlexOfferResult.


        :param aggr_flex_offer: The aggr_flex_offer of this FlexOfferResult.
        :type aggr_flex_offer: FlexOfferResultAggrFlexOffer
        """

        self._aggr_flex_offer = aggr_flex_offer

    @property
    def expected_result(self) -> List[FlexOfferResultExpectedResult]:
        """Gets the expected_result of this FlexOfferResult.


        :return: The expected_result of this FlexOfferResult.
        :rtype: List[FlexOfferResultExpectedResult]
        """
        return self._expected_result

    @expected_result.setter
    def expected_result(self, expected_result: List[FlexOfferResultExpectedResult]):
        """Sets the expected_result of this FlexOfferResult.


        :param expected_result: The expected_result of this FlexOfferResult.
        :type expected_result: List[FlexOfferResultExpectedResult]
        """

        self._expected_result = expected_result