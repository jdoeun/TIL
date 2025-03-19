-- programmers: 업그레이드 된 아이템 구하기

SELECT A.ITEM_ID, A.ITEM_NAME, A.RARITY
FROM ITEM_INFO AS A
INNER JOIN ITEM_TREE AS B
ON A.ITEM_ID = B.ITEM_ID
WHERE B.PARENT_ITEM_ID IN (SELECT ITEM_ID FROM ITEM_INFO WHERE RARITY = 'RARE')
ORDER BY A.ITEM_ID DESC;