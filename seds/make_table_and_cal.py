'''Make the browse table and calibration plot for
fitting just photospheres to the Chen+2012 sample'''

import mysql.connector

from sdf import tables
from sdf import plotting
from sdf import config as cfg

# the browse table
cnx = mysql.connector.connect(user=cfg.mysql['user'],
                              password=cfg.mysql['passwd'],
                              host=cfg.mysql['host'],
                              database=cfg.mysql['db_sdb'])

cursor = cnx.cursor(buffered=True)

tables.sample_table_www(cursor,'chen_2012_','browse_chen_2012.html',
						absolute_paths=False,
						rel_loc="all_chen_2012/',sdbid,'/public")

# the calibration plot
plotting.calibration(sample='chen_2012_',fileroot='./')