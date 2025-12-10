-- 코드를 입력하세요
WITH MYC AS (SELECT DISTINCT CART_ID 
             FROM (SELECT CART_ID, NAME
                   FROM CART_PRODUCTS
                   WHERE NAME = 'Milk') A INNER JOIN (SELECT CART_ID, NAME
                                                      FROM CART_PRODUCTS
                                                      WHERE NAME = 'Yogurt') B USING(CART_ID))
SELECT DISTINCT CART_ID
FROM CART_PRODUCTS
WHERE CART_ID IN (SELECT MYC.CART_ID FROM MYC)