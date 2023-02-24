import correctionlib as _core
import itertools
import ROOT

folder = "/cvmfs/cms.cern.ch/rsync/cms-nanoAOD/jsonpog-integration/POG/TAU/{}/tau.json.gz"

years = ["2016_Legacy", "2017_ReReco", "2018_ReReco"]
tau_pt = [25. + i for i in range(0, 175, 5)]
tau_dm = [0, 1, 10, 11]
tau_genmatch = [0, 1, 2, 3, 4, 5, 6]
tau_wp = ["Loose", "Medium", "Tight", "VLoose", "VTight", "VVLoose", "VVTight", "VVVLoose"]

min_sf = 999
max_sf = -999

all_sf = []
histo = ROOT.TH1F("tau_sf", "; ; Entries", 50, 0.7, 1.2)

for year in years:
    cset = _core.CorrectionSet.from_file(folder.format(year))
    corr1 = cset["DeepTau2017v2p1VSjet"]
    for pt, dm, genmatch, wp in itertools.product(tau_pt, tau_dm, tau_genmatch, tau_wp):
        sf = corr1.evaluate(pt, dm, genmatch, wp, "nom", "pt")
        if sf < min_sf:
            min_sf = sf
        if sf > max_sf:
            max_sf = sf
        all_sf.append(sf)
        histo.Fill(sf)

print(min_sf, max_sf)

print(sum(all_sf) / len(all_sf))

c = ROOT.TCanvas()
histo.Draw()
c.SaveAs("tau_sf.pdf")
c.SaveAs("tau_sf.png")
    
