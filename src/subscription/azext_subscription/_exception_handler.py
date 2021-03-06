# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError


def subscription_exception_handler(ex):
    from azext_subscription.subscription.models import ErrorResponseException
    if isinstance(ex, ErrorResponseException):
        message = ex.error.error.message
        raise CLIError(message)
    else:
        import sys
        from six import reraise
        reraise(*sys.exc_info())
