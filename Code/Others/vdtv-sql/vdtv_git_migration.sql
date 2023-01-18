
INSERT INTO atom.vdtv_30ma(git_commits, asset, ma_date)
SELECT sum(git_commits) as git_commits,
		max(atom.atom_commits.asset) as asset,
        max(atom.atom_commits.datetime) as ma_date
FROM atom.atom_commits
WHERE atom.atom_commits.datetime > NOW() - INTERVAL 30 DAY
AND atom.atom_commits.datetime < NOW() + INTERVAL 30 DAY

-- Gathering git_commit data from another table, 
-- calculating the total(sum) of commits within a 30 day period,
-- then, appending or (INSERT INTO) the proper table.

