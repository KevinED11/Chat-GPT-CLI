"""
This module define the supported operating system
"""
from os_platform.options_os_platform import OptionsOsPlatform


supported_os: list[str] = [os.value for os in OptionsOsPlatform]
