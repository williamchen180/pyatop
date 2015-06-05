#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.5 on Wed Jun  3 15:15:09 2015

import signal
import sys
import pickle
import pprint
import os
import time
import wx
import Gnuplot


# begin wxGlade: extracode
# end wxGlade



class MyMenuBar(wx.MenuBar):
    def __init__(self, *args, **kwds):
        # content of this block not found: did you rename this class?
        pass

    def __set_properties(self):
        # content of this block not found: did you rename this class?
        pass

    def __do_layout(self):
        # content of this block not found: did you rename this class?
        pass

# end of class MyMenuBar
class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):

        # begin wxGlade: MyFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.button_4 = wx.Button(self, -1, "Save settings")
        self.checkbox_45 = wx.CheckBox(self, -1, "FILE A :")
        self.text_ctrl_2 = wx.TextCtrl(self, -1, "atopA.raw")
        self.button_2 = wx.Button(self, -1, "LOAD")
        self.text_ctrl_4 = wx.TextCtrl(self, -1, "", style=wx.TE_READONLY)
        self.checkbox_46 = wx.CheckBox(self, -1, "FILE B : ")
        self.text_ctrl_3 = wx.TextCtrl(self, -1, "atopB.raw")
        self.button_3 = wx.Button(self, -1, "LOAD")
        self.text_ctrl_5 = wx.TextCtrl(self, -1, "", style=wx.TE_READONLY)
        self.notebook_1 = wx.Notebook(self, -1, style=0)
        self.notebook_1_pane_1 = wx.Panel(self.notebook_1, -1)
        self.checkbox_1 = wx.CheckBox(self.notebook_1_pane_1, 9, "CPU's in system mode")
        self.checkbox_2 = wx.CheckBox(self.notebook_1_pane_1, 10, "consumption for all  CPU's in user mode")
        self.checkbox_4 = wx.CheckBox(self.notebook_1_pane_1, 12, "consumption for all CPU's in idle mode")
        self.checkbox_5 = wx.CheckBox(self.notebook_1_pane_1, 13, "consumption for all CPU's in wait mode")
        self.checkbox_6 = wx.CheckBox(self.notebook_1_pane_1, 14, "consumption for all CPU's in irq mode")
        self.checkbox_7 = wx.CheckBox(self.notebook_1_pane_1, 15, "consumption for all CPU's in softirq mode")
        self.checkbox_8 = wx.CheckBox(self.notebook_1_pane_1, 16, "consumption for all CPU's in steal mode")
        self.checkbox_9 = wx.CheckBox(self.notebook_1_pane_1, 17, "consumption for all CPY's in guest mode")
        self.notebook_1_pane_2 = wx.Panel(self.notebook_1, -1)
        self.checkbox_11 = wx.CheckBox(self.notebook_1_pane_2, 9, "free memory (pages)")
        self.checkbox_12 = wx.CheckBox(self.notebook_1_pane_2, 10, "page cache (pages)")
        self.checkbox_13 = wx.CheckBox(self.notebook_1_pane_2, 11, "buffer cache (pages)")
        self.checkbox_14 = wx.CheckBox(self.notebook_1_pane_2, 12, "slab (pages)")
        self.checkbox_15 = wx.CheckBox(self.notebook_1_pane_2, 13, "number of dirty pages in cache")
        self.notebook_1_pane_3 = wx.Panel(self.notebook_1, -1)
        self.checkbox_18 = wx.CheckBox(self.notebook_1_pane_3, 8, "1 Min. Avg. loading")
        self.checkbox_19 = wx.CheckBox(self.notebook_1_pane_3, 9, "5 Min. Avg. loading")
        self.checkbox_20 = wx.CheckBox(self.notebook_1_pane_3, 10, "10 Min. Avg. loading")
        self.checkbox_3 = wx.CheckBox(self.notebook_1_pane_3, 11, "Number of Context switching")
        self.checkbox_16 = wx.CheckBox(self.notebook_1_pane_3, 12, "Number of serviced interrupts")
        self.notebook_1_pane_4 = wx.Panel(self.notebook_1, -1)
        self.checkbox_23 = wx.CheckBox(self.notebook_1_pane_4, 8, "number of page scans")
        self.checkbox_24 = wx.CheckBox(self.notebook_1_pane_4, 9, "number of allocs stalls")
        self.checkbox_25 = wx.CheckBox(self.notebook_1_pane_4, 11, "number of swap ins")
        self.checkbox_26 = wx.CheckBox(self.notebook_1_pane_4, 12, "Number of swap outs")
        self.notebook_1_pane_5 = wx.Panel(self.notebook_1, -1)
        self.checkbox_27 = wx.CheckBox(self.notebook_1_pane_5, 8, "packets received by TCP")
        self.checkbox_28 = wx.CheckBox(self.notebook_1_pane_5, 9, "packets transmitted by TCP")
        self.checkbox_29 = wx.CheckBox(self.notebook_1_pane_5, 10, "packets received by UDP")
        self.checkbox_30 = wx.CheckBox(self.notebook_1_pane_5, 11, "packets transmitted by UDP")
        self.checkbox_31 = wx.CheckBox(self.notebook_1_pane_5, 12, "packets received by IP")
        self.checkbox_32 = wx.CheckBox(self.notebook_1_pane_5, 13, "packets transmitted by IP")
        self.checkbox_33 = wx.CheckBox(self.notebook_1_pane_5, 14, "packets delivered to higher layer by IP")
        self.checkbox_34 = wx.CheckBox(self.notebook_1_pane_5, 15, "packets forwarded by IP")
        self.notebook_1_pane_6 = wx.Panel(self.notebook_1, -1)
        self.checkbox_39 = wx.CheckBox(self.notebook_1_pane_6, 8, "ms spent for I/O")
        self.checkbox_40 = wx.CheckBox(self.notebook_1_pane_6, 9, "reads issued")
        self.checkbox_41 = wx.CheckBox(self.notebook_1_pane_6, 10, "sectors transferred for reads")
        self.checkbox_42 = wx.CheckBox(self.notebook_1_pane_6, 11, "writes issues")
        self.checkbox_43 = wx.CheckBox(self.notebook_1_pane_6, 12, "sectors transferred for writes")
        self.notebook_1_pane_7 = wx.Panel(self.notebook_1, -1)
        self.checkbox_10 = wx.CheckBox(self.notebook_1_pane_7, 8, "eth0 packets received")
        self.checkbox_17 = wx.CheckBox(self.notebook_1_pane_7, 9, "eth0 bytes received")
        self.checkbox_21 = wx.CheckBox(self.notebook_1_pane_7, 10, "eth0 packets transmitted")
        self.checkbox_22 = wx.CheckBox(self.notebook_1_pane_7, 11, "eth0 bytes transmitted")
        self.notebook_1_pane_8 = wx.Panel(self.notebook_1, -1)
        self.checkbox_10_copy = wx.CheckBox(self.notebook_1_pane_8, 8, "eth1 packets received")
        self.checkbox_17_copy = wx.CheckBox(self.notebook_1_pane_8, 9, "eth1 bytes received")
        self.checkbox_21_copy = wx.CheckBox(self.notebook_1_pane_8, 10, "eth1 packets transmitted")
        self.checkbox_22_copy = wx.CheckBox(self.notebook_1_pane_8, 11, "eth1 bytes transmitted")
        self.notebook_1_pane_9 = wx.Panel(self.notebook_1, -1)
        self.checkbox_10_copy_1 = wx.CheckBox(self.notebook_1_pane_9, 8, "eth2 packets received")
        self.checkbox_17_copy_1 = wx.CheckBox(self.notebook_1_pane_9, 9, "eth2 bytes received")
        self.checkbox_21_copy_1 = wx.CheckBox(self.notebook_1_pane_9, 10, "eth2 packets transmitted")
        self.checkbox_22_copy_1 = wx.CheckBox(self.notebook_1_pane_9, 11, "eth2 bytes transmitted")
        self.notebook_1_pane_10 = wx.Panel(self.notebook_1, -1)
        self.checkbox_10_copy_2 = wx.CheckBox(self.notebook_1_pane_10, 8, "eth3 packets received")
        self.checkbox_17_copy_2 = wx.CheckBox(self.notebook_1_pane_10, 9, "eth3 bytes received")
        self.checkbox_21_copy_2 = wx.CheckBox(self.notebook_1_pane_10, 10, "eth3 packets transmitted")
        self.checkbox_22_copy_2 = wx.CheckBox(self.notebook_1_pane_10, 11, "eth3 bytes transmitted")
        self.button_1 = wx.Button(self, -1, "Generate")
        self.text_ctrl_1 = wx.TextCtrl(self, -1, "", style=wx.TE_MULTILINE | wx.TE_READONLY | wx.HSCROLL | wx.TE_LINEWRAP | wx.TE_WORDWRAP)

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.save_settings_handler, self.button_4)
        self.Bind(wx.EVT_BUTTON, self.load_fileA, self.button_2)
        self.Bind(wx.EVT_BUTTON, self.load_fileB, self.button_3)
        self.Bind(wx.EVT_BUTTON, self.generate_report, self.button_1)
        # end wxGlade


        # My code starts from here...

        self.Bind( wx.EVT_CLOSE, self.frame_close, self )

        self.text_ctrl_1.SetLabel( 'text_ctrl_1' )
        self.text_ctrl_2.SetLabel( 'text_ctrl_2' )
        self.text_ctrl_3.SetLabel( 'text_ctrl_3' )
        self.text_ctrl_4.SetLabel( 'text_ctrl_4' )
        self.text_ctrl_5.SetLabel( 'text_ctrl_5' )

        self.setting_file = '.pyatop'

        self.load_settings()

        self.parsable = ['CPU', 'cpu', 'CPL', 'MEM', 'SWP', 'PAG', 'NET', 'DSK' ]
        self.eths = ['upper', 'eth0', 'eth1', 'eth2', 'eth3' ]

        self.fileACheckBox = self.checkbox_45
        self.fileBCheckBox = self.checkbox_46
        self.fileATextCtrl = self.text_ctrl_2
        self.fileBTextCtrl = self.text_ctrl_3
        self.fileA = self.fileATextCtrl.GetValue()
        self.fileB = self.fileBTextCtrl.GetValue()
        self.fileAStatus = self.text_ctrl_4
        self.fileBStatus = self.text_ctrl_5

        fileA_not_ready = False
        fileB_not_ready = False
        for x in self.parsable:
            if os.path.isfile( '/tmp/%s_%s.txt' % (os.path.basename( self.fileA ), x ) ) is False:
                print '/tmp/%s_%s.txt no exist' % (os.path.basename( self.fileA ), x )
                fileA_not_ready = True
                break
        if fileA_not_ready is True:
            self.fileAStatus.SetValue( 'not loaded' )
        for x in self.parsable:
            if os.path.isfile( '/tmp/%s_%s.txt' % (os.path.basename( self.fileB ), x ) ) is False:
                fileB_not_ready = True
                break
        if fileB_not_ready is True:
            self.fileBStatus.SetValue( 'not loaded' )


        self.status( 'ready..' )


    def status(self, string ):
        self.text_ctrl_1.SetValue( string )


    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle("frame_1")
        self.checkbox_45.SetValue(1)
        self.text_ctrl_2.SetMinSize((280, 31))
        self.checkbox_46.SetValue(1)
        self.text_ctrl_3.SetMinSize((280, 31))
        self.checkbox_1.SetValue(1)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_12_copy_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_12_copy_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_12_copy = wx.BoxSizer(wx.VERTICAL)
        sizer_12 = wx.BoxSizer(wx.VERTICAL)
        sizer_8 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_5 = wx.GridSizer(8, 1, 0, 0)
        grid_sizer_4 = wx.GridSizer(4, 1, 0, 0)
        grid_sizer_2 = wx.GridSizer(5, 1, 0, 0)
        grid_sizer_1 = wx.GridSizer(7, 1, 0, 0)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_7 = wx.BoxSizer(wx.VERTICAL)
        sizer_6 = wx.BoxSizer(wx.VERTICAL)
        sizer_5 = wx.BoxSizer(wx.VERTICAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_9 = wx.BoxSizer(wx.VERTICAL)
        sizer_11 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_10 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1.Add(self.button_4, 0, 0, 0)
        sizer_10.Add(self.checkbox_45, 0, 0, 0)
        sizer_10.Add(self.text_ctrl_2, 0, 0, 0)
        sizer_10.Add(self.button_2, 0, 0, 0)
        sizer_10.Add(self.text_ctrl_4, 0, 0, 0)
        sizer_9.Add(sizer_10, 1, wx.EXPAND, 0)
        sizer_11.Add(self.checkbox_46, 0, 0, 0)
        sizer_11.Add(self.text_ctrl_3, 0, 0, 0)
        sizer_11.Add(self.button_3, 0, 0, 0)
        sizer_11.Add(self.text_ctrl_5, 0, 0, 0)
        sizer_9.Add(sizer_11, 1, wx.EXPAND, 0)
        sizer_3.Add(sizer_9, 1, wx.EXPAND, 0)
        sizer_2.Add(sizer_3, 1, wx.EXPAND, 0)
        sizer_5.Add(self.checkbox_1, 0, 0, 0)
        sizer_5.Add(self.checkbox_2, 0, 0, 0)
        sizer_5.Add(self.checkbox_4, 0, 0, 0)
        sizer_5.Add(self.checkbox_5, 0, 0, 0)
        sizer_5.Add(self.checkbox_6, 0, 0, 0)
        sizer_5.Add(self.checkbox_7, 0, 0, 0)
        sizer_5.Add(self.checkbox_8, 0, 0, 0)
        sizer_5.Add(self.checkbox_9, 0, 0, 0)
        sizer_4.Add(sizer_5, 1, wx.EXPAND, 0)
        sizer_4.Add(sizer_6, 1, wx.EXPAND, 0)
        sizer_4.Add(sizer_7, 1, wx.EXPAND, 0)
        self.notebook_1_pane_1.SetSizer(sizer_4)
        grid_sizer_1.Add(self.checkbox_11, 0, 0, 0)
        grid_sizer_1.Add(self.checkbox_12, 0, 0, 0)
        grid_sizer_1.Add(self.checkbox_13, 0, 0, 0)
        grid_sizer_1.Add(self.checkbox_14, 0, 0, 0)
        grid_sizer_1.Add(self.checkbox_15, 0, 0, 0)
        self.notebook_1_pane_2.SetSizer(grid_sizer_1)
        grid_sizer_2.Add(self.checkbox_18, 0, 0, 0)
        grid_sizer_2.Add(self.checkbox_19, 0, 0, 0)
        grid_sizer_2.Add(self.checkbox_20, 0, 0, 0)
        grid_sizer_2.Add(self.checkbox_3, 0, 0, 0)
        grid_sizer_2.Add(self.checkbox_16, 0, 0, 0)
        self.notebook_1_pane_3.SetSizer(grid_sizer_2)
        grid_sizer_4.Add(self.checkbox_23, 0, 0, 0)
        grid_sizer_4.Add(self.checkbox_24, 0, 0, 0)
        grid_sizer_4.Add(self.checkbox_25, 0, 0, 0)
        grid_sizer_4.Add(self.checkbox_26, 0, 0, 0)
        self.notebook_1_pane_4.SetSizer(grid_sizer_4)
        grid_sizer_5.Add(self.checkbox_27, 0, 0, 0)
        grid_sizer_5.Add(self.checkbox_28, 0, 0, 0)
        grid_sizer_5.Add(self.checkbox_29, 0, 0, 0)
        grid_sizer_5.Add(self.checkbox_30, 0, 0, 0)
        grid_sizer_5.Add(self.checkbox_31, 0, 0, 0)
        grid_sizer_5.Add(self.checkbox_32, 0, 0, 0)
        grid_sizer_5.Add(self.checkbox_33, 0, 0, 0)
        grid_sizer_5.Add(self.checkbox_34, 0, 0, 0)
        self.notebook_1_pane_5.SetSizer(grid_sizer_5)
        sizer_8.Add(self.checkbox_39, 0, 0, 0)
        sizer_8.Add(self.checkbox_40, 0, 0, 0)
        sizer_8.Add(self.checkbox_41, 0, 0, 0)
        sizer_8.Add(self.checkbox_42, 0, 0, 0)
        sizer_8.Add(self.checkbox_43, 0, 0, 0)
        self.notebook_1_pane_6.SetSizer(sizer_8)
        sizer_12.Add(self.checkbox_10, 0, 0, 0)
        sizer_12.Add(self.checkbox_17, 0, 0, 0)
        sizer_12.Add(self.checkbox_21, 0, 0, 0)
        sizer_12.Add(self.checkbox_22, 0, 0, 0)
        self.notebook_1_pane_7.SetSizer(sizer_12)
        sizer_12_copy.Add(self.checkbox_10_copy, 0, 0, 0)
        sizer_12_copy.Add(self.checkbox_17_copy, 0, 0, 0)
        sizer_12_copy.Add(self.checkbox_21_copy, 0, 0, 0)
        sizer_12_copy.Add(self.checkbox_22_copy, 0, 0, 0)
        self.notebook_1_pane_8.SetSizer(sizer_12_copy)
        sizer_12_copy_1.Add(self.checkbox_10_copy_1, 0, 0, 0)
        sizer_12_copy_1.Add(self.checkbox_17_copy_1, 0, 0, 0)
        sizer_12_copy_1.Add(self.checkbox_21_copy_1, 0, 0, 0)
        sizer_12_copy_1.Add(self.checkbox_22_copy_1, 0, 0, 0)
        self.notebook_1_pane_9.SetSizer(sizer_12_copy_1)
        sizer_12_copy_2.Add(self.checkbox_10_copy_2, 0, 0, 0)
        sizer_12_copy_2.Add(self.checkbox_17_copy_2, 0, 0, 0)
        sizer_12_copy_2.Add(self.checkbox_21_copy_2, 0, 0, 0)
        sizer_12_copy_2.Add(self.checkbox_22_copy_2, 0, 0, 0)
        self.notebook_1_pane_10.SetSizer(sizer_12_copy_2)
        self.notebook_1.AddPage(self.notebook_1_pane_1, "CPU")
        self.notebook_1.AddPage(self.notebook_1_pane_2, "MEM")
        self.notebook_1.AddPage(self.notebook_1_pane_3, "CPL")
        self.notebook_1.AddPage(self.notebook_1_pane_4, "PAG")
        self.notebook_1.AddPage(self.notebook_1_pane_5, "NET")
        self.notebook_1.AddPage(self.notebook_1_pane_6, "DSK")
        self.notebook_1.AddPage(self.notebook_1_pane_7, "eth0")
        self.notebook_1.AddPage(self.notebook_1_pane_8, "eth1")
        self.notebook_1.AddPage(self.notebook_1_pane_9, "eth2")
        self.notebook_1.AddPage(self.notebook_1_pane_10, "eth3")
        sizer_2.Add(self.notebook_1, 1, wx.EXPAND, 0)
        sizer_2.Add(self.button_1, 0, wx.EXPAND, 0)
        sizer_1.Add(sizer_2, 1, wx.EXPAND, 0)
        sizer_1.Add(self.text_ctrl_1, 0, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        self.Layout()
        # end wxGlade

    def load_fileA(self, event):  # wxGlade: MyFrame.<event_handler>
        self.fileA = self.fileATextCtrl.GetValue()
        if os.path.isfile( self.fileA ) is False:
            self.status( '%s not exist' % self.fileA )
            return
        basename = os.path.basename( self.fileA )
        for x in self.parsable:
            os.system( 'atop -r %s -P %s | grep %s | sed \'1d\' > /tmp/%s_%s.txt' % (self.fileA, x, x, basename, x ) )

        for x in self.eths:
            os.system( 'grep upper /tmp/%s_NET.txt | sed \'1d\' > /tmp/%s_NET_%s.txt' % ( basename, basename, x ) )

        self.fileAStatus.SetValue('loaded')
	
        event.Skip()

    def load_fileB(self, event):  # wxGlade: MyFrame.<event_handler>
        self.fileB = self.fileBTextCtrl.GetValue()
        if os.path.isfile( self.fileB ) is False:
            self.status( '%s not exist' % self.fileB )
            return
        basename = os.path.basename( self.fileB )
        for x in self.parsable:
            os.system( 'atop -r %s -P %s | grep %s | sed \'1d\' > /tmp/%s_%s.txt' % (self.fileA, x, x, basename, x ) )
        for x in self.eths:
            os.system( 'grep upper /tmp/%s_NET.txt | sed \'1d\' > /tmp/%s_NET_%s.txt' % ( basename, basename, x ) )

        self.fileBStatus.SetValue('loaded')
        event.Skip()


    def visitall( self, obj, load = False ):
        if hasattr( obj, 'GetChildren' ) is True:
            for x in obj.GetChildren():
                self.visitall( x, load )
        #print 'label:', obj.GetLabel(), ' name:', obj.GetName()
        if load is True:
            if type(obj) is wx._controls.CheckBox or type(obj) is wx._controls.TextCtrl:
                if self.settings.has_key( obj.GetLabel() ):
                    #print 'SetValue:', self.settings[ obj.GetLabel() ], ' to ', obj.GetLabel()
                    obj.SetValue( self.settings[ obj.GetLabel() ] )
        else:
            if type(obj) is wx._controls.CheckBox:
                self.settings[ obj.GetLabel() ] = obj.IsChecked()
            if type(obj) is wx._controls.TextCtrl:
                self.settings[ obj.GetLabel() ] = obj.GetValue()

    def load_settings(self):
        if os.path.isfile( self.setting_file ):
            with open( self.setting_file ,'rb') as f:
                self.settings = pickle.load( f )
            #pprint.pprint(self.settings)
            self.visitall( self, load = True ) 

    def do_save(self):
        self.settings = {}
        self.visitall( self ) 
        #pprint.pprint(self.settings)
        with open( self.setting_file, 'w') as f:
            pickle.dump( self.settings, f )


    def save_settings_handler(self, event):  # wxGlade: MyFrame.<event_handler>
        self.do_save()
        self.status( 'settings saved' )
        event.Skip()

    def frame_close( self, event ):
        self.do_save()
        self.Destroy()

    def do_the_plot( self, atop_file, target ):
        pngFile = '%s_%s.png' % ( os.path.basename( atop_file ), target )
        p = Gnuplot.Gnuplot()
        p('set terminal png size 1200, 600')
        p('set lmargin 8')
        p('set rmargin 4')
        p('set tmargin 3')
        p('set bmargin 8')
        p('set timefmt "%H:%M:%S"')
        p('set format x "%H:%M:%S"')
        p('set xdata time')
        p('set output "%s"' % pngFile ) 
        p('set xtics rotate')
        p('set title "CPU"')
        plotstr = ''
        for x in self.notebook_1.GetCurrentPage().GetChildren():
            #print x.GetId(), x.GetLabel()
            if x.IsChecked() is True:
                if plotstr != '':
                    plotstr += ' , '
                plotstr += '"/tmp/%s_%s.txt" using 5:%d title "%s" with lines' % ( os.path.basename(atop_file), target , x.GetId(), x.GetLabel() )     
        p( 'plot ' + plotstr )
        time.sleep(1)
        os.system('display ' + pngFile )

    def generate_report(self, event):  # wxGlade: MyFrame.<event_handler>

        target = self.notebook_1.GetPageText( self.notebook_1.GetSelection() )

        if self.fileACheckBox.IsChecked() is True and os.path.isfile( self.fileATextCtrl.GetValue() ):
            self.do_the_plot( self.fileATextCtrl.GetValue(), target ) 
        if self.fileBCheckBox.IsChecked() is True and os.path.isfile( self.fileBTextCtrl.GetValue() ):
            self.do_the_plot( self.fileBTextCtrl.GetValue(), target ) 

        event.Skip()

# end of class MyFrame
if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    frame_1 = MyFrame(None, -1, "")
    app.SetTopWindow(frame_1)
    frame_1.Show()
    app.MainLoop()

