-- 코드를 입력하세요
SELECT CAR_RENTAL_COMPANY_CAR.CAR_ID, CAR_RENTAL_COMPANY_CAR.CAR_TYPE, CAR_RENTAL_COMPANY_CAR.DAILY_FEE, CAR_RENTAL_COMPANY_CAR.OPTIONS FROM CAR_RENTAL_COMPANY_CAR
WHERE OPTIONS LIKE '%네비게이션%'
ORDER BY CAR_ID DESC;