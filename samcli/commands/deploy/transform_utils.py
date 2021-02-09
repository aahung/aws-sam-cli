"""
Transform for SAM templates to convert into function resource representation.
"""
from typing import List

from samcli.lib.providers.provider import Stack
from samcli.lib.providers.sam_function_provider import SamFunctionProvider


# pylint: disable=fixme
# FIXME: this function's naming and purpose is confusing, to refactor in the future.
def transform_template(stacks: List[Stack]) -> SamFunctionProvider:
    """

    :param dict stacks: List of stacks to transform
    :return:
    """
    sam_function_provider = SamFunctionProvider(stacks, ignore_code_extraction_warnings=True)

    return sam_function_provider
