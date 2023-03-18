"""

"""
from dataclasses import dataclass

from pants.engine.internals.target_adaptor import TargetAdaptor
from pants.engine.rules import collect_rules, rule
from pants.engine.unions import UnionRule
from pants.version import PANTS_SEMVER, Version

RULES = ()

if PANTS_SEMVER >= Version("2.15.0.dev0"):
    from pants.engine.internals.synthetic_targets import (
        SyntheticAddressMaps,
        SyntheticTargetsRequest,
    )

    @dataclass(frozen=True)
    class SyntheticEmptyImageRequest(SyntheticTargetsRequest):
        path: str = SyntheticTargetsRequest.SINGLE_REQUEST_FOR_ALL_TARGETS

    @rule
    async def example_synthetic_targets(
        request: SyntheticEmptyImageRequest,
    ) -> SyntheticAddressMaps:
        return SyntheticAddressMaps.for_targets_request(
            request,
            [
                (
                    "BUILD.synthetic-example",
                    (
                        TargetAdaptor(
                            "oci_image_empty",
                            "empty",
                        ),
                    ),
                ),
            ],
        )

    RULES = (
        *collect_rules(),
        UnionRule(SyntheticTargetsRequest, SyntheticEmptyImageRequest),
    )


def rules():
    return RULES