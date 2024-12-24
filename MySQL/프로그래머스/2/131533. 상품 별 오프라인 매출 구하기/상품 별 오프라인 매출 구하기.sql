SELECT
    PRODUCT_CODE,
    SUM(PRICE*SALES_AMOUNT) as SALES
FROM 
    PRODUCT RIGHT JOIN OFFLINE_SALE ON PRODUCT.PRODUCT_ID = OFFLINE_SALE.PRODUCT_ID
GROUP BY
    PRODUCT_CODE
ORDER BY SALES DESC, PRODUCT_CODE