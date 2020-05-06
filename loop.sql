--Заповнення таблиці міст
DECLARE
	V_CITY_NUMBER INTEGER := 10;
	V_CITY_NAME CITY.CITY%Type;
BEGIN
	V_CITY_NAME := 'City number ';

	FOR i IN 1..V_CITY_NUMBER LOOP
		INSERT INTO
			CITY (city, region , state_code, country_code)
		VALUES
			(CONCAT(V_CITY_NAME,i), 'California', 'CA', 'USA');
	END LOOP;
END;
