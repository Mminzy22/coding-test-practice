SELECT i.INGREDIENT_TYPE, SUM(TOTAL_ORDER) as TOTAL_ORDER
FROM FIRST_HALF f JOIN ICECREAM_INFO i ON f.FLAVOR = i.FLAVOR
GROUP BY i.INGREDIENT_TYPE
ORDER BY TOTAL_ORDER