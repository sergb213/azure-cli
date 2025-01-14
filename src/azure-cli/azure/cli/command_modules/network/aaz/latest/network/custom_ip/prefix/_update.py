# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "network custom-ip prefix update",
)
class Update(AAZCommand):
    """Update a custom IP prefix resource.

    :example: Update a custom IP prefix resource.
        az network custom-ip prefix update --name MyCustomIpPrefix --resource-group MyResourceGroup --tags foo=bar
    """

    _aaz_info = {
        "version": "2022-05-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.network/customipprefixes/{}", "2022-05-01"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    AZ_SUPPORT_GENERIC_UPDATE = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.name = AAZStrArg(
            options=["-n", "--name"],
            help="The name of the custom IP prefix.",
            required=True,
            id_part="name",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.authorization_message = AAZStrArg(
            options=["--authorization-message"],
            help="Authorization message for WAN validation.",
            nullable=True,
        )
        _args_schema.state = AAZStrArg(
            options=["--state"],
            help="Commissioned State of the custom ip prefix.",
            nullable=True,
            enum={"commission": "Commissioning", "decommission": "Decommissioning", "deprovision": "Deprovisioning", "provision": "Provisioning"},
        )
        _args_schema.no_internet_advertise = AAZBoolArg(
            options=["--no-internet-advertise"],
            help="Whether to Advertise the range to Internet.",
            nullable=True,
        )
        _args_schema.signed_message = AAZStrArg(
            options=["--signed-message"],
            help="Signed message for WAN validation.",
            nullable=True,
        )
        _args_schema.tags = AAZDictArg(
            options=["--tags"],
            help="Space-separated tags: key[=value] [key[=value] ...].",
            nullable=True,
        )

        tags = cls._args_schema.tags
        tags.Element = AAZStrArg(
            nullable=True,
        )

        # define Arg Group "Parameters"

        # define Arg Group "Properties"
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.CustomIPPrefixesGet(ctx=self.ctx)()
        self.pre_instance_update(self.ctx.vars.instance)
        self.InstanceUpdateByJson(ctx=self.ctx)()
        self.InstanceUpdateByGeneric(ctx=self.ctx)()
        self.post_instance_update(self.ctx.vars.instance)
        yield self.CustomIPPrefixesCreateOrUpdate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    @register_callback
    def pre_instance_update(self, instance):
        pass

    @register_callback
    def post_instance_update(self, instance):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class CustomIPPrefixesGet(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/customIpPrefixes/{customIpPrefixName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "customIpPrefixName", self.ctx.args.name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-05-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()
            _build_schema_custom_ip_prefix_read(cls._schema_on_200)

            return cls._schema_on_200

    class CustomIPPrefixesCreateOrUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "location"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200, 201]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "location"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/customIpPrefixes/{customIpPrefixName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "customIpPrefixName", self.ctx.args.name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-05-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=self.ctx.vars.instance,
            )

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()
            _build_schema_custom_ip_prefix_read(cls._schema_on_200_201)

            return cls._schema_on_200_201

    class InstanceUpdateByJson(AAZJsonInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance(self.ctx.vars.instance)

        def _update_instance(self, instance):
            _instance_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=instance,
                typ=AAZObjectType
            )
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})
            _builder.set_prop("tags", AAZDictType, ".tags")

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("authorizationMessage", AAZStrType, ".authorization_message")
                properties.set_prop("commissionedState", AAZStrType, ".state")
                properties.set_prop("noInternetAdvertise", AAZBoolType, ".no_internet_advertise")
                properties.set_prop("signedMessage", AAZStrType, ".signed_message")

            tags = _builder.get(".tags")
            if tags is not None:
                tags.set_elements(AAZStrType, ".")

            return _instance_value

    class InstanceUpdateByGeneric(AAZGenericInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance_by_generic(
                self.ctx.vars.instance,
                self.ctx.generic_update_args
            )


_schema_custom_ip_prefix_read = None


def _build_schema_custom_ip_prefix_read(_schema):
    global _schema_custom_ip_prefix_read
    if _schema_custom_ip_prefix_read is not None:
        _schema.etag = _schema_custom_ip_prefix_read.etag
        _schema.extended_location = _schema_custom_ip_prefix_read.extended_location
        _schema.id = _schema_custom_ip_prefix_read.id
        _schema.location = _schema_custom_ip_prefix_read.location
        _schema.name = _schema_custom_ip_prefix_read.name
        _schema.properties = _schema_custom_ip_prefix_read.properties
        _schema.tags = _schema_custom_ip_prefix_read.tags
        _schema.type = _schema_custom_ip_prefix_read.type
        _schema.zones = _schema_custom_ip_prefix_read.zones
        return

    _schema_custom_ip_prefix_read = AAZObjectType()

    custom_ip_prefix_read = _schema_custom_ip_prefix_read
    custom_ip_prefix_read.etag = AAZStrType(
        flags={"read_only": True},
    )
    custom_ip_prefix_read.extended_location = AAZObjectType(
        serialized_name="extendedLocation",
    )
    custom_ip_prefix_read.id = AAZStrType()
    custom_ip_prefix_read.location = AAZStrType()
    custom_ip_prefix_read.name = AAZStrType(
        flags={"read_only": True},
    )
    custom_ip_prefix_read.properties = AAZObjectType(
        flags={"client_flatten": True},
    )
    custom_ip_prefix_read.tags = AAZDictType()
    custom_ip_prefix_read.type = AAZStrType(
        flags={"read_only": True},
    )
    custom_ip_prefix_read.zones = AAZListType()

    extended_location = _schema_custom_ip_prefix_read.extended_location
    extended_location.name = AAZStrType()
    extended_location.type = AAZStrType()

    properties = _schema_custom_ip_prefix_read.properties
    properties.asn = AAZStrType()
    properties.authorization_message = AAZStrType(
        serialized_name="authorizationMessage",
    )
    properties.child_custom_ip_prefixes = AAZListType(
        serialized_name="childCustomIpPrefixes",
        flags={"read_only": True},
    )
    properties.cidr = AAZStrType()
    properties.commissioned_state = AAZStrType(
        serialized_name="commissionedState",
    )
    properties.custom_ip_prefix_parent = AAZObjectType(
        serialized_name="customIpPrefixParent",
    )
    _build_schema_sub_resource_read(properties.custom_ip_prefix_parent)
    properties.express_route_advertise = AAZBoolType(
        serialized_name="expressRouteAdvertise",
    )
    properties.failed_reason = AAZStrType(
        serialized_name="failedReason",
        flags={"read_only": True},
    )
    properties.geo = AAZStrType()
    properties.no_internet_advertise = AAZBoolType(
        serialized_name="noInternetAdvertise",
    )
    properties.prefix_type = AAZStrType(
        serialized_name="prefixType",
    )
    properties.provisioning_state = AAZStrType(
        serialized_name="provisioningState",
        flags={"read_only": True},
    )
    properties.public_ip_prefixes = AAZListType(
        serialized_name="publicIpPrefixes",
        flags={"read_only": True},
    )
    properties.resource_guid = AAZStrType(
        serialized_name="resourceGuid",
        flags={"read_only": True},
    )
    properties.signed_message = AAZStrType(
        serialized_name="signedMessage",
    )

    child_custom_ip_prefixes = _schema_custom_ip_prefix_read.properties.child_custom_ip_prefixes
    child_custom_ip_prefixes.Element = AAZObjectType()
    _build_schema_sub_resource_read(child_custom_ip_prefixes.Element)

    public_ip_prefixes = _schema_custom_ip_prefix_read.properties.public_ip_prefixes
    public_ip_prefixes.Element = AAZObjectType()
    _build_schema_sub_resource_read(public_ip_prefixes.Element)

    tags = _schema_custom_ip_prefix_read.tags
    tags.Element = AAZStrType()

    zones = _schema_custom_ip_prefix_read.zones
    zones.Element = AAZStrType()

    _schema.etag = _schema_custom_ip_prefix_read.etag
    _schema.extended_location = _schema_custom_ip_prefix_read.extended_location
    _schema.id = _schema_custom_ip_prefix_read.id
    _schema.location = _schema_custom_ip_prefix_read.location
    _schema.name = _schema_custom_ip_prefix_read.name
    _schema.properties = _schema_custom_ip_prefix_read.properties
    _schema.tags = _schema_custom_ip_prefix_read.tags
    _schema.type = _schema_custom_ip_prefix_read.type
    _schema.zones = _schema_custom_ip_prefix_read.zones


_schema_sub_resource_read = None


def _build_schema_sub_resource_read(_schema):
    global _schema_sub_resource_read
    if _schema_sub_resource_read is not None:
        _schema.id = _schema_sub_resource_read.id
        return

    _schema_sub_resource_read = AAZObjectType()

    sub_resource_read = _schema_sub_resource_read
    sub_resource_read.id = AAZStrType()

    _schema.id = _schema_sub_resource_read.id


__all__ = ["Update"]
