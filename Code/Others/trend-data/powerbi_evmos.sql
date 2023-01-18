-- PowerBI table example for Evmos

SELECT cast(atom.evmos_trends.date as date) as evm_date, avg($evmos + evmos + 'Evmos ETH' + 'Evmos EVM' + 'Evmos Crypto') as evm_sum
FROM atom.evmos_trends
GROUP BY cast(atom.evmos_trends.date as DATE);

-- Grabs the hourly data from PyTrends (Google Trends community python package) and,
-- converts it into daily for ease of use in PowerBI