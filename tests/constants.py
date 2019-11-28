from .testutils import VerminTest, detect

class VerminConstantMemberTests(VerminTest):
  def test_flags_of_sys(self):
    self.assertOnlyIn(((2, 6), (3, 0)), detect("from sys import flags"))

  def test_supports_unicode_filenames_of_os_path(self):
    self.assertOnlyIn(((2, 3), (3, 0)), detect("from os.path import supports_unicode_filenames"))

  def test_supports_bytes_environ_of_os(self):
    self.assertOnlyIn((3, 2), detect("from os import supports_bytes_environ"))

  def test_environb_of_os(self):
    self.assertOnlyIn((3, 2), detect("from os import environb"))

  def test_PRIO_PROCESS_of_os(self):
    self.assertOnlyIn((3, 3), detect("from os import PRIO_PROCESS"))

  def test_PRIO_PGRP_of_os(self):
    self.assertOnlyIn((3, 3), detect("from os import PRIO_PGRP"))

  def test_PRIO_USER_of_os(self):
    self.assertOnlyIn((3, 3), detect("from os import PRIO_USER"))

  def test_F_LOCK_of_os(self):
    self.assertOnlyIn((3, 3), detect("from os import F_LOCK"))

  def test_F_TLOCK_of_os(self):
    self.assertOnlyIn((3, 3), detect("from os import F_TLOCK"))

  def test_F_ULOCK_of_os(self):
    self.assertOnlyIn((3, 3), detect("from os import F_ULOCK"))

  def test_F_TEST_of_os(self):
    self.assertOnlyIn((3, 3), detect("from os import F_TEST"))

  def test_O_CLOEXEC_of_os(self):
    self.assertOnlyIn((3, 3), detect("from os import O_CLOEXEC"))

  def test_O_PATH_of_os(self):
    self.assertOnlyIn((3, 4), detect("from os import O_PATH"))

  def test_O_TMPFILE_of_os(self):
    self.assertOnlyIn((3, 4), detect("from os import O_TMPFILE"))

  def test_POSIX_FADV_NORMAL_of_os(self):
    self.assertOnlyIn((3, 3), detect("from os import POSIX_FADV_NORMAL"))

  def test_POSIX_FADV_SEQUENTIAL_of_os(self):
    self.assertOnlyIn((3, 3), detect("from os import POSIX_FADV_SEQUENTIAL"))

  def test_POSIX_FADV_RANDOM_of_os(self):
    self.assertOnlyIn((3, 3), detect("from os import POSIX_FADV_RANDOM"))

  def test_POSIX_FADV_NOREUSE_of_os(self):
    self.assertOnlyIn((3, 3), detect("from os import POSIX_FADV_NOREUSE"))

  def test_POSIX_FADV_WILLNEED_of_os(self):
    self.assertOnlyIn((3, 3), detect("from os import POSIX_FADV_WILLNEED"))

  def test_POSIX_FADV_DONTNEED_of_os(self):
    self.assertOnlyIn((3, 3), detect("from os import POSIX_FADV_DONTNEED"))

  def test_SF_NODISKIO_of_os(self):
    self.assertOnlyIn((3, 3), detect("from os import SF_NODISKIO"))

  def test_SF_MNOWAIT_of_os(self):
    self.assertOnlyIn((3, 3), detect("from os import SF_MNOWAIT"))

  def test_SF_SYNC_of_os(self):
    self.assertOnlyIn((3, 3), detect("from os import SF_SYNC"))

  def test_float_info_of_sys(self):
    self.assertOnlyIn(((2, 6), (3, 0)), detect("from sys import float_info"))

  def test_float_repr_style_of_sys(self):
    self.assertOnlyIn(((2, 7), (3, 0)), detect("from sys import float_repr_style"))

  def test_long_info_of_sys(self):
    self.assertOnlyIn((2, 7), detect("from sys import long_info"))

  def test_py3kwarning_of_sys(self):
    self.assertOnlyIn((2, 6), detect("from sys import py3kwarning"))

  def test_subversion_of_sys(self):
    self.assertOnlyIn((2, 5), detect("from sys import subversion"))

  def test_api_version_of_sys(self):
    self.assertOnlyIn(((2, 3), (3, 0)), detect("from sys import api_version"))

  def test_version_info_of_sys(self):
    self.assertOnlyIn(((2, 0), (3, 0)), detect("from sys import version_info"))

  def test_sentinel_of_multiprocessing_Process(self):
    self.assertOnlyIn((3, 3),
                      detect("from multiprocessing import Process\np = Process()\np.sentinel"))

  def test_skipped_of_unittest_TestResult(self):
    self.assertOnlyIn(((2, 7), (3, 0)),
                      detect("from unittest import TestResult\np = TestResult()\np.skipped"))

  def test_buffer_of_unittest_TestResult(self):
    self.assertOnlyIn(((2, 7), (3, 0)),
                      detect("from unittest import TestResult\np = TestResult()\np.buffer"))

  def test_failfast_of_unittest_TestResult(self):
    self.assertOnlyIn(((2, 7), (3, 0)),
                      detect("from unittest import TestResult\np = TestResult()\np.failfast"))

  def test_fold_of_datetime_datetime(self):
    self.assertOnlyIn((3, 6), detect("from datetime import datetime\np = datetime()\np.fold"))

  def test_fold_of_datetime_time(self):
    self.assertOnlyIn((3, 6), detect("from datetime import time\np = time()\np.fold"))

  def test_TYPE_CHECKING_of_typing(self):
    self.assertOnlyIn(((2, 7), (3, 5)), detect("from typing import TYPE_CHECKING"))

  def test_algorithms_of_hashlib(self):
    self.assertOnlyIn((2, 7), detect("from hashlib import algorithms"))

  def test_algorithms_available_of_hashlib(self):
    self.assertOnlyIn(((2, 7), (3, 2)), detect("from hashlib import algorithms_available"))

  def test_algorithms_guaranteed_of_hashlib(self):
    self.assertOnlyIn(((2, 7), (3, 2)), detect("from hashlib import algorithms_guaranteed"))

  def test_reverse_pointer_of_ipaddress_IPv4Address(self):
    self.assertOnlyIn((3, 5),
                      detect("from ipaddress import IPv4Address\n"
                             "addr = IPv4Address('127.0.0.1')\n"
                             "addr.reverse_pointer"))

  def test_is_global_of_ipaddress_IPv4Address(self):
    self.assertOnlyIn((3, 4),
                      detect("from ipaddress import IPv4Address\n"
                             "addr = IPv4Address('127.0.0.1')\n"
                             "addr.is_global"))

  def test_is_global_of_ipaddress_IPv6Address(self):
    self.assertOnlyIn((3, 4),
                      detect("from ipaddress import IPv6Address\n"
                             "addr = IPv6Address(':::1')\n"
                             "addr.is_global"))

  def test_nested_scopes_of___future__(self):
    self.assertOnlyIn(((2, 1), (3, 0)), detect("from __future__ import nested_scopes"))

  def test_generators_of___future__(self):
    self.assertOnlyIn(((2, 2), (3, 0)), detect("from __future__ import generators"))

  def test_division_of___future__(self):
    self.assertOnlyIn(((2, 2), (3, 0)), detect("from __future__ import division"))

  def test_absolute_import_of___future__(self):
    self.assertOnlyIn(((2, 5), (3, 0)), detect("from __future__ import absolute_import"))

  def test_with_statement_of___future__(self):
    self.assertOnlyIn(((2, 5), (3, 0)), detect("from __future__ import with_statement"))

  def test_print_function_of___future__(self):
    self.assertOnlyIn(((2, 6), (3, 0)), detect("from __future__ import print_function"))

  def test_unicode_literals_of___future__(self):
    self.assertOnlyIn(((2, 6), (3, 0)), detect("from __future__ import unicode_literals"))

  def test_generator_stop_of___future__(self):
    self.assertOnlyIn((3, 5), detect("from __future__ import generator_stop"))

  def test_eof_of_bz2_BZ2Decompressor(self):
    self.assertOnlyIn((3, 3),
                      detect("from bz2 import BZ2Decompressor\nd = BZ2Decompressor()\nd.eof"))

  def test_needs_input_of_bz2_BZ2Decompressor(self):
    self.assertOnlyIn((3, 5),
                      detect("from bz2 import BZ2Decompressor\n"
                             "d = BZ2Decompressor()\n"
                             "d.needs_input"))

  def test_maxlen_of_collections_deque(self):
    self.assertOnlyIn(((2, 7), (3, 1)),
                      detect("from collections import deque\nd = deque()\nd.maxlen"))

  def test_block_size_of_hmac_HMAC(self):
    self.assertOnlyIn((3, 4), detect("from hmac import HMAC\nd = HMAC()\nd.block_size"))

  def test_name_of_hmac_HMAC(self):
    self.assertOnlyIn((3, 4), detect("from hmac import HMAC\nd = HMAC()\nd.name"))

  def test_CO_COROUTINE_of_inspect(self):
    self.assertOnlyIn((3, 5), detect("import inspect\ninspect.CO_COROUTINE"))

  def test_CO_ITERABLE_COROUTINE_of_inspect(self):
    self.assertOnlyIn((3, 5), detect("import inspect\ninspect.CO_ITERABLE_COROUTINE"))

  def test_CO_ASYNC_GENERATOR_of_inspect(self):
    self.assertOnlyIn((3, 6), detect("import inspect\ninspect.CO_ASYNC_GENERATOR"))

  def test_lastResort_of_logging(self):
    self.assertOnlyIn((3, 2), detect("import logging\nlogging.lastResort"))

  def test_escape_of_shlex(self):
    self.assertOnlyIn(((2, 3), (3, 0)), detect("import shlex\nshlex.escape"))

  def test_escapedquotes_of_shlex(self):
    self.assertOnlyIn(((2, 3), (3, 0)), detect("import shlex\nshlex.escapedquotes"))

  def test_whitespace_split_of_shlex(self):
    self.assertOnlyIn(((2, 3), (3, 0)), detect("import shlex\nshlex.whitespace_split"))

  def test_eof_of_shlex(self):
    self.assertOnlyIn(((2, 3), (3, 0)), detect("import shlex\nshlex.eof"))

  def test_punctuation_chars_of_shlex(self):
    self.assertOnlyIn((3, 6), detect("import shlex\nshlex.punctuation_chars"))

  def test_rpc_paths_of_SimpleXMLRPCServer_SimpleXMLRPCRequestHandler(self):
    self.assertOnlyIn((2, 5),
                      detect("from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler\n"
                             "SimpleXMLRPCRequestHandler.rpc_paths"))
    self.assertOnlyIn((3, 0),
                      detect("from xmlrpc.server import SimpleXMLRPCRequestHandler\n"
                             "SimpleXMLRPCRequestHandler.rpc_paths"))

  def test_encode_threshold_of_SimpleXMLRPCServer_SimpleXMLRPCRequestHandler(self):
    self.assertOnlyIn((2, 7),
                      detect("from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler\n"
                             "SimpleXMLRPCRequestHandler.encode_threshold"))

  def test_library_of_ssl_SSLError(self):
    self.assertOnlyIn(((2, 7), (3, 3)), detect("from ssl import SSLError\nSSLError.library"))

  def test_reason_of_ssl_SSLError(self):
    self.assertOnlyIn(((2, 7), (3, 3)), detect("from ssl import SSLError\nSSLError.reason"))

  def test_VERIFY_DEFAULT_of_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 4)), detect("from ssl import VERIFY_DEFAULT"))

  def test_VERIFY_CRL_CHECK_LEAF_of_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 4)), detect("from ssl import VERIFY_CRL_CHECK_LEAF"))

  def test_VERIFY_CRL_CHECK_CHAIN_of_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 4)), detect("from ssl import VERIFY_CRL_CHECK_CHAIN"))

  def test_VERIFY_X509_STRICT_of_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 4)), detect("from ssl import VERIFY_X509_STRICT"))

  def test_VERIFY_X509_TRUSTED_FIRST_of_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 4)), detect("from ssl import VERIFY_X509_TRUSTED_FIRST"))

  def test_PROTOCOL_TLS_of_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 6)), detect("from ssl import PROTOCOL_TLS"))

  def test_PROTOCOL_TLSv1_1_of_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 4)), detect("from ssl import PROTOCOL_TLSv1_1"))

  def test_PROTOCOL_TLSv1_2_of_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 4)), detect("from ssl import PROTOCOL_TLSv1_2"))

  def test_OP_ALL_of_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 2)), detect("from ssl import OP_ALL"))

  def test_OP_NO_SSLv2_of_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 2)), detect("from ssl import OP_NO_SSLv2"))

  def test_OP_NO_SSLv3_of_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 2)), detect("from ssl import OP_NO_SSLv3"))

  def test_OP_NO_TLSv1_of_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 2)), detect("from ssl import OP_NO_TLSv1"))

  def test_OP_NO_TLSv1_1_of_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 4)), detect("from ssl import OP_NO_TLSv1_1"))

  def test_OP_NO_TLSv1_2_of_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 4)), detect("from ssl import OP_NO_TLSv1_2"))

  def test_OP_NO_TLSv1_3_of_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 6)), detect("from ssl import OP_NO_TLSv1_3"))

  def test_OP_CIPHER_SERVER_PREFERENCE_of_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 3)), detect("from ssl import OP_CIPHER_SERVER_PREFERENCE"))

  def test_OP_SINGLE_DH_USE_of_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 3)), detect("from ssl import OP_SINGLE_DH_USE"))

  def test_OP_SINGLE_ECDH_USE_of_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 3)), detect("from ssl import OP_SINGLE_ECDH_USE"))

  def test_OP_NO_COMPRESSION_of_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 3)), detect("from ssl import OP_NO_COMPRESSION"))

  def test_HAS_ALPN_of_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 5)), detect("from ssl import HAS_ALPN"))

  def test_HAS_ECDH_of_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 3)), detect("from ssl import HAS_ECDH"))

  def test_HAS_SNI_of_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 2)), detect("from ssl import HAS_SNI"))

  def test_HAS_NPN_of_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 3)), detect("from ssl import HAS_NPN"))

  def test_HAS_TLSv1_3_of_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 6)), detect("from ssl import HAS_TLSv1_3"))

  def test_CHANNEL_BINDING_TYPES_of_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 3)), detect("from ssl import CHANNEL_BINDING_TYPES"))

  def test_OPENSSL_VERSION_of_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 2)), detect("from ssl import OPENSSL_VERSION"))

  def test_OPENSSL_VERSION_INFO_of_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 2)), detect("from ssl import OPENSSL_VERSION_INFO"))

  def test_OPENSSL_VERSION_NUMBER_of_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 2)), detect("from ssl import OPENSSL_VERSION_NUMBER"))

  def test_ALERT_DESCRIPTION_HANDSHAKE_FAILURE_of_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 4)),
                      detect("from ssl import ALERT_DESCRIPTION_HANDSHAKE_FAILURE"))

  def test_ALERT_DESCRIPTION_INTERNAL_ERROR_of_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 4)), detect("from ssl import ALERT_DESCRIPTION_INTERNAL_ERROR"))

  def test_context_of_ssl_SSLSocket(self):
    self.assertOnlyIn(((2, 7), (3, 2)), detect("from ssl import SSLSocket\nSSLSocket.context"))

  def test_server_side_of_ssl_SSLSocket(self):
    self.assertOnlyIn((3, 2), detect("from ssl import SSLSocket\nSSLSocket.server_side"))

  def test_server_hostname_of_ssl_SSLSocket(self):
    self.assertOnlyIn((3, 2), detect("from ssl import SSLSocket\nSSLSocket.server_hostname"))

  def test_session_of_ssl_SSLSocket(self):
    self.assertOnlyIn((3, 2), detect("from ssl import SSLSocket\nSSLSocket.session"))

  def test_session_reused_of_ssl_SSLSocket(self):
    self.assertOnlyIn((3, 2), detect("from ssl import SSLSocket\nSSLSocket.session_reused"))

  def test_check_hostname_of_ssl_SSLContext(self):
    self.assertOnlyIn((3, 4), detect("from ssl import SSLContext\nSSLContext.check_hostname"))

  def test_verify_flags_of_ssl_SSLContext(self):
    self.assertOnlyIn((3, 4), detect("from ssl import SSLContext\nSSLContext.verify_flags"))

  def test_post_handshake_auth_of_ssl_SSLContext(self):
    self.assertOnlyIn((3, 8), detect("from ssl import SSLContext\nSSLContext.post_handshake_auth"))

  def test_hostname_checks_common_name_of_ssl_SSLContext(self):
    self.assertOnlyIn((3, 7),
                      detect("from ssl import SSLContext\nSSLContext.hostname_checks_common_name"))

  def test_DEVNULL_of_subprocess(self):
    self.assertOnlyIn((3, 3), detect("from subprocess import DEVNULL"))

  def test_pax_headers_of_tarfile_TarFile(self):
    self.assertOnlyIn(((2, 6), (3, 0)), detect("from tarfile import TarFile\nTarFile.pax_headers"))

  def test_pax_headers_of_tarfile_TarInfo(self):
    self.assertOnlyIn(((2, 6), (3, 0)), detect("from tarfile import TarInfo\nTarInfo.pax_headers"))

  def test_args_of_subprocess_Popen(self):
    self.assertOnlyIn((3, 3), detect("from subprocess import Popen\nPopen.args"))

    # In this test "args" cannot be matched as "subprocess.Popen.args" constant (as above)!
    self.assertOnlyIn(((2, 4), (3, 0)),
                      detect("import subprocess\nargs=[]\nsubprocess.Popen(args)"))

  def test_ZIP_BZIP2_of_zipfile(self):
    self.assertOnlyIn((3, 3), detect("import zipfile\nzipfile.ZIP_BZIP2"))

  def test_ZIP_LZMA_of_zipfile(self):
    self.assertOnlyIn((3, 3), detect("import zipfile\nzipfile.ZIP_LZMA"))

  def test_METHOD_SHA512_of_crypt(self):
    self.assertOnlyIn((3, 3), detect("import crypt\ncrypt.METHOD_SHA512"))

  def test_METHOD_SHA256_of_crypt(self):
    self.assertOnlyIn((3, 3), detect("import crypt\ncrypt.METHOD_SHA256"))

  def test_METHOD_MD5_of_crypt(self):
    self.assertOnlyIn((3, 3), detect("import crypt\ncrypt.METHOD_MD5"))

  def test_METHOD_CRYPT_of_crypt(self):
    self.assertOnlyIn((3, 3), detect("import crypt\ncrypt.METHOD_CRYPT"))

  def test_METHOD_BLOWFISH_of_crypt(self):
    self.assertOnlyIn((3, 7), detect("import crypt\ncrypt.METHOD_BLOWFISH"))

  def test_methods_of_crypt(self):
    self.assertOnlyIn((3, 3), detect("import crypt\ncrypt.methods"))

  def test_tau_of_math(self):
    self.assertOnlyIn((3, 6), detect("import math\nmath.tau"))

  def test_inf_of_math(self):
    self.assertOnlyIn((3, 5), detect("import math\nmath.inf"))

  def test_nan_of_math(self):
    self.assertOnlyIn((3, 5), detect("import math\nmath.nan"))

  def test_name_of_contextvars_ContextVar(self):
    self.assertOnlyIn((3, 7), detect("from contextvars import ContextVar\nContextVar.name"))

  def test_SOURCE_SUFFIXES_of_importlib_machinery(self):
    self.assertOnlyIn((3, 3), detect("from importlib import machinery\nmachinery.SOURCE_SUFFIXES"))

  def test_DEBUG_BYTECODE_SUFFIXES_of_importlib_machinery(self):
    self.assertOnlyIn((3, 3),
                      detect("from importlib import machinery\nmachinery.DEBUG_BYTECODE_SUFFIXES"))

  def test_OPTIMIZED_BYTECODE_SUFFIXES_of_importlib_machinery(self):
    self.assertOnlyIn((3, 3),
                      detect("from importlib import machinery\n"
                             "machinery.OPTIMIZED_BYTECODE_SUFFIXES"))

  def test_BYTECODE_SUFFIXES_of_importlib_machinery(self):
    self.assertOnlyIn((3, 3),
                      detect("from importlib import machinery\nmachinery.BYTECODE_SUFFIXES"))

  def test_EXTENSION_SUFFIXES_of_importlib_machinery(self):
    self.assertOnlyIn((3, 3),
                      detect("from importlib import machinery\nmachinery.EXTENSION_SUFFIXES"))

  def test_MAGIC_NUMBER_of_importlib_util(self):
    self.assertOnlyIn((3, 4), detect("from importlib import util\nutil.MAGIC_NUMBER"))

  def test_CLOCK_BOOTTIME_of_time(self):
    self.assertOnlyIn((3, 7), detect("from time import CLOCK_BOOTTIME"))

  def test_CLOCK_HIGHRES_of_time(self):
    self.assertOnlyIn((3, 3), detect("from time import CLOCK_HIGHRES"))

  def test_CLOCK_MONOTONIC_of_time(self):
    self.assertOnlyIn((3, 3), detect("from time import CLOCK_MONOTONIC"))

  def test_CLOCK_MONOTONIC_RAW_of_time(self):
    self.assertOnlyIn((3, 3), detect("from time import CLOCK_MONOTONIC_RAW"))

  def test_CLOCK_PROCESS_CPUTIME_ID_of_time(self):
    self.assertOnlyIn((3, 3), detect("from time import CLOCK_PROCESS_CPUTIME_ID"))

  def test_CLOCK_THREAD_CPUTIME_ID_of_time(self):
    self.assertOnlyIn((3, 3), detect("from time import CLOCK_THREAD_CPUTIME_ID"))

  def test_CLOCK_PROF_of_time(self):
    self.assertOnlyIn((3, 7), detect("from time import CLOCK_PROF"))

  def test_CLOCK_UPTIME_of_time(self):
    self.assertOnlyIn((3, 7), detect("from time import CLOCK_UPTIME"))

  def test_CLOCK_UPTIME_RAW_of_time(self):
    self.assertOnlyIn((3, 8), detect("from time import CLOCK_UPTIME_RAW"))

  def test_CLOCK_REALTIME_of_time(self):
    self.assertOnlyIn((3, 3), detect("from time import CLOCK_REALTIME"))

  def test_cssclass_noday_of_calendar_HTMLCalendar(self):
    self.assertOnlyIn((3, 7),
                      detect("from calendar import HTMLCalendar\n"
                             "c=HTMLCalendar()\nc.cssclass_noday"))

  def test_cssclasses_weekday_head_of_calendar_HTMLCalendar(self):
    self.assertOnlyIn((3, 7),
                      detect("from calendar import HTMLCalendar\n"
                             "c=HTMLCalendar()\nc.cssclasses_weekday_head"))

  def test_cssclass_month_head_of_calendar_HTMLCalendar(self):
    self.assertOnlyIn((3, 7),
                      detect("from calendar import HTMLCalendar\n"
                             "c=HTMLCalendar()\nc.cssclass_month_head"))

  def test_cssclass_year_of_calendar_HTMLCalendar(self):
    self.assertOnlyIn((3, 7),
                      detect("from calendar import HTMLCalendar\n"
                             "c=HTMLCalendar()\nc.cssclass_year"))

  def test_cssclass_year_head_of_calendar_HTMLCalendar(self):
    self.assertOnlyIn((3, 7),
                      detect("from calendar import HTMLCalendar\n"
                             "c=HTMLCalendar()\nc.cssclass_year_head"))

  def test_tau_of_cmath(self):
    self.assertOnlyIn((3, 6), detect("from cmath import tau"))

  def test_inf_of_cmath(self):
    self.assertOnlyIn((3, 6), detect("from cmath import inf"))

  def test_infj_of_cmath(self):
    self.assertOnlyIn((3, 6), detect("from cmath import infj"))

  def test_nan_of_cmath(self):
    self.assertOnlyIn((3, 6), detect("from cmath import nan"))

  def test_nanj_of_cmath(self):
    self.assertOnlyIn((3, 6), detect("from cmath import nanj"))

  def test_is_jump_target_of_dis_Instruction(self):
    self.assertOnlyIn((3, 4),
                      detect("from dis import Instruction\ni=Instruction()\ni.is_jump_target"))

  def test_FAIL_FAST_of_doctest(self):
    self.assertOnlyIn((3, 4), detect("import doctest\ndoctest.FAIL_FAST"))

  def test_ACCESS_DEFAULT_of_mmap(self):
    self.assertOnlyIn((3, 7), detect("import mmap\nmmap.ACCESS_DEFAULT"))

  def test_MADV_NORMAL_of_mmap(self):
    self.assertOnlyIn((3, 8), detect("import mmap\nmmap.MADV_NORMAL"))

  def test_MADV_RANDOM_of_mmap(self):
    self.assertOnlyIn((3, 8), detect("import mmap\nmmap.MADV_RANDOM"))

  def test_MADV_SEQUENTIAL_of_mmap(self):
    self.assertOnlyIn((3, 8), detect("import mmap\nmmap.MADV_SEQUENTIAL"))

  def test_MADV_WILLNEED_of_mmap(self):
    self.assertOnlyIn((3, 8), detect("import mmap\nmmap.MADV_WILLNEED"))

  def test_MADV_DONTNEED_of_mmap(self):
    self.assertOnlyIn((3, 8), detect("import mmap\nmmap.MADV_DONTNEED"))

  def test_MADV_REMOVE_of_mmap(self):
    self.assertOnlyIn((3, 8), detect("import mmap\nmmap.MADV_REMOVE"))

  def test_MADV_DONTFORK_of_mmap(self):
    self.assertOnlyIn((3, 8), detect("import mmap\nmmap.MADV_DONTFORK"))

  def test_MADV_DOFORK_of_mmap(self):
    self.assertOnlyIn((3, 8), detect("import mmap\nmmap.MADV_DOFORK"))

  def test_MADV_HWPOISON_of_mmap(self):
    self.assertOnlyIn((3, 8), detect("import mmap\nmmap.MADV_HWPOISON"))

  def test_MADV_MERGEABLE_of_mmap(self):
    self.assertOnlyIn((3, 8), detect("import mmap\nmmap.MADV_MERGEABLE"))

  def test_MADV_UNMERGEABLE_of_mmap(self):
    self.assertOnlyIn((3, 8), detect("import mmap\nmmap.MADV_UNMERGEABLE"))

  def test_MADV_SOFT_OFFLINE_of_mmap(self):
    self.assertOnlyIn((3, 8), detect("import mmap\nmmap.MADV_SOFT_OFFLINE"))

  def test_MADV_HUGEPAGE_of_mmap(self):
    self.assertOnlyIn((3, 8), detect("import mmap\nmmap.MADV_HUGEPAGE"))

  def test_MADV_NOHUGEPAGE_of_mmap(self):
    self.assertOnlyIn((3, 8), detect("import mmap\nmmap.MADV_NOHUGEPAGE"))

  def test_MADV_DONTDUMP_of_mmap(self):
    self.assertOnlyIn((3, 8), detect("import mmap\nmmap.MADV_DONTDUMP"))

  def test_MADV_DODUMP_of_mmap(self):
    self.assertOnlyIn((3, 8), detect("import mmap\nmmap.MADV_DODUMP"))

  def test_MADV_FREE_of_mmap(self):
    self.assertOnlyIn((3, 8), detect("import mmap\nmmap.MADV_FREE"))

  def test_MADV_NOSYNC_of_mmap(self):
    self.assertOnlyIn((3, 8), detect("import mmap\nmmap.MADV_NOSYNC"))

  def test_MADV_AUTOSYNC_of_mmap(self):
    self.assertOnlyIn((3, 8), detect("import mmap\nmmap.MADV_AUTOSYNC"))

  def test_MADV_NOCORE_of_mmap(self):
    self.assertOnlyIn((3, 8), detect("import mmap\nmmap.MADV_NOCORE"))

  def test_MADV_CORE_of_mmap(self):
    self.assertOnlyIn((3, 8), detect("import mmap\nmmap.MADV_CORE"))

  def test_MADV_PROTECT_of_mmap(self):
    self.assertOnlyIn((3, 8), detect("import mmap\nmmap.MADV_PROTECT"))

  def test_MFD_CLOEXEC_of_os(self):
    self.assertOnlyIn((3, 8), detect("from os import MFD_CLOEXEC"))

  def test_MFD_ALLOW_SEALING_of_os(self):
    self.assertOnlyIn((3, 8), detect("from os import MFD_ALLOW_SEALING"))

  def test_MFD_HUGETLB_of_os(self):
    self.assertOnlyIn((3, 8), detect("from os import MFD_HUGETLB"))

  def test_MFD_HUGE_SHIFT_of_os(self):
    self.assertOnlyIn((3, 8), detect("from os import MFD_HUGE_SHIFT"))

  def test_MFD_HUGE_MASK_of_os(self):
    self.assertOnlyIn((3, 8), detect("from os import MFD_HUGE_MASK"))

  def test_MFD_HUGE_64KB_of_os(self):
    self.assertOnlyIn((3, 8), detect("from os import MFD_HUGE_64KB"))

  def test_MFD_HUGE_512KB_of_os(self):
    self.assertOnlyIn((3, 8), detect("from os import MFD_HUGE_512KB"))

  def test_MFD_HUGE_1MB_of_os(self):
    self.assertOnlyIn((3, 8), detect("from os import MFD_HUGE_1MB"))

  def test_MFD_HUGE_2MB_of_os(self):
    self.assertOnlyIn((3, 8), detect("from os import MFD_HUGE_2MB"))

  def test_MFD_HUGE_8MB_of_os(self):
    self.assertOnlyIn((3, 8), detect("from os import MFD_HUGE_8MB"))

  def test_MFD_HUGE_16MB_of_os(self):
    self.assertOnlyIn((3, 8), detect("from os import MFD_HUGE_16MB"))

  def test_MFD_HUGE_32MB_of_os(self):
    self.assertOnlyIn((3, 8), detect("from os import MFD_HUGE_32MB"))

  def test_MFD_HUGE_256MB_of_os(self):
    self.assertOnlyIn((3, 8), detect("from os import MFD_HUGE_256MB"))

  def test_MFD_HUGE_512MB_of_os(self):
    self.assertOnlyIn((3, 8), detect("from os import MFD_HUGE_512MB"))

  def test_MFD_HUGE_1GB_of_os(self):
    self.assertOnlyIn((3, 8), detect("from os import MFD_HUGE_1GB"))

  def test_MFD_HUGE_2GB_of_os(self):
    self.assertOnlyIn((3, 8), detect("from os import MFD_HUGE_2GB"))

  def test_MFD_HUGE_16GB_of_os(self):
    self.assertOnlyIn((3, 8), detect("from os import MFD_HUGE_16GB"))

  def test_XATTR_SIZE_MAX_of_os(self):
    self.assertOnlyIn((3, 3), detect("from os import XATTR_SIZE_MAX"))

  def test_XATTR_CREATE_of_os(self):
    self.assertOnlyIn((3, 3), detect("from os import XATTR_CREATE"))

  def test_XATTR_REPLACE_of_os(self):
    self.assertOnlyIn((3, 3), detect("from os import XATTR_REPLACE"))

  def test_ncurses_version_of_curses(self):
    self.assertOnlyIn((3, 8), detect("from curses import ncurses_version"))

  def test_A_ITALIC_of_curses(self):
    self.assertOnlyIn((3, 7), detect("from curses import A_ITALIC"))

  def test_FMT_XML_of_plistlib(self):
    self.assertOnlyIn((3, 4), detect("from plistlib import FMT_XML"))

  def test_FMT_BINARY_of_plistlib(self):
    self.assertOnlyIn((3, 4), detect("from plistlib import FMT_BINARY"))

  def test_TIMEOUT_MAX_of_threading(self):
    self.assertOnlyIn((3, 2), detect("from threading import TIMEOUT_MAX"))
