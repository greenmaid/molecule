#  Copyright (c) 2015-2018 Cisco Systems, Inc.
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to
#  deal in the Software without restriction, including without limitation the
#  rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
#  sell copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#  DEALINGS IN THE SOFTWARE.
"""Lint Command Module."""

import click

from molecule import logger
from molecule.command import base

LOG = logger.get_logger(__name__)


class Lint(base.Base):
    """
    Lint Command Class.

    .. program:: molecule lint

    .. option:: molecule lint

        Target the default scenario.

    .. program:: molecule lint --scenario-name foo

    .. option:: molecule lint --scenario-name foo

        Targeting a specific scenario.

    .. program:: molecule --debug lint

    .. option:: molecule --debug lint

        Executing with `debug`.

    .. program:: molecule --base-config base.yml lint

    .. option:: molecule --base-config base.yml lint

        Executing with a `base-config`.

    .. program:: molecule --env-file foo.yml lint

    .. option:: molecule --env-file foo.yml lint

        Load an env file to read variables from when rendering
        molecule.yml.
    """

    def execute(self):
        """
        Execute the actions necessary to perform a `molecule lint` and \
        returns None.

        :return: None
        """
        self.print_info()
        linters = [
            l
            for l in [
                self._config.lint,
                self._config.verifier.lint,
                self._config.provisioner.lint,
            ]
            if l
        ]

        for l in linters:
            l.execute()


@click.command()
@click.pass_context
@click.option(
    '--scenario-name',
    '-s',
    default=base.MOLECULE_DEFAULT_SCENARIO_NAME,
    help='Name of the scenario to target. ({})'.format(
        base.MOLECULE_DEFAULT_SCENARIO_NAME
    ),
)
def lint(ctx, scenario_name):  # pragma: no cover
    """Lint the role (dependency, lint)."""
    args = ctx.obj.get('args')
    subcommand = base._get_subcommand(__name__)
    command_args = {'subcommand': subcommand}

    base.execute_cmdline_scenarios(scenario_name, args, command_args)
