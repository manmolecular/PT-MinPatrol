#!/usr/bin/env python3
import wmi

from transports import get_transport


def setup_module():
    global WMIconnect
    global WMIregistry
    WMIconnect = get_transport('WMI')
    WMIregistry = get_transport('WMIreg')


def test_valid_command_status():
    assert (bool(WMIconnect.wmi_exec('ipconfig')['result']) == False)


def test_return_object_wmi_query():
    result = WMIconnect.wmi_query("Select Name, \
            DNSHostName, Domain, Workgroup, PartOfDomain \
            from Win32_ComputerSystem")[0]
    assert isinstance(result, wmi._wmi_object)


def test_registry_get_value():
    result = WMIregistry.get_value(
        'Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System',
        'EnableLUA')
    accepted_values = [0, 1]
    assert result in accepted_values
