.headers on
.mode column
SELECT * FROM model_metrics ORDER BY mae;
SELECT product_id, month, demand, ROUND(pred_random_forest,0) AS predicted,
       ROUND(ABS(demand-pred_random_forest),0) AS absolute_error
FROM predictions ORDER BY month, product_id;
