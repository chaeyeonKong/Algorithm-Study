# SELECT
#     child.id,
#     child.genotype,
#     parent.genotype AS parent_genotype
# FROM
#     ecoli_data child
#     JOIN ecoli_data parent 
#     ON child.parent_id = parent.id
# WHERE
#     (child.genotype & parent.genotype) = parent.genotype
# ORDER BY
#     child.id

SELECT CHILD.ID, CHILD.GENOTYPE,  PARENT.GENOTYPE AS PARENT_GENOTYPE FROM ECOLI_DATA CHILD
JOIN ECOLI_DATA PARENT ON CHILD.PARENT_ID = PARENT.ID
WHERE (CHILD.GENOTYPE & PARENT.GENOTYPE) = PARENT.GENOTYPE
ORDER BY ID