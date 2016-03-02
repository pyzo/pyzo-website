#!/usr/bin/env python3

import urllib.request
import re
import xml.etree.ElementTree as et

download_urls = [   'http://bitbucket.org/pyzo/pyzo/downloads' ]

INFO_INTRO = """
You're just a couple of minutes away from doing scientific computing in Python!
You can safely try Pyzo, since it is designed to be minimally intruisive
and not interfere with other Python distibutions.

Featured downloads
==================

.. image:: _static/download.png
  :align: right


"""
INFO_NOTES = """

Windows
-------
* The easiest way to install Pyzo on Windows is to use the installer
  (which does not require admin rights).
* Alternatively, you can download and unpack the zip-file. Since Pyzo
  distro is portable, you can place the Pyzo directory anywhere you
  like (we suggest *c:\\\\pyzo*).

Linux
-----
* To install Pyzo on Linux, download and extract the archive
  corresponding to your architecture. 
* In case you want to place a link on your desktop for convenience,
  icons are in the *pyzo/data/icons* folder.
* The binaries for Linux are build on Ubuntu Lucid Lynx, so should
  work on most modern Linux distros (glibc >= 2.11).
* You can also install a :ref:`Pyzo-compatible <pyzolinux>` environment.

OS X
----
* To install Pyzo on Mac, mount the disk image and copy the pyzo
  directory to to your user directory. 
* The binaries are build on OSX 10.6.2 and should work on Snow Leopard
  and above.

Uninstalling
------------
To remove Pyzo distro, either run the uninstaller (when you used the
installer on Windows), or simply remove the directory that you unpacked
from the archive.

Eula
----
Pyzo distro is free software. No limitations, no DRM. Please read the Pyzo
distro end user agreement for details: `Pyzo EULA
<_static/pyzo_eula.txt>`_.

"""

INFO_PREVIOUS = """
A list of all Pyzo distro releases. See also the :ref:`release notes <releasenotes>`.
"""


class Download:
    LIST_URL = None
    PREFIX_URL = None
    
    @classmethod
    def find_matches(cls, source):
        raise NotImplementedError()
    
    def __init__(self, name):
        self.name = name
        self.valid = self.partition_name()
    
    @classmethod
    def get_downloads(cls, links):
        # Load source from url
        with urllib.request.urlopen(cls.LIST_URL) as file:
            source = file.read().decode('utf-8', errors='ignore')
        
        # Get matches and instances
        matches = cls.find_matches(source)
        instances = [cls(match) for match in matches]
        
        # Parse the matches (filter out bad ones), and sort by version
        for instance in instances:
            if not instance.valid:
                print('Warning: ignoring link %s' % instance.name)
            else:
                # Get list for this version (create new one if it does not exist)
                L = links.setdefault(instance.versioncomp, [])
                # Add
                L.append(instance)
    
    def partition_name(self):
        """ Given a download name, this function returns a
        tuple (original_name, version, architecture, extension)
        If it did not look like a proper name, it returns None.
        """
        name = self.name
        
        # Remove the preamble
        pyzo_name, dash, rest = name.partition('-')
        
        # Split the rest and search for the part that specifies the architecture
        parts = rest.split('.')
        i = 0
        for part in parts:
            part = part.lower()
            if 'linux' in part or 'win' in part or 'osx' in part  or 'mac' in part or 'source' in part:
                break
            i += 1
        else:
            return None
        
        # Assemble information of interest
        self.version = '.'.join(parts[:i])
        self.arch = parts[i]
        self.extension = '.' + '.'.join(parts[i+1:])
        
        # Return success
        return True
    
    @property
    def url(self):
        return self.PREFIX_URL + self.name
    
    @property
    def versioncomp(self):
        """ Version number for comparisons.
        """
        # The dot comes before any letters or numbers in the ASCII
        # table, so '3.2beta' > '3.2.1'. So we replace dots with tilde,
        # which is at the end of the ascii table. We also put a tilde
        # at the end, so that '3.2~' > '3.2beta~'.
        return self.version.replace('.', '~') + '~'



class BitbucketDownload(Download):
    LIST_URL = 'http://bitbucket.org/pyzo/pyzo/downloads'
    PREFIX_URL = 'http://bitbucket.org/pyzo/pyzo/downloads/'
    
    @classmethod
    def find_matches(cls, source):
        matches = re.findall(r'>pyzo_distro-.+?<', source)
        return [match[1:-1] for match in matches]


def print_downloads(lines, os, bits):
    """ Bullets by os+arch. """
    bittext = ' (%s bit)'%bits if bits else ''
    lines.append('* %s%s: ' % (os, bittext))
    for link in links[versions[0]]:
        if os.lower() in link.arch.lower() and bits in link.arch:
            lines[-1] += ' `%s <%s>`_ or' % (link.name, link.url)
    lines[-1] = lines[-1][:-2] # strip last or


def print_downloads2(lines, os):
    """ Nested bullets; vertical space a bit big. """
    lines.append('* %s: ' % os)
    for bits in ('64', '32'):
        for link in links[versions[0]]:
            if os.lower() in link.arch.lower() and bits in link.arch:
                bittext = '%s bit'%bits if bits else ''
                if link.url.endswith('.exe'):
                    description = '%s installer' % bittext
                elif link.url.endswith('.zip'):
                    description = '%s zip' % bittext
                else:
                    description = bittext
                lines.append(' - `%s <%s>`_ (%s)' % (link.name, link.url, description))
 
 
def print_downloads3(lines, os):
    """ A table. """
    N = 150
    lines.append('+' + '-'*20 + '+' + '-'*N + '+')
    lines.append('|' + (' %s' % os).ljust(20) + '|' +  ' '*N + '|' )
    for bits in ('64', '32'):
        for link in links[versions[0]]:
            if os.lower() in link.arch.lower() and bits in link.arch:
                bittext = '%s bit'%bits if bits else ''
                if link.url.endswith('.exe'):
                    description = '%s installer' % bittext
                elif link.url.endswith('.zip'):
                    description = '%s zip' % bittext
                else:
                    description = bittext
                text = ' - `%s <%s>`_ (%s)' % (link.name, link.url, description)
                lines.append('|' + ' '*20 + '|' + text.ljust(N) + '|')   
    if os == 'OSX':
        lines.append('+' + '-'*20 + '+' + '-'*N + '+')


# Find links
links = {}
BitbucketDownload.get_downloads(links)

# Get sorted list of versions
versions = list(reversed(sorted(links)))

# # Get the latest version
# latest_version = max(links.keys())
# latest_links = links.pop(latest_version)
# latest_links.sort(key=lambda x: x[0])


# Generate RST
lines = [""".. _downloads:

=============
Download Pyzo
=============

"""]
lines.append(INFO_INTRO)

# print_downloads(lines, 'Win', '64')
# print_downloads(lines, 'Win', '32')
# print_downloads(lines, 'Linux', '64')
# print_downloads(lines, 'Linux', '32')
# print_downloads(lines, 'OSX', '64')
print_downloads3(lines, '   ')  # Dummy so that an extra row is printed
print_downloads3(lines, 'Win')
print_downloads3(lines, 'Linux')
print_downloads3(lines, 'OSX')

# Add notes
lines.append('')
lines.append('Installation instructions')
lines.append('='*len(lines[-1]))
lines.append(INFO_NOTES)


# Section for remaining versions
if links:
    lines.append('All versions')
    lines.append('='*len(lines[-1]))
    lines.append(INFO_PREVIOUS)
    for version in versions:
        L = sorted(links[version], key=lambda x: x.name)
        for link in L:
            lines.append( '  * `%s <%s>`_' % (link.name, link.url) )


# Write
with open('downloads.rst', 'wb') as file:
    lines.append('')
    text = '\n'.join(lines)
    file.write(text.encode('utf-8'))

