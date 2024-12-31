SELECT MEMBER_ID, MEMBER_NAME, GENDER, DATE_FORMAT(DATE_OF_BIRTH, '%Y-%m-%d') as DATE_OF_BIRTH
FROM MEMBER_PROFILE 
WHERE EXTRACT(MONTH FROM DATE_OF_BIRTH) = 03 and TLNO IS NOT NULL and GENDER IN ('W')
ORDER BY MEMBER_ID