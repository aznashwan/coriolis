# Copyright 2016 Cloudbase Solutions Srl
# All Rights Reserved.

EXECUTION_STATUS_RUNNING = "RUNNING"
EXECUTION_STATUS_COMPLETED = "COMPLETED"
EXECUTION_STATUS_ERROR = "ERROR"

TASK_STATUS_PENDING = "PENDING"
TASK_STATUS_RUNNING = "RUNNING"
TASK_STATUS_COMPLETED = "COMPLETED"
TASK_STATUS_ERROR = "ERROR"
TASK_STATUS_CANCELED = "CANCELED"

TASK_TYPE_EXPORT_INSTANCE = "EXPORT_INSTANCE"
TASK_TYPE_IMPORT_INSTANCE = "IMPORT_INSTANCE"

TASK_TYPE_GET_INSTANCE_INFO = "GET_INSTANCE_INFO"
TASK_TYPE_DEPLOY_REPLICA_DISKS = "DEPLOY_REPLICA_DISKS"
TASK_TYPE_DELETE_REPLICA_DISKS = "DELETE_REPLICA_DISKS"
TASK_TYPE_REPLICATE_DISKS = "REPLICATE_DISKS"
TASK_TYPE_DEPLOY_REPLICA_RESOURCES = "DEPLOY_REPLICA_RESOURCES"
TASK_TYPE_DELETE_REPLICA_RESOURCES = "DELETE_REPLICA_RESOURCES"
TASK_TYPE_SHUTDOWN_INSTANCE = "SHUTDOWN_INSTANCE"
TASK_TYPE_DEPLOY_REPLICA_INSTANCE = "DEPLOY_REPLICA_INSTANCE"
TASK_TYPE_CREATE_REPLICA_DISK_SNAPSHOTS = "CREATE_REPLICA_DISK_SNAPSHOTS"
TASK_TYPE_DELETE_REPLICA_DISK_SNAPSHOTS = "DELETE_REPLICA_DISK_SNAPSHOTS"


PROVIDER_TYPE_IMPORT = 1
PROVIDER_TYPE_EXPORT = 2

DISK_FORMAT_VMDK = 'vmdk'
DISK_FORMAT_RAW = 'raw'
DISK_FORMAT_QCOW = "qcow"
DISK_FORMAT_QCOW2 = 'qcow2'
DISK_FORMAT_VHD = 'vhd'
DISK_FORMAT_VHDX = 'vhdx'

FIRMWARE_TYPE_BIOS = 'BIOS'
FIRMWARE_TYPE_EFI = 'EFI'

HYPERVISOR_VMWARE = "vmware"
HYPERVISOR_HYPERV = "hyperv"
HYPERVISOR_QEMU = "qemu"
HYPERVISOR_KVM = "kvm"
HYPERVISOR_XENSERVER = "xenserver"

PLATFORM_AZURE_RM = "azure"
PLATFORM_OPENSTACK = "openstack"
PLATFORM_VMWARE_VSPHERE = "vmware_vsphere"

TASK_EVENT_INFO = "INFO"
TASK_EVENT_WARNING = "WARNING"
TASK_EVENT_ERROR = "ERROR"

OS_TYPE_BSD = "bsd"
OS_TYPE_LINUX = "linux"
OS_TYPE_OS_X = "osx"
OS_TYPE_SOLARIS = "solaris"
OS_TYPE_WINDOWS = "windows"

TMP_DIRS_KEY = "__tmp_dirs"
