import sqlalchemy as sq


## Initializing the SQL DB
hostname = "#####:#####"
dbname="#####"
uname="#####"
pwd="#####"

db = sq.create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
				.format(host=hostname, db=dbname, user=uname, pw=pwd))


## The SQL Statement that uploads the data from other tables into an aggregated VDTV table for future metrics. More soon!!
def upload():

    db.execute("INSERT INTO atom.vdtv_30ma(git_commits, asset, ma_date) SELECT sum(git_commits) as git_commits, max(atom.atom_commits.asset) as asset, max(atom.atom_commits.datetime) as ma_date FROM atom.atom_commits WHERE atom.atom_commits.datetime > NOW() - INTERVAL 30 DAY AND atom.atom_commits.datetime < NOW() + INTERVAL 30 DAY")
    db.execute("INSERT INTO atom.vdtv_30ma(git_commits, asset, ma_date) SELECT sum(git_commits) as git_commits, max(atom.osmo_commits.asset) as asset, max(atom.osmo_commits.datetime) as ma_date FROM atom.osmo_commits WHERE atom.osmo_commits.datetime > NOW() - INTERVAL 30 DAY AND atom.osmo_commits.datetime < NOW() + INTERVAL 30 DAY")
    db.execute("INSERT INTO atom.vdtv_30ma(git_commits, asset, ma_date) SELECT sum(git_commits) as git_commits, max(atom.evmos_commits.asset) as asset, max(atom.evmos_commits.datetime) as ma_date FROM atom.evmos_commits WHERE atom.evmos_commits.datetime > NOW() - INTERVAL 30 DAY AND atom.evmos_commits.datetime < NOW() + INTERVAL 30 DAY")


    return(print("Done?"))

upload()