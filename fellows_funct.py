#!/Users/julia_mav/anaconda/bin/python
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
from textwrap import wrap
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})
from pylab import *

import pandas
from matplotlib.table import Table

from collections import OrderedDict
from pandas import DataFrame
import pandas as pd
import numpy as np

def sort_fellows_list(list_q):
    u_list_q = set(list_q)
    u_list_qs = list(u_list_q)
    u_list_qs = sorted(u_list_qs)

    count_comps = []
    mcomps = []
    scomps = []

    for ix in range(0,len(u_list_qs)):
    	counts = list_q.count(u_list_qs[ix])
    	if counts > 1:
       	   count_comps.append(counts)
           mcomps.append(u_list_qs[ix])
    	if counts == 1:
           scomps.append(u_list_qs[ix])

    return u_list_qs, count_comps, mcomps, scomps

def sort_fellows_str(names, jobs, companies, projects, subjects, unis, degs, string, index):
    names_small = []
    jobs_small = []
    companies_small = []
    projects_small = []
    subjects_small = []
    unis_small = []
    degs_small = []
    
    if index == 0:
        search = names
    if index == 2:
        search = jobs
    if index == 3:
        search = companies
    if index == 4:
        search = projects
    if index == 5:
        search = subjects
    if index == 6:
        search = unis
    if index == 7:
        search = degs                

    for ix in range(0,len(names)):
        strg = search[ix].lower()
        if strg.find(string) != -1:
            #print search[ix]
            #raw_input('check')
            names_small.append(names[ix])
            jobs_small.append(jobs[ix])
            companies_small.append(companies[ix])
            projects_small.append(projects[ix])
            subjects_small.append(subjects[ix]) 
            unis_small.append(unis[ix])
            degs_small.append(degs[ix])

    return names_small, jobs_small, companies_small, projects_small, subjects_small, unis_small, degs_small

def sort_fellows_table_pdf(names, jobs, companies, projects, subjects, unis, degs, name_plot):

    table = OrderedDict((
    ('Name',names),
    ('Job',jobs),
    ('Company',companies),
    ('Project',projects),
    ('Subject',subjects),
    ('University', unis),
    ('Degree',degs)))

    Headn = ['Name','Job','Company','Project','Subject','University','Degree']
    data = pandas.DataFrame(table)

    #print data
    
    fig, ax = plt.subplots()
    ax.set_axis_off()
    tb = Table(ax, bbox=[0,0,1,1])

    nrows, ncols = data.shape
    wcell = 1
    hcell = 1
    wpad = 0.5
    hpad = 0.5
    print "Making table" 
    #fig = plt.figure(figsize=(5, 20))
    width, height = 1.0 / (ncols*1.0), 1.0 / (nrows*2.0)
    matplotlib.rcParams.update({'font.size': 50})
    print nrows, ncols
    # Add cells
    print data[Headn[1]].iloc[0]

    for i in range(0,ncols):
        for j in range(0,nrows-1):
            # Index either the first or second item of bkg_colors based on
            # a checker board pattern
            #idx = [j % 2, (j + 1) % 2][i % 2]
            txt = "\n".join(wrap(data[Headn[i]].iloc[j], 40))
            nmrows = len(txt)/20.0
            print len(txt), nmrows
            #raw_input('check')
            color = "white"
            tb.add_cell(j, i, width, height*2.0, text=txt, 
                    loc='center', facecolor="white")

    # Row Labels...
    for i in range(0,nrows-1):
        label = str(i)
        tb.add_cell(i, -1, width, height*2.0, text=label, loc='right', 
                    edgecolor='black', facecolor='lightblue')
    # Column Labels...
    for j, label in enumerate(data.columns):
        tb.add_cell(-1, j, width, height, text=label, loc='center', 
                           edgecolor='black', facecolor='lightcoral')
    ax.add_table(tb)
    plt.savefig(name_plot+'.pdf', bbox_inches = "tight")
    return ''

############ CREATES TABLE MINUS PROJECT NAMES
def sort_fellows_table_nproj_pdf(names, jobs, companies, subjects, unis, degs, name_plot):

    table = OrderedDict((
    ('Name',names),
    ('Job',jobs),
    ('Company',companies),
    ('Subject',subjects),
    ('University', unis),
    ('Degree',degs)))

    Headn = ['Name','Job','Company', 'Subject','University','Degree']
    data = pandas.DataFrame(table)

    #print data
    
    fig, ax = plt.subplots()
    ax.set_axis_off()
    tb = Table(ax, bbox=[0,0,1,1])

    nrows, ncols = data.shape
 
    #fig = plt.figure(figsize=(5, 20))
    width, height = 1.0 / (ncols), 1.0 / (nrows)
    matplotlib.rcParams.update({'font.size': 20})
    print nrows, ncols
    # Add cells
    print data[Headn[1]].iloc[0]

    for i in range(0,ncols):
        for j in range(0,nrows-1):
            txt = "\n".join(wrap(data[Headn[i]].iloc[j], 40))
            color = "white"
            tb.add_cell(j, i, width, height, text=txt, 
                    loc='center', facecolor="white")

    # Row Labels...
    for i in range(0,nrows-1):
        label = str(i)
        tb.add_cell(i, -1, width, height, text=label, loc='right', 
                    edgecolor='black', facecolor='lightblue')
    # Column Labels...
    for j, label in enumerate(data.columns):
        tb.add_cell(-1, j, width, height/2.0, text=label, loc='center', 
                           edgecolor='black', facecolor='lightcoral')
    ax.add_table(tb)
    plt.savefig(name_plot+'.pdf', bbox_inches = "tight")
    return ''

def plot_fellows_list_pdf(u_list_qs, count_comps, mcomps, scomps, name_type, name_plot):
    # Wrap txt for caption
    lscomps = ''
    for l in scomps:
        lscomps += l + ', '
    txt = "\n".join(wrap('Other '+name_type+': '+lscomps, 100))
    
    # Plot a bar graph
    y_pos = np.arange(len(count_comps))
    y_pos1 = len(count_comps)-y_pos

    fig = plt.figure()
    gs = gridspec.GridSpec(10, 5)
    ax1 = plt.subplot(gs[0:8, :])
    ax1.barh(y_pos1, count_comps, align = "center", color='b')
    plt.yticks(y_pos1,mcomps)
    ax1.xaxis.grid(True)
    ax1.set_ylim([0.0, len(count_comps)+0.5])
    plt.xlabel('Number of fellows')

    # Put a legend below current axis    
    ax2 = plt.subplot(gs[8:,:])
    ax2.plot(0.0, 0.0, color='w', label=txt)
    ax2.legend(bbox_to_anchor=(0.98, 0.98),fancybox=True, shadow=True, ncol=5, prop={'size':10})
    ax2.axis("off")
    plt.tight_layout()
    plt.savefig(name_plot+'.pdf', bbox_inches = "tight")

    
def plot_fellows_list_screen(u_list_qs, count_comps, mcomps, scomps, name_plot):
    # Wrap txt for caption
    lscomps = ''
    for l in scomps:
        lscomps += l + ', '
    txt = "\n".join(wrap('Other '++': '+lscomps, 100))
    
    # Plot a bar graph
    y_pos = np.arange(len(count_comps))
    y_pos1 = len(count_comps)-y_pos

    fig = plt.figure()
    gs = gridspec.GridSpec(10, 5)
    ax1 = plt.subplot(gs[0:8, :])
    ax1.barh(y_pos1, count_comps, align = "center", color='b')
    plt.yticks(y_pos1,mcomps)
    ax1.xaxis.grid(True)
    ax1.set_ylim([0.0, len(count_comps)+0.5])
    plt.xlabel('Number of fellows')

    # Put a legend below current axis    
    ax2 = plt.subplot(gs[8:,:])
    ax2.plot(0.0, 0.0, color='w', label=txt)
    ax2.legend(bbox_to_anchor=(0.98, 0.98),fancybox=True, shadow=True, ncol=5, prop={'size':10})
    ax2.axis("off")
    plt.tight_layout()
    #plt.savefig(name_plot+'.pdf', bbox_inches = "tight")
    plt.show()
