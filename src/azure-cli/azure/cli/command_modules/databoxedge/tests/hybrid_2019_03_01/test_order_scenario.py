# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

import os
from azure.cli.testsdk import ScenarioTest
from azure.cli.testsdk import ResourceGroupPreparer
from .example_steps import step_device_create
from .example_steps import step_device_delete
from .example_steps import step_order_create
from .example_steps import step_order_show
from .example_steps import step_order_list
from .example_steps import step_order_delete
from .. import (
    try_manual,
    raise_if,
    calc_coverage
)


TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


# Env setup_scenario
@try_manual
def setup_scenario(test, rg):
    step_device_create(test, rg)


# Env cleanup_scenario
@try_manual
def cleanup_scenario(test, rg):
    step_device_delete(test, rg)


# Testcase: Scenario
@try_manual
def call_scenario(test, rg):
    setup_scenario(test, rg)
    step_order_create(test, rg, checks=[
        test.check("contactInformation.companyName", "Microsoft", case_sensitive=False),
        test.check("contactInformation.contactPerson", "John Mcclane", case_sensitive=False),
        test.check("shippingAddress.country", "United States", case_sensitive=False),
    ])
    step_order_show(test, rg, checks=[
        test.check("contactInformation.companyName", "Microsoft", case_sensitive=False),
        test.check("contactInformation.contactPerson", "John Mcclane", case_sensitive=False),
        test.check("shippingAddress.country", "United States", case_sensitive=False),
    ])
    step_order_list(test, rg, checks=[
        test.check('length(@)', 1),
    ])
    step_order_delete(test, rg, checks=[])
    step_order_list(test, rg, checks=[
        test.check('length(@)', 0),
    ])
    cleanup_scenario(test, rg)


# Test class for Scenario
@try_manual
class OrderScenarioTest(ScenarioTest):

    @ResourceGroupPreparer(name_prefix='clitestdataboxedge_GroupForEdgeAutomation'[:7], key='rg', parameter_name='rg')
    def test_order_Scenario(self, rg):

        self.kwargs.update({
            'myDevice': 'testedgedevice',
        })

        call_scenario(self, rg)
        calc_coverage(__file__)
        raise_if()