INSERT INTO "public".construction ( description, valeur, unite, "date") VALUES ('cout', 20000, 'Ar', current_date );
INSERT INTO "public".construction ( description, valeur, unite, "date") VALUES ('duree', 3, 'jours', current_date );

INSERT INTO "public".filtrable (identifiant, description, latitude, longitude) VALUES ( concat('B' , nextval('batiment_seq')) , 'Hopital A', -18.9846 ,47.5327);
INSERT INTO "public".filtrable (identifiant, description, latitude, longitude) VALUES ( concat('O' , nextval('homme_seq')) , 'Olona A', -18.9844 ,47.5337);
