SELECT
    CAR_TYPE,
    count(*) as CARS
FROM CAR_RENTAL_COMPANY_CAR 
WHERE OPTIONS LIKE '%통풍시트%' or OPTIONS LIKE '%열선시트%'or OPTIONS LIKE '%가죽시트%'
group by CAR_TYPE
order by CAR_TYPE
