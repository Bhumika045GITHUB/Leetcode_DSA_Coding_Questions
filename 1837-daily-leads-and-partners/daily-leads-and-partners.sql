# Write your MySQL query statement below

SELECT date_id, lower(make_name) as make_name, COUNT(DISTINCT lead_id) AS unique_leads, COUNT(DISTINCT partner_id) AS unique_partners FROM DailySales GROUP BY date_id, lower(make_name);