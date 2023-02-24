from analysis_tools.utils import import_root
from copy import deepcopy as copy
from plotting_tools.root import get_labels, Canvas, RatioCanvas

ROOT = import_root()


f_true = "/eos/user/j/jleonhol/cmt/FeaturePlotLLR/llr_2018/cat_baseline/prod_2202/root/HHKinFit_mass__pg_ggf__nodata.root"
f_rew = "/eos/user/j/jleonhol/cmt/ggFFeaturePlotLLR/llr_2018/cat_baseline/prod_2202/root/HHKinFit_mass__pg_ggf__nodata.root"

legends = ["Produced sample", "Reweighted"]
colors = [1, 2]

c = Canvas()

n_cols = 1
n_rows = 2

# col_width = 0.125
col_width = 0.25
row_width = 0.06

legend_x2 = 0.88
legend_x1 = legend_x2 - n_cols * col_width
legend_y2 = 0.88
legend_y1 = legend_y2 - n_rows * row_width

legend = ROOT.TLegend(legend_x1, legend_y1, legend_x2, legend_y2)
histos = []

max_val = -1

for i, (f, leg, color) in enumerate(zip([f_true, f_rew], legends, colors)):
    tf = ROOT.TFile.Open(f)
    histos.append(copy(tf.Get("histograms/ggf_0_1")))
    histos[-1].GetXaxis().SetTitle("HH Mass [GeV]")
    histos[-1].GetYaxis().SetTitle("Events / 40 GeV")
    histos[-1].SetLineColor(color)

    if histos[-1].GetMaximum() > max_val:
        max_val = histos[-1].GetMaximum()

    legend.AddEntry(histos[-1], leg, "l")

for histo in histos:
    histo.SetMaximum(1.1 * max_val)
    histo.SetMinimum(0)
    histo.Draw("histo, same, E")

draw_labels = get_labels(upper_right="2018, 13 TeV (59.74 fb^{-1})")

legend.Draw("same")
for label in draw_labels:
    label.Draw("same")

c.SaveAs("ggf_kl0.pdf")
c.SaveAs("ggf_kl0.png")

