SELECT * 
FROM filtrable
WHERE ST_DISTANCE(ST_GeographyFromText('point('||latitude||' '||longitude||')'), ST_GeographyFromText('point(-18.9842 47.5339)')) < 136 AND identifiant like 'B%'
