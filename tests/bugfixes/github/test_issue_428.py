# -*- coding: utf-8 -*-

import system_tests


def stderr_exception(fname):
    return f"""$exiv2_exception_message {fname}:
$kerFailedToReadImageData
"""


class PngReadRawProfile(metaclass=system_tests.CaseMeta):
    url = "https://github.com/Exiv2/exiv2/issues/428"

    filenames = [
        system_tests.path("$data_path/issue_428_poc1.png"),
        system_tests.path("$data_path/issue_428_poc3.png"),
        system_tests.path("$data_path/issue_428_poc4.png"),
        system_tests.path("$data_path/issue_428_poc5.png"),
        system_tests.path("$data_path/issue_428_poc8.png"),
        system_tests.path("$data_path/issue_428_poc7.png"),
        system_tests.path("$data_path/issue_428_poc2.png"),
        system_tests.path("$data_path/issue_428_poc6.png"),
    ]

    commands = [f"$exiv2 {fname}" for fname in filenames]
    stdout = [""] * len(filenames)
    stderr = [stderr_exception(fname) for fname in filenames[0:6]]

    stderr.append(
        f"""$exiv2_exception_message {filenames[6]}:
$kerInputDataReadFailed
"""
    )

    stderr.append(
        """Error: XMP Toolkit error 201: Error in XMLValidator
Warning: Failed to decode XMP metadata.
"""
        + stderr_exception(filenames[7])
    )

    retval = [1] * len(filenames)
