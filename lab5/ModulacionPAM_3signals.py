#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: ModulacionPAM_3signals
# GNU Radio version: 3.9.5.0

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import analog
from gnuradio import blocks
from gnuradio import gr
from gnuradio.fft import window
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio.qtgui import Range, RangeWidget
from PyQt5 import QtCore
from modulacionPAM import modulacionPAM  # grc-generated hier_block



from gnuradio import qtgui

class ModulacionPAM_3signals(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "ModulacionPAM_3signals", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("ModulacionPAM_3signals")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "ModulacionPAM_3signals")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 1000000
        self.fs = fs = samp_rate/100
        self.w = w = 10
        self.fm = fm = fs/10
        self.d4 = d4 = 0
        self.d3 = d3 = 30
        self.d2 = d2 = 20
        self.d1 = d1 = 10

        ##################################################
        # Blocks
        ##################################################
        self._w_range = Range(0, 50, 1, 10, 200)
        self._w_win = RangeWidget(self._w_range, self.set_w, "ancho de pulso", "counter_slider", int, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._w_win)
        self._d4_range = Range(0, 100, 1, 0, 200)
        self._d4_win = RangeWidget(self._d4_range, self.set_d4, "demodulador", "counter_slider", int, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._d4_win)
        self._d3_range = Range(0, 100, 1, 30, 200)
        self._d3_win = RangeWidget(self._d3_range, self.set_d3, "saw tooth", "counter_slider", int, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._d3_win)
        self._d2_range = Range(0, 100, 1, 20, 200)
        self._d2_win = RangeWidget(self._d2_range, self.set_d2, "triangle", "counter_slider", int, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._d2_win)
        self._d1_range = Range(0, 100, 1, 10, 200)
        self._d1_win = RangeWidget(self._d1_range, self.set_d1, "square", "counter_slider", int, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._d1_win)
        self.qtgui_time_sink_x_1 = qtgui.time_sink_f(
            1024, #size
            samp_rate, #samp_rate
            "", #name
            2, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_1.set_update_time(0.10)
        self.qtgui_time_sink_x_1.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_1.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_1.enable_tags(True)
        self.qtgui_time_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1.enable_autoscale(False)
        self.qtgui_time_sink_x_1.enable_grid(False)
        self.qtgui_time_sink_x_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_1.enable_control_panel(False)
        self.qtgui_time_sink_x_1.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(2):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_1_win = sip.wrapinstance(self.qtgui_time_sink_x_1.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_1_win)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
            1024, #size
            samp_rate, #samp_rate
            "", #name
            4, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(4):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.modulacionPAM_4 = modulacionPAM(
            d=w,
            fs=fs,
            samp_rate=samp_rate,
        )
        self.modulacionPAM_0_0_0_0 = modulacionPAM(
            d=w,
            fs=fs,
            samp_rate=samp_rate,
        )
        self.modulacionPAM_0_0_0 = modulacionPAM(
            d=w,
            fs=fs,
            samp_rate=samp_rate,
        )
        self.modulacionPAM_0_0 = modulacionPAM(
            d=w,
            fs=fs,
            samp_rate=samp_rate,
        )
        self.modulacionPAM_0 = modulacionPAM(
            d=w,
            fs=fs,
            samp_rate=samp_rate,
        )
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_delay_3 = blocks.delay(gr.sizeof_float*1, d4)
        self.blocks_delay_2 = blocks.delay(gr.sizeof_float*1, d3)
        self.blocks_delay_1 = blocks.delay(gr.sizeof_float*1, d1)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_float*1, d2)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.analog_sig_source_x_3 = analog.sig_source_f(samp_rate, analog.GR_SAW_WAVE, fm, 1, 0, 0)
        self.analog_sig_source_x_2 = analog.sig_source_f(samp_rate, analog.GR_TRI_WAVE, fm, 1, 0, 0)
        self.analog_sig_source_x_1 = analog.sig_source_f(samp_rate, analog.GR_SQR_WAVE, fm, 1, 0, 0)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, fm, 1, 0, 0)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.analog_sig_source_x_1, 0), (self.modulacionPAM_0_0, 0))
        self.connect((self.analog_sig_source_x_2, 0), (self.modulacionPAM_0_0_0, 0))
        self.connect((self.analog_sig_source_x_3, 0), (self.modulacionPAM_0_0_0_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_delay_3, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.qtgui_time_sink_x_1, 0))
        self.connect((self.blocks_delay_0, 0), (self.blocks_add_xx_0, 2))
        self.connect((self.blocks_delay_0, 0), (self.qtgui_time_sink_x_0, 2))
        self.connect((self.blocks_delay_1, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_delay_1, 0), (self.qtgui_time_sink_x_0, 1))
        self.connect((self.blocks_delay_2, 0), (self.blocks_add_xx_0, 3))
        self.connect((self.blocks_delay_2, 0), (self.qtgui_time_sink_x_0, 3))
        self.connect((self.blocks_delay_3, 0), (self.modulacionPAM_4, 0))
        self.connect((self.blocks_throttle_0, 0), (self.modulacionPAM_0, 0))
        self.connect((self.modulacionPAM_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.modulacionPAM_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.modulacionPAM_0_0, 0), (self.blocks_delay_1, 0))
        self.connect((self.modulacionPAM_0_0_0, 0), (self.blocks_delay_0, 0))
        self.connect((self.modulacionPAM_0_0_0_0, 0), (self.blocks_delay_2, 0))
        self.connect((self.modulacionPAM_4, 0), (self.qtgui_time_sink_x_1, 1))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "ModulacionPAM_3signals")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_fs(self.samp_rate/100)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_1.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_2.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_3.set_sampling_freq(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.modulacionPAM_0.set_samp_rate(self.samp_rate)
        self.modulacionPAM_0_0.set_samp_rate(self.samp_rate)
        self.modulacionPAM_0_0_0.set_samp_rate(self.samp_rate)
        self.modulacionPAM_0_0_0_0.set_samp_rate(self.samp_rate)
        self.modulacionPAM_4.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_1.set_samp_rate(self.samp_rate)

    def get_fs(self):
        return self.fs

    def set_fs(self, fs):
        self.fs = fs
        self.set_fm(self.fs/10)
        self.modulacionPAM_0.set_fs(self.fs)
        self.modulacionPAM_0_0.set_fs(self.fs)
        self.modulacionPAM_0_0_0.set_fs(self.fs)
        self.modulacionPAM_0_0_0_0.set_fs(self.fs)
        self.modulacionPAM_4.set_fs(self.fs)

    def get_w(self):
        return self.w

    def set_w(self, w):
        self.w = w
        self.modulacionPAM_0.set_d(self.w)
        self.modulacionPAM_0_0.set_d(self.w)
        self.modulacionPAM_0_0_0.set_d(self.w)
        self.modulacionPAM_0_0_0_0.set_d(self.w)
        self.modulacionPAM_4.set_d(self.w)

    def get_fm(self):
        return self.fm

    def set_fm(self, fm):
        self.fm = fm
        self.analog_sig_source_x_0.set_frequency(self.fm)
        self.analog_sig_source_x_1.set_frequency(self.fm)
        self.analog_sig_source_x_2.set_frequency(self.fm)
        self.analog_sig_source_x_3.set_frequency(self.fm)

    def get_d4(self):
        return self.d4

    def set_d4(self, d4):
        self.d4 = d4
        self.blocks_delay_3.set_dly(self.d4)

    def get_d3(self):
        return self.d3

    def set_d3(self, d3):
        self.d3 = d3
        self.blocks_delay_2.set_dly(self.d3)

    def get_d2(self):
        return self.d2

    def set_d2(self, d2):
        self.d2 = d2
        self.blocks_delay_0.set_dly(self.d2)

    def get_d1(self):
        return self.d1

    def set_d1(self, d1):
        self.d1 = d1
        self.blocks_delay_1.set_dly(self.d1)




def main(top_block_cls=ModulacionPAM_3signals, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
