# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class GetTdeCertificatesSqlTaskInput(Model):
    """Input for the task that gets TDE certificates in Base64 encoded format.

    All required parameters must be populated in order to send to Azure.

    :param connection_info: Required. Connection information for SQL Server
    :type connection_info: ~azure.mgmt.datamigration.models.SqlConnectionInfo
    :param backup_file_share: Required. Backup file share information for file
     share to be used for temporarily storing files.
    :type backup_file_share: ~azure.mgmt.datamigration.models.FileShare
    :param selected_certificates: Required. List containing certificate names
     and corresponding password to use for encrypting the exported certificate.
    :type selected_certificates:
     list[~azure.mgmt.datamigration.models.SelectedCertificateInput]
    """

    _validation = {
        'connection_info': {'required': True},
        'backup_file_share': {'required': True},
        'selected_certificates': {'required': True},
    }

    _attribute_map = {
        'connection_info': {'key': 'connectionInfo', 'type': 'SqlConnectionInfo'},
        'backup_file_share': {'key': 'backupFileShare', 'type': 'FileShare'},
        'selected_certificates': {'key': 'selectedCertificates', 'type': '[SelectedCertificateInput]'},
    }

    def __init__(self, *, connection_info, backup_file_share, selected_certificates, **kwargs) -> None:
        super(GetTdeCertificatesSqlTaskInput, self).__init__(**kwargs)
        self.connection_info = connection_info
        self.backup_file_share = backup_file_share
        self.selected_certificates = selected_certificates
