from analysis_tools.utils import import_root
from copy import deepcopy as copy
from plotting_tools.root import get_labels, Canvas, RatioCanvas

ROOT = import_root()


f_true = "/eos/user/j/jleonhol/cmt/PlotNanoAODStuff/base_config/htautau_ggf/cat_base/prod_2710/all_histos.root"
f_rew = "/eos/user/j/jleonhol/cmt/PlotNanoAODStuff/base_config/ggf_sm/cat_base/prod_2710/all_histos.root"

features = ["ngenjets", "l1_jet_pt"]
xaxis = ["Number of generated jets", "leading L1 jet p_{T} [GeV]"]

legends = ["H#rightarrow#tau#tau", "HH#rightarrowbb#tau#tau"]
colors = [1, 2]



n_cols = 1
n_rows = 2

# col_width = 0.125
col_width = 0.25
row_width = 0.06

legend_x2 = 0.88
legend_x1 = legend_x2 - n_cols * col_width
legend_y2 = 0.88
legend_y1 = legend_y2 - n_rows * row_width






for ifeat, feat in enumerate(features):
    c = Canvas()
    histos = []
    max_val = -1
    legend = ROOT.TLegend(legend_x1, legend_y1, legend_x2, legend_y2)
    for i, (f, leg, color) in enumerate(zip([f_true, f_rew], legends, colors)):
        tf = ROOT.TFile.Open(f)
        histos.append(copy(tf.Get(feat)))
        histos[-1].Scale(1./histos[-1].Integral())
        histos[-1].GetXaxis().SetTitle(xaxis[ifeat])
        histos[-1].GetYaxis().SetTitle("Normalized entries")
        # histos[-1].GetYaxis().SetTitleOffset(1.5)
        histos[-1].SetLineColor(color)

        if histos[-1].GetMaximum() > max_val:
            max_val = histos[-1].GetMaximum()

        legend.AddEntry(histos[-1], leg, "l")

    for histo in histos:
        histo.SetMaximum(1.2 * max_val)
        histo.SetMinimum(0)
        histo.Draw("histo, same, E")

    draw_labels = get_labels(
        upper_left="Private work",
        upper_right="2018 Simulation, 13 TeV"
    )

    legend.Draw("same")
    for label in draw_labels:
        label.Draw("same")

    c.SaveAs("%s.pdf" % feat)
    c.SaveAs("%s.png" % feat)

