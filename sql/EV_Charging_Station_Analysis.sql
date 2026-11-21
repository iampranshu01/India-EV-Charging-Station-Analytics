-- Ques 1 Which cities have the highest number of EV charging stations?

-- SELECT
--     city,
--     COUNT(station_id) AS total_stations
-- FROM charging_stations
-- WHERE city IS NOT NULL
-- GROUP BY city
-- ORDER BY total_stations DESC
-- LIMIT 10;


-- Ques 2 Which districts have the highest number of EV charging stations?
-- SELECT
--     district,
--     COUNT(station_id) AS total_stations
-- FROM charging_stations
-- WHERE district IS NOT NULL
-- GROUP BY district
-- ORDER BY total_stations DESC
-- LIMIT 10;



-- Question 3 Who are the top 10 EV charging station operators based on infrastructure presence?
-- SELECT
--     operator,
--     COUNT(station_id) AS total_stations
-- FROM charging_stations
-- WHERE operator IS NOT NULL
-- GROUP BY operator
-- ORDER BY total_stations DESC
-- LIMIT 10;


-- Question 4 Which EV charging networks have the largest infrastructure presence based on the total number of charging stations?
-- SELECT
--     network,
--     COUNT(station_id) AS total_stations
-- FROM charging_stations
-- WHERE network IS NOT NULL
-- GROUP BY network
-- ORDER BY total_stations DESC
-- LIMIT 8;



-- Q5. Which EV charging operators provide the highest number of DC charging points?
-- SELECT
--     operator,
--     SUM(dc_points) AS total_dc_points
-- FROM charging_stations
-- WHERE operator IS NOT NULL
-- GROUP BY operator
-- ORDER BY total_dc_points DESC
-- LIMIT 10;


-- Q6. Which EV charging networks have the highest average charging power capacity?-- 
-- SELECT
--     network,
--     COUNT(station_id) AS total_stations,
--     ROUND(AVG(max_power_kw), 2) AS avg_power_kw
-- FROM charging_stations
-- WHERE network IS NOT NULL
--   AND max_power_kw IS NOT NULL
-- GROUP BY network
-- HAVING COUNT(station_id) >= 5
-- ORDER BY avg_power_kw DESC
-- LIMIT 10;

-- Question 7 Which EV charging stations support multiple connector types, and what connector combinations are available?

SELECT
    station_id,
    city,
    operator,
    connectors
FROM charging_stations
WHERE connectors IS NOT NULL
  AND TRIM(connectors) <> ''
  AND (
      connectors LIKE '%,%'
      OR connectors LIKE '%;%'
      OR connectors LIKE '%|%'
  )
ORDER BY city, operator;

-- Q8: Identification of EV Stations with Both AC and DC Charging Facilities

-- SELECT
--     COUNT(station_id) AS stations_with_both_ac_dc
-- FROM charging_stations
-- WHERE ac_points > 0
--   AND dc_points > 0;







-- Q9:Which states have the highest EV charging infrastructure coverage based on the number of charging stations?

-- SELECT
--     state,
--     COUNT(station_id) AS total_charging_stations
-- FROM charging_stations
-- WHERE state IS NOT NULL
--   AND TRIM(state) <> ''
-- GROUP BY state
-- ORDER BY total_charging_stations DESC;



-- Q10. Which cities have the highest average number of charging points per station?
-- SELECT
--     SUM(ac_points) AS total_ac_points,
--     SUM(dc_points) AS total_dc_points,
--     ROUND(AVG(max_power_kw), 2) AS avg_station_power_kw
-- FROM charging_stations;


-- Q11. Which cities have the highest number of high-power EV charging stations?

-- SELECT
--     city,
--     COUNT(station_id) AS high_power_stations,
--     ROUND(AVG(max_power_kw), 2) AS avg_power_kw,
--     MAX(max_power_kw) AS highest_power_kw
-- FROM charging_stations
-- WHERE city IS NOT NULL
--   AND max_power_kw >= 50
-- GROUP BY city
-- ORDER BY high_power_stations DESC
-- LIMIT 10;


-- Q12: Operator-wise Missing Pricing Information Analysis

-- SELECT
--     operator,
--     COUNT(station_id) AS stations_with_missing_pricing
-- FROM charging_stations
-- WHERE operator IS NOT NULL
--   AND (
--       pricing IS NULL
--       OR TRIM(pricing) = ''
--   )
-- GROUP BY operator
-- ORDER BY stations_with_missing_pricing DESC
-- LIMIT 10; 