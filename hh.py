import ROOT
ROOT.gROOT.SetBatch(True)
ROOT.gStyle.SetOptStat(0)

br = [57.7, 21.5, 8.6, 6.3, 2.7, 2.3]

axis = ["bb", "WW", "gg", "#tau#tau", "ZZ", "#gamma#gamma"]

histo = ROOT.TH2F("histo", "", len(br), 0, len(br), len(br), 0, len(br))

for ibr in range(len(br)):
    histo.GetXaxis().SetBinLabel(ibr + 1, axis[ibr])
    histo.GetYaxis().SetBinLabel(len(br) - ibr, axis[ibr])
    for ibr2 in range(ibr, len(br)):
        histo.SetBinContent(ibr + 1, len(br) - ibr2, br[ibr] * br[ibr2] / 100)

histo.GetZaxis().SetRangeUser(0.001, 100)
histo.GetXaxis().SetLabelSize(0.05)
histo.GetYaxis().SetLabelSize(0.05)


c = ROOT.TCanvas("", "", 800, 800)
c.SetRightMargin(0.16)
c.SetLogz()
histo.Draw("colz")
c.SaveAs("hh_br.png")
c.SaveAs("hh_br.pdf")
