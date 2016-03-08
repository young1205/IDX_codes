#!/Users/julia_mav/anaconda/bin/python  
import MySQLdb
import optparse
import os
import re
import numpy as np
import fellows_funct

#########################################################################
#########################################################################
# This program is written to read in a file with '|' as a delimiter and
# to create a SQL database.
#
# JCY , July 25th , 2015
#########################################################################
#########################################################################


#########################################################################
# Read in file and create a 2d python list
#########################################################################
filename_in = '/Users/julia_mav/Code/Python/fellows-cleaned.txt'
file = open(filename_in,'r')

table_py = []
c = ' '
while len(c) > 0:
        c = file.readline()

        # Split line by delimiter
        split_line = c.split("|")

        # Process a typical line
        if len (split_line) == 7:
                split_line.pop(-1)
                job = split_line.pop(1)
                job = job.split(",")
                split_line.insert(1,job[0])
                if len(job) > 1:
                        split_line.insert(2,job[1])
                else:
                        split_line.insert(2,'Null')
                        #print split_line
                        #print raw_input('check')
                split_line[0]= split_line[0].strip()
                split_line[1]= split_line[1].strip()
                split_line[2]= split_line[2].strip()
                split_line[3]= split_line[3].strip()
                split_line[4]= split_line[4].strip()
                split_line[5]= split_line[5].strip()
                split_line[6]= split_line[6].strip()
                table_py.append(split_line)
        if len (split_line) == 8:
                split_line.pop(-1)
                split_line[0]= split_line[0].strip()
                split_line[1]= split_line[1].strip()
                split_line[2]= split_line[2].strip()
                split_line[3]= split_line[3].strip()
                split_line[4]= split_line[4].strip()
                split_line[5]= split_line[5].strip()
                split_line[6]= split_line[6].strip()
                entry_end_job = split_line[1]
                entry_end_uni = split_line[4]
                if entry_end_job[-1] == ',':
                        split_line[1]=split_line[1].replace(",","")
                else:
                       if entry_end_uni[-1] == ',':
                           split_line[4:6] = [''.join(split_line[4:6])]
                           job = split_line.pop(1)
                           job = job.split(",")
                           split_line.insert(1,job[0])
                           if len(job) > 1:
                               split_line.insert(2,job[1])
                           else:
                               split_line.insert(2,'Null')
                #if len (split_line) == 8:
                #        table_py.append(split_line)
                #        print split_line
                #raw_input('check')

# Split into individual columns 
names = [d[0] for d in table_py]
jobs = [d[1] for d in table_py]
companies = [d[2] for d in table_py]
projects = [d[3] for d in table_py]
subjects = [d[4] for d in table_py]
unis = [d[5] for d in table_py]
degs = [d[6] for d in table_py]

#Find the max length of individual columns + number of fellows
ml_names = max(len(s) for s in names) + 1
ml_jobs = max(len(s) for s in jobs) + 1
ml_companies = max(len(s) for s in companies) + 1
ml_projects = max(len(s) for s in projects) + 1
ml_subjects = max(len(s) for s in subjects) + 1
ml_unis = max(len(s) for s in unis) + 1
ml_degs = max(len(s) for s in degs) + 1

print "The number of fellows with data:", len(unis)
#print " The Maximum length of characters for: "
#print " Name | Job | Company | Project | Subject | University | Degree |"
#print " "+str(ml_names)+"|"+str(ml_jobs)+"|"+str(ml_companies)+"|"+str(ml_projects)+"|"+str(ml_subjects)+"|"+str(ml_unis)+"|"+str(ml_degs)

num_fellows = len(names)

######## Create a sorted list by type
u_list_qs, count_comps, mcomps, scomps = fellows_funct.sort_fellows_list(subjects)

###### Get all entries related to a string
names_small, jobs_small, companies_small, projects_small, subjects_small, unis_small, degs_small = fellows_funct.sort_fellows_str(names, jobs, companies, projects, subjects, unis, degs, "astro", 5)

#### Find percentage of astro fellows
print "The percentage of astro fellows is: "+str((float(len(names_small))/float(len(names))*100.0))

print raw_input("Check")
#c=fellows_funct.sort_fellows_table_pdf(names_small, jobs_small, companies_small, projects_small, subjects_small, unis_small, degs_small, "Astro")
c=fellows_funct.sort_fellows_table_nproj_pdf(names_small, jobs_small, companies_small, subjects_small, unis_small, degs_small, "Astro_small")

###### Create a table of first seven entries
names_small=names[:8]
jobs_small=jobs[:8]
companies_small=companies[:8]
projects_small=projects[:8]
subjects_small=subjects[:8]
unis_small=unis[:8]
degs_small=degs[:8]
#c=fellows_funct.sort_fellows_table_pdf(names_small, jobs_small, companies_small, projects_small, subjects_small, unis_small, degs_small, "first_ten")
#print u_list_qs
#print count_comps
#print mcomps
#print scomps

#name_plot = "fellows_subjects"
#name_type = "subjects"
#fellows_funct.plot_fellows_list_pdf(u_list_qs, count_comps, mcomps, scomps, name_type, name_plot)

"""
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
plt.xlabel('Companies')

ax2 = plt.subplot(gs[8:,:])
# Put a legend below current axis
ax2.plot(0.0, 0.0, color='w', label=txt)
ax2.legend(bbox_to_anchor=(0.98, 0.98),fancybox=True, shadow=True, ncol=5, prop={'size':10})
ax2.axis("off")
plt.tight_layout()
#plt.show()
plt.savefig('pic.pdf', bbox_inches = "tight")


#########################################################################
# Use python list to create SQL database
#########################################################################

connection = MySQLdb.connect(host='localhost',  # the host the database server is running on.
                             user='root',       # the database user you use to connect to thedatabase server
                             passwd='Scuppy1')      
curs=connection.cursor()
curs.execute("USE insight;")
curs.execute("DROP TABLE IF EXISTS fellows;")
curs.execute("SET @saved_cs_client = @@character_set_client;")
curs.execute("SET character_set_client = utf8;")
curs.execute("CREATE TABLE fellows ( ID int("+str(num_fellows)+") NOT NULL auto_increment, Name varchar("+str(ml_names)+") NOT NULL default '', Job varchar("+str(ml_jobs)+") NOT NULL default '', Company varchar("+str(ml_companys)+") NOT NULL default '', Project varchar("+str(ml_projects)+") NOT NULL default '', Subject varchar("+str(ml_subjects)+") NOT NULL default '', University varchar("+str(ml_unis)+") NOT NULL default '', Degree varchar("+str(ml_degs)+") NOT NULL default '', PRIMARY KEY(ID)) ENGINE=myISAM AUTO_INCREMENT=27 DEFAULT CHARSET=latin1;")
curs.execute("LOCK TABLES fellows WRITE;")

for ix in range(1,num_fellows):
    #curs.execute("INSERT INTO fellows VALUES ("+str(ix)+",'Tom', 'Job', 'Company', 'Project', 'Subject', 'Uni', 'Deg');")
    print table_py[ix-1]
    curs.execute("INSERT INTO fellows VALUES ("+str(ix)+",'"+table_py[ix-1][0]+"', '"+table_py[ix-1][1]+"', '"+table_py[ix-1][2]+"', '"+table_py[ix-1][3]+"', '"+table_py[ix-1][4]+"', '"+table_py[ix-1][5]+"', '"+table_py[ix-1][6]+"');")
curs.execute("UNLOCK TABLES;")

"""
