# Copyright 2016 Cloudbase Solutions Srl
# All Rights Reserved.

from coriolis import constants
from coriolis import exception
from coriolis.tasks import migration_tasks
from coriolis.tasks import osmorphing_tasks
from coriolis.tasks import replica_tasks

_TASKS_MAP = {
    constants.TASK_TYPE_DEPLOY_MIGRATION_SOURCE_RESOURCES:
        migration_tasks.DeployMigrationSourceResourcesTask,
    constants.TASK_TYPE_DEPLOY_MIGRATION_TARGET_RESOURCES:
        migration_tasks.DeployMigrationTargetResourcesTask,
    constants.TASK_TYPE_DELETE_MIGRATION_SOURCE_RESOURCES:
        migration_tasks.DeleteMigrationSourceResourcesTask,
    constants.TASK_TYPE_DELETE_MIGRATION_TARGET_RESOURCES:
        migration_tasks.DeleteMigrationTargetResourcesTask,
    constants.TASK_TYPE_DEPLOY_INSTANCE_RESOURCES:
        migration_tasks.DeployInstanceResourcesTask,
    constants.TASK_TYPE_FINALIZE_INSTANCE_DEPLOYMENT:
        migration_tasks.FinalizeInstanceDeploymentTask,
    constants.TASK_TYPE_CREATE_INSTANCE_DISKS:
        migration_tasks.CreateInstanceDisksTask,
    constants.TASK_TYPE_CLEANUP_FAILED_INSTANCE_DEPLOYMENT:
        migration_tasks.CleanupFailedInstanceDeploymentTask,
    constants.TASK_TYPE_GET_OPTIMAL_FLAVOR:
        migration_tasks.GetOptimalFlavorTask,
    constants.TASK_TYPE_VALIDATE_MIGRATION_SOURCE_INPUTS:
        migration_tasks.ValidateMigrationSourceInputsTask,
    constants.TASK_TYPE_VALIDATE_MIGRATION_DESTINATION_INPUTS:
        migration_tasks.ValidateMigrationDestinationInputsTask,
    constants.TASK_TYPE_DEPLOY_OS_MORPHING_RESOURCES:
        osmorphing_tasks.DeployOSMorphingResourcesTask,
    constants.TASK_TYPE_OS_MORPHING:
        osmorphing_tasks.OSMorphingTask,
    constants.TASK_TYPE_DELETE_OS_MORPHING_RESOURCES:
        osmorphing_tasks.DeleteOSMorphingResourcesTask,
    constants.TASK_TYPE_GET_INSTANCE_INFO:
        replica_tasks.GetInstanceInfoTask,
    constants.TASK_TYPE_REPLICATE_DISKS:
        replica_tasks.ReplicateDisksTask,
    constants.TASK_TYPE_SHUTDOWN_INSTANCE:
        replica_tasks.ShutdownInstanceTask,
    constants.TASK_TYPE_DEPLOY_REPLICA_DISKS:
        replica_tasks.DeployReplicaDisksTask,
    constants.TASK_TYPE_DELETE_REPLICA_DISKS:
        replica_tasks.DeleteReplicaDisksTask,
    constants.TASK_TYPE_DEPLOY_REPLICA_TARGET_RESOURCES:
        replica_tasks.DeployReplicaTargetResourcesTask,
    constants.TASK_TYPE_DELETE_REPLICA_TARGET_RESOURCES:
        replica_tasks.DeleteReplicaTargetResourcesTask,
    constants.TASK_TYPE_DEPLOY_REPLICA_SOURCE_RESOURCES:
        replica_tasks.DeployReplicaSourceResourcesTask,
    constants.TASK_TYPE_DELETE_REPLICA_SOURCE_RESOURCES:
        replica_tasks.DeleteReplicaSourceResourcesTask,
    constants.TASK_TYPE_DEPLOY_REPLICA_INSTANCE:
        replica_tasks.DeployReplicaInstanceTask,
    constants.TASK_TYPE_FINALIZE_REPLICA_INSTANCE_DEPLOYMENT:
        replica_tasks.FinalizeReplicaInstanceDeploymentTask,
    constants.TASK_TYPE_CLEANUP_FAILED_REPLICA_INSTANCE_DEPLOYMENT:
        replica_tasks.CleanupFailedReplicaInstanceDeploymentTask,
    constants.TASK_TYPE_CREATE_REPLICA_DISK_SNAPSHOTS:
        replica_tasks.CreateReplicaDiskSnapshotsTask,
    constants.TASK_TYPE_DELETE_REPLICA_DISK_SNAPSHOTS:
        replica_tasks.DeleteReplicaDiskSnapshotsTask,
    constants.TASK_TYPE_RESTORE_REPLICA_DISK_SNAPSHOTS:
        replica_tasks.RestoreReplicaDiskSnapshotsTask,
    constants.TASK_TYPE_VALIDATE_REPLICA_SOURCE_INPUTS:
        replica_tasks.ValidateReplicaExecutionSourceInputsTask,
    constants.TASK_TYPE_VALIDATE_REPLICA_DESTINATION_INPUTS:
        replica_tasks.ValidateReplicaExecutionDestinationInputsTask,
    constants.TASK_TYPE_VALIDATE_REPLICA_DEPLOYMENT_INPUTS:
        replica_tasks.ValidateReplicaDeploymentParametersTask,
    constants.TASK_TYPE_UPDATE_SOURCE_REPLICA:
        replica_tasks.UpdateSourceReplicaTask,
    constants.TASK_TYPE_UPDATE_DESTINATION_REPLICA:
        replica_tasks.UpdateDestinationReplicaTask
}


def get_task_runner(task_type):
    cls = _TASKS_MAP.get(task_type)
    if not cls:
        raise exception.NotFound(
            "TaskRunner not found for task type: %s" % task_type)
    return cls()
