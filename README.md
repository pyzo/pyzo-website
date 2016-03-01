This the codebase for the Pyzo website.
Managing the website is done via the HG repository and the make command.


### Website editing

To the website follow the following procedure:

  * hg pull + hg up
  * Make your changes
  * build: "make clean html"
  * test local:  "make showinchrome" or "make showinff"
  * make s3upload / ftpupload / gitupload
  * hg commit + hg push
  * test online


It is also convenient to edit the .rst files via the bitbucket interface.
After editing, update the website as follows:

  * hg pull -u
  * make clean html s3upload



### Available make commands
  
  * make showinchrome: show the local website in the chrome browser
  * make showinff: show the local website in the ff browser
  * make ftpupload: upload the website to an ftp server (specified in conf.py)
  * make gitupload: upload the website to a git repo (specified in conf.py)
  * make s3upload: upload the website to an AWS S3 bucket (specified in conf.py)



### Notes on hosting

Github offers static website hosting via a git repo. The associated domain
would be X.github.io, and it can be linked to a domain name that you own.

Bitbucket offers the same functionality, except that it does not yet 
allow linking of a domain name, which makes that we cannot use it.

We have an account at a website host, but we have a very limited account, 
so we'd rather use something that scales more nicely.

You can host a website via Amazon S3. The only problem is that in order
to point a naked domain there (e.g. http://pyzo.org) you would need to
use some redirection. This can be done via AWS Route 53, or via wwwizer.com.
The latter offers a free service for precisely this problem. To make it work,
set the DNS A record of the naked name to 174.129.25.170, and set the wwww.X.org 
CNAME to the S3 bucket address. When using S3, dont forget to set the 
'Content Type' meta information for http and css files (our s3upload script
takes care of this).


