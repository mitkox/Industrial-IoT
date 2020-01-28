# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator 2.3.33.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class PublishStopRequestApiModel(Model):
    """Unpublish request.

    :param node_id: Node of published item to unpublish
    :type node_id: str
    :param header:
    :type header: ~azure-iiot-opc-publisher.models.RequestHeaderApiModel
    """

    _validation = {
        'node_id': {'required': True},
    }

    _attribute_map = {
        'node_id': {'key': 'nodeId', 'type': 'str'},
        'header': {'key': 'header', 'type': 'RequestHeaderApiModel'},
    }

    def __init__(self, node_id, header=None):
        super(PublishStopRequestApiModel, self).__init__()
        self.node_id = node_id
        self.header = header