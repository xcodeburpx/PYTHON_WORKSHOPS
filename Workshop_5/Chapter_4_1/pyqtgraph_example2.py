import numpy as np
import pyqtgraph as pg

# Generate data
data = np.random.normal(size=1000)
# PLot the data
pg.plot(data, title="Simplest possible plotting example")


data = np.random.normal(size=(500,500))

pg.image(data, title="Simplest possible image example")


if __name__ == '__main__':
    import sys
    if sys.flags.interactive != 1 or not hasattr(pg.QtCore, 'PYQT_VERSION'):
        pg.QtGui.QApplication.exec_()