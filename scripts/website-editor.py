
import os, sys, time
import subprocess
import shutil

from PySide import QtCore, QtGui, QtWebKit

SOURCE_DIR = '/home/almar/projects/www/pyzo-website'
RST_PAGES = '.'
HTML_PAGES = '_build/html'

PROJECT_NAME = os.path.basename(SOURCE_DIR).split('-')[0]
DEPLOY_DIR = os.path.join(os.path.split(SOURCE_DIR)[0], '%s.github.io'%PROJECT_NAME)


class Main(QtGui.QWidget):
    def __init__(self):
        super().__init__(None)
        
        # Create console
        self._console = MonoSpaceTextEdit(self, relativesize=-2)
        self._console.setReadOnly(True)
        self._console.setMinimumSize(400, 100)
        self._console.setMaximumSize(400, 100)
        self._console.addPlainText('Console output\n')
        
        # Create buttons
        self._pullBut = QtGui.QPushButton('Pull source', self)
        self._pullBut.clicked.connect(self.onPull)
        self._generateBut = QtGui.QPushButton('Generate!', self)
        self._generateBut.clicked.connect(self.onGenerate)
        self._deployBut = QtGui.QPushButton('Deploy', self)
        self._deployBut.clicked.connect(self.onDeploy)
        #
        self._backBut = QtGui.QPushButton('Previous', self)
        self._refreshBut = QtGui.QPushButton('Refresh', self)
        
        # Create splitter
        self._splitter = QtGui.QSplitter(self)
        
        # Create list for source files and initialize
        self._sourceList = QtGui.QListWidget(self._splitter)
        self._sourceList.itemActivated.connect(self.onFileSelected)
        for fname in sorted(os.listdir(SOURCE_DIR)):
            if fname.endswith('.rst'):
                self._sourceList.addItem(fname)
        
        # Create editor to edit the source
        self._sourceEdit = MonoSpaceTextEdit(self._splitter)
        self._currentFile = None
        
        # Create html viewer
        self._htmlView = QtWebKit.QWebView(self._splitter)
        self._htmlView.setUrl( os.path.join(SOURCE_DIR, HTML_PAGES, 'index.html') )
        self._htmlView.setZoomFactor(0.8)
        
        # Connect some more signals
        self._backBut.clicked.connect(self._htmlView.back)
        self._refreshBut.clicked.connect(self._htmlView.reload)
        
        self._layout()
    
    
    def _layout(self):
        
        # Add buttons to layout
        #
        butLayoutH1 = QtGui.QHBoxLayout()
        butLayoutH1.addWidget(self._pullBut)
        butLayoutH1.addStretch(1)
        #
        butLayoutH2= QtGui.QHBoxLayout()
        butLayoutH2.addWidget(self._generateBut)
        butLayoutH2.addWidget(self._deployBut)
        butLayoutH2.addStretch(1)
        #
        butLayoutH3= QtGui.QHBoxLayout()
        butLayoutH3.addStretch(1)
        butLayoutH3.addWidget(self._refreshBut)
        butLayoutH3.addWidget(self._backBut)
        #
        butLayoutV = QtGui.QVBoxLayout()
        butLayoutV.addLayout(butLayoutH1)
        butLayoutV.addLayout(butLayoutH2)
        butLayoutV.addLayout(butLayoutH3)
        
        # Top layout
        topLayout = QtGui.QHBoxLayout()
        topLayout.addWidget(self._console, 0)
        topLayout.addLayout(butLayoutV, 1)
        
        # Main Layout
        layout = QtGui.QVBoxLayout(self)
        self.setLayout(layout)
        #
        layout.addLayout(topLayout)
        layout.addWidget(self._splitter)
    
    
    def onPull(self):
        #self.run_command('ls')
        self.run_command('git pull')
    
    
    def onGenerate(self):
        self._saveCurrentFile()
        self.run_command('make html')
        self._htmlView.reload()
    
    
    def onFileSelected(self, item):
        self._saveCurrentFile()
        
        # Load new
        fname = os.path.join(SOURCE_DIR, item.text())
        text = open(fname, 'rb').read().decode('utf-8')
        self._sourceEdit.setPlainText(text)
        self._currentFile = fname
    
    
    def onDeploy(self):
        
        self.run_command('git pull', DEPLOY_DIR)
        
        # Copy all files
        try:
            src_dir = os.path.join(SOURCE_DIR, HTML_PAGES)
            for fname in os.listdir(src_dir):
                src = os.path.join(src_dir, fname)
                dst = os.path.join(DEPLOY_DIR, fname)
                if os.path.isdir(src):
                    if os.path.isdir(dst):
                        shutil.rmtree(dst)
                    shutil.copytree(src, dst)
                elif os.path.isfile(src):
                    shutil.copy2(src, dst)
        except Exception as err:
            self._console.addPlainTex('Error copying files:\n')
            self._console.addPlainTex(str(err)+'\n')
            raise
        
        # Get Git credentials
        username = QtGui.QInputDialog.getText(self, 'Credentials', 'Git username')
        password = QtGui.QInputDialog.getText(self, 'Credentials', 'Git password',
           QtGui.QLineEdit.Password)
        if isinstance(username, tuple): username = username[0]
        if isinstance(password, tuple): password = password[0]
        
        # Push it!
        self.run_command('git push', DEPLOY_DIR, [username, password])
    
    
    def _saveCurrentFile(self):
        # Save current if we can
        if self._currentFile:
            with open(self._currentFile, 'wb') as f:
                text = self._sourceEdit.toPlainText()
                f.write(text.encode('utf-8'))


    def run_command(self, cmd, cwd=None, input=None):
        """ Run a command, showing its stdout/stderr in a new window.
        """
        # Show command
        self._console.addPlainText('\n$ %s\n' % str(cmd))
        
        # Run command
        inputPipe = subprocess.PIPE if input else None
        print(inputPipe)
        cwd = cwd or SOURCE_DIR
        p = subprocess.Popen(cmd, shell=True, cwd=cwd,
                    stdin=inputPipe, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        
        # Input?
        if input:
            for line in input:
                p.stdin.write(line.encode('utf-8')+b'\n')
        
        # Enter a loop ...
        self.setDisabled(True)
        try:
            stop = False
            while not stop:
                time.sleep(0.01)
                QtGui.qApp.processEvents()
                # Should we stop?
                stop = p.poll() is not None
                # Pipe output (called one time after process is stopped)
                text = p.stdout.read().decode('utf-8', 'ignore')
                if text:
                    self._console.addPlainText(text)
        except Exception as err:
            self._console.addPlainText('Error!\n%s\n' % str(err))
        finally:
            self.setDisabled(False)
        
        # Notify finished
        if p.poll() == 0:
            self._console.addPlainText("\n==> Done\n")
        elif p.poll():
            self._console.addPlainText("\n==> Error\n")



class MonoSpaceTextEdit(QtGui.QPlainTextEdit):
    def __init__(self, *args, **kwargs):
        # Get kwargs
        relativesize = kwargs.pop('relativesize', 0)
        # Normal init
        QtGui.QPlainTextEdit.__init__(self, *args, **kwargs)
        # Get size and family
        size = QtGui.QFont().pointSize()
        size += relativesize
        f = QtGui.QFont('lalala this is not a valid font name')
        f.setStyleHint(f.TypeWriter, f.PreferDefault)
        family = QtGui.QFontInfo(f).family()
        # Set font
        self.setFont(QtGui.QFont(family, size))

    def addPlainText(self, text):
        self.setPlainText(self.toPlainText() + text)
        cursor = self.textCursor()
        cursor.movePosition(cursor.End)
        self.setTextCursor(cursor)
        self.ensureCursorVisible()



    
    

if __name__ == '__main__':
    m = Main()
    m.show()
