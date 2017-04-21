# Copyright 2016 Cloudbase Solutions Srl
# All Rights Reserved.

import oslo_messaging as messaging

from coriolis import rpc

VERSION = "1.0"


class WorkerClient(object):
    def __init__(self):
        target = messaging.Target(topic='coriolis_worker', version=VERSION)
        self._client = rpc.get_client(target)

    def begin_task(self, ctxt, server, task_id, task_type, origin, destination,
                   instance, task_info):
        cctxt = self._client.prepare(server=server)
        cctxt.cast(
            ctxt, 'exec_task', task_id=task_id, task_type=task_type,
            origin=origin, destination=destination, instance=instance,
            task_info=task_info)

    def cancel_task(self, ctxt, server, task_id, process_id, force):
        # Needs to be executed on the same server
        cctxt = self._client.prepare(server=server)
        cctxt.call(ctxt, 'cancel_task', task_id=task_id, process_id=process_id,
                   force=force)

    def update_migration_status(self, ctxt, task_id, status):
        self._client.call(ctxt, "update_migration_status", status=status)

    def get_endpoint_instances(self, ctxt, endpoint_type, connection_info,
                               marker=None, limit=None,
                               instance_name_pattern=None):
        return self._client.call(
            ctxt, 'get_endpoint_instances',
            endpoint_type=endpoint_type,
            connection_info=connection_info,
            marker=marker,
            limit=limit,
            instance_name_pattern=instance_name_pattern)
