import ROOT
ROOT.gROOT.SetBatch(True)
ROOT.gStyle.SetOptStat(0)

def myrounding(num):
    i = 10.
    while True:
        rounded_num = num * i
        if rounded_num > 1:
            return round(rounded_num) / i
        i *= 10

br = [58.24, 21.37, 8.187, 6.272, 2.619, 0.227]

axis = ["bb", "WW", "gg", "#tau#tau", "ZZ", "#gamma#gamma"]

histo = ROOT.TH2F("histo", "", len(br), 0, len(br), len(br), 0, len(br))

total = 0

for ibr in range(len(br)):
    histo.GetXaxis().SetBinLabel(ibr + 1, axis[ibr])
    histo.GetYaxis().SetBinLabel(len(br) - ibr, axis[ibr])
    for ibr2 in range(ibr, len(br)):
        hh_br = br[ibr] * br[ibr2] / 100
        if ibr != ibr2:
            hh_br *= 2
        hh_br = myrounding(hh_br)
        histo.SetBinContent(ibr + 1, len(br) - ibr2, hh_br)
        total += hh_br

histo.GetZaxis().SetRangeUser(0.0001, 100)
histo.GetZaxis().SetTitle("Branching fraction (%)")
histo.GetZaxis().SetTitleOffset(1.5)

histo.GetXaxis().SetLabelSize(0.05)
histo.GetYaxis().SetLabelSize(0.05)


c = ROOT.TCanvas("", "", 800, 800)
c.SetRightMargin(0.16)
c.SetLogz()
histo.Draw("colz, text")
c.SaveAs("hh_br.png")
c.SaveAs("hh_br.pdf")

print(total)