# Copyright 2016 Cloudbase Solutions Srl
# All Rights Reserved.

from oslo_log import log as logging

from coriolis import constants
from coriolis import events
from coriolis.providers import factory as providers_factory
from coriolis.tasks import base
from coriolis.tasks import replica_tasks

LOG = logging.getLogger(__name__)


class GetOptimalFlavorTask(base.TaskRunner):
    def run(self, ctxt, instance, origin, destination, task_info,
            event_handler):
        provider = providers_factory.get_provider(
            destination["type"], constants.PROVIDER_TYPE_INSTANCE_FLAVOR,
            event_handler)

        connection_info = base.get_connection_info(ctxt, destination)
        target_environment = destination.get("target_environment") or {}
        export_info = task_info["export_info"]

        flavor = provider.get_optimal_flavor(
            ctxt, connection_info, target_environment, export_info)

        if task_info.get("instance_deployment_info") is None:
            task_info["instance_deployment_info"] = {}
        task_info["instance_deployment_info"]["selected_flavor"] = flavor

        events.EventManager(event_handler).progress_update(
            "Selected flavor: %s" % flavor)

        task_info["retain_export_path"] = True

        return task_info


class DeployMigrationSourceResourcesTask(
        replica_tasks.DeployReplicaSourceResourcesTask):
    pass


class DeployMigrationTargetResourcesTask(
        replica_tasks.DeployReplicaTargetResourcesTask):
    pass


class CreateInstanceDisksTask(
        replica_tasks.DeployReplicaDisksTask):
    pass


class FinalizeInstanceDeploymentTask(
        replica_tasks.FinalizeReplicaInstanceDeploymentTask):
    pass


class CleanupFailedInstanceDeploymentTask(base.TaskRunner):
    """ Combines the functionality of Replica cleanup and Replica
    disk deletion tasks sequentially to ensure no conflicts occur.
    """
    def __init__(self):
        self._cleanup_task = (
            replica_tasks.CleanupFailedReplicaInstanceDeploymentTask())
        self._del_disk_task = (
            replica_tasks.DeleteReplicaDisksTask())

    def run(self, ctxt, instance, origin, destination, task_info,
            event_handler):
        task_info = self._cleanup_task.run(
            ctxt, instance, origin, destination, task_info, event_handler)
        task_info = self._del_disk_task.run(
            ctxt, instance, origin, destination, task_info, event_handler)
        return task_info


class ValidateMigrationSourceInputsTask(
        replica_tasks.ValidateReplicaExecutionSourceInputsTask):
    pass


class ValidateMigrationDestinationInputsTask(
        replica_tasks.ValidateReplicaExecutionDestinationInputsTask):
    def _validate_provider_replica_import_input(
            self, provider, ctxt, conn_info, target_environment, export_info):
        provider.validate_replica_import_input(
            ctxt, conn_info, target_environment, export_info,
            check_os_morphing_resources=True,
            check_final_vm_params=True)


class DeleteMigrationSourceResourcesTask(
        replica_tasks.DeleteReplicaSourceResourcesTask):
    pass


class DeleteMigrationTargetResourcesTask(
        replica_tasks.DeleteReplicaTargetResourcesTask):
    pass


class DeployInstanceResourcesTask(replica_tasks.DeployReplicaInstanceTask):
    pass
