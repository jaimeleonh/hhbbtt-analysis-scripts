from copy import deepcopy as copy
from analysis_tools.utils import import_root
from plotting_tools.root import get_labels, Canvas, RatioCanvas

ROOT = import_root()

folder = "/eos/user/j/jleonhol/cmt/FeaturePlot/ul_2018_v10/cat_base_selection/prod_1312/root/"

file_template = "{}__pg_signal__nodata.root"

var_names = ["Htt_mass", "Htt_met_mass", "Htt_svfit_mass"]
legends = ["H(#tau#tau)", "H(#tau#tau) + MET", "H(#tau#tau) (SVFit)"]
colors = [1, 2, 4]

c = Canvas()

n_cols = 1
n_rows = 3

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

for i, (var, leg, color) in enumerate(zip(var_names, legends, colors)):
    tf = ROOT.TFile.Open(folder + file_template.format(var))
    histos.append(copy(tf.Get("histograms/ggf_sm")))
    histos[-1].GetXaxis().SetTitle("Mass [GeV]")
    histos[-1].GetYaxis().SetTitle("A.U.")
    histos[-1].SetLineColor(color)
    
    if histos[-1].GetMaximum() > max_val:
        max_val = histos[-1].GetMaximum()

    legend.AddEntry(histos[-1], leg, "l")


for histo in histos:
    histo.SetMaximum(1.1 * max_val)
    histo.Draw("histo, same")

draw_labels = get_labels(upper_right="2018, 13 TeV (59.74 fb^{-1})")

legend.Draw("same")
for label in draw_labels:
    label.Draw("same")

c.SaveAs("ggf_sm_mass.pdf")
c.SaveAs("ggf_sm_mass.png")