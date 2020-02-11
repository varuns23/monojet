from ROOT import TH1F
from array import array
import numpy as np

class b_info:
    template = None
    cut = None
    weight = None
    @staticmethod
    def initVariable():
        b_info.template = None
        b_info.cut = None

def linspace(xmin,xmax,nx): return list(np.linspace(xmin,xmax,nx+1))

def rebin(arg,sample,name):
    bins = array('d',[250.,280.,310.,340.,370.,400.,430.,470.,510.,550.,590.,640.,690.,740.,790.,840.,900.,960.,1020.,1090.,1160.,1250.,1400.])
    histo = TH1F(name,'',len(bins)-1,bins)
    histo.Rebin(2)
    b_info.template = histo
    
b_info.binninglist = {
    'rebin':rebin
}
