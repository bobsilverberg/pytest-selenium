# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from functools import partial

import pytest

pytestmark = pytest.mark.nondestructive


@pytest.fixture
def testfile(testdir):
    return testdir.makepyfile("""
        import pytest
        @pytest.mark.nondestructive
        def test_pass(mozwebqa): pass
    """)


def failure_with_output(testdir, *args, **kwargs):
    reprec = testdir.inline_run(*args, **kwargs)
    passed, skipped, failed = reprec.listoutcomes()
    assert len(failed) == 1
    out = failed[0].longrepr.reprcrash.message
    return out


@pytest.fixture
def failure(testdir, testfile, webserver_base_url):
    return partial(failure_with_output, testdir, testfile, webserver_base_url)


def test_missing_browser_name(failure):
    out = failure()
    assert out == ('UsageError: --browsername must be specified '
                   'when using a server.')


def test_missing_platform(failure):
    out = failure('--browsername=firefox')
    assert out == ('UsageError: --platform must be specified '
                   'when using a server.')
