# -*- coding: utf-8 -*-
"""
    musicindex.monitor
    ~~~~~~~~~~~~~~~~~~

    This module provides functios for monitoring music directory's changes.

    :copyright: (c) 2014 by Lenny.
    :license: LGPL, see LICENSE for more details.
"""

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class FSEventHandler(FileSystemEventHandler):
    """Directory change event handler"""

    def on_any_event(self, event):
        #Catch-all event handler.
        #Parameters: event (FileSystemEvent) – The event object representing the file system event.
        pass

    def on_created(self, event):
        #Called when a file or directory is created.
        #Parameters: event (DirCreatedEvent or FileCreatedEvent) – Event representing file/directory creation.
        print('get create event')

    def on_deleted(self, event):
        #Called when a file or directory is deleted.
        #Parameters: event (DirDeletedEvent or FileDeletedEvent) – Event representing file/directory deletion.
        print('get delete event')

    def on_modified(self, event):
        #Called when a file or directory is modified.
        #Parameters: event (DirModifiedEvent or FileModifiedEvent) – Event representing file/directory modification.
        print('get modified event')

    def on_moved(self, event):
        #Called when a file or a directory is moved or renamed.
        #Parameters: event (DirMovedEvent or FileMovedEvent) – Event representing file/directory movement.
        print('get moved event')

class DirMontior(object):
    """monitro directory file changes"""
    def __init__(self, path):
        self.observer = Observer()
        event_handler = FSEventHandler()
        self.observer.schedule(event_handler, path, recursive=True)

    def start(self):
        self.observer.start()

    def stop(self):
        self.observer.stop()
        self.observer.join()

if __name__ == '__main__':
    import time
    from os.path import expanduser

    monitor_path = expanduser("~/test")
    print('monitor your home dircetory:{0}'.format(monitor_path))

    monitor = DirMontior(monitor_path)
    monitor.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        monitor.stop()

