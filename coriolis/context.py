# Copyright 2016 Cloudbase Solutions Srl
# All Rights Reserved.

import copy

from oslo_context import context
from oslo_db.sqlalchemy import enginefacade
from oslo_utils import timeutils

from coriolis import exception
from coriolis import policy


@enginefacade.transaction_context_provider
class RequestContext(context.RequestContext):
    def __init__(self, user, tenant, is_admin=None,
                 roles=None, project_name=None, remote_address=None,
                 timestamp=None, request_id=None, auth_token=None,
                 overwrite=True, domain_name=None, domain_id=None,
                 user_domain_name=None, user_domain_id=None,
                 project_domain_name=None, project_domain_id=None,
                 show_deleted=None, trust_id=None, coriolis_task_id=None,
                 delete_trust_id=False, **kwargs):

        super(RequestContext, self).__init__(auth_token=auth_token,
                                             user=user,
                                             tenant=tenant,
                                             domain_name=domain_name,
                                             domain_id=domain_id,
                                             user_domain_name=user_domain_name,
                                             user_domain_id=user_domain_id,
                                             project_domain_name=(
                                                 project_domain_name),
                                             project_domain_id=(
                                                 project_domain_id),
                                             is_admin=is_admin,
                                             show_deleted=show_deleted,
                                             request_id=request_id,
                                             overwrite=overwrite)
        self.roles = roles or []
        self.project_name = project_name
        self.remote_address = remote_address
        if not timestamp:
            timestamp = timeutils.utcnow()
        elif isinstance(timestamp, str):
            timestamp = timeutils.parse_isotime(timestamp)
        self.timestamp = timestamp
        self.trust_id = trust_id
        self.delete_trust_id = delete_trust_id
        self.coriolis_task_id = coriolis_task_id

    def to_dict(self):
        result = super(RequestContext, self).to_dict()
        result['user'] = self.user
        result['tenant'] = self.tenant
        result['project_name'] = self.project_name
        result['domain_id'] = self.domain_id
        result['domain_name'] = self.domain_name
        result['user_domain_id'] = self.user_domain_id
        result['user_domain_name'] = self.user_domain_name
        result['project_domain_id'] = self.project_domain_id
        result['project_domain_name'] = self.project_domain_name
        result['roles'] = self.roles
        result['remote_address'] = self.remote_address
        result['timestamp'] = self.timestamp.isoformat()
        result['request_id'] = self.request_id
        result['show_deleted'] = self.show_deleted
        result['trust_id'] = self.trust_id
        result['delete_trust_id'] = self.delete_trust_id
        result['coriolis_task_id'] = self.coriolis_task_id
        return result

    @classmethod
    def from_dict(cls, values):
        return cls(**values)

    def to_policy_values(self):
        policy = super(RequestContext, self).to_policy_values()
        # TODO(aznashwan): determine if there are any other custom
        # context params we'd like to be used for policy validation:
        return policy

    def can(self, action, target=None, fatal=True):
        """ Validates policies allow the requested action to be
        perfomed in the given context, and raises otherwise.
        """
        default_target = {
            'project_id': self.project_id, 'user_id': self.user_id}
        if target is None:
            target = default_target
        else:
            target = copy.deepcopy(target)
            target.update(default_target)

        result = False
        try:
            result = policy.check_policy_for_context(self, action, target)
        except exception.PolicyNotAuthorized:
            if fatal:
                raise

        return result


def get_admin_context(trust_id=None):
    return RequestContext(
        user=None, tenant=None, is_admin=True,
        trust_id=trust_id)
