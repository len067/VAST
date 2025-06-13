#!/usr/bin/env python

import glob
import os

epochs = glob.glob("epoch_*")
epochs.sort()
cwd = os.getcwd()
for epoch in epochs:
    if epoch in ["epoch_75"]:
        continue
    os.chdir(epoch)
    flist = glob.glob("cat*.csv")
    cats = []
    for fname in flist:
        cat = fname.split("_")[2]
        if cat in cats:
            continue
        cats.append(cat)
    os.system("rm cat_match.tgz")
    for cat in cats:
        os.system(f"tar -cvzf cat_match_{cat}.tgz cat_match_{cat}*.csv")
        os.system(f"rm cat_match_{cat}*.csv")
    os.system("tar -cvzf beam_inf.tgz beam_inf*.csv")
    os.system("rm beam_inf*.csv")
    os.system("rm free")
    os.chdir(cwd)