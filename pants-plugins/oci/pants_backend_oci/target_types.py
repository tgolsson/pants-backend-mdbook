from __future__ import annotations


from typing import Optional

from pants.engine.addresses import Address
from pants.engine.target import (
    BoolField,
    Dependencies,
    ScalarField,
    SpecialCasedDependencies,
    StringField,,
    StringSequenceField,
)
from pants.util.strutil import softwrap


class ImageBundle(StringField):
    alias = ""
    help = softwrap(
        """
        The tag to use.
        """
    )


class ImageRepositoryAnonymous(BoolField):
    alias = "anonymous"
    default = False
    help = softwrap(
        """
        Whether the repository access should be anonymous.
        """
    )


class ImageRepository(StringField):
    alias = "repository"

    help = softwrap(
        """
        The repository to import the image from.
        """
    )


class ImageDigest(StringField):
    alias = "digest"
    help = softwrap(
        """
        The tag to use.
        """
    )


class ImageTag(StringField):
    alias = "tag"

    help = softwrap(
        """
        The tag to use for the image.
        """
    )


class ImageDependencies(Dependencies):
    alias = "packages"

    help = softwrap(
        """
        The content to package.
        """
    )


class ImageBase(SpecialCasedDependencies):
    alias = "base"

    help = softwrap(
        """
        The base image to use.
        """
    )


class ImageRunTty(BoolField):
    alias = "terminal"
    default = False

    help = softwrap(
        """Whether the image requires an interactive tty to execute.

        This prevents the image from running in many situations and isn't recommended."""
    )


NoneType = type(None)


class ImageEmptyMarker(ScalarField):
    alias = "_marker"
    expected_type = type(None)
    expected_type_description = ""
    default = None

    @classmethod
    def compute_value(cls, raw_value: Optional[NoneType], address: Address) -> Optional[NoneType]:
        return super().compute_value(raw_value, address=address)

class ImageBuildOutputs(StringSequenceField):
    alias = "outputs"

    help = softwrap(
        """
        Globs to capture as outputs from the build step.
        """
    )


class ImageEnvironment(StringSequenceField):
    alias = "env"

    help = softwrap(
        """
        Environment variables to set.
        """
    )


class ImageBuildCommand(StringField):
    alias = "commands"

    help = softwrap(
        """
        Globs to capture as outputs from the build step.
        """
    )


class ImageEntrypoint(StringField):
    alias = "entrypoint"

    help = softwrap(
        """
        The entrypoint to use
        """
    )


class ImageArgs(StringSequenceField):
    alias = "args"

    help = softwrap(
        """
        Globs to capture as outputs from the build step.
        """
    )
